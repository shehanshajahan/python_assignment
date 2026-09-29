def sum_numbers(*args):
    sum=0
    for x in args:
        sum+=x
    return sum
print(sum_numbers(32,30))
print(sum_numbers(4,6,90))
print(sum_numbers(65,1,6,7))
