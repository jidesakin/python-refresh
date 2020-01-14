# generator
xyz = (i for i in range(50000000))
print(list(xyz)[:5])

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

input_list = [4, 4, 5, 10, 12, 7, 6]

xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))

# list comprehension
xyz = [i for i in range(50000000)]
print(xyz[:5])

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)