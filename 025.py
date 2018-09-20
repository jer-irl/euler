def fib():
    a = 1
    b = 1
    yield a
    while True:
        yield b
        prev_a = a
        a = b
        b = prev_a + b

for i, f in enumerate(fib()):
    if len(str(f)) == 1000:
        print(f)
        print(i + 1)
        break
