import os
from models.endereco import Endereco
from models.engenheiro import Engenheiro


os.system("clear||cls")

engenheiro1 = Engenheiro("Breno","4002-8922","brenin@gmail.com",
                         Endereco("R dos uruguaios",333,"Perto da Madre teresa","546321000","Salvador")
                         ,2500.01,"n sei")


print(engenheiro1)