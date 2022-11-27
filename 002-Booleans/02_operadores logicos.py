# Operadores logicos AND y OR

# ========================================
# AND
# ========================================

#      True         True
#      vvvvvv      vvvvvvvv
print((5 == 5) and (5 == 5)) # True

#      True         False
#      vvvvvv      vvvvvvvv
print((5 == 5) and (5 == 0)) # False

password_input_2 = '123'
password_db_2 = '123'

_2fa_input = '123456'
_2fa_app = '482913'

print((password_input_2 == password_db_2) and (_2fa_input == _2fa_app)) # False

# ========================================
# OR
# ========================================

print((5 == 0) or (10 == 10)) # True
