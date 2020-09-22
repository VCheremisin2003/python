number = 8
list_1 = list("hi i am list")
str_1 = "this is string"
set_1 = {1,2,4,2,6,4}
dict_1 = dict(name="Valya", surname="Cheremisin")
tuple_1 = ("1","2","3")

my_list = [list_1, str_1,set_1,dict_1,tuple_1]
for item in my_list:
    print(type(item))