
def password(x):
    y =''
    for i in range(1,x):
        for j in range(i+1,x):
            if x % (i+j) == 0:
                y += str(i)+str(j)
    return y


print("Введите число:",end='')
print(password(int(input())))


