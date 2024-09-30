from models.funcionario import Funcionario
from models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, salario_final)
        self.crm = crm

    def calcular_salario(self, salario_final):
        return super().calcular_salario(salario_final)

    def __str__(self) -> str:
        return f"\n{super().__str__()}\nCRM: {self.crm}"