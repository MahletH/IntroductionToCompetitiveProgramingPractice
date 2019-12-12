class Solution:
    def tribonacci(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n==1):
            return 1
        elif(n==2):
            return 1
        else:
            sum0=0
            sum1=1
            sum2=1
            sum=sum0+sum1+sum2
            for i in range(3,n):
                sum0=sum1
                sum1=sum2
                sum2=sum
                sum=sum0+sum1+sum2
            return sum

def main():
    while True:
        try:
            n = int(input());
            
            ret = Solution().tribonacci(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
