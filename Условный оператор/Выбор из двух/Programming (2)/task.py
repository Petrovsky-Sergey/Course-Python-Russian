# put your python code here
i = int(input())
a = i // 1000 
b = (i // 100) % 10
c = (i // 10) % 10
d = i % 10
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')


