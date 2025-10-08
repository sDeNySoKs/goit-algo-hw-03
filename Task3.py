import re

def normalize_phone(phone_number):
    
    cleaning_number = re.sub(r"[^\d+]", '', phone_number.strip()) #видаляємо все окрім цифр та +

    if cleaning_number.startswith('+'):
        if cleaning_number.startswith('+38'):
            return cleaning_number
        
        else:
            return cleaning_number
    
    elif cleaning_number.startswith('380'):
        return "+" + cleaning_number
    
    else:
        return '38' + cleaning_number
    


