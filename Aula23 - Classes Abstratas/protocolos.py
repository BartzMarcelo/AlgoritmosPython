from typing import Protocol, Dict, Any

class Serializavel(Protocol):
    """ Protocolo: define a estrutura esperada.
        Qualquer objeto com estes métodos será aceito.
    """

    def salvar(self, caminho: str) -> bool: ...
    def to_dict(self) -> Dict[str, Any]: ...

class LoggerSimples:
    """ Não herda de nada, mas satisfaz Serializavel. """
    def salvar(self, caminho: str) -> bool: 
        print(f"Log salvo em {caminho}")
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        return{"tipo": "logger", "nível": " INFO"}
    
    def processar_serializavel(obj: Serializavel):
        """ Aceita QUALQUER objeto que satisfaça o protocolo."""
        obj.salvar("temp.txt")
        print(obj.to_dict())
