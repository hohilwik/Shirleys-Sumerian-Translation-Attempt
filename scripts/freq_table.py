import json
import sys
from collections import Counter

def generate_frequency_table(word_dict):
    #Generate a frequency table for the number of meanings per word.
    #
    #Args:
    #    word_dict (dict): A dictionary where keys are words and values are lists of meanings.
    #
    #Returns:
    #    dict: A dictionary where keys are the number of meanings and values are the count of words with that many meanings.

    # Count the number of meanings for each word
    num_meanings = [len(meanings) for meanings in word_dict.values()]

    # Generate the frequency table
    frequency_table = Counter(num_meanings)

    return dict(frequency_table)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
  
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            word_dict = json.load(f)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Generate the frequency table
    frequency_table = generate_frequency_table(word_dict)

    # Calculate the total count of words
    total_count = sum(frequency_table.values())

    # Output the frequency table with percentages
    print("Frequency Table:\n")
    for num_meanings, count in sorted(frequency_table.items()):
        percentage = (count / total_count) * 100
        print(f"Words with {num_meanings} meanings: {count} ({percentage:.2f}%)")

if __name__ == "__main__":
    main()
