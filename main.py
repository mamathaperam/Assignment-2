import os

def create_sample_file(file_path):
    """Creates a sample text file if it does not already exist."""
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(
                "Hello world! Hello everyone.\n"
                "This is a sample text file. This file is used to demonstrate the word counting feature.\n"
            )
        print(f"Created a new file: {file_path}")
    else:
        print(f"File already exists: {file_path}")

def count_word_frequencies(file_path):
    """Reads a text file and counts occurrences of each word, displaying them in descending order."""
    word_counts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')).lower()
                words = line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print("The file was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

def main():
    file_path = "sample.txt"
    create_sample_file(file_path)
    count_word_frequencies(file_path)

if __name__ == "__main__":
    main()