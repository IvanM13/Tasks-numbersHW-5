def Compress (oneString: str):
    secondString = ''
    my_lst = [0]
    for i in range(1, len(oneString)):
        if oneString[i] != oneString[i - 1]:
            my_lst.append(i)

    my_lst.append(len(oneString))
    for j in range(0, len(my_lst) - 1):
        secondString += (oneString[my_lst[j]:my_lst[j + 1]]) + ' '

    stringArr = secondString[:-1]
    splitList = stringArr.split(" ")
    pressArr = ''
    for k in range(0, len(splitList)):
        pressArr += str(len(splitList[k])) + str(splitList[k][0])
    return pressArr


with open('File1.txt', "r") as originDoc:
    originStr = originDoc.readline()
print(originStr)
print(Compress(originStr))
with open("Compress_File1.txt", 'w') as compressDoc:
    compressDoc.write(Compress(originStr))