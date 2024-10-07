import pytest
from ..models.endereco import Endereco
from ..models.medico import Medico


@pytest.fixture
def criar_medico():
    return Medico("Breno","987654321","brenosalvavidas@gmail.com",
                  Endereco("Rua da computação","177","Proximo a rua dos pasteis",2224401,"Salvador"),
                  2000.01,"6554632")

def test_nome_valido(criar_medico):
    assert criar_medico.nome == "Breno"

