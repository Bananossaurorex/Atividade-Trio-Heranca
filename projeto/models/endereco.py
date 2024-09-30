
class Endereco:
    def __init__(self, logadouro:str, numero:int, complemento:str, cep:int, cidade:str) -> None:
        self.logaouro = logadouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return(
        f"Logadouro: {self.logaouro}"
        f"Complemento: {self.logaouro}"
        f"Logadouro: {self.logaouro}"
        f"Logadouro: {self.logaouro}"
        f"Logadouro: {self.logaouro}"
        
        )