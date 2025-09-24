
num = int(input('Enter a number: '))

for d in range(2,(num//2)+1):
    if num % d == 0:
        print('Not prime')
        break
else:
    print('Prime')
