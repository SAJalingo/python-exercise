score = 0
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
elif score >= 0 and score < 60:
    print('F')
elif score < 0:
    print('You entered a negative number... Not within marking range!')
else:
    print('You eneterd above 100... out of marking range!!!')