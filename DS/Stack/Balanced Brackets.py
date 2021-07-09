#Function to check whether the brackets are balanced in an expression
def isBalancedBrackets(s):
    stack = []
    for bracket in s:
        if bracket in ['(', '{', '[']:
            stack.append(bracket)
        else:            
            if not stack:
                return "NO"
            curr_bracket = stack.pop()
            
            if bracket == ')':
                if curr_bracket != '(':
                    return "NO"
            if bracket == '}':
                if curr_bracket != '{':
                    return "NO"
            if bracket == ']':
                if curr_bracket != '[':
                    return "NO"
        
    if stack:
        return "NO"
    return "YES"
        
s = input()
print (isBalancedBrackets(s))

#Time Complexity: O(n)
#Auxilary Space: O(n)
