# We are seen more examples of control flow loops

# Here we are taking same favorites desert example

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

# for loop using if condition
for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)

# for loop else block
for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
else:
    print('No sorry, that dessert is not on my list')

# `break` The code works as intended, but you may notice one flaw. If you change the search term to something that is on the list like "Churros" and run it again
for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break
else:
    print('No sorry, not a dessert on my list')

# `continue` Similar to break, continue can be used to control the iteration of the loop. The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest.
for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)

# `pass` The pass statement allows you to run through the loop in its entirety and effectively ignore that the if condition has been satisfied.
for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)