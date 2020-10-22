def fizzbuzz(number):
  '''If number div by 3 print 'fizz', if div by 5, then 'buzz', if 3 and 5 'fizzbuzz' '''

  for x in range(number+1):
    if x % 3 == 0 and x % 5 == 0:
      print(x,'FizzBuzz')
    elif x % 3 == 0:
      print(x,'Fizz')
    elif x % 5 == 0:
      print(x,'Buzz')
    else:
      print(x)
