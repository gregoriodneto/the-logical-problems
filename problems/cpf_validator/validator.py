import re

def validate_cpf(cpf: str) -> bool:
    cpf = re.sub(r'[.-]', '', cpf)
    if len(cpf) > 11 or cpf == cpf[0] * 11:
        return False
    
    sum_primary = sum(int(cpf[i]) * (10 - i) for i in range(9))
    first_digit = (sum_primary * 10) % 11
    if first_digit == 10 or first_digit == 11:
        first_digit = 0
    if first_digit != int(cpf[9]):
        return False

    sum_secondary = sum(int(cpf[i]) * (11 - i) for i in range(10))
    second_digit = (sum_secondary * 10) % 11
    if second_digit == 10 or second_digit == 11:
        second_digit = 0
    if second_digit != int(cpf[10]):
        return False

    return True

if __name__ == "__main__":
    cpf = input("Digite o cpf: ")
    validate = validate_cpf(cpf)
    result = f"O cpf é: {'Válido' if validate else 'Inválido'}"
    print(result)