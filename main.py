import math
from decimal import Decimal
# Exercise 1
list = ['one', 'two', 'three']
tuple = ('four', 'five', 'six')
float = 7.8
integer = 9
predecimal = 10.1112
decimal = Decimal(predecimal)
print(decimal)
dict = {
    "Name" : "Pablo",
    "Course" : "Full Stack"
}

# Exercise 2
print(math.ceil(float))

# Exercise 3
print(math.sqrt(float))

# Exercise 4
element = dict.get('Name')
print(element)

# Exercise 5
print(tuple[1])

# Exercise 6
list_two = ['Lunes', 'Martes']
list_two.append('Miercoles')
print(list_two)

# Exercise 7
list[0] = 'ten'
print(list)

# Exercise 8
list_three = ['oveja', 'vaca', 'perro']
sorted_list = sorted(list_three)
print(sorted_list)

# Exercise 9
tuple += ('seven',)
print(tuple)