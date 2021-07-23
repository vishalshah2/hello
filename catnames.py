catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames)) + ' (Enter Nothing to stop)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
    
print('The name of cates are ')
print(catNames)

for i in catNames:
    print(i)
