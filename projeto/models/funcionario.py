from abc import ABC, abstractmethod
<<<<<<< HEAD
from ..models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float) -> None:
        self.nome = self._nome_vazio(nome)
=======
from models.endereco import Endereco
from models.enum.sexo import Sexo

class Funcionario(ABC):
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float, sexo: Sexo) -> None:
        self.nome = nome
>>>>>>> 1dd4821 (up)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario_final = salario_final
        self.sexo = sexo

    @abstractmethod
    def calcular_salario(self,salario_final):
        pass

    def _nome_vazio(self,nome):
        if not nome.strip():
            raise TypeError("O nome não pode ser vazio")
        return nome

    def __str__(self) -> str:
        return (
<<<<<<< HEAD
            f"Nome: {self.nome}"
=======
            f"\nNome: {self.nome}"
>>>>>>> 1dd4821 (up)
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSalario: {self.salario_final}"
            f"\nSexo: {self.sexo.name}"
            f"\n{self.endereco}"
        )