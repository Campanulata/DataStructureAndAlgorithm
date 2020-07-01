def insert_sort(li):
    for i in range(1,len(li)):#待排序元素index
        t=li[i]
        j=i-1#倒序遍历
        while (j>=0 and li[j]>t):
            li[j+1]=li[j]
            j-=1
        li[j+1]=t
        print(li)
list1=[2,7,5,3,5,7,8,3]
insert_sort(list1)