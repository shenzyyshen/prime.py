
def is_divisible_by(number, by):
  return number % by == 0

def is_prime(number):
  if number <=1:
    return False
  for i in range(2, int(number ** 0.5) +1):
    if is_divisible_by(number, i):
      return False
  return True

def primes_in_range(start, end):
  for num in range(start , end):
    if is_prime(num):
      print(num)

def main():
  start = int(input("Enter start range: "))
  end = int(input("Enter end range: "))
  primes_in_range(start, end)

if __name__=="__main__":
  main()
