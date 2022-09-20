"""
299. Bulls and Cows (medium)

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you\

provide a hint with the following info:

    - The number of "bulls", which are digits in the guess that are in the correct position.
    - The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong
      position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess 'guess', return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both\
secret and guess may contain duplicate digits.

Note: you may assume that the secret number and your friend's guess only contain digits and their lengths are equal.
"""

def getHint(secret: str, guess: str) -> str:
    """
    Bulls = correct digit and correct index position
    Cows = correct digit but wrong index position
    """
    bulls, cows = 0, 0
    # bucket for tally of cows, ten zeros -> numbers` 0 to 9
    bucket = [0] * 10  # [0,0,0,0,0,0,0,0,0,0]

    for s, g, in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            # anything not a bull, is potentially a cow

            # at bucket-index of secret digit ADD
            bucket[int(s)] += 1
            # at bucket-index of guess digit SUBTRACT
            bucket[int(g)] -= 1
    # subtract from the maximum number of cows (length minus bulls) the sum in the bucket that is larger 0
    cows = len(secret) - bulls - sum(x for x in bucket if x > 0)
    return f'{bulls}A{cows}B'


def main():
    print(getHint(secret="1807", guess="7810"), 'expected 1A3B')
    print(getHint(secret="1123", guess="0111"), 'expected 1A1B')


if __name__ == "__main__":
    main()
