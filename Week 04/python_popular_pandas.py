import pandas as pd

# The first output is for the DataFrame called a that displays the output in a very systematic format
a = pd.DataFrame({'Animals': ['Dog', 'Cat', 'Lion', 'Cow', 'Elephant'],
                  'Sounds': ['Barks', 'Meow', 'Roars', 'Moo', 'Trumpet']})

# it will print dataframe in readable format
print(a)

# The second output uses to describe() function in pandas that will give the count, frequency, top values and frequency among other values.
print(a.describe())

# In the second DataFrame, b consists of letters and numbers in random order.
b = pd.DataFrame({
    "Letters": ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers": [12, 7, 9, 3, 5, 1]})

# The third output is a sorting function that will provide a sorted table leading to shuffling of the data entries in the table.
print(b.sort_values(by="Numbers"))

# Lastly, the assign() function takes the values present inside the table, performs an operation over them and creates a new variable called new_values that is then added to the table.
b = b.assign(new_values=b['Numbers'] * 3)
print(b)
