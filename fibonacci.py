"""Fibonacci Series Generator.

Give a number N, it prints the Fibonacci series up to N terms.
If no number is given, it defaults to 0 (prints nothing).
"""

import sys  # needed to read the number passed from the command line


def fibonacci_series(n):
    """Return a list containing the first n Fibonacci numbers."""
    if n <= 0:                      # if input is 0 or negative, return empty series
        return []
    if n == 1:                      # if input is 1, series is just [0]
        return [0]

    series = [0, 1]                 # first two Fibonacci numbers are always 0 and 1
    for _ in range(2, n):           # loop from the 3rd term up to the nth term
        next_num = series[-1] + series[-2]  # next term = sum of last two terms
        series.append(next_num)     # add the new term to the series
    return series                   # give back the full series


def main():
    # sys.argv[0] is the script name, sys.argv[1] is the first argument (the number)
    if len(sys.argv) > 1:           # check if the user passed a number
        try:
            n = int(sys.argv[1])    # convert the text argument into an integer
        except ValueError:          # if they passed something like "abc"
            print("Error: please pass a valid integer, e.g. python fibonacci.py 7")
            sys.exit(1)             # exit with error code 1 so CI marks it as failed
    else:
        n = 0                       # default value when no argument is given

    result = fibonacci_series(n)    # calculate the series

    print(f"Input number: {n}")     # show what input was used
    if result:                      # if the series has values
        print(f"Fibonacci series ({n} terms): {result}")
    else:                           # empty series for n = 0
        print("Fibonacci series: [] (default is 0, so no terms generated)")


if __name__ == "__main__":          # run main() only when executed directly, not on import
    main()
