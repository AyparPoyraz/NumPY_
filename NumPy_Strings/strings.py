import numpy as np

#Single Dimension
                 #0#1#2#3#4   
data1 = np.array([1,2,3,4,5])
print([data1[0] + data1[2]])

#Two Dimensional
                  #0       #1       #2       #3
data2 = np.array([[1,2,3], [4,5,6], [7,8,9], [13, 15, 18]])

#Exp:
#Check Data List
print(data1[2] ** 2) #**2 //squaring == 9  or you can get a sample of data from any list

# For range (len) for two dimesional:
for i in range(len(data2)):
    for j in range(len(data2[i])):
        print(data2[i][j], end=' ')  #Transactions can be Regulated by Checking Data here
    print()

print("Exp 2 :")
print()

# 2 Exmp
for row in data2:
    for elem in row:
        print(elem,end=' ')
    print()

print()

#Total for the entire list
t = 0
for i in range(len(data2)):
    for j in range(len(data2[i])):
        t += data2[i][j]
    print(t)

# nested data:
n = 3
m = 4
data2 = [[0] * m] * n
data2[0][0] = 60
print(data2[1][0])

# Join Two Diemesional
#2.
b = int(input())
data2 = []
for i in range(b):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    data2.append(row)



    


