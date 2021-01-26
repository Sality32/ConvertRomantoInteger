def romansConvert(numRomans):
    res = 0
    if numRomans == "I":
        res += 1
    elif numRomans == "V":
        res += 5
    elif numRomans == "X":
        res += 10
    elif numRomans == "L":
        res += 50
    elif numRomans == "C":
        res += 100
    elif numRomans == "D":
        res += 500
    elif numRomans == "M":
        res += 1000
    return res

def romanToInteger(listString):
    lst = list(listString)
    result = 0
    i = 0
    x = len(lst)
    while i < x:
        if i != x-1:
            if(lst[i]=="I" and (lst[i+1]=="V" or lst[i+1]=="X") ):
                i+=1
                result += romansConvert(lst[i])
                result -= 1
            elif(lst[i] == "X" and (lst[i+1] == "L" or lst[i+1] == "C") ):
                i += 1
                result += romansConvert(lst[i])
                result -= 10
            elif(lst[i] == "C" and (lst[i+1] == "D" or lst[i+1] == "M")):
                i += 1
                result += romansConvert(lst[i])
                result -= 100
            else:
                result += romansConvert(lst[i])
            i+=1
        else:
            result += romansConvert(lst[i])
            i+=1

    return result


res = romanToInteger("III")
print(res)
