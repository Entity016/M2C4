import math
# Exercise 1
list = ['one', 'two', 'three']
tuple = ('four', 'five', 'six')
float = 7.8
integer = 9
decimal = 10.1112
dict = {
    "Name" : "Pablo",
    "Course" : "Full Stack"
}

# Exercise 2
print(round(float))

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
tuple = tuple + ('seven',)
print(tuple)