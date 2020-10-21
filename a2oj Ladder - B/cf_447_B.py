s=input()
n=int(input())
k=input().split()
# print(k)
max1=0
for i in k:
    if (int(i)> max1):
        max1=int(i)
sum=0
# print(max1)
l=1
for i in s:
    # print(int(k[ord(i)-97]))
    sum = sum+l*int(k[ord(i)-97])
    l+=1

# print(sum,l)
for i in range(0,n):
    sum=sum+l*max1
    l+=1
# print(sum,l)
print(sum)
# s1 = input()
# p=s1
# k = int(input())
# s = list(map(int,input().split()))
# ad = []
# for i in range(1,len(s1)+1):
#     ad.append(s[ord(s1[i-1])-97])
#
# print(ad)
# print(k)
# while(k!=0):
#     if ad[k-1]>1 and ad[k-1]>=k:
#         p=p+(p[k-1]*ad[k-1])
#         k-=ad[k-1]
#     print(k)
#
# print(p)