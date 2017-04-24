decNum = 0
binNum = [0, 0, 0, 0, 0, 0, 0, 0]



def binFunc():
    global decNum
    global binNum
    global pow2Num
    global powerCount
    binNum = [0, 0, 0, 0, 0, 0, 0, 0]

    while decNum != 0:
        pow2Num = 1
        powerCount = 0
        while pow2Num <= decNum:
            pow2Num *= 2
            powerCount += 1
        pow2Num //= 2
        powerCount -= 1

        decNum -= pow2Num
        binNum[powerCount] = "1"

    binNum.reverse()
    print(binNum)

print("Type in a number between 0 and 255. Press Ctrl + C to exit.")
while True:
    decNum = int(input("Input a number between 0 and 255 "))
    if decNum > 255:
        while decNum > 255:
            print("This number is too big. Type in a number less than 256.")
            decNum = int(input("Input a number between 0 and 255 "))
    elif decNum < 0:
        while decNum < 0:
            print("This number is too small. Type in a number greater than 0.")
            decNum = int(input("Input a number between 0 and 255 "))
    binFunc()