
list_1 = [1, 2, 3, 4, 5]
list_2 = ['A', 'B', 'C']

tuple_1 = ("Walid","Omar",'Khalaf','Mahomud')

dict_1 = {'Name' : 'Walid', 'Age' : 26 , 'Country' : 'Egypt'}

for item1,item2,item3,item4 in zip (list_1,list_2,tuple_1,dict_1):  #it will loop for the lowest number of the compination ==> 3

    print(f"List 1 Item ==> {item1}")
    print(f"List 2 Item ==> {item2}")
    print(f"Tuple  Item ==> {item3}")
    print(f"Dictionary key == > {item4} With value {dict_1[item4]}")