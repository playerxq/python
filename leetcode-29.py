class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if(divisor==0) or (divisor==-1 and dividend==MIN_INT):
            return MAX_INT
        vals = []
        if ((dividend>0) and (divisor>0)) or ((dividend<0) and (divisor<0)):
            sign = 1
        else:
            sign  = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            vals.append(divisor)
            divisor+=divisor
        result = 0
        for i in range(len(vals)-1,-1,-1):
            if(dividend>=vals[i]):
                dividend-=vals[i]
                result += 2**i
        return result*sign
