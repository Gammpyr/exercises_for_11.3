def check_email(email):
    if '@' in email and '.' in email:
        dog_index = email.find('@')  # 5
        point_index = email.find('.', dog_index)  # 8
        if dog_index >= 1 and dog_index + 1 < point_index < len(email) - 1:
            if dog_index < point_index:
                return True
    return False

