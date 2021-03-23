
PATH = 'tvr.txt'

file = open(PATH, mode='r')
array_file = (file.read()).splitlines()
print(array_file)
arr2 = ''.join(array_file)
arr3 = arr2.split(', ')
new_final_list = []
for i in arr3:
    x = i.split(" ")
    new_final_list.append(x)
print(new_final_list)

