def sum_squares(n):
    # Using list comprehension and built-in sum() for better performance
    return sum(i*i for i in range(2, n+1, 2))

if __name__ == "__main__":
    print(sum_squares(100000))
