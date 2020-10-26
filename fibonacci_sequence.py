import matplotlib.pyplot as plt

x = []
y = []

def fib(quantity):
    l = [0, 1]
    for x in range(quantity - 2):
        l.append(int(l[len(l) - 1]) + int(l[len(l) - 2]))
    
    y.append(l[len(l) - 1])

    print('List for ' + str(r) + ' Cases:')
    print(l)

for r in range(1, int(input('Enter quantity of n:\n')) + 1):
    fib(r)
    x.append(r)

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(x, y)
plt.show()
