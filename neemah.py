"""
SWAP CASE, everywhere the is a small letter convert to capital letter
and anywhere there is capital letter, convert to small letter

"""

def swap_case(s):
    result = ''
    
    for i in s:
        if i.islower():
          result += i.upper() 
        else:
            result += i.lower()
                   
    print(result)
swap_case('boyGIRL')