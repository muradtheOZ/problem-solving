while True:
    mainInput = input()
    splitInput = mainInput.split()
    n = int(splitInput[0])
    m = int(splitInput[1])

    if n == 0 and m == 0:
        break

    remaining = ( m -n)

    billList = [2,5,10,20,50,100]
    result = 0
    counter = 0
    for i in range (len(billList)):
        tempValue = billList[i]
        for j in range (len(billList)):
            result = billList[i]
            counter = 0
            for k in range(1):
                if billList[j] != tempValue:
                    result += billList[j]
                    counter += 1
                        
                if result == remaining:
                    if counter == 0:
                        continue
                    else:
                        break
            if result == remaining and counter != 0:
                    break
        if result == remaining and counter != 0:
                    break
    if result == remaining:
        print("possible")
    else:
        print("impossible")

