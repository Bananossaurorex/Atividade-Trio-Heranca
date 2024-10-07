import pytest
from ..models.endereco import Endereco
from ..models.medico import Medico
from ..models.enum.sexo import Sexo
from ..models.enum.unidadefederativa import UnidadeFederativa

@pytest.fixture
def criar_medico():
    return Medico("Breno","987654321","brenosalvavidas@gmail.com",
                  Endereco("Rua da computação","177","Proximo a rua dos pasteis",2224401,"Salvador",UnidadeFederativa.BAHIA),
                  2000.01,Sexo.FEMININO,"6554632")

def test_nome_valido(criar_medico):
    assert criar_medico.nome == "Breno"

def test_alterar_nome(criar_medico):
    criar_medico.nome = "Claudio"
    assert criar_medico.nome == "Claudio" 

def test_nome_vazio_invalido():
        with pytest.raises(TypeError, match= "O nome não pode ser vazio"):
            Medico("","987654321","brenosalvavidas@gmail.com",
                  Endereco("Rua da computação","177","Proximo a rua dos pasteis",2224401,"Salvador",UnidadeFederativa.BAHIA),
                  2000.01,Sexo.FEMININO,"6554632")
