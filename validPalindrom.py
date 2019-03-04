class Sol:
    def validPalindrom(self,num):
        l=len(str(num))
        for i in range(0,l//2):
            if str(num)[i] != str(num)[l-1- i]:
                return False
                break
        return True

p1=Sol()
print(p1.validPalindrom(2172))
