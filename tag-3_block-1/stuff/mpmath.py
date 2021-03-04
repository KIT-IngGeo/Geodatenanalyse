from mpmath import mp

mp.dps = 10000
mp.nprint(mp.pi, 10000)

mp.dps = 50
mp.nprint(mp.mpf(1)/6, 50)

print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)

