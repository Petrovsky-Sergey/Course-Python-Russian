# put your python code here
i = int(input())
c = i % 10
b = (i // 10) % 10
a = i // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

