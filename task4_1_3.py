'''
По данному числу 1≤n≤109 найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

'''
def adds(n):
    S = n
    terms = [0]
    if n<=2: return [n]
    for t in range(1, n):
        if S-t >= t+1:
            terms.append(t)
            S = S - t
        else:
            terms.append(S)
            break
    return terms[1:]

def print_answer(terms):
    print(len(terms))
    for t in terms:
        print(t, end=' ')

def main():
    n = 12
    print_answer(adds(n))


if __name__ == "__main__":
    main()


