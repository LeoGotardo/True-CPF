from test import ValidCPF



cpf = ValidCPF('413.717.708-24')

if cpf.valid():
    print('CPF VALIDO.')
else:
    print('CPF INVALIDO.')