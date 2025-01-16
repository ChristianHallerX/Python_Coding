import os
import random


def mock_lorem_ipsum_file(file_path, size_in_kb):
    """
    Create a mock text file with randomized occurrences of "lorem ipsum" text.

    Args:
        file_path (str): Path to the file to create.
        size_in_kb (int): Desired size of the file in kilobytes.
    """
    # Pool of words
    words = [
        "lorem",
        "ipsum",
        "dolor",
        "sit",
        "amet",
        "consectetur",
        "adipiscing",
        "elit",
        "sed",
        "do",
        "eiusmod",
        "tempor",
        "incididunt",
        "ut",
        "labore",
        "et",
        "dolore",
        "magna",
        "aliqua",
    ]
    with open(file_path, "w", encoding="utf-8") as file:
        while os.path.getsize(file_path) < size_in_kb * 1024:
            # pick random words from pool and periods.
            random_sentence = (
                " ".join(random.choices(words, k=random.randint(5, 15))) + ". "
            )
            file.write(random_sentence)


def top_n_frequent_words(file_path, n):
    """
    Identify the top n most frequent words in a large text file.

    Args:
        file_path (str): Path to the text file.
        n (int): Number of top frequent words to return.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing the word and its frequency.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # Read the file content
            text = file.read()

        # Normalize the text: convert to lowercase and remove punctuation manually
        # Create new text with lowercase and space (no punctuation)
        text = "".join(
            char.lower() if char.isalnum() or char.isspace() else " " for char in text
        )

        # Split on space -> list of word elements
        words = text.split()

        # Count the frequency of each word with dictionary
        counts_hashmap = {}
        for word in words:
            # Get the count of the current word from dict and add 1. If it does not exist, get 0 and add 1.
            counts_hashmap[word] = counts_hashmap.get(word, 0) + 1

        # Convert the dict to a list of tuples ('lorem', 147) and sort descending by second element (count integer)
        sorted_word_counts = sorted(
            counts_hashmap.items(), key=lambda item: item[1], reverse=True
        )
        # Return a list of the n most frequent tuples
        return sorted_word_counts[:n]

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Example usage
if __name__ == "__main__":
    # Generate text file
    mock_file = "mock_lorem_ipsum.txt"
    mock_lorem_ipsum_file(mock_file, 1)  # Create a 1 KB mock file

    top_words = top_n_frequent_words(mock_file, 10)

    # Print with nice formatting
    for word, count in top_words:
        print(f"{word}: {count}")

    # Delete the mock file after usage
    os.remove(mock_file)
