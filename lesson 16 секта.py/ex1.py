a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))
if (a==b) and (c==b):
#     print('3')
# else:
    print('all numbers coinside')
elif (a==b) or (b==c) or (a==c):
    print('two numbers coinside')
else:
    print('all numbers are different')