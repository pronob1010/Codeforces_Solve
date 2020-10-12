for i in range(int(input())):
    a,k = list(map(int,input().split()))
    if k>1:
        for j in range(0,k-1):
            digit = []
            t = a
            m = t % 10
            min = t%10

            while(t!=0):
                # digit.append(t%10)
                if m<t%10:
                    m = t%10
                elif min>t%10 and m>0:
                    min = t % 10
                t=t//10
            if min == 0:
                break

            a += (m*min)

    print(a)



    #
    # for i in range(int(input())):
    #     a, k = list(map(int, input().split()))
    #     if k > 1:
    #         for j in range(0, k - 1):
    #             digit = []
    #             t = a
    #             while (t != 0):
    #                 digit.append(t % 10)
    #                 t = t // 10
    #             m = max(digit)
    #             mi = min(digit)
    #             a += (m * mi)
    #     print(a)

    # for t in range(k):
    #     alen = len(str(a))
    #     ns = []
    #     r = 0
    #     a = str(a)
    #     for j in range(1, alen):
    #         ns.append(int(a[j - 1]))
    #
    #     if len(ns)>0:
    #         ma = max(ns)
    #         mi = min(ns)
    #         a=int(a)+(ma*mi)
    #
    # print(a)
# a = input()
# alen = len(a)
# ns = []
# for j in range(1,alen):
#     ns.append(int(a[j-1]))
#
# ma = max(ns)
# mi = min(ns)
# print(ma, mi)