names = ["Chukwumam Akachukwu", "Jimoh Reahanat", "Omoyibo Samuel", "Chekube Madu", "Chukwumam Mesoma"]

def findPerson(name):
    if "Chukwumam" in name:
        return name
    
mappedNames = map(findPerson, names)

for name in mappedNames:
    print(name)
    
filteredNames = filter(findPerson, names)

for name in filteredNames:
    print(name)
    
a = [[96], [69]]

print(''.join(list(map(str, a))))