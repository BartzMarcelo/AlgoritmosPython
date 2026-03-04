class RoboIndustrial:
    """
    Classe que representa um robô industrial de soldagem.
    """
    
    # Atributos de classe (precisam estar recuados!)
    FABRICANTE = "Autotech Industries"
    VERSÃO_SOFTWARE = "2.5.1"

    def __init__(self, nome, x=0, y=0):  
        """
        Método construtor: inicializa um novo robô.
        """
        self.nome = nome
        self.posicao_x = x
        self.posicao_y = y # Corrigi para 'y' aqui, antes estava 'x'

        # O prefixo _ (underscore) indica atributos protegidos
        self._bateria = 100
        self._esta_ligado = False

    def ligar(self):
        """
        Método de instância: opera sobre os dados do próprio objeto.
        """
        if not self._esta_ligado:
            self._esta_ligado = True
            print(f"[{self.nome}] Sistema Iniciado: Bateria {self._bateria} % .")
        else:
            print(f"[{self.nome}] Já esta ligado.")
        return self
    # Fim do método ligar()

    def desligar(self):
        """ Desliga o robô de forma segura."""
        if self._esta_ligado:
            self._esta_ligado = False
            print(f"[{self.nome}] Sistema desligado.")
        return self
    # Fim metodo desligar()

    def mover_para(self, novo_x, novo_y):
        """ Move o motor para nova posição. 
        Args:
        novo_x, novo_y: são as coordenadas de destino.  

        """
        if not self._esta_ligado:
            print(f"[{self.nome}] Erro: Robô desligado. Ligue antes de mover. ")
            return self
        # Calcula a distância Euclidiana
        distancia = ((novo_x - self.posicao_x)**2 + (novo_y - self.posicao_y)**2)**0.5
        # Atualiza estado interno
        self.posicao_x = novo_x
        self.posicao_y = novo_y
        self._bateria -= distancia * 0.1
        print(f"[{self.nome}] Movido para ({novo_x}, {novo_y})." f"Distância:{distancia:.1f}m | Bateria: {self._bateria:.1f}% .") 
        return self

    # Fim do método mover_para

    def status(self):
        """ Retorna reprsentação textual do estado atual."""
        estado = "Ligado" if self._esta_ligado else " Desligado"
        return(f"[{self.nome}] Pos:({self.posicao_x}, {self.posicao_y})| " f"{self._bateria:.0f}% | {estado}")
    # Fim do método status
    
# Fim da classe RoboIndustrial

