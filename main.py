def encoder(password):
    pw_return = ""
    value = 0
    for i in range(len(password)):
        value = int(password[i]) + 3
        pw_return += str(value)
    return pw_return

