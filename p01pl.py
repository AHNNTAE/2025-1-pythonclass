p = 1

n = 1

p = p * (((2*n + 1)**2 - 1) / (2*n + 1)**2)

n = 2

p = p * (((2*n + 1)**2 - 1) / (2*n + 1)**2)

print(p * 4)

p = 1
for n in range(1, 100):
    p = p * ((2 * n +1) ** 2 -1) / (2 * n + 1) **2

    print(p*4)

import matplotlib.pyplot as plt
plt.plot([1,3,4])
plt.show()

p=1
for n in range(1,100):
    p = p * ((2 * n * 1) ** 2 - 1) / (2* n + 1) **2
    print(p*4)

import matplotlib.pyplot as plt
plt.plot([1,3,4])
plt.show()