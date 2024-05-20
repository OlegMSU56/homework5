my_list=['apple', 'banana', 'orange', 'kiwi',5,9,88]
print(my_list)
print(my_list[0]) #первый элемент
print(my_list[-1]) #последний элемент
print(my_list[2:4]) #элементы с третьего до пятого
my_list[2]="melon" #замена третьего элемента списка
print(my_list)
my_dict={'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
print(my_dict)
print(my_dict['banana'])#значение для заданного ключа
my_dict['elefant']='слон'#добавил новый ключ и значение
my_dict.update({'banana':'помидор'})#изменил значение для заданного ключа
print(my_dict)