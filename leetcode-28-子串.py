class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def pre(sub):
            f = [0]*len(sub)
            for i in xrange(1,len(sub)):
                k = f[i-1]
                while k>0 and sub[i]!=sub[k]:
                    k = f[k-1]
                if sub[i]==sub[k]:
                    k+=1
                f[i]=k
            return f
        if not haystack and not needle:
            return 0
        if haystack and not needle:
            return 0
        if len(needle)>len(haystack):
            return -1
        f = pre(needle)
        k = 0
        for i in xrange(len(haystack)):
            while k>0 and haystack[i]!=needle[k]:
                k = f[k-1]
            if haystack[i]==needle[k]:
                k+=1
            if k==len(needle):
                return i-len(needle)+1
        return -1