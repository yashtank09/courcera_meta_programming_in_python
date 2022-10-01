# While loop is entry controlled loop as like for with different syntax

# here we are using the same favorite desert example
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# initializing count for condition check
count = 0

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count])
    # incrementing value of count, so it will stop when condition became true
    # and if I do not increment count then it will end up in infinite loop and will looping and looping until the compiler stops it from running out of memory.
    count += 1
