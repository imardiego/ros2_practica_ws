# Codificación algoritmo genético

import random
from operator import itemgetter

#algoritmo genético
class Genetico:

    # Se ejecuta automáticamente al generar una instancia de 
    # la clase Genetico
    def __init__(self):
        #Fitness
        self.Fitness = 0;
        self.w = (25., .6, 200., 15.) # weight of ts, d, overshot, ess 
        # Ponderación de los valores calculados. 
        self.porcentaje=0.5
        self.torneo=8
        self.cambiar_cruce_genes=0 
        
    def set_factores(self,alfa,beta,gamma,delta):
        self.w = (alfa, beta, gamma, delta)
        
    def set_torneo(self,torneo):
        self.torneo = torneo
    
    def set_cambiar_cruce_genes(self,cambiar):
        self.cambiar_cruce_genes=cambiar
    
    def llamada_control(self, Gen_Kp, Gen_Ki, Gen_Kd):   
        # Crear una instancia del controlador
        controller = Controller()
        Kp=Gen_Kp
        Ki=Gen_Ki
        Kd=Gen_Kd   
        velocidad=[]
        ut=[]
        coordenadax=[]
        Velocidad_de_referencia = 50.0
        overshoot = 0.0
        d=0.0
        Ess=0.0
        Ts = 0.0
        
        # Inicializar el controlador con los valores de ganancia
        controller.Init(Kp, Ki, Kd)
        
        # Establecer la velocidad de referencia
        controller.Set_reference(Velocidad_de_referencia)

        # Ejecutar 320 ciclos del controlador
        for ite in range(320):
            x,y = controller.Exec_controller_cycle()
            velocidad.append(x)
            
        #Cálculo de los índices de rendimiento
        P = Performance() 
        P.Init(velocidad,ut, Velocidad_de_referencia,self.porcentaje)
        overshoot, d, Ess, Ts = P.Calcula_indexes()
   
        Fitness= overshoot * self.w[2] + d * self.w[1] + Ess * self.w[3] + Ts * self.w[0]
        return Fitness

    
    # Función de evaluación (fitness)
    # En realidad en esta función no se hace nada, donde se hace es en el lugar del código
    # donde esta función de evaluación de la calidad del cromosoma, en función de sus genes
    # gen_Kp=chromosome[0], gen_Ki=chromosome[1], gen_Kd=cromosome[2]
    # Es en el punto donde ess llamaa donde se ejecuta la función de optimización y se 
    # devuelve su valor a través de fitness.
    # Fitness es calculado en la llamada de ejecuion del controlador PID del motor
    # que es donde se calculan los  índices de rendimiento. 
    def evaluate(self, chromosome):
        # Aquí debes implementar la evaluación del cromosoma y retornar un valor de fitness
        fitness = self.llamada_control(chromosome[0], chromosome[1], chromosome[2])
        return fitness
    
    
    # Generar un cromosoma aleatorio de longitud length con valores entre [0.0,10.0]
    # Se genera un cromosoma completamente aleatorio en el intervalor semicerrado [0.0,10.0)
    # Esto generará problemas a la hora de mantener los mismos algoritmos de cálculo de los 
    # índices de rendimiento, en concreto deberemos modificar Ts. 
    def generate_random_chromosome(self, length):  
        chromosome = []
        for _ in range(length):
            gene = random.uniform(0.0, 10.0)  # Generar número aleatorio en el rango [0.0, 10.0]
            chromosome.append(gene)   
            #print("cromosoma:",chromosome)         
        return chromosome

    #¿ES RELEVANTE QUE NUNCA HAYA CRUZAMIENTO DE KP?
    # Se ha  modificado el código para que cuando se quiera cruzar Kp
    # se permita el cruce dependiendo del valor de la varible cambiar_cruce_genes
    # si esta variable está a cero el cruce se hace de forma canónica
    def crossover(self, chromosome1, chromosome2, crossover_rate):
        new_chromosome=chromosome1
        if random.random() < crossover_rate:
            if(self.cambiar_cruce_genes):       
               crossover_point = random.randint(0, len(chromosome1) - 1)    
               if(crossover_point==0):
                    new_chromosome= [chromosome1[0]] + chromosome2[1:]
               else: 
                    new_chromosome = chromosome1[:crossover_point] + chromosome2[crossover_point:]
            else:
                crossover_point = random.randint(1, len(chromosome1) - 1)
                new_chromosome = chromosome1[:crossover_point] + chromosome2[crossover_point:]
        return new_chromosome
        
    # Mutar un cromosoma
    # Resultado de mutar un cromosoma. En realidad se comprueba si se cambia o no 
    # el valor de cada uno de sus genes, de tal manera que su valor en función de un
    # valor aleatorio < Pmut hará que el gen que cumpla la condición anterior, tome
    # un valor aleatorio del rango de valores posibles de entre[0.0, 10.0)
    def mutate(self, chromosome, mutation_rate):
        mutated_chromosome = []
        for gene in chromosome:
            if random.random() < mutation_rate:
                mutated_gene = random.uniform(0.0, 10.0)  # Generar número aleatorio en el rango [0.0, 5.0]
            else:
                mutated_gene = gene
            mutated_chromosome.append(mutated_gene)
        return mutated_chromosome

    # selección por torneo de los cromosomas
    # de manera aleatoria se eligen 8 candidatos en cada iteración
    # de los ocho se eligen el de menor valor de la función objetivo
    # uno de cada 8 hasta llegar a 100 o population_size
    def selection_tournament(self, population_size, evaluated_population, T):
            parents = []            
            while len(parents) < population_size:
                candidates=[]
                for ite in range(T):
                    candidates.append(random.choice(evaluated_population))                            
                parents.append(min(candidates, key=itemgetter(1))[0])
            return parents

    def set_porcentaje(self, porcentaje):
        self.porcentaje= porcentaje
            
    # Algoritmo genético
    def genetic_algorithm(self, population_size, chromosome_length, generations, mutation_rate, crossover_rate):
        
        # Generamos la población de cromosomas del tamaño de population_size=100
        # Esta es la población inicial de 100 cromosomas con tres genes con sus valores
        # generados aleatoriamente dentro de un rango [0.0,10.0) mediante generate_random_cromosome
        # la longitud de los cromosomas es  de tres genes: Kp, Ki,Kd
        population = []
        for _ in range(population_size):
            chromosome = self.generate_random_chromosome(chromosome_length)
            population.append(chromosome)
        # resultado: population tiene 100 cromosomas de tres genes cada uno kp,ki,kd
       
        # Calculamos el número de generaciones elegidas. Inicialmente = 200
        for generation in range(generations):            
            # Evaluación de la población
            # Cada cromosoma (kp,ki,kd) es evaluado por evaluate, que a su vez llama a 
            # llamada control, que debe aplicar la función fitness a los indices de 
            # rendimiento calculado para esos genes.
            # en evaluated_population se guardan los fitness de cada cromosoma del total de 100
            evaluated_population = [(chromosome, self.evaluate(chromosome)) for chromosome in population]
            
            # La forma de elegir los cromosomas iniciales, es por torneo
            parents = []
            #T=8 
            parents = self.selection_tournament(population_size, evaluated_population, self.torneo)
            # de entre 8 elegimos el de menor valor en la función objetivo y repetimos hasta
            # obtener una población.

            # De dos en dos tomamos esa primera población y 
            # los enfrentamos a la posibilidad de emparejamiento y mutación
            # DE 0 a 100 y de 2 en 2, acabamos obteniendo descendencia u offspring
            offspring = []
            for i in range(0, population_size, 2):
                
                # inf self.cambiar_orden_genes: cambiar el orden en los padres
                # ...... else: 
                # Si quisieramos cabiar el orden del gen Kp por el del Kd para 
                # estudiar su incidencia en la convergencia, habría de hacerse aquí 
                # intercambiando el orden en ambos padres.
                parent1 = parents[i]
                parent2 = parents[i + 1]
                child1 = self.crossover(parent1, parent2, crossover_rate)
                child2 = self.crossover(parent2, parent1, crossover_rate)
                # una vez realizado el posible cruzamiento
                # devolveríamos los genes a su lugar original antes de ser sometidos
                # a una posible mutación
                mutated_child1 = self.mutate(child1, mutation_rate)
                mutated_child2 = self.mutate(child2, mutation_rate)
                offspring.extend([mutated_child1, mutated_child2])

            # Reemplazar la población anterior con la descendencia
            # otros 100 cromosomas
            population = offspring

        # Devolver el mejor cromosoma de la última generación
        # De cada generación, obtego el mejor cromosoma, que será el de valor
        # el que tenga el valor mínimo en la función objetivo u optimización
        best_chromosome = min(evaluated_population, key=lambda x: x[1])#[0]
        
        return best_chromosome, self.w