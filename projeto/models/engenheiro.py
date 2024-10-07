from ..models.funcionario import Funcionario
from ..models.endereco import Endereco

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, salario_final)
        self.crea = crea

    def calcular_salario(self, salario_final):
        return super().calcular_salario(salario_final)
