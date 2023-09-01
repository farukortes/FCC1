st=input('Enter a list of strings:')
print(st)

input_list=st.split(',')
input_list = [element.strip() for element in input_list]  # Removing extra spaces
print("User input list:", input_list)


lng=len(input_list)
print('The length of list: ', lng)


def arithmetic_arranger(list):
    """
    1- Error: Too many problems.
    # 1- length of list-- limit is 5,  Check if too many inputs are available
    # For trials  "32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","523 - 49","523 - 49"  ---too many
    #   For trials "32 + 8", "1 - 3801", "9999 + 9999",---- less than 5 """  
    if lng>5:
        return print("Error: Too many problems.")
        exit()
    else:
        print("Go on, the number of items is less than 5")
    
     """  
     # 2-Error: Operator must be '+' or '-'. 
     # The appropriate operators the function will accept are addition and subtraction. 
     # Multiplication and division will return an error. Other operators not mentioned in this 
     # bullet point will not need to be tested. The error returned will be: 
     # Error: Operator must # be '+' or '-'.   
     
     # For trials: "32 + 8", "1 * 3801", "9999 + 9999" """ 
        
    for x in input_list:
        val=x.split(' ')
        print("Pieces of one element in the string: ",val)
        val2=val[1]
        print(type(val2))
        print(val[1])
        if val2 != '+' or val2 !='-':
            return print("Error: Operator must be '+' or '-'.")
            exit()
            
    for x in input_list:
        
        
        if '+' in x or '-' in x:
            try:
            result = eval(x)
        print(f"Result: {result}")
    except:
        print("An error occurred while evaluating the expression.")
else:
    print("Invalid operator. Only + and - are allowed.")        
            
            
            
arithmetic_arranger(list)



