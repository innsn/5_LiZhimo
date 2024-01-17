import json
from matplotlib import pyplot as plt

with open('test.json') as f:
    data = json.load(f)

loss = []
for i in data['log_history']:
    if 'loss' in i:
        loss.append(i['loss'])

x = range(3,501)
plt.plot(x,loss)
plt.show()