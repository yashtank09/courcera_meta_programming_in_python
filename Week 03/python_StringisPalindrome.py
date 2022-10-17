# String is palindrome or not using functions
def isPalindrome(Str):
    startIndex = 0
    endIndex = len(Str) - 1
    for x in Str:
        if Str[startIndex] != Str[endIndex]:
            startIndex += 1
            endIndex -= 1
            return False
    return True


print(isPalindrome('racsdgar'))


# Using different approach
# Algorithm for a palendrome
def isPalin(a):
    sI = 0
    eI = len(a) - 1
    print(eI)

    for x in a:
        if a[sI] != a[eI]:
            return False
    return True


print(isPalin('rar'))

"""
    There are many different types of algorithms that have been designed to solve all kinds of different types of problems in computer science. When writing an algorithm, it can be solved in many different ways and each can have its own pros and cons. 
    
    Recursion
    Recursion refers to a method or a function that will call itself. It is used to resolve problems by breaking the problem down into sub-problems. Let us take a look at some of the most popular types of recursive algorithms.
    
    Divide and conquer
    This consists of two parts. The first is breaking the problem down into smaller sub-problems and the second is solving the final solution.
    
    Dynamic programming
    This is mainly used for optimization problems. It is similar to the divide and conquer algorithm in that it splits the problems into sub-problems.
    
    Greedy algorithm
    This one finds the best solution in each and every step instead of approaching optimization in a global way.
"""
