class Endereco:
    def __init__(self, logadouro:str, numero:int, complemento:str, cep:int, cidade:str) -> None:
        self.logadouro = logadouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return(
        f"Logadouro: {self.logadouro}"
        f"Número: {self.numero}"
        f"Complemento: {self.complemento}"
        f"Cep: {self.cep}"
        f"Cidade: {self.cidade}"
        
        )