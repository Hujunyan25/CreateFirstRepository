
def solution(list):
    number = len(list)
    num = max(list)
    list2 = []
    for i in range(number-1):
        j=i+1
        if(list[i]==list[j]):
            list2.append(list[i])
            list2.append(list[i])
    # map=[0 for i in range(num+1)]
    # for i in range(number):
    #     map[list[i]]+=1
    # for i in range(len(map)):
    #     if(map[i]==2):
    #         list2.append(list[i])
    #         list2.append(list[i])
        # if list[i]==list[i+1] and list[i]!=list[i-1]:
        #     list2.append(list[i])
        #     list2.append(list[i])
    return list2

list = [1,2,2,3,3,5,6,6,3]
list2 = solution(list)
print(list2)