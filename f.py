# k-mer
import sys

l1 = ['A','T','C','G']
l2 = ['A','T','C','G']

def mer (l1,l2,n):
    if n == 1:
        return l2
    l_t = []
    for i in l1:
        for j in l2:
            l_t.append(i+j)
    return mer(l1, l_t, n-1)

n = int(sys.argv[1])
print(mer(l1,l2,n))



#if __name__=="__main__":
#    if len(sys.argv) != 2:
#        print(f"#usage : python {argv[0]} [mer]")
#        sys.exit()


