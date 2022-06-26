#Code_1
numberOfSeconds = int(input('How long is the number of seconds: '))
numberOfMinutes = (numberOfSeconds // 60)

numberOfSeconds = (numberOfSeconds % 60)

if numberOfMinutes < 10:
    numberOfMinutes = '0' + str(numberOfMinutes)

if numberOfSeconds < 10:
    numberOfSeconds = '0' + str(numberOfSeconds)

print('your run was ' + str(numberOfMinutes) + ':' + str(numberOfSeconds))