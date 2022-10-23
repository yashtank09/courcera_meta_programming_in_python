import nltk

# First a block of text is copied inside the code-block and assigned to a variable called text.
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# nltk.download()
# Print statement 1
# word_tokenize() takes this text and produces the first part of the output in which the words are ‘tokenized’ or simply separated by a whitespace.
# The same can be done with the split() function in the string, but the use of the package is far more efficient when it comes to larger blocks of code.
print(word_tokenize(text))

# Print statement 2
# The second function sent_tokenize() takes this block of text and tokenizes by ‘sentences’.
print(nltk.tokenize.sent_tokenize(text))

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)
