squares_of_evens = []
for x in range(11):
    if x % 2 == 0:
        squares_of_evens.append(x ** 2)

print(squares_of_evens)


squares_of_evens = [number * number for number in range(0, 11) if number % 2 == 0]
print(squares_of_evens)