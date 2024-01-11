def get_prime_factors(number):
  factors = []
  divisor = 2
  while divisor <= number:
    if number % divisor == 0:
      factors.append(divisor)
      number //= divisor
    else:
      divisor += 1
  return factors

if __name__ == '__main__':
  print(get_prime_factors(630))
  print(get_prime_factors(13))



