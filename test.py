import random

def calc_digitos_verificadores(cpf_base):
    """Calcula os dígitos verificadores para o CPF."""
    def calcula_digito(soma):
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    soma1 = sum((10 - i) * int(num) for i, num in enumerate(cpf_base))
    digito1 = calcula_digito(soma1)
    
    soma2 = sum((11 - i) * int(num) for i, num in enumerate(cpf_base + digito1))
    digito2 = calcula_digito(soma2)
    
    return digito1, digito2

def gera_cpf():
    """Gera um número de CPF válido."""
    cpf_base = ''.join(str(random.randint(0, 9)) for _ in range(9))
    digito1, digito2 = calc_digitos_verificadores(cpf_base)
    cpf_base = dividir_lista(cpf_base)
    cpf_base = ".".join(map(str, cpf_base))
    return f'{cpf_base}-{digito1}{digito2}'

def dividir_lista(lista, tamanho=3):
    # Usa compreensão de lista para criar sub-listas
    return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

# Gerar e imprimir um CPF válido
cpf_valido = gera_cpf()
print(f'CPF válido gerado: {cpf_valido}')
