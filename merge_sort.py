def merge_sort(s):
    if len(s)<2:
        return
    else:
        x=len(s)//2
        s1=s[0:x]
        s2=s[x:len(s)]
        merge_sort(s1)
        merge_sort(s2)
    return merge(s1,s2,s)


def merge(x,y,z):
    i=0
    j=0
    while (i+j)<len(z):
        if (i==len(x))or(j<len(y) and y[j]>x[i]):
            z[i+j]=y[j]
            j+=1
        else:
            z[i+j]=x[i]
            i+=1
    return z
if __name__=='__main__':
    print('enter list element')
    l=[int(a) for a in input().split()]
    print(merge_sort(l))


