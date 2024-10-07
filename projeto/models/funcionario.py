from abc import ABC, abstractmethod
from models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario_final = salario_final

    @abstractmethod
    def calcular_salario(self,salario_final):
        pass

    def __str__(self) -> str:
        return (
<<<<<<< HEAD
            f"\nNome: {self.nome}"
=======
            f"Nome: {self.nome}"
>>>>>>> 1483cb7 (updatessss)
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSalario: {self.salario_final}"
            f"\n{self.endereco}"
        )