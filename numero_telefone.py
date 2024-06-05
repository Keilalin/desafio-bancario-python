import re

def validate_numero_telefone(phone_number):
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"
    if re.match(pattern, phone_number):
        return "O telefone é válido."
    else:
        return "O telefone é inválido."
    
phone_number = input()

result = validate_numero_telefone(phone_number)

print(result)