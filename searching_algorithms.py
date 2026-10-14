#Linear
def search_list(example_list, n):
    example_list.sort()
    for i in example_list:
        if i>n:
            return 'no'
        if i==n:
            return 'yes'
    return 'no'
x=[8,5,3,5,3,7,9,15,10]
print(search_list(x, 6))
