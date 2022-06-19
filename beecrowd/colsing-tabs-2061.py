
takeInput = input()
twoVar = takeInput.split()

tab = int(twoVar[0])
action = int(twoVar[1])

for i in range (action):
    s = input()
    if(s == "fechou"):
        tab += 1
    else:
        tab -= 1
print(tab)