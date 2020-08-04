
n,m = input().split()
n = int(n)
m = int(m)
str = '.|.'
for i in range(n//2):
    str_final = str*i + str + str*i
    print(str_final.center(m,'-'))

print('WELCOME'.center(m,'-'))

for i in range(n//2-1, -1, -1):
    str_final = str*i + str + str*i
    print(str_final.center(m,'-'))
