

def extract_features(password) -> list[int]:

    if not isinstance(password, str):
        return [0,0,0,0,0]
    
    pass_strength = {
        'length': 0, 
        'uppercase_count': 0, 
        'lowercase_count': 0, 
        'digit_count': 0,
        'symbol_count': 0
        }
    pass_strength['length'] = len(password)
    
    for char in password:
        if char.isupper():
            pass_strength['uppercase_count'] += 1
        elif char.islower():
            pass_strength['lowercase_count'] += 1
        elif char.isdigit():
            pass_strength['digit_count'] += 1   
        else:
            pass_strength['symbol_count'] += 1

    return list(pass_strength.values())

