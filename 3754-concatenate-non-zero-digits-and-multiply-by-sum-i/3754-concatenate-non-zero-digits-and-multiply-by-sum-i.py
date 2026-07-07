class Solution:
    def sumAndMultiply(self, N: int) -> int:
        total=0
        shift=0
        digits=[]
        current=N
        
        while current > 0:
            total += current%10
            if current % 10 > 0:
                digits.append(current%10)
            current //=10

        digits.reverse()
        for x in digits:
            shift *= 10
            shift += x
        return total*shift 

        