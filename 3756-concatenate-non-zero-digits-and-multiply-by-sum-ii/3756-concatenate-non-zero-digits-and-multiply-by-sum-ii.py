class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        prefix = [0]
        prefixa = [0]
        prefixz = [0]

        for x in s:
            prefix.append(prefix[-1] + int(x))  

        for x in s:
            if x=="0":
                prefixa.append(prefixa[-1])
                prefixz.append(prefixz[-1])
            else:
                prefixa.append((prefixa[-1]*10+int(x))%MOD)
                prefixz.append(prefixz[-1]+1)

        ans = []
            
        for l, r in queries:
            t=prefix[r+1]-prefix[l]
            c=prefixz[r+1]-prefixz[l]
            d=(prefixa[r+1]-prefixa[l] * pow(10, c, MOD))%MOD

            print(t,c,d)
            ans.append((t*d)%MOD)
        return ans