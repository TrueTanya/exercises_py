name = 'Matt'
first = name
age = 1000
print(id(age))
age = age + 1
print(id(age))
names = []
print(id(names))
names.append('Freud')
print(id(names))

variable_float = 1.5
print(id(variable_float))
print(type(variable_float))
print(variable_float)
variable_float = variable_float + 20
print(id(variable_float))
print(type(variable_float))
print(variable_float)
