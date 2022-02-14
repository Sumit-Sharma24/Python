# Lists and Lists Function
grocery = ["Dettol", "Maggie", "Tooth paste", "Cold drinks", 34]
print(grocery)
numbers = [2, 3, 67, 23, 54, 23]
"""numbers.sort() --> It changes the original list
numbers.reverse() --> It changes the original list
print(numbers)
print(numbers[0:5])
print(numbers[:])
print(numbers[::])
print(numbers[::2])
print(numbers[::-1])
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(len(grocery))
numbers.append(99)"""
print(numbers)
numbers.insert(6, 56)
print(numbers)
numbers.insert(9, 33)
print(numbers)
numbers.remove(33)
print(numbers)
numbers.pop()
print(numbers)
numbers[0] = 45
print(numbers)
# Mutable --> can change
# Immutable --> can't change
tp = (1, 2, 3)  # This is a tuple
print(tp)

# Swapping of numbers
a = 1
b = 7
a, b = b, a
# temp = a
# a = b
# b = temp
print(a, b)

