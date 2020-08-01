
# using if
even_numbers = [x for x in range(20) if x %2 == 0]
print(even_numbers)

# nested if comparison
# to check if divisble by 2 then check for 5 divisibility
divisibles_2_5 = [x for x in range(100) if x %2 == 0 if x %5 == 0]
print(divisibles_2_5)

# if-else comparison
even_odd_10 = ["Even" if x%2==0 else "Odd" for x in range(10)]
print(even_odd_10)

# nested loops
# transpose a matrix
matrix = [[1,2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)

# another one
matrix1 = [[1,2,3,4], [4,5,6,8]]
transpose1 = [[row[i] for row in matrix1] for i in range(4)]
print(transpose1)
