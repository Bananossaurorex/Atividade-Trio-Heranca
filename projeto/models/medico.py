from ..models.funcionario import Funcionario
from ..models.endereco import Endereco
from ..models.enum.sexo import Sexo
from ..models.enum.unidadefederativa import UnidadeFederativa


class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float, sexo: Sexo, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, salario_final, sexo)
        self.crm = crm

    def calcular_salario(self, salario_final):
        return super().calcular_salario(salario_final)

    def __str__(self) -> str:
        return f"\n{super().__str__()}\nCRM: {self.crm}"