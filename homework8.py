list1 = [2, 5, 3, 4, 5, 7, 3, 6, 7, 7, 7, 3, 3]
dct = {}

def func1(list2, dict1):
    for i in list2:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for item in dct:
        print("'%d':%d" % (item, dct[item]))

func1(list1, dct)



