#Balancing Parenthesis using stack

def compare_left_right(left, right):
    if left == "(" and right == ")":
        return True
    elif left == "[" and right == "]":
        return True
    elif left == "{" and right == "}":
        return True
    else:
        return False
    
# The second function is what actuallt takes a string as argument 
# and uses principles of stack to evaluate if the string is balanced. 

def pairing(s):
    stack = []
    for bracket in s:
        if bracket in ["(", "[", "{"]:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if not compare_left_right(top, bracket):
                return False
    
    if len(stack) != 0:
        return False
    else:
        return True

    
    

print pairing('({])')
print pairing('({[}])')
print pairing('({[]})')
print pairing('{[(])}')
print pairing('{{[[(())]]}}')
print pairing('()(){}{}')






