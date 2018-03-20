
print('Quiz:How pathetic are you? Instructions: you will get a set of questions and at the end however manypoints you have out of five is how else you are to truly pathetic. 5 is 100% pathetic')
      
#1st question
print('1st question')
print('How old are you?')

points = 0
age = int(input())

if age > 0 and age <= 15:
    points += 1

#2nd question
print('2nd question')
print('How many significant others have you had?')

SignificantOthers = int(input())

if SignificantOthers > 0 and SignificantOthers <= 3:
    points += 1

#3rd question
print('3rd question')
print('How many times have you fallen on your face?')

facehits = int(input())

if facehits > 3 and SignificantOthers <= 100:
    points += 1

#4th question
print('4th question')
print('How many times are you shit your pants?')

shit = int(input())

if shit> 1 and shit <= 100:
    points += 1

print('look at how many points you have and accept the truth about how pathetic you are.')

print('well, it has been fun. Bye B*tch')

#5th question
print('5th question')
print('How many times have you thought (you know what i mean) about your friends parent in that way?')

times = int(input())

if times > 1 and times <= 999:
    points += 1



