from abc import ABC, abstractmethod
from endereco import Endereco
class Funcionario(ABC):
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario_final = salario_final

    @abstractmethod
    def calculo_salario():
        pass

    def __str__(self) -> str:
        return (
            (f"Nome: {self.nome}")
            (f"\nTelefone: {self.telefone}")
            (f"\nEmail: {self.email}")
            (f"\nSalário{self.salario_final}")
            (f"\n{self.endereco}")
        )