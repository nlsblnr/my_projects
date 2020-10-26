import matplotlib.pyplot as plt

x = []
y = []

def fib(anzahl):
    l = [0, 1]
    for x in range(anzahl - 2):
        l.append(int(l[len(l) - 1]) + int(l[len(l) - 2]))
    
    y.append(l[len(l) - 1])

    print('List for ' + str(r) + ' Cases:')
    print(l)

try:
    for r in range(1, int(input('Enter case quantity:\n')) + 1):
        fib(r)
        x.append(r)
except:
    print('\nNOOOO\n')

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(x, y)
plt.show()