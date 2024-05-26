import sys
import rclpy
from rclpy.node import Node
from msgs_control.srv import SimPID
 # importo este interfaz para cambio de parámetro string
from std_msgs.msg import String 
from genetic_algorithm_pkg.utils.algoritmo_genetico_profesor import Genetico

# clase que declara el nodo
class GeneticIndexesClient(Node):
    
    # Este init se ejecuta de manera automática al instanciar
    # la clase GeneticPerformanceClient
    def __init__(self):
           
        # nombre del nodo de cara a otros nodos
        super().__init__('genetic_algorithm_node')
        
        # ZONA TOPICS
        # suscripción al topic miguel para prueba de 
        # cambio de parámetros leyendo de un topic
        self.subscription = self.create_subscription(String,'miguel', self.listener_callback,10)
        
        # ZONA DE DECLARACIÓN DE PARAMTEROS DE PRUEBA
        # declaración de parámetro para pruebas de cambio de valor
        # en tiempo de ejecución
        self.declare_parameter('my_parameter', 'world')
        
        #ZONA DE DECLARACION DE PARAMETROS AG  
        self.declare_parameter('population_size', 100)
        self.declare_parameter('chromosome_length',3)
        self.declare_parameter('generations',500)
        self.declare_parameter('mutation_rate', 0.1)
        self.declare_parameter('crossover_rate', 0.6)
                
        # ZONA CREACIÓN CLIENTE DE SERVICIO
        # creación del  cliente de servicio especificando 
        # estructura de comunicación y servidor de servicio 
        self.cli = self.create_client(SimPID, '/serv/sim_pid')
        
        # bucle de espera para ser atendido por el servidor
        # avisa de que el servidor no está activo
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
            
        # cuando el servidor esté activo instancia 
        # la interfaz de comunicación
        self.req = SimPID.Request()
        
        #INSTANCIA AG
        self.AG = Genetico()
        
        
    # ZONA TOPIC CALLBACK        
    # En el momento que se recibe un valor por el topic
    # se ejecuta esta función asignando dicho valor al parámetro declarado arriba
    def listener_callback(self, msg):
        self.my_param=msg.data
    
    
    # ZONA FUNCIÓN ENVIO PETICIÓN SERVICIO
    # declaración de la función de peticion de servico
    def send_request(self, kp, ki, kd):
        # se asignan los valores en relación
        # a la estructura de la interfaz
        # en su parte de solicitu de servicio
        self.req.kp = kp
        self.req.ki = ki
        self.req.kd = kd
        
        # se define comunicacion asíncrona
        self.future = self.cli.call_async(self.req)
        
        # ejecutar hasta que se self.future se complete
        rclpy.spin_until_future_complete(self, self.future)
        
        # devolver el resultado de la respuesta del servidor
        return self.future.result()
    
    
 
    
# función principal
def main():
   
    # inicializa comunicaciones
    rclpy.init()
    # instanciacion de la clase declarada arriba.
    indexes_client =GeneticIndexesClient()
    
    # Seteo como objeto de AG a indexes_client
    indexes_client.AG.set_request(indexes_client)
    indexes_client.AG.llamada_control(335.0,336.0,337.0)
   
    # ZONA DE OBTENCION DE PARÁMETROS
    # el parámetro se inicializó en su declaración, pero si ha habido un lanzamiento con parámetros
    # o si ha habido una llegada de parámatros por topic, estos alteran el valor inicial del parámetro
    # si no se ha producido ninguno, la solicitar el valor del parámetro y depositarlo en una variable
    # éste será de la declaración inicial del parámetro.      
    poblacion=indexes_client.get_parameter('population_size').get_parameter_value().integer_value
    cromosomas=indexes_client.get_parameter('chromosome_length').get_parameter_value().integer_value
    generaciones=indexes_client.get_parameter('generations').get_parameter_value().integer_value
    mutacion=indexes_client.get_parameter('mutation_rate').get_parameter_value().double_value
    emparejamiento=indexes_client.get_parameter('crossover_rate').get_parameter_value().double_value
    
    print("Poblacion:", poblacion, "Cromosomas:", cromosomas, "Generaciones:", generaciones, "Mutacion:", mutacion, "Emparejamiento:",emparejamiento)
   
    # hay que llamar al algoritmo genético con todos los parámetros del profe
    # mejor_cromosoma=indexex_client.genetic_algorithm(poblacion, cromosomas, generaciones, mutation, emparejamiento)
    
    # mensaje dese aquí 
    # info del mejor cromosoma
    
    # ver si puedo hacer topic para pintar
   
    # bucle de dos iteraciones para imitiar el algoritmo genético
    # que realiza una petición por cada individuo enviando kp, ki, kd
    num_generaciones=2
    for generacion in range(num_generaciones):
        
        # se solicita el valor del parámetro my_parameter, si no ha llegado por fichero de inicialización
        # o no se ha cambiado por la llegada de un valor por el topioc de arriba, conserva el valor que 
        # tenga en su declaración, en este caso "world" 
        indexes_client.my_param=indexes_client.get_parameter('my_parameter').get_parameter_value().string_value
        
               
        # en response, se guarda la respuesta del servidor al que se le solicita el servicio
        # en este caso la petición se realiza con los argumentos que se entregan o por línea de comando o por fichero
        # de inicialización, respectivamente: ros2 run genetic_pkg genetic 2.0 3.0 4.0  y argument['2.0','3.0','4.0']
        response = indexes_client.send_request(float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion)
        
        # aviso por pantalla para comprobar si se ha cambiado en tiempo de ejecución un parámetro 
        # recepcionado tanto por topic como por fichero de inicialización :  parameter [ ]
        indexes_client.get_logger().info('Hello %s!' % indexes_client.my_param) 
        
        # utilizo los índices de rendimiento o,d, Ess, ts del response para generar un aviso en el que se informa
        # la respuesta con o, d, Ess, ts, con la petición de servicio con kp, ki, kd
        indexes_client.get_logger().info(
            'Result from server to this three parameters: for Kp= %d  Ki=%d Kd= %d \n Overshoot= %d d= %d Ess= %d ts= %d' %
            (float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion, response.overshoot, response.d, 
                                                                                                                 response.ess, response.ts))

    # cuando el cliente acaba de necesitar el servicio
    # se destruye
    indexes_client.destroy_node()
    rclpy.shutdown() 


if __name__ == '__main__':
    main()
    
    
    
    