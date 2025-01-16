from collections import Counter

text = """
Frank Ocean born Christopher Edwin Breauxis an American singer and songwriter. He has been credited 
by several music critics as a pioneer of the alternative R&B genre.Ocean has won two Grammy Awards 
and a Brit Award for International Male Solo Artist, 
among other accolades; both of his studio albums have been listed on Rolling Stone's five hundered Greatest Albums of All Time.
"""
words = text.lower(). split()
word_count = Counter(words)

#print("Word Frequencies:")
#for word, count in word_count.items():
    #print(f"{word}: {count}")
print(len(text))

top_3_words = word_count.most_common(3)

print("Top 3 Most Frequent Words:")
for word, count in top_3_words:
    print(f"{word}: {count}")

