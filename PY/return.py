print("Simple Calculator v1.0 by Aiden")
print("Note: For the current version, only 1 use of each operation is supported per equation (+,-,/,*)")
def Calculate(calculation):
    calcArr = calculation.split(' ')
    # Multiplication & Division
    if "*" in calcArr or "/" in calcArr:
        if "*" in calcArr: mpos = calcArr.index("*")
        else: mpos = 0
        if "/" in calcArr: dpos = calcArr.index("/")
        else: dpos = 0
        if mpos > dpos:
            mposm = int(calcArr[mpos-1]) * int(calcArr[mpos+1])
            calcArr[mpos-1:mpos+2] = [mposm]
        else:
            dposd = int(calcArr[dpos-1]) / int(calcArr[dpos+1])
            calcArr[dpos-1:dpos+2] = [dposd]

    #Addition & Subtraction
    if "+" in calcArr or "-" in calcArr:
        if "+" in calcArr: apos = calcArr.index("+")
        else: apos = 0
        if "-" in calcArr: spos = calcArr.index("-")
        else: spos = 0
        if apos > spos:
            aposa = int(calcArr[apos-1]) + int(calcArr[apos+1])
            calcArr[apos-1:apos+2] = [aposa]
        else:
            sposs = int(calcArr[spos-1]) - int(calcArr[spos+1])
            calcArr[spos-1:spos+2] = [sposs]
    print(calcArr)

calculation = input("Type out your calculation with spaces separating the operators and numbers: ")
Calculate(calculation)