"""
Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200
¡
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
depsit=[a for a in input("enter deposit amount:").split(',')]
withdrw=[a for a in input("enter withdraw amount").split(',')]
total=0
for i in depsit:
    total=total+int(i)
for i in withdrw:
    total=total-int(i)
print("net amount is",total)
