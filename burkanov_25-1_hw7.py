ten = list(range(1,11))
evens = list (filter(lambda x:x % 2 == 0, ten))
evens1 = list (map(lambda x:x**2,evens))

# print (evens1)
# def function(lst=(list(ten))):
#     while True:
#         index = input("введите индекс для вывода обьекта из списка.")
#         if index.lower() == 'exit' or index.lower() == "выход":
#             break
#         try:
#             print(lst[int(index)])
#         except:
#             print(f'Введите индекс от {ten}')
# function()
