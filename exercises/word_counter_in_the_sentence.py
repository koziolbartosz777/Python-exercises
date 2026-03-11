# user_input = input("Enter your longer sentence: ")

# dict = {}
# input_list = user_input.split()


# for word in input_list:
#     if word not in dict:
#         dict[word]=1
#     elif word in dict:
#         dict[word]+=1

# print(dict)    

#-----------------------------------------------


# from collections import Counter

# text = input("Enter your longer sentence: ")
# word_counter = Counter(text.split())
# print(word_counter)
# print(f"Most common word: {word_counter.most_common(1)[0][0]}")

#-----------------------------------------------
from collections import Counter

text = input("Enter your longer sentence: ")

word_counter = Counter(text.split())
# print(word_counter)
for word, count in word_counter.items():
    print(f"Słowo {word} wystąpiło {count} raz(y)")

print("-"*25)
print(f"Najczęściej występujące słowo to : {word_counter.most_common(1)[0][0]}")