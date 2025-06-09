# Sum of squares of even numbers from 1 to n
def sum_squares(n):
    result = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            result = result + i*i
    return result

print(sum_squares(100000))
