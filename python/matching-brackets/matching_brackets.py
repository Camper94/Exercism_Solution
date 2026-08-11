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
    try:
        brackets_cond = brackets[0] == '[' and brackets[-1] ==']'
    except IndexError:
        print('brackets list is empty')
    braces_cond = braces[0] == '{' and braces[-1] =='}'
    parentheses_cond = parentheses[0] == '(' and parentheses[-1] ==')'

    return first_cond and brackets_cond and braces_cond and parentheses_cond  
