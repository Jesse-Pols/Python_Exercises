def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) > 5 and any(i.isdigit() for i in newpassword):
        return True
    else:
        return False

print(new_password("password", "incorrect"))