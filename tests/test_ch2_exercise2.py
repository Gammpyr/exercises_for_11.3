from chapter2_tests.exercise2 import check_email


def test_check_email():
    email = 'gamid@ya.ru'
    assert check_email(email) == True

def test_check_email_with_empty_email():
    email = ''
    assert check_email(email) == False

def test_check_email_with_false_email():
    assert check_email('email') == False
    assert check_email('email@test') == False
    assert check_email('email@test.') == False
    assert check_email('em.mailtest') == False
    assert check_email('email@.ru') == False
    assert check_email('@email.ru') == False



