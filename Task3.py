def shift_left(input2):
    if input2 < 0:
        print(list(input1[-input2:] + input1[:-input2]))

def shift_right(input2):
    if input2 > 0:
        print(list(input1[-input2:] + input1[:-input2]))

# input1 = list(input("Input some numbers with spaces: ").split(" "))
input1 = [1,2,3,4,5]
input2 = int(input("Input number to shift numbers: "))
print(input1)

if int(input2) < 0:
    shift_left(input2)
elif int(input2) > 0:
    shift_right(input2)
else:
    print("Can't use '0'")