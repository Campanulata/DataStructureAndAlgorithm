def bubble_sort(li):
    for i in range(len(li)-1):
        isExchange=False
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                isExchange=True
        print(li)
        if not isExchange:
            break
        
list1=[2,7,5,3,5,7,8,3]
bubble_sort(list1)