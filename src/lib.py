def validate_cpf(cpf):

    cpf = ''.join(re.findall('\d', str(cpf)))
    
    if (not cpf) or (len(cpf) < 11):
        return False

    integers = map(int, cpf)
    new = integers[:9]

    while len(new) < 11:
        r = sum([(len(new)+1-i)*v for i,v in enumerate(new)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        new.append(f)

    if new == integers:
        return True
    
    return False