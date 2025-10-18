"""
Find all circular primes less than or equal to a given number n
Implement a function that identifies all circular primes up to n. 
A circular prime is a prime number that remains prime under all rotations of its digits.
"""

class A():
    def __init__(self, n):
        self.number = n
    
    def check_prime(self, number):
        if number < 2:
            return False
        
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1 
        return True
        

    def getAllCPrimes(self):
        number  = self.number
        
        output = []
        for num in range(number):
            s = str(num)
            is_circular = True
            for i in range(len(s)):
                rnumber = int(s[i:] + s[:i])
                if self.check_prime(rnumber) is False:
                    is_circular = False
            if is_circular == True:
                output.append(rnumber)
        return output
                
            
        
        

obj = A(179)
print(obj.getAllCPrimes())