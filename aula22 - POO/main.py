# Imports
from robo import RoboIndustrial

print("--- Criando robôs (instâncias) ---\n")

# Instanciando os objetos
robo_alpha =  RoboIndustrial("Alpha_01", x=0, y=0)
robo_beta  =  RoboIndustrial("Beta_02", x= 10, y= 5)

# Usando os objetos criados
robo_alpha.ligar().mover_para(5,5)
print(f"status do Alpha:{robo_alpha.status}")
print()
print(f"Objeto Alpha: {robo_alpha}")
print(f"ID da mémoria: {id(robo_alpha)}")
print(f"Tipo: {type(robo_alpha).__name__}")
print()
print(f"\nObjeto Beta: {robo_beta}")
print(f"ID da mémoria: {id(robo_beta)}")
print()
print(f"Mesma classe? {type(robo_alpha) == type(robo_beta)}")
print()  
print(f"\n--- Atributo de Classe vs Instância ---")
print(f"Fabricante (classe: {RoboIndustrial.FABRICANTE})")
print(f"Fabricante ( via objeto) {robo_alpha.FABRICANTE})")
print(f"Mesma fabricante? {robo_alpha.FABRICANTE == robo_alpha.FABRICANTE}")
print(f"")


