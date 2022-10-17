# str[start_index : stop_index : steps]

# reversing string
trial = "reversal"

new_trial = trial[::-1]

print(new_trial)

# Using slice function with different ways

# Declaring a string
value_String = "absolute"

print("This will remove first character from given string: " + value_String[1:])  # Output: bsolute
print("This will print index 1 to 5 character: " + value_String[1:5])  # Output: bsol
print("This will print index 0 to 8 and skip the second index: " + value_String[0:8:2])  # Output: aslt
print("This will print every odd indexes: " + value_String[::2])  # Output: aslt
print("This will skip two character and print third one: " + value_String[::3])  # Output: aot
