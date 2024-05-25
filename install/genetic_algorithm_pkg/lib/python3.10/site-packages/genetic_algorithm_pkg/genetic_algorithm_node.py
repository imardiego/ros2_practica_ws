import sys
import rclpy
from rclpy.node import Node
from msgs_control.srv import SimPID
 # importo este interfaz para cambio de parámetro string
from std_msgs.msg import String 
from genetic_algorithm_pkg.utils.algoritmo_genetico_profesor import Genetico

# clase que declara el nodo
class GeneticPerformanceClient(Node):
    
    # Este init se ejecuta de manera automática al instanciar
    # la clase GeneticPerformanceClient
    def __init__(self):
        
        self.AG = Genetico()
       
        # nombre del nodo que aparecerá si hacemos
        super().__init__('genetic_algorithm_node')
        
        # declaración de parámetro para pruebas de cambio de valor
        # en tiempo de ejecución
        self.declare_parameter('my_parameter', 'world')
        
        # suscripción al topic miguel para prueba de 
        # cambio de parámetros leyendo de un topic
        self.subscription = self.create_subscription(String,'miguel', self.listener_callback,10)
        
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
        
        self.AG = Genetico()

        
    # En el momento que se recibe un valor por el topic
    # se ejecuta esta función asignando dicho valor al parámetro declarado arriba
    def listener_callback(self, msg):
        self.my_param=msg.data
    
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
    
    
    ## NOTA, DONDE SEA DEBO DE HACER LA LLAMADA A GA CON LOS PARÁMETROS
    # COMO EN LA PRÁCTICA
    
# función principal
def main():
   
    # inicializa comunicaciones
    rclpy.init()
    # instanciacion de la clase declarada arriba
    minimal_client =GeneticPerformanceClient()
   
    # bucle de dos iteraciones para imitiar el algoritmo genético
    # que realiza una petición por cada individuo enviando kp, ki, kd
    generaciones=2
    for generacion in range(generaciones):
        
        # se solicita el valor del parámetro my_parameter, si no ha llegado por fichero de inicialización
        # o no se ha cambiado por la llegada de un valor por el topioc de arriba, conserva el valor que 
        # tenga en su declaración, en este caso "world" 
        minimal_client.my_param=minimal_client.get_parameter('my_parameter').get_parameter_value().string_value
        
               
        # en response, se guarda la respuesta del servidor al que se le solicita el servicio
        # en este caso la petición se realiza con los argumentos que se entregan o por línea de comando o por fichero
        # de inicialización, respectivamente: ros2 run genetic_pkg genetic 2.0 3.0 4.0  y argument['2.0','3.0','4.0']
        response = minimal_client.send_request(float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion)
        
        # aviso por pantalla para comprobar si se ha cambiado en tiempo de ejecución un parámetro 
        # recepcionado tanto por topic como por fichero de inicialización :  parameter [ ]
        minimal_client.get_logger().info('Hello %s!' % minimal_client.my_param) 
        
        # utilizo los índices de rendimiento o,d, Ess, ts del response para generar un aviso en el que se informa
        # la respuesta con o, d, Ess, ts, con la petición de servicio con kp, ki, kd
        minimal_client.get_logger().info(
            'Result from server to this three parameters: for Kp= %d  Ki=%d Kd= %d \n Overshoot= %d d= %d Ess= %d ts= %d' %
            (float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion, response.overshoot, response.d, 
                                                                                                                 response.ess, response.ts))

    # cuando el cliente acaba de necesitar el servicio
    # se destruye
    minimal_client.destroy_node()
    rclpy.shutdown() 


if __name__ == '__main__':
    main()
    
    
    
    