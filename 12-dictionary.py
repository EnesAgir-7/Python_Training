my_dict = {
    #^ 'Key' : 'value' 
            #& => 2 ayni key ile farkli value giremeyiz her bir key 1 tane olmali 
    'name': 'Pasha',
    'nationality': 'Turkish',
    'age': 27,
    'is_tall': True,
    'Qualification': 'College',
    'friends':['Ali','Veli','Yahya']
}
x = my_dict['name']

print(type(my_dict))
print(my_dict)
print(my_dict['name'])
print(len(my_dict))
print(my_dict['is_tall'])
print(my_dict['friends'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items)
print(x)
