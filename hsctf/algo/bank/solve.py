num = int(input())



time_list = 0
inp =[]
for i in range(num):
    inp.append(input().split())
a=int(inp[0][0])
for i in range(num):
    b=int(inp[i][1])
    print(a, b)
    if a < int(inp[i][0]):
        a=int(inp[i][0])
    time = b-a
    # print(a, b)
    if time > 9:
       time_list+=1
    #    print(i)
       a+=10
# print('============')
print(time_list)

