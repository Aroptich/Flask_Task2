def isvalid_email(first_email: str, second_email: str)-> bool:
    """Проверка зарегестрированных пользователей по emails"""
    if first_email == second_email:
        return False
    else:
        return True
