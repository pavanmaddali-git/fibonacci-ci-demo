"""Fibonacci Series Generator.

Give a number N, it prints the Fibonacci series up to N terms.
If no number is given, it defaults to 0 (prints nothing).
"""

import sys


def fibonacci_series(n):
    """Return a list containing the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]
    for _ in range(2, n):
        next_num = series[-1] + series[-2]
        series.append(next_num)
    return series


def main():
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Error: please pass a valid integer, e.g. python fibonacci.py 7")
            sys.exit(1)
    else:
        n = 0

    result = fibonacci_series(n)

    print(f"Input number: {n}")
    if result:
        print(f"Fibonacci series ({n} terms): {result}")
    else:
        print("Fibonacci series: [] (default is 0, so no terms generated)")


if __name__ == "__main__":
    main()
