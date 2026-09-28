# declaracao so conjunto (chaves)
frutas = {"maca", "uva", "maca"}
# duplicadas sao elimadas
print(frutas)  # {'maca', 'uva'}
# teste de pertinencia (acesso)
print("uva" in frutas)  # True
# percorrendo o conjunto
for f in frutas:
    print(f)