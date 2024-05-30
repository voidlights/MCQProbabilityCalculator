from flask import Flask, render_template, request
from math import comb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    TotalMark = int(request.form['TotalMark'])
    MinMark = int(request.form['MinMark'])
    NofCertain = int(request.form['NofCertain'])
    NofHalf = int(request.form['NofHalf'])
    NofThird = int(request.form['NofThird'])
    NofQuarter = int(request.form['NofQuarter'])
    NofUncertain = NofHalf + NofThird + NofQuarter
    if (NofUncertain + NofCertain != TotalMark):
        return f"Total marks can be a maximum of {TotalMark} and you had {NofUncertain + NofCertain}"

    NofOptions = int(request.form['NofOptions'])

    Probability1 = 0
    Probability2 = 0
    Probability3 = 0
    for i in range(MinMark - (TotalMark - NofUncertain), NofUncertain + 1):
        Probability1 += bnProb(NofUncertain, i, 1 / NofOptions)
    for i in range(MinMark - (TotalMark - NofUncertain), NofUncertain + 1):
        Probability2 += bnProb(NofUncertain, i, 1 / (NofOptions-1))
    for i in range(MinMark - (TotalMark - NofUncertain), NofUncertain + 1):
        Probability3 += bnProb(NofUncertain, i, 1 / (NofOptions-2))

    totalProbability = Probability1 * (NofQuarter / NofUncertain) + Probability2 * (NofThird / NofUncertain) + Probability3 * (NofHalf / NofUncertain)

    return f"Your probability of getting {MinMark}/{TotalMark} and above is {totalProbability * 100:.2f}%"

def bnProb(n, k, p):
    if k > n:
        return 0

    binom_coeff = comb(n, k)
    probability = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
    return probability

if __name__ == '__main__':
    app.run(debug=True)
