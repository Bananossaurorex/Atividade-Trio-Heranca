from abc import ABC, abstractmethod
from import Endereco
class Funcionario(ABC):
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario_final = salario_final

    def