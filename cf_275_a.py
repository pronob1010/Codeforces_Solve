
# m = []
# re = []
# for i in range(3):
#     s = list(map(int, input().split()))
#     m.append(s)
#     t = [1,1,1]
#     re.append(t)
# # print(re)
# i=0
# while(i<3):
#     for j in range(1,3+1):
#         if (m[i][j-1]==1):
#             if i<2 and j!=2:
#                 if re[i][j-1]==0:
#                     re[i][j-1]=1
#                 else:
#                     re[i][j-1] = 0
#
#                 if re[i][j]==0:
#                     re[i][j] = 1
#                 else:
#                     re[i][j] = 0
#
#                 if re[i+1][j-1]==0:
#                     re[i+1][j-1] = 1
#                 else:
#                     re[i+1][j-1] = 0
#
#                 if re[i+1][j]==0:
#                     re[i + 1][j] = 1
#                 else:
#                     re[i+1][j]=0
#
#             elif j==2 and i<2:
#                 if re[i][j] == 0:
#                     re[i][j] = 1
#                 else:
#                     re[i][j] = 0
#
#                 if re[i + 1][j] == 0:
#                     re[i + 1][j] = 1
#                 else:
#                     re[i + 1][j] = 0
#
#                 if re[i][j - 1] == 0:
#                     re[i][j - 1] = 1
#                 else:
#                     re[i][j - 1] = 0
#
#                 if re[i+1][j-1]==0:
#                     re[i+1][j-1]=1
#                 else:
#                     re[i+1][j-1]= 0
#
#             elif i==2 and j<2:
#                 if re[i][j - 1] == 0:
#                     re[i][j - 1] = 1
#                 else:
#                     re[i][j - 1] = 0
#
#                 if re[i-1][j - 1] == 0:
#                     re[i-1][j - 1] = 1
#                 else:
#                     re[i-1][j - 1] = 0
#
#                 if re[i][j] == 0:
#                     re[i][j] = 1
#                 else:
#                     re[i][j] = 0
#
#                 re[i+1][j]=0
#
#             elif i == 2 and j == 2:
#                 if re[i][j] == 0:
#                     re[i][j] = 1
#                 else:
#                     re[i][j] = 0
#
#                 if re[i][j - 1] == 0:
#                     re[i][j - 1] = 1
#                 else:
#                     re[i][j - 1] = 0
#
#                 if re[i-1][j] == 0:
#                     re[i-1][j] = 1
#                 else:
#                     re[i-1][j] = 0
#
#                 if re[i-1][j - 1] == 0:
#                     re[i-1][j - 1] = 1
#                 else:
#                     re[i-1][j - 1] = 0
#
#         print("--------")
#         for l in range(1,3+1):
#             print(re[l-1])
#         print("--------")
#     print()
#     i+=1
#     print()
#
