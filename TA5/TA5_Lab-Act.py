from textblob import TextBlob

positive_count = 0
neutral_count = 0
negative_count = 0

for i in range(1, 11):
    sentence = input(f"Enter sentence {i}: ")
    s = TextBlob(sentence)
    p = s.sentiment.polarity

    if p < 0:
        print("Sentiment: Negative\n")
        negative_count += 1
    elif p == 0:
        print("Sentiment: Neutral\n")
        neutral_count += 1
    elif p > 0 and p <= 1:
        print("Sentiment: Positive\n")
        positive_count += 1

print("--- SENTIMENT SUMMARY ---")
print(f"Positive sentences: {positive_count}")
print(f"Neutral sentences:  {neutral_count}")
print(f"Negative sentences: {negative_count}")