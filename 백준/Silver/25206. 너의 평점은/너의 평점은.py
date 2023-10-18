credit = 0
score = 0
grade = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
for i in range(20):
    a = list(input().split())
    if a[2] != 'P':
        thiscredit = int(float(a[1]))
        credit += thiscredit
        score += grade[a[2]]*thiscredit
print(score/credit)