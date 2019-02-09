#converte kms em milhas

print('How many kilometers did you cycle today? ')
kms = input()
miles = float(kms) / 1.60934
miles = round(miles, 2)

print('That is equal to ' + str(miles) + ' miles')
