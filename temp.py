import numpy as np
import matplotlib.pyplot as plt

group40 = np.random.normal(loc=40, scale=5, size=50)
group35 = np.random.normal(loc=35, scale=5, size=50)
datapoints = []
for threshold in range(0, 81):
    NumOfTP = 0
    for temperature in group40:
        if temperature >= threshold:
            NumOfTP += 1
    NumOfTN = 0
    for temperature in group35:
        if temperature < threshold:
            NumOfTN += 1

    NumOfFN = 50 - NumOfTP
    NumOfFP = 50 - NumOfTN
    data = np.array([[NumOfTP, NumOfTN], [NumOfFP, NumOfFN]])
    TPR = NumOfTP / (NumOfTP + NumOfFN)
    FPR = NumOfFP / (NumOfFP + NumOfTN)

    datapoints.append((threshold, FPR, TPR))

#datapoints.sort(key=lambda x: -x[0])

x = [datapoint[1] for datapoint in datapoints]
y = [datapoint[2] for datapoint in datapoints]

plt.title("ROC Curve")
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.scatter(x, y, color='pink', s=30, alpha=1)
plt.plot(x, y, color='crimson')
plt.show()
