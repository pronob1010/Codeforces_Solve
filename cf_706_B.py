def binarySearch(list, n):
    first = 0
    last = len(list)-1
    r = -1
    while(first<=last):

        mid = (first + ((last - first) // 2))

        if list[mid] <= n:
            r = mid
            first = mid+1

        elif list[mid]>n:
            last = mid-1

    return r+1


if __name__=='__main__':
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    q = int(input())
    coin = []
    for i in range(q):
        coin.append(int(input()))

    # print(x)
    # print(coin)
    for i in coin:
        c = binarySearch(x,i)
        # for j in x:
        #     if i>= j:
        #         c+=11
        print(c)
