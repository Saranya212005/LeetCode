class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l=str(n)
        s=0
        l1=[]
        for j in l:
            l1.append(int(j))
        for i in range(len(l1)):
            if i%2==0:
                s+=int(l1[i])
            else:
                s-=int(l[i])
        return s
