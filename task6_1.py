'''
Binary search
'''

def search(lst, k):
    l = 0
    r = len(lst)-1
    while l<=r:
        m=(l+r)//2
        if lst[m]==k: return m+1
        if lst[m]>k: r=m-1
        else: l=m+1
    return -1


def main():
   
    lst = list(map(int, input().split()))[1:]
    keys = list(map(int, input().split()))[1:]
    for k in keys:
        print(search(lst, k), end=' ')
    

if __name__=='__main__':
    main()


