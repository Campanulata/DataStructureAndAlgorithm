def select_sort(li):
    for i in range(len(li)-1):
        max=0
        for j in range(len(li)-i):
            if li[j]>li[max]:
                max=j
        li[max],li[len(li)-1-i]=li[len(li)-1-i],li[max]
        print(li)
list1=[2,7,5,3,5,7,8,3]
select_sort(list1)