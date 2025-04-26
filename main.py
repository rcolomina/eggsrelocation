"""
You've got a box with 12 eggs.

You take them from them box, scramble them, and finally put them back.

Questions:

1) What is the average number of eggs ending up at the same location?
2) What is the probability of not having any egg at the same location?

Bonus question:

What would happen with a box of N eggs?

"""

import random


class ScrambleEggs:
    def __init__(self, number_eggs: int = 12, seed: int = 42):
        self.number_eggs = number_eggs
        self.box = [x + 1 for x in range(self.number_eggs)]
        self.seed = seed
        self.scrambled_box = self._scramble()
        random.seed(self.seed)
        self._number_on_same_location = 0

    def __repr__(self):
        return "(" + ",".join([str(x) for x in self.scrambled_box]) + ")"

    def _scramble(self):
        sb = []
        box = self.box.copy()
        while len(sb) < self.number_eggs:
            extraction = random.choice(box)
            box.remove(extraction)
            sb.append(extraction)
        return sb + box

    def number_on_same_location(self):
        self._number_on_same_location = sum([int(x == y) for x, y in zip(self.box, self.scrambled_box)])
        return self._number_on_same_location

    def none_on_same_loc(self):
        return self._number_on_same_location == 0


def monte_carlo_sim(number_of_experiments, box_sizes):
    results = []
    for number_eggs in box_sizes:  # [2,3,5,10]:
        num_same_loc = 0
        num_non_same_loc = 0
        for seed in range(number_of_experiments):
            b = ScrambleEggs(number_eggs, seed)
            num_same_loc += b.number_on_same_location()
            if b.none_on_same_loc():
                num_non_same_loc += 1
        print(number_eggs, number_of_experiments, num_same_loc, num_non_same_loc)
        results.append((number_eggs, number_of_experiments, num_same_loc, num_non_same_loc))
    return results


def write_results(results, mode = "w"):

    with open("results.txt", mode) as f:
        if mode == "w":
            f.write("Number_Eggs, Num_Experiments, Num_ending_same_loc, Num_not_ending_same_loc \n")
        for re in results:
            f.write(",".join([str(x) for x in re]))
            f.write("\n")
    f.close()


def main():
    number_of_experiments = 100000
    box_sizes = [2, 3, 4, 5, 8, 10, 15, 20, 30, 50]
    results = monte_carlo_sim(number_of_experiments, box_sizes)
    write_results(results)

    number_of_experiments = 10000
    box_sizes = [100, 200, 500, 1000]
    results = monte_carlo_sim(number_of_experiments, box_sizes)
    write_results(results, mode="a+")

    #number_of_experiments = 25
    #box_sizes = [2000, 5000, 10000]
    #results = monte_carlo_sim(number_of_experiments, box_sizes)
    #write_results(results)


if __name__ == "__main__":
    main()
