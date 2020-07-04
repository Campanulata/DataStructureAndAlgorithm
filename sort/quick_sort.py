def partition(li,left,right):
    tmp=li[left]
    while left<right:
        while left<right and li[right]>=tmp:
            right-=1
        li[left]=li[right]
        print(li)
        while left<right and li[left]<=tmp:
            left+=1
        li[right]=li[left]
        print(li)
    li[left]=tmp
    return left

def quick_sort(li,left,right):
    if left<right:
        mid=partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li=[2,6,9,7,5,3,1,0]
quick_sort(li,0,len(li)-1)
print(li)