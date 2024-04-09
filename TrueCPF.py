from tkinter import messagebox as msg
from threading import Thread

import customtkinter as ctk
import pyperclip
import random
import re
import os

class CustomThread(Thread):
    def __init__(self, group=None, target= None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return

class CreateCPF:
    def __init__(self) -> None:
        self.cpf = self.generateCpf()

    def format(self, lista, tamanho=3):
        # Usa compreensão de lista para criar sub-listas
        return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

    def calcula_digito(self, soma):
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    
    def calc_verify_digit(self, seed):
        soma1 = sum((10 - i) * int(num) for i, num in enumerate(seed))
        digito1 = self.calcula_digito(soma1)
        
        soma2 = sum((11 - i) * int(num) for i, num in enumerate(seed + digito1))
        digito2 = self.calcula_digito(soma2)
        
        return digito1, digito2

    def generateCpf(self):
        """Gera um número de CPF válido."""
        cpf_base = ''.join(str(random.randint(0, 9)) for _ in range(9))
        digito1, digito2 = self.calc_verify_digit(cpf_base)
        cpf_base = self.format(cpf_base)
        cpf_base = ".".join(map(str, cpf_base))
        return f'{cpf_base}-{digito1}{digito2}'


class ValidCPF:
    def __init__(self, cpf) -> None:
        self.cpf = cpf

    def valid(self):
        if not self.cpf or len(self.cpf) != 11:
            return False

        # Checks if the CPF is a sequence of repeating digits (e.g., 11111111111). Such CPFs are considered invalid.
        if self.cpf == self.cpf[0] * len(self.cpf):
            return False

        newCpf = self._calcDigit(self.cpf[:9])
        newCpf = self._calcDigit(newCpf)

        return newCpf == self.cpf

    @staticmethod
    def _calcDigit(cpfPart):
        if not cpfPart:
            return False

        sum_ = 0
        for key, mult in enumerate(range(len(cpfPart) + 1, 1, -1)):
            sum_ += int(cpfPart[key]) * mult

        resto = 11 - (sum_ % 11)
        resto = resto if resto <= 9 else 0
        return cpfPart + str(resto)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self._formatCPF(cpf)

    @staticmethod
    def _formatCPF(cpf):
        return re.sub('[^0-9]', '', cpf)

class screen(ctk.CTk):
    def __init__(self) -> None:
        self.cls = os.system('cls' if os.name == 'nt' else 'clear')
        self.app = ctk.CTk()

        self.app.resizable(width=False, height=False)
        self.app.geometry("500x600")
        self.app.title('True CPF')

        ctk.set_appearance_mode('dark')

        self.mainScreen()
        self.app.mainloop()

    def validCPF(self, cpf):
        try:
            if ValidCPF(cpf).valid():
                msg.showinfo(title="Valido", message=f"{cpf} é um cpf valido.")
            else:
                msg.showinfo(title="Invalido", message=f"{cpf} é um cpf invalido.")
        except Exception as e:
            msg.showerror(title='Error', message=e)

    def createCPF(self):
        try:
            self.generetedCPF = CreateCPF().generateCpf()
            pyperclip.copy(self.generetedCPF)
            msg.showinfo(title='Done', message=f'O CPF {self.generetedCPF} foi copiado ao seu copyboard.')
        except Exception as e:
            msg.showerror(title='ERROR', message=e)

    def mainScreen(self):
        frame = ctk.CTkFrame(master=self.app)
        frame.place(in_=self.app, anchor="center", relx=0.5, rely=0.5)

        tittle = ctk.CTkLabel(
            master = frame,
            text="Validar CPF",
            font=ctk.CTkFont(family="Helvetica", size=36, weight="bold", slant="italic")
        )

        label = ctk.CTkLabel(
            master=frame,
            text="CPF",
            font=ctk.CTkFont(family="Helvetica", size=16)
        )

        cpfEntry = ctk.CTkEntry(
            master=frame,
            placeholder_text='XXX.XXX.XXX-XX',
            font=("RobotoSlab", 12),
            border_width=2,
            height=40,
            width=200,
            )
        
        validButton = ctk.CTkButton(
            master=frame,
            text='Validar CPF',
            command=lambda:self.validCPF(cpfEntry.get())
        )

        newCPF = ctk.CTkButton(
            master= frame,
            text='Criar CPF',
            command=lambda:self.createCPF(),
        )

        tittle.pack(padx=50, pady=10)
        label.place(relx=2, rely=4)
        cpfEntry.pack(padx=50, pady=50)
        validButton.pack(padx=50, pady=10)
        newCPF.pack(padx=50, pady=10)

        self.app.bind("<Return>", lambda _: self.validCPF(cpfEntry.get()))

if __name__ == "__main__":
    screen = screen()