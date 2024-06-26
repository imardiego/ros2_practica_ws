#from logging import debug, warn
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
        # suscripción al topic stop para prueba de 
        # cambio shutdown desde el topic
        self.subscription = self.create_subscription(String,'stop_genetic_node', self.listener_callback,10)
                     
        #ZONA DE DECLARACION DE PARAMETROS AG  
        self.declare_parameter('population_size', 100)
        self.declare_parameter('chromosome_length',3)
        self.declare_parameter('generations',200)
        self.declare_parameter('mutation_rate', 0.1)
        self.declare_parameter('crossover_rate', 0.6)
        
        #self.declare_parameter('log_level','INFO')
        
        # idioma de de información de solicitudes y respuesta de servicio, es: español en:ingles
        self.declare_parameter('idioma','en')    
        
        # ZONA CREACIÓN CLIENTE DE SERVICIO
        # creación del  cliente de servicio especificando 
        # estructura de comunicación y servidor de servicio 
        self.cli = self.create_client(SimPID, '/serv/sim_pid')
        
        # bucle de espera para ser atendido por el servidor
        # avisa de que el servidor no está activo
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
            self.get_logger().info('si el nodo servidor no está levantado, levántalo!!')
            
        # cuando el servidor esté activo instancia la interfaz de comunicación
        self.req = SimPID.Request()
        
        #INSTANCIA AG
        self.AG = Genetico()
        
        # ZONA DE LOG LEVEL
        # el  nivel de log es INFO
        # rclpy.logging.set_logger_level('genetic_algorithm_node', rclpy.logging.LoggingSeverity.INFO)
        
    # ZONA TOPIC CALLBACK        
    # En el momento que se recibe un valor por el topic
    # se ejecuta esta función 
    def listener_callback(self, msg):
        if(msg.data=="True"): 
            self.get_logger().info('Apagado del nodo mediante el valor llegado por el topic /stop_genetic_node:= %s' % (msg.data))
            self.destroy_node() 
            rclpy.shutdown() 
    
    
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
    
    # la siguiente línea se ejecuta en el método llamada control de AG:
    #idioma=indexes_client.get_parameter('idioma').get_parameter_value().string_value
    #yestop=indexes_client.get_parameter('stop').get_parameter_value().integer_value
   
   
    #cadena="rclpy.logging.set_logger_level('genetic_algorithm_node', rclpy.logging.LoggingSeverity." + nivel_log +")"
    rclpy.logging.set_logger_level('genetic_algorithm_node', rclpy.logging.LoggingSeverity.INFO)
    indexes_client.get_logger().info('PARÁMETROS DE EJECUCIÓN DEL ALGORITMO GENÉTICO') 
    indexes_client.get_logger().info('Población: %d  Cromosomas: %d Generaciones: %d Mutación: %f Emparejamiento: %f' % 
                                                        (poblacion, cromosomas, generaciones, mutacion, emparejamiento)) 
    
    # ZONA  DE INTERACCIÓN CON EL USUARIO
    # input("Pulsa Enter para ejecutar el algoritmo genético!!")
    
    # ZONA EJECUCIÓN ALGORTIMO GENETICO
    mejor_cromosoma=indexes_client.AG.genetic_algorithm(poblacion, cromosomas, generaciones, mutacion, emparejamiento)

    # ZONA FINALIZACIÓN ALGORITMO GENÉTICO
    indexes_client.get_logger().info('Mejor cromosoma: %s' % str(mejor_cromosoma)) 
    
    # ZONA DE DESTRUCCIÓN DEL NODO CLIENTE    
    # cuando el cliente acaba de necesitar el servicio se destruye
    # Podría meter esto en un try except, de modo que preguntase
    # al usuario si quiere volver a ejecutar el nodo
    # no obstante, debido a los problemas encontrados para cambiar de parámetros en 
    # tiempo de ejecución, explicados en el punto 4.7.1, no veo necesidad de mantener el nodo 
    # "corriendo", prefiero preparar distintos ficheros de inicialización de parámetros con 
    # distintos valroes
    indexes_client.destroy_node() 
    rclpy.shutdown() 


if __name__ == '__main__':
    main()
    
    
    
    