#Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.
#The string of brackets is correct if it satisfies the following conditions:
#1. Number of opening and closing brackets are equal.
#2. Pattern should not start with closing bracket and end with opening bracket.

#lex_auth_0127135773590405121141
def bracket_pattern(input_str):
    #Remove pass and write your code here
     open_list = ["("]
     close_list = [")"]
     stack = []
     
     for i in input_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0 ) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "False"
     if len(stack) == 0:
        return True
     else:
        return False
    

    
input_str="(())("
print(bracket_pattern(input_str))
