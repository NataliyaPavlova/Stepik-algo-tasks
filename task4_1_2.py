'''
Первая строка содержит количество предметов 1≤n≤103 и вместимость рюкзака 0≤W≤2⋅106. Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅106 и объём 0<wi≤2⋅106 предмета (n, W, ci, wi — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

'''

# put your python code here
def backpack(n, W, store):
    store.sort(key=lambda x: x[0]/x[1] if x[1] else 0, reverse=True)
    S=0
    bp=[]
    rmnd = 0
    for tup in store:
        fin = tup
        if S+tup[1]<=W:
            bp.append(tup)
            S+=tup[1]
        else:
            rmnd = fin[0] * (W - S) / fin[1]
            break

    return sum([a[0] for a in bp])+rmnd

def print_answer(S):
    print('{:06.3f}'.format(S))


def main():
    n, W = map(int, input().split())
    store=[]
    for i in range(n):
        ci, wi = map(int, input().split())
        store.append((ci, wi))
    print_answer(backpack(n, W, store))

if __name__ == "__main__":
    main()





