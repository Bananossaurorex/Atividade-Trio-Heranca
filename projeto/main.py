import os
<<<<<<< HEAD

os.system("clear||cls")

if __name__ == "__main__":
    os.system("pytest")
=======
from models.endereco import Endereco
from models.engenheiro import Engenheiro
from models.enum.sexo import Sexo
from models.medico import Medico
from models.enum.unidadefederativa import UnidadeFederativa

os.system("clear||cls")

engenheiro1 = Engenheiro("Breno","4002-8922","brenin@gmail.com", 
                         Endereco("R dos uruguaios",333,"Perto da Madre teresa",546321000,"Salvador")
                         ,2500.01,Sexo.MASCULINO, "n sei" )

medico = Medico("João", "7159959", "joão@gmail.com", Endereco("Rua São josé", 15, "Casa", 54554, "Rio de Janeiro", U))

print(engenheiro1)
>>>>>>> 1dd4821 (up)
