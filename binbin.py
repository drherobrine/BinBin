
decNum = 0
binNum = 0
pow2Num = 1

def binFunc():
    global decNum
    global binNum
    global pow2Num
    for x in range(0, 8):
        while pow2Num <= int(decNum):
            pow2Num *= 2
            if pow2Num > int(decNum):
                pow2Num /= 2
                break
        int(decNum) -= int(pow2Num)
        if pow2Num == 128:
            binNum += 10000000
        elif pow2Num == 64:
            binNum += 1000000
        elif pow2Num == 32:
            binNum += 100000
        elif pow2Num == 16:
            binNum += 10000
        elif pow2Num == 8:
            binNum += 1000
        elif pow2Num == 4:
            binNum += 100
        elif pow2Num == 2:
            binNum += 10
        elif pow2Num == 1:
            binNum += 1

        str(binNum)
        if len(binNum) == 1:
            binNum = "0000000" + binNum
        elif len(binNum) == 2:
            binNum = "000000" + binNum
        elif len(binNum) == 3:
            binNum = "00000" + binNum
        elif len(binNum) == 4:
            binNum = "0000" + binNum
        elif len(binNum) == 5:
            binNum = "000" + binNum
        elif len(binNum) == 6:
            binNum = "00" + binNum
        elif len(binNum) == 7:
            binNum = "0" + binNum

        pow2Num = 1
    print(binNum)


while True:
    decNum = input("What is your Number?")
    binFunc()
    int(binNum)
    binNum = 0