

class Solution:

    @staticmethod
    def longest_palindromic(self, s: str) -> str:

        # Instead of taking the left and right edges of the string
        # We will start in the middle of the string

        # Making base function to help us in the method and pass in 'l' and 'r' parameters

        def baseFun (l,r):
            while (l >= 0 and r < len(s) and s[l]==s[r]):

                # Since the left is greater or equal 0, right is less that string length
                # After checking if the 'l' character is equal 'r' character
                # We need to decrease 'l' by 1 and increase 'r' by 1

                l -= 1
                r += 1
            return s[l+1:r]
        
        # Define an empty variable to store result

        res = ""
        for i in range(len(s)):

            # If the length of "s" is odd it will start from the same character
            test = baseFun (i,i)
            if len(test) > len(res):
                res = test

            # If the length of "s" is even it will start from the two middle characters
            test = baseFun (i,i+1)
            if len(test) > len(res):
                res = test

        return res