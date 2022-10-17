# reversing a string using recursion
def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        # reversing string
        return reverse_string(str[1:]) + str[0]


str = "reversal"
ReversedString = reverse_string(str)
print(ReversedString)
