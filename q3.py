from abc import ABC, abstractmethod

class Veiculo():
    def __init__(self,tipo):
        self.tipo_veiculo = tipo

    @abstractmethod
    def criarMotor(self):
        pass

    def descricao(self):
        produto = self.criarMotor()
        return self.tipo_veiculo + ' com ' + produto.operacao()


class VeiculoCombustao(Veiculo):
    def __init__(self,tipo):
        super().__init__(tipo)
    def criarMotor(self):
        return MotorCombustao()

class VeiculoEletrico(Veiculo):
    def __init__(self,tipo):
        super().__init__(tipo)
    def criarMotor(self):
        return MotorEletrico()

class VeiculoHibrido(Veiculo):
    def __init__(self,tipo):
        super().__init__(tipo)
    def criarMotor(self):
        return MotorHibrido()


class Motor():

    @abstractmethod
    def operacao(self):
        pass

class MotorCombustao(Motor):
    def operacao(self):
        return "motor movido a combustao"

class MotorEletrico(Motor):
    def operacao(self):
        return "motor movido a energia eletrica"

class MotorHibrido(Motor):
    def operacao(self):
        return "motor movido a combustao e energia eletrica"


auto1 = VeiculoEletrico('moto')
print(auto1.descricao())

auto2 = VeiculoHibrido('carro')
print(auto2.descricao())

auto3 =VeiculoCombustao('caminhao')
print(auto3.descricao())
