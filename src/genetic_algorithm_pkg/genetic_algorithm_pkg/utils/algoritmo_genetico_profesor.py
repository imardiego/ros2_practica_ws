import random
from operator import itemgetter

#algoritmo genético
class Genetico:

    def __init__(self):
        #Fitness
        self.Fitness = 0;
        self.w = (25., .6, 200., 15.) # weight of ts, d, overshot, ess 
        
    def set_request(self,request):
        self.request = request
        
    def llamada_control(self, Gen_Kp, Gen_Ki, Gen_Kd):   
        
        # Crear una instancia del controlador
        #controller = Controller()
        #Kp=Gen_Kp
        #Ki=Gen_Ki
        #Kd=Gen_Kd
        #velocidad=[]
        #ut=[]
        #coordenadax=[]
        #Velocidad_de_referencia = 50.0
        #overshoot = 0.0
        #d=0.0
        #Ess=0.0
        #Ts = 0.0
        
        # Inicializar el controlador con los valores de ganancia
        #controller.Init(Kp, Ki, Kd)
        
        # Establecer la velocidad de referencia
        #controller.Set_reference(Velocidad_de_referencia)

        # Ejecutar 320 ciclos del controlador
        #for ite in range(320):
        #    x,y = controller.Exec_controller_cycle()
        #    velocidad.append(x)
            
        #Cálculo de los índices de rendimiento
        #P = Performance() 
        #P.Init(velocidad, Velocidad_de_referencia)
        #overshoot, d, Ess, Ts = P.Calcula_indexes()
        print("hola")
        Fitness = 0 # Aquí se debe implementar la función de fitness correspondiente
    #Fitness= overshoot * self.w[2] + d * self.w[1] + Ess * self.w[3] + Ts * self.w[0]
        # MIRAR INIT SELF.W
        # LEER EL ARTICULO PARA MEJORAR
        return Fitness

    
    # Función de evaluación (fitness)
    def evaluate(self, chromosome):
        # Aquí debes implementar la evaluación del cromosoma y retornar un valor de fitness
        fitness = self.llamada_control(chromosome[0], chromosome[1], chromosome[2])
        return fitness

    # Generar un cromosoma aleatorio
    def generate_random_chromosome(self, length):  
        chromosome = []
        for _ in range(length):
            gene = random.uniform(0.0, 10.0)  # Generar número aleatorio en el rango [0.0, 10.0]
            chromosome.append(gene)            
        return chromosome

    # Cruzar dos cromosomas
    def crossover(self, chromosome1, chromosome2, crossover_rate):
        new_chromosome=chromosome1
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, len(chromosome1) - 1)
            new_chromosome = chromosome1[:crossover_point] + chromosome2[crossover_point:]
        return new_chromosome
        
    # Mutar un cromosoma
    def mutate(self, chromosome, mutation_rate):
        mutated_chromosome = []
        for gene in chromosome:
            if random.random() < mutation_rate:
                mutated_gene = random.uniform(0.0, 10.0)  # Generar número aleatorio en el rango [0.0, 5.0]
            else:
                mutated_gene = gene
            mutated_chromosome.append(mutated_gene)
        return mutated_chromosome

    #selección por torneo
    def selection_tournament(self, population_size, evaluated_population, T):
            parents = []            
            while len(parents) < population_size:
                candidates=[]
                for ite in range(T):
                    candidates.append(random.choice(evaluated_population))                            
                parents.append(min(candidates, key=itemgetter(1))[0])
            return parents
    
    # Algoritmo genético
    def genetic_algorithm(self, population_size, chromosome_length, generations, mutation_rate, crossover_rate):
        population = []
        for _ in range(population_size):
            chromosome = self.generate_random_chromosome(chromosome_length)
            population.append(chromosome)
       
        for generation in range(generations):            
            # Evaluación de la población
            evaluated_population = [(chromosome, self.evaluate(chromosome)) for chromosome in population]

            # Selección de padres mediante torneo de longitud T
            parents = []
            T=8 # Se seleccionan 8 cromosomas de manera aleatoria pra el torneo. Nos quedaremos con el de menor función de fitness
            parents = self.selection_tournament(population_size, evaluated_population, T)

            # Cruzamiento y mutación para generar descendencia
            offspring = []
            for i in range(0, population_size, 2):
                parent1 = parents[i]
                parent2 = parents[i + 1]
                child1 = self.crossover(parent1, parent2, crossover_rate)
                child2 = self.crossover(parent2, parent1, crossover_rate)
                mutated_child1 = self.mutate(child1, mutation_rate)
                mutated_child2 = self.mutate(child2, mutation_rate)
                offspring.extend([mutated_child1, mutated_child2])

            # Reemplazar la población anterior con la descendencia
            population = offspring

        # Devolver el mejor cromosoma de la última generación
        best_chromosome = min(evaluated_population, key=lambda x: x[1])#[0]
        return best_chromosome