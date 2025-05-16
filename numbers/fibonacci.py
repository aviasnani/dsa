def check_fibonacci(n):
  if n == 0 or n == 1:
    return None
  fib = [0, 1]
  for i in range(2, n):
    next_val = fib[i-1] + fib[i-2]
    fib.append(next_val)
  return fib

print(check_fibonacci(7))