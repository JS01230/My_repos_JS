#Power Up
#Simulates exponents without using ** a single time

def powerup(x, y):
    i = 0
    j = 1
    while i < y:
        j = j * x
        i += 1
    if i == y:
        return j


print(powerup(2, 5))
print(powerup(3,3))

print(powerup(10, 10))
