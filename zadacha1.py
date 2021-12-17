# list = [1, 1, 3, 2, 1, 3, 4]
# my_dict = {i:list.count(i) for i in list}
# print(my_dict)

def count_digit(num_list):
    set1 = set(num_list)
    list1 = list(set1)
    for i in list1:
        result = num_list.count(i)
        print(f'Число {i} встречаеться {result}')


num_list = [1, 1, 3, 2, 1, 3, 4]
count_digit(num_list)
