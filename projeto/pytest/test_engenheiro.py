import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from ..models.enum.sexo import Sexo
from ..models.enum.unidadefederativa import UnidadeFederativa
@pytest.fixture
def criar_engenheiro():
    return  Engenheiro("Maria","40028922","maria@gmail.com",
                       Endereco("Rua da Maluca",22,"1° andar",23232,"Salvador",UnidadeFederativa.BAHIA),600.3,Sexo.FEMININO,"Crea")


def test_nome_engenheiro(criar_engenheiro):
    assert criar_engenheiro.nome == "Maria"

def test_nome_vazio_engenheiro(criar_engenheiro):
    with pytest.raises(TypeError,match = "O nome não pode ser vazio"):
        Engenheiro("","40028922","maria@gmail.com",
                       Endereco("Rua da Maluca",22,"1° andar",23232,"Salvador",UnidadeFederativa.BAHIA),600.3,Sexo.FEMININO,"Crea")

def test_email_engenheiro(criar_engenheiro):
    with pytest.raises(TypeError,match = "O email deve conter o @"):
        Engenheiro("Maria","40028922","mariahotmail.co",
                       Endereco("Rua da Maluca",22,"1° andar",23232,"Salvador",UnidadeFederativa.BAHIA),600.3,Sexo.FEMININO,"Crea")
