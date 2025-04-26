import random
from typing import List, Tuple
import numpy as np


class EggScrambler:
    """Simulates scrambling eggs and analyzing their final positions."""

    def __init__(self, num_eggs: int = 12, seed: int = None):
        """
        Initialize the egg scrambler.

        Args:
            num_eggs: Number of eggs in the box
            seed: Optional random seed for reproducibility
        """
        self.num_eggs = num_eggs
        self.original_positions = list(range(1, num_eggs + 1))
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.scrambled_positions = self._scramble_eggs()
        self._same_location_count = None

    def _scramble_eggs(self) -> List[int]:
        """Scramble the eggs using Fisher-Yates shuffle algorithm."""
        scrambled = self.original_positions.copy()
        for i in range(self.num_eggs - 1, 0, -1):
            j = random.randint(0, i)
            scrambled[i], scrambled[j] = scrambled[j], scrambled[i]
        return scrambled

    def count_same_location(self) -> int:
        """Count how many eggs end up in their original position."""
        self._same_location_count = sum(
            1 for orig, new in zip(self.original_positions, self.scrambled_positions)
            if orig == new
        )
        return self._same_location_count

    def is_derangement(self) -> bool:
        """Check if no eggs are in their original position (derangement)."""
        if self._same_location_count is None:
            self.count_same_location()
        return self._same_location_count == 0


def run_simulation(num_experiments: int, box_sizes: List[int]) -> List[Tuple[int, int, float, float]]:
    """
    Run Monte Carlo simulation for different box sizes.

    Args:
        num_experiments: Number of experiments to run per box size
        box_sizes: List of different numbers of eggs to simulate

    Returns:
        List of tuples with results (num_eggs, avg_same_loc, prob_derangement)
    """
    results = []

    for num_eggs in box_sizes:
        same_loc_counts = []
        derangement_count = 0

        for _ in range(num_experiments):
            scrambler = EggScrambler(num_eggs)
            same_loc = scrambler.count_same_location()
            same_loc_counts.append(same_loc)
            if scrambler.is_derangement():
                derangement_count += 1

        avg_same_loc = np.mean(same_loc_counts)
        prob_derangement = derangement_count / num_experiments
        results.append((num_eggs, avg_same_loc, prob_derangement))

        print(f"Eggs: {num_eggs:4d} | Avg same location: {avg_same_loc:.4f} | "
              f"Derangement prob: {prob_derangement:.6f}")

    return results


def save_results(results: List[Tuple], filename: str = "results.csv"):
    """Save simulation results to a CSV file."""
    with open(filename, "w") as f:
        f.write("Num_Eggs,Avg_Same_Loc,Prob_Derangement\n")
        for row in results:
            f.write(f"{row[0]},{row[1]:.6f},{row[2]:.6f}\n")


def main():
    # Small to medium box sizes with many experiments
    results = run_simulation(100000, [2, 3, 4, 5, 8, 10, 12, 15, 20, 30, 50])
    save_results(results)

    # Large box sizes with fewer experiments
    large_results = run_simulation(10000, [100, 200, 500, 1000])
    save_results(large_results, "large_results.csv")


if __name__ == "__main__":
    main()