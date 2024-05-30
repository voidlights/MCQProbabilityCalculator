from math import comb

def GetData():
    TotalMark = int(input("What was the total mark allocation? "))
    MinMark = int(input("What is the minimum mark you would like? "))
    NofCertain = int(input("How many marks are you sure you'll get? "))
    NofHalf = int(input("How many marks do you think you have a 50% chance of getting? "))
    NofThird = int(input("How many marks do you think you have a 33% chance of getting? "))
    NofQuarter = int(input("How many marks do you think you have a 25% chance of getting? "))
    NofUncertain = NofHalf + NofThird + NofQuarter
    if (NofUncertain + NofCertain != TotalMark):
        print(f"Total marks can be a maximum of {TotalMark} and you had {NofUncertain + NofCertain}")
    NofOptions = int(input("What is the number of possible answers? "))
    
    return TotalMark, MinMark, NofUncertain, NofOptions, NofHalf, NofThird, NofQuarter
        
def bnProb(n, k, p):

    # n is number of trials aka: NofUncertain
    # k is the number of successes aka: MinMark and its others MinMark + 1, MinMark + 2, etc, up until TotalMark
    # p is the probability of success aka: 1 / NofOptions

    if k > n:  # If the number of successes is greater than the number of trials, probability is 0
        return 0

    binom_coeff = comb(n, k)
    
    # Calculate the binomial probability
    probability = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
    return probability

TotalMark, MinMark, NofUncertain, NofOptions, NofHalf, NofThird, NofQuarter = GetData()
print(TotalMark, MinMark, NofUncertain, NofOptions)

Probability1 = 0
Probability2 = 0
Probability3 = 0
# Sum probabilities from MinMark - NofCertain to NofUncertain
for i in range(MinMark - (TotalMark - NofUncertain), NofUncertain + 1):
    Probability1 += bnProb(NofUncertain, i, 1 / NofOptions)
for i in range(MinMark - (TotalMark - NofUncertain), NofUncertain + 1):
    Probability2 += bnProb(NofUncertain, i, 1 / (NofOptions-1))
for i in range(MinMark - (TotalMark - NofUncertain), NofUncertain + 1):
    Probability3 += bnProb(NofUncertain, i, 1 / (NofOptions-2))

totalProbability = Probability1 * (NofQuarter / NofUncertain) + Probability2 * (NofThird / NofUncertain) + Probability3 * (NofHalf / NofUncertain)

print(f"Your probability of getting {MinMark}/{TotalMark} and above is {totalProbability * 100:.2f}%")
