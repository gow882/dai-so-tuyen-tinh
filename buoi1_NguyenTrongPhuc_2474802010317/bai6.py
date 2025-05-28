import numpy as np


A = np.array([[1,1,0,0,1],[3,1,0,1,1],[5,2,0,1,2],[2,0,1,2,3]])
B = np.array([[1,1,2,2,1],[2,2,2,0,2],[0,1,2,4,2],[1,4,1,2,2]])
C = np.array([[0,5,1,1,1],[0,1,1,1,3],[1,3,1,3,1],[0,1,3,3,0]])
D = np.array([[3,1,1,0,1],[5,0,0,3,7],[7,0,0,3,5],[5,0,3,5,3]])
E = np.array([[0,0,0,10,0],[0,0,15,0,0],[0,5,15,5,0],[0,20,5,0,0]])


score = {
    'A': [0,1,2,3,5], 'B': [0,1,2,4,8], 'C': [0,1,3,5,9],
    'D': [0,1,3,5,7], 'E': [0,5,10,15,20]
}

def convert(grid, level): return np.vectorize(lambda x: level[x])(grid)

a = convert(A, score['A'])
b = convert(B, score['B'])
c = convert(C, score['C'])
d = convert(D, score['D'])
e = convert(E, score['E'])


def safe(*layers): return sum(layers) <= 5

zones = {
    'a - tránh lộ': safe(e),
    'b - thời bình': safe(a, b, c),
    'c - mùa khô': safe(a, d),
    'd - mùa mưa': safe(b, c, d),
    'e - đủ 8 tháng': safe(a, b, c, d, e)
}


for k, v in zones.items():
    print(f"\nVùng an toàn ({k}):")
    print(np.where(v, '✔', '✘'))
