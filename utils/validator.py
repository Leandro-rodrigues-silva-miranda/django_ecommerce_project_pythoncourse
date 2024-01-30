import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]                 
    reverso = 10                        
    total = 0

    
    for index in range(19):
        if index > 8:                   
            index -= 9                  

        total += int(novo_cpf[index]) * reverso  

        reverso -= 1                   
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   
                d = 0
            total = 0                   
            novo_cpf += str(d)          

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False
    


def calc_age(year,month,day):
    date = datetime(year,month,day)
    date_now = datetime.now()
    age = relativedelta(date,date_now)

    return age.years if age.years > 0 else -age.years

if __name__ == '__main__':
    print(valida_cpf('132.461.016-63'))
    print(calc_age(datetime(2001,10,2)))
