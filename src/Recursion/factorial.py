# Naive factorial implementation
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

def main():
    n = int(input('Insert a positive number: '))
    while n >= 0:
        print(factorial(n))
        n = int(input('Insert a number: '))
    print('Bye')

if __name__ == '__main__':
    main()
