def fibonacci(n):
  if n <= 0:
      return "Input should be positive integer"
  elif n == 1:
      return [0]
  elif n == 2:
      return [0, 1]
  else:
      fib_sequence = [0, 1]
      for i in range(2, n):
          fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
      return fib_sequence
n = 20
print(fibonacci(n))