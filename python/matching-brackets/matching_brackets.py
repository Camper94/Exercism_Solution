def is_paired(input_string):
    
    brackets = []
    braces = []
    parentheses= []

  
    for item in input_string:
        if item in ('[',']'):
            brackets.append(item)
        elif item in ('{','}'):
            braces.append(item)
        elif item in ('(',')'):
            parentheses.append(item)
    
    frst_cond = len(brackets)%2==0 and len(braces)%2==0  and len(parentheses)%2==0
    print(brackets, braces, parentheses)

    try :
        if brackets :
            brackets_cond = brackets[0] == '[' and brackets[-1] ==']'
        else: brackets_cond = False
        if braces:
            braces_cond = braces[0] == '{' and braces[-1] =='}'
        else: braces_cond = False
        if parentheses:
            parentheses_cond = parentheses[0] == '(' and parentheses[-1] ==')'
        else: parentheses_cond = False
    except Exception as e:
        print(f"Something went wrong: {e}")

    print(frst_cond)
    print(brackets_cond)
    print(braces_cond)
    print(parentheses_cond)
   
    

    return frst_cond and (brackets_cond or braces_cond or parentheses_cond)
