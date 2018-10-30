'''
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤109, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.
'''
def points(n, lst):
    lst.sort(key=lambda x: x[1])
    sgms=lst[:]
    pts=[]
    while sgms:
        pts.append(sgms[0][1])
        sgms = list(filter(lambda sgm: sgm[0]>pts[-1], sgms))
    return pts

def printpoints(pts):
    print(len(pts))
    for point in pts:
        print(point, end=' ')


def main():
    n = int(input(n))
    lst=[]
    for i in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))
    printpoints(points(n, lst))


if __name__ == "__main__":
    main()
