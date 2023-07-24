no = int(input('Enter a number: '))
c = 0

print(no)
while not no == 1:
    if no % 2 == 0:
        no = no/2
    else:
        no = no * 3 + 1
    c = c + 1
    print(no)
print(f'{c} is number of iterations')
