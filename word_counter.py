''''Counting same words in a text'''
# 1stmethod:
import re

word_counter = {}
str_input = input("Please enter a text: ").lower()
word_pattern = re.findall(r'\b\w+\b', str_input)
for word in word_pattern:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

print(word_counter)


# 2nd method:
# import re

# word_counter = {}
# user_input = input("Please enter a text: ").lower()
# clean_input= re.sub(r'[!?.,;:-_]', '', user_input)
# words = clean_input.split()
# for word in words:
#     counter= words.count(word)
#     word_counter.update({word : counter})

# print(word_counter)


