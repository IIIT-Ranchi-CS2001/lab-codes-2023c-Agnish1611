name = input('Name: ')
roll = input('Roll: ')
marks = int(input('Marks: '))

print('Name: ', name, '\nRoll Number: ', roll, '\nMarks: ', marks)

if (marks>=90): 
    print('Grade Point: 10 \nRemark: OUTSTANDING')
elif (marks>=80):
    print('Grade Point: 9 \nRemark: VERY GOOD')
elif (marks>=70):
    print('Grade Point: 8 \nRemark: GOOD')
elif (marks>=60):
    print('Grade Point: 7 \nRemark: AVERAGE')
elif (marks>=50):
    print('Grade Point: 6 \nRemark: PASS')
else:
    print('Grade Point: 0 \nRemark: FAIL')