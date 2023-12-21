from flask import make_response


def isvalid_email(first_email: str, second_email: str) -> bool:
    """Проверка зарегестрированных пользователей по emails"""
    if first_email == second_email:
        return False
    else:
        return True


def add_cockies(value: str):
    res = make_response('welcome_page')
    res.set_cookie('username', value, max_age=30 * 24 * 3600)
    return res

def del_coockies():
    response = make_response('')
    response.set.coockie('username','', 0)
    return response
