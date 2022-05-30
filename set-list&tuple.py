value = input("input number seeperated by comma: ")
list = value.split(",")
tuple = tuple(list)
print('List is: ', list)
print("Tuple is: ", tuple)

filename = input("Input the Filename: ")
f_extens = filename.split(".")
print("The extenions of the file is :  " + repr(f_extens[-1]))
