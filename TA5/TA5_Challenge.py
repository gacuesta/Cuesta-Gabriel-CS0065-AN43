import string

def load_dataset(filename):
    with open(filename, "r", encoding="utf-8") as file:
        words = {
            line.strip().lower()
            for line in file
            if line.strip() and not line.startswith(";")
        }
    return words

# Load the happy and sad word datasets
HAPPY_DATASET = load_dataset("Cuesta-Gabriel-CS0065-AN43/TA5/happy_words.txt")
SAD_DATASET = load_dataset("Cuesta-Gabriel-CS0065-AN43/TA5/sad_words.txt")

def number_happy(sentence):
    # Remove punctuation and convert to lowercase
    cleaned = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned.split()
    
    count = 0
    for word in words:
        if word in HAPPY_DATASET:
            count += 1
    return count

def number_sad(sentence):
    cleaned = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned.split()
    
    count = 0
    for word in words:
        if word in SAD_DATASET:
            count += 1
    return count

# Main
user_sentence = input("Enter a sentence: ")

happy_count = number_happy(user_sentence)
sad_count = number_sad(user_sentence)

print(f"Happy words: {happy_count}")
print(f"Sad words: {sad_count}")

if happy_count > sad_count:
    print("Analysis: The tone of the sentence is Positive (Happy).")
elif sad_count > happy_count:
    print("Analysis: The tone of the sentence is Negative (Sad).")
else:
    print("Analysis: The tone of the sentence is Neutral.")