try:
    while True :
        num = int(input('Enter a positive number: '))
        if num >= 0 :
             print(num * num)
        else :
             raise ValueError('Negative number')
except ValueError as ve :
   print(ve.args)
output:
Enter a positive number: 88
7744
Enter a positive number: 6
36
Enter a positive number: 78
6084
Enter a positive number: -8
('Negative number',)
