from abc import ABC, abstractmethod
from ..models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float) -> None:
        self.nome = self._nome_vazio(nome)
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
            f"Nome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSalario: {self.salario_final}"
            f"\nSexo: {self.sexo.name}"
            f"\n{self.endereco}"
        )