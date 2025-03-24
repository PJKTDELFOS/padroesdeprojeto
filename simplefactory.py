from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro Luxo esta buscando cliente ...")

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular esta buscando cliente ...")


class VeiculoFactory(Veiculo):
    @staticmethod
    def get_carro(tipo:str)->Veiculo:
        if tipo == "Luxo":
            return CarroLuxo()
        if tipo == "Popular":
            return CarroPopular()
        assert 0,'veiculo nao existe'

if __name__ == '__main__':
    from random import choice
    carros_disponivel=['Luxo','Popular']
    for i in range(10):
        carro=VeiculoFactory.get_carro(choice(carros_disponivel))
        carro.buscar_cliente()

