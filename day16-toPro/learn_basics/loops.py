# for loop
print('---------for loops---------')
primes = [2,3,5,7]
for prime in primes:
    print(prime, end=' ')
print('')
for x in range(5):
    print(x, end=' ')
print('')
for x in range(3,6):
    print(x, end=' ')
print('')
for x in range(3,8,2):
    print(x, end=' ')
print('\n---------while loops---------')
# while loop
count = 0
while count<5:
    print(count, end=' ')
    count += 1
print(' ')

# break and continue statements
# break : is used to exit a for/while loop
# continue: is used to skip the current block, and return to the for/while statement

# example1 : prints out 0,12,3,4
print('==break example==')
count=0
while True:
    print(count, end=' ')
    count += 1
    if count >= 5:
        break
print(' ')
# example2: prints out only odd numbers - 1,3,5,7,9
print('==continue example==')
for x in range(10):
    # check if x is even
    if x % 2 == 0:
        continue
    print(x, end=' ')
print('')
# using else clause with loops
print("==Else clause example with loops==")
count = 0
while count < 5:
    print(count, end=' ')
    count += 1
else:
    print("\nCount value reached %d" % count)
