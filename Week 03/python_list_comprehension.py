"""
    Comprehensions:
         - Comprehensions in Python are a way to create a new sequence from an already existing sequence.

         There are four main types of comprehensions in Python:
            - List comprehension
            - Dictionary comprehension
            - Set comprehension
            - Generator comprehension
"""

# Syntax: [ <expression> for x in <sequence> if <condition> ]
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x * 2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)
""""
    # List comprehension:
    data = [x + 3 for x in data]
    
    # Regular for loop:
    for x in range(len(data)):
        data[x] = data[x] + 3
    print(data)
"""
"""
    Here is the difference between map() function and list comprehensions:
    
        newdata = map(square, data)
        
        newdata = [x + 3 for x in data] 
    
    Notice how both map() functions and list comprehension effectively do the same job of modifying iterator sequences such as the list in the example above.
    List comprehensions have been a relatively recent development but it does not necessarily mean they are more efficient.
    Comprehensions have gained popularity primarily for providing cleaner code readability and ease of use.
    They also provide some added advantages such as providing filtering using if else conditions.
    List comprehensions also provide direct return of a list as compared to map() function that returns a map object.
    It is mainly the clarity that has made list comprehensions popular, but map() functions are still arguably a better choice when it comes to the use of larger sequences.
"""
a = [[96], [33]]

print(''.join(list(map(str,a))))