def reverseStr(str):
    return str[::-1]
    
names = ["David", "Emma", "Gabriel", "Raphael"]
reversedStr = map(reverseStr, names)

for name in reversedStr:
    print(name)
