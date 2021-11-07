# Iterate through the numbers 1 through 100 and do the following:
#   If the number is divisible by 3 then print 'fizz'
#   If the number is divisible by 5 then print 'buzz'
#   If the number is both divible by 3 AND 5 then print 'fizzbuzz'
#   If the number is none of the above print number.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        # Divisible by 3 and 5
        print('fizzbuzz')
    elif number % 5 == 0:
        # Divisible by 5
        print('buzz')
    elif number % 3 == 0:
        # Divisible by 3
        print('fizz')
    else:
        print(number)