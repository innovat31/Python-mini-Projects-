# word_counter.py

def count_words(sentence):
    words = sentence.split()
    return len(words)

# Write any senetence and it will count the number of words it contains

if __name__ == "__main__":
    sample = "GitHub is a great platform to share and collaborate on code."
    word_count = count_words(sample)
    print(f"The sentence has {word_count} words.")
