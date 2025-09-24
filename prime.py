
num = int(input('Enter a number: '))
d = 1
cnt = 0
while d < 0:
    if num % d == 0:
        cnt = cnt + 1
    d = d+1
if cnt == 2:
    print('Prime')
else:
    print('Not prime')
