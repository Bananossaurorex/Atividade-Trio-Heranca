<<<<<<< HEAD
from ..models.funcionario import Funcionario
from ..models.endereco import Endereco
=======
from models.funcionario import Funcionario
from models.endereco import Endereco
from models.enum.sexo import Sexo
>>>>>>> 1dd4821 (up)

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_final: float, sexo: Sexo, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, salario_final, sexo)
        self.crea = crea

    def calcular_salario(self, salario_final):
        return super().calcular_salario(salario_final)
