import numpy as np
import statistics as stat


class Performance:    
    def __init__(self):
        self.Overshoot = 0.0
        self.d = 0.0
        self.Ess = 0.0
        self.Ts = 0.0
        self.v = []
        self.VR = 0.0

    def Init(self, velocidades, Velocidad_de_referencia):
        self.Overshoot = 0.0
        self.d = 0.0
        self.Ess = 0.0
        self.Ts = 0.0
        self.v = velocidades
        self.VR = Velocidad_de_referencia
        
    def Calcula_indexes(self):
       # We assign the stable speed as the mean of the last 30 values
       # calcula la media de los últimos 30 valores de velocidad
        vel_estable = sum(self.v[-30:]) / 30

        # We define the stabilization error as the difference between the stable speed and the reference speed
        # define el error en régimen estacionario como la diferencia entre el SSV y el SP
        # obtendrá un valor negativo generalmente
        self.Ess = vel_estable - self.VR

        # This code activates a flag once the first maximum over the stable speed has been found, and stores that speed as the overshoot
        # Due to the extreme value theorem, in a closed interval of a continuous function, between two maximums there must be at least 
        # one minimum, so we use this to ensure that we are registering the next maximum that goes over the threshold after a minimum
        # to compute the decay value. Once this is done, we can exit the loop
        
        found_overshoot = False
        A = 0
        # Comienza a explorar todos los valores de velocidad desde la izquierda, desde 1 a 319  
        for i in range(1, len(self.v) - 1):
            # comprueba para cada i:
            # si el valor anterior es menor que el actual
            # si el valor actual es mayor que el siguiente 
            # y si el actual es mayor que el SSV 
            # Si i cumple estas condicions habrá encontrado índice del overshoot 
            # Para calcular el punto A se resta SSV
            # Para calcular el overshoot se divide por el SSV 
            if self.v[i - 1] < self.v[i] > self.v[i + 1] and self.v[i] > vel_estable:
                if not found_overshoot:
                    A = self.v[i] - vel_estable
                    self.Overshoot = A/vel_estable
                    found_overshoot = True
                # si se cumple la condición del primer if y se ha encontrado el primer 
                # overshoot, entonces se ha encontrado el segundo
                # y se calcula el punto C para obtener el decay ratio = C/A
                else:
                    self.d = (self.v[i] - vel_estable) / A 
                    break

        # We assign the threshold as a 1% variation respective to the stable speed
        # como tanto por ciento de error se asigna un 1%
        # el 1% de SSV . Ejemplo: supongamos SSV=50 el 1% de 50 es 0.5 = 0,01 *50 = 0.5
        # tenemos una banda de error de 0.5
        threshold = 0.01 * vel_estable

        # We will traverse the speed list and activate a flag that indicates that the speed is within the threshold if it is. 
        # If the flag is not activated, this means the previous values were not within the threshold, this way we will store the
        # first value within threshold while the next ones are also within the threshold. Otherwise, the value will be updated
        
        inThreshold = False
        # se recorre toda la lista de velocidades 
        # se resta a cada valor de la lista el valor estable 
        # en valor absoluto se comprueba si están dentro del rango.
        # si es así se guarda el índice
        for i, vel in enumerate(self.v):
            if abs(vel-vel_estable) < threshold:
                if not isThreshold:
                    self.Ts = i
                isThreshold = True
            else:
                isThreshold = False

        # If the last value was not within the threshold, this means that we did not reach stabilization
        # We will note that with the length of the velocity list + 1, but it could potentially be described in other ways
        # such as with a flag
        # si no se encuentra ningún valor dentro dentro del intervalo, se toma el último valor +1
        # NO LO ENTIENDO: este valor sería 321 y no existe
        if not isThreshold:
            self.Ts = len(self.v) + 1
        
        # devuelve el valor de Ts en segundos y no en ciclos
        self.Ts = self.Ts * 30 / 320
  
        return self.Overshoot, self.d, self.Ess, self.Ts
