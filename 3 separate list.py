array = [1,2,3,4,5,6,7,8,9]
list = [array[i:i+3] for i in range (0,len(array),3)]
print(list)
