def findSubStr(substr, str, i):
    count = 0
    while i > 0:
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index+1:]   #第一次出现的位置截止后的字符串
            print (str)
            i -= 1
            count = count + index + 1   #字符串位置数累加
    return count - 1

print(findSubStr('23','123456789101112131415161718192021222324252627282930313233343536...',3))
