'''
loop control 

can be used else in loops

for i in range(1,11):
    if i == 5:
        break #break - prints till 4(1 to 4) 
    print(i)


for i in range(1 , 11):
    if i == 5:
        continue #continue - prints till 10 ( 1 to 10 but 5 is not included)
    print(i , end = " ")
else:
    print("loop completed")

password retry system(max 3 attempts)
if password is correct show login successful
else ask for password 3 times
once attempts exceed show account locked
'''
p1 = "abc123"
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("login successful")
        break
else:
    print("account locked")


    