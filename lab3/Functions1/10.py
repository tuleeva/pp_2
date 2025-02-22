#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#  Note: don't use collection `set`.
def Unique(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

input_list = [1, 2, 2, 3, 4, 4, 5]
print(Unique(input_list))