import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def tokenizer(my_string):
    # Convert to lowercase string
    input_text = str(my_string.lower())
    # Remove all punctuation .,()/\!
    input_text = input_text.translate(str.maketrans(' ', ' ', string.punctuation))
    # Remove all digits 123454
    input_text = input_text.translate(str.maketrans('', '', string.digits))
    # remove all newlines and returns
    input_text = ' '.join([line.strip() for line in input_text.strip().splitlines() if line.strip()])

    # Instantiate NLTK stopwords object
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_text)

    # List comprehension if word token not in stop_words
    return [w for w in word_tokens if not w in stop_words]


def counter(my_tokens):
    # Counter dictionary
    count_dict = dict()
    # Iterate over each word filtered tokens
    for token in my_tokens:
        # Check if the word is already in dictionary
        if token in count_dict:
            # If already in dict, Increment count of word's value by 1
            count_dict[token] += 1
        else:
            # If NOT in dict, add the word to dictionary with value count 1
            count_dict[token] = 1

    # Create new dictionary sorted by values
    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))

    # Print key (word token) and count (value)
    for key, value in sorted_dict.items():
        print(key, ' : ', value)

if __name__ == "__main__":
    my_tokens = tokenizer(my_string=input('Paste text and enter:'))
    counter(my_tokens)
