"""
Greedy Pont (easy??)

Similar to LeetCode 455 Assign Cookies

You are given two lists:

- fish (list of ints)     representing the sizes of fish
- baits (list of ints)     representing the sizes of baits

Each bait can be used up to 3 times.
A fish can be caught only if there exists a bait whose size is smaller than the fish.

Return the maximum number of fish that can be caught using the available baits.
"""


def greedyPond(fish, baits):
    # Sort fish and baits in descending order (largest to smallest)
    fish.sort(reverse=True)
    baits.sort(reverse=True)

    # Initialize the number of fish caught
    fishCaught = 0

    # Initialize bait index and create a list to track remaining uses for each bait.
    baitIndex = 0
    baitUse = [3] * len(baits)  # Each bait can be used up to 3 times.

    # Loop through each fish, trying to catch it using available baits.
    for fishSize in fish:

        # Try to find an eligible bait for the current fish.
        while baitIndex < len(baits):

            # Check if the current bait still has remaining uses.
            if baitUse[baitIndex] > 0:

                # If the bait is smaller than the fish, catch the fish.
                if baits[baitIndex] < fishSize:
                    fishCaught += 1  # Increment count of caught fish.
                    baitUse[baitIndex] -= 1  # Decrease the bait's remaining uses.
                    break  # Move on to the next fish.
                else:
                    # If the bait is too large, try the next bait.
                    baitIndex += 1
            else:
                # If the current bait is depleted, move to the next one.
                baitIndex += 1

    return fishCaught


def main():
    fish = [8, 7, 6]
    baits = [5, 4]
    print(greedyPond(fish, baits), "expected: 3")

    fish = [3, 3, 3]
    baits = [3, 2]
    print(greedyPond(fish, baits), "expected: 3")

    fish = [10, 9, 8]
    baits = [8, 7, 5]
    print(greedyPond(fish, baits), "expected: 3")


if __name__ == "__main__":
    main()
