def greet(name):
    print("Привет,",name)

def square(number):
    return(number*number)

def max_of_two(x, y):
    if x>=y:
        return x
    else:
        return y

name = "Ivan"
num = 7
a = 4
b = 6

greet(name)
print(square(num))
print(max_of_two(a,b))