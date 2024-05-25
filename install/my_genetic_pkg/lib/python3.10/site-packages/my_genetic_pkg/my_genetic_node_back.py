import sys
import rclpy
from rclpy.node import Node
from my_messages_control.srv import MySimulatorPID

# clase que declara el nodo
class MyGeneticPIDClient(Node):
    
    # función de inicialización de ejecución automátic
    # cuando se instancia la clase
    def __init__(self):
       
        super().__init__('my_genetic_client_node_async')
        # creación del cliente de servicio, con el tipo de comunicación , 
        # y nombre del nodo cliente         
        self.cli = self.create_client(MySimulatorPID, '/serv/my_sim_pid')
        
        # declaramos un parámetro my_parameter con valor world 
        self.declare_parameter('my_parameter', 'world')
        self.declare_parameter('num_generaciones', 3)
        # bucle de espera para ser atendido por el servidor
        # da un mensaje de información diciendo que se está a la espera de  
        # ser atendido
        # Cuando se sale del bucle se realiza la petición de servicio
        
    # nuevo   
    #while not self.cli.wait_for_service(timeout_sec=1.0):
        #    self.get_logger().info('service not available, waiting again...')
        #self.req = MySimulatorPID.Request()

    # función de petición de servicio al servidor con los parámetros 
    # de los cuales se requiere saber sus índices de rendimiento
    def send_request(self, kp, ki, kd):
        self.req.kp = kp
        self.req.ki = ki
        self.req.kd = kd
        # se define una comunicación asíncrona
        self.future = self.cli.call_async(self.req)
        # ejecutar hasta que self.future se complete
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

# función pricipal
def main():
    # incialización de comunicaciones
    rclpy.init()
    #instanciación de la clase declarada arriba
    minimal_client =MyGeneticPIDClient()
    #nuevo
    while not minimal_client.cli.wait_for_service(timeout_sec=5.0):
        minimal_client.get_logger().info('Service not available, waiting again...')
        minimal_client.get_logger().info('Aprovecha para configurar el nodo cambiando parámetros desde otro terminal,')
        minimal_client.get_logger().info('antes de activar el nodo servidor. Tambien puedes dejarlo con los valores')
        minimal_client.get_logger().info('por defecto que se encuentren en el código, o con los cargados mediante el ')
        minimal_client.get_logger().info('el fichero de configuración. Después  de decidir, arranca el servidor. ')
        minimal_client.get_logger().info('###################################################################### ')
        # si no se recibe ningún valor parametro_generaciones será 3
        param_generaciones= minimal_client.get_parameter('num_generaciones').get_parameter_value().integer_value
        #minimal_client.req = MySimulatorPID.Request()
        
    minimal_client.req=MySimulatorPID.Request()

    
   
    # bucle de dos iteraciones para imitar el algoritmo genético 
    # el AG deberá llamar tantas veces al servicio como cromosomas o 
    # individuos tenga que evolucionar. 
    
    # esto es de topics
        #num_generaciones= minimal_client.create_subscription(int(),"num_generaciones")

    # en teoría si no se cambia, tenemos 3 y si se cambia tendremos el valor en el que se cambia       
    minimal_client.get_logger().info('número de generaciones: %d' % param_generaciones)
    
    for generacion in range(param_generaciones):
        
        my_param = minimal_client.get_parameter('my_parameter').get_parameter_value().string_value
        # podríamos generar aleatoriamente los parámetros kp, ki y kd
        # pero vamos a probar a introducirlos junto con la ejecución del nodo cliente
        # a partir del primer parámetro ya se genera el segundo en el bucle
        # son valores y operaciones básicas para comprobar la comunicación
        
        # en response, se guarda la respuesta del servidor al que se le mandan
        # kp, ki y kd como parámetros junto con la ejecución del nodo cliente genetic: ros2 run genetic_pkg genetic 2.0 3.0 4.0 
        response = minimal_client.send_request(float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion)
        
        # con la información de la respuesta se genera un mensaje de información 
        minimal_client.get_logger().info('Hello %s!' % my_param)
        minimal_client.get_logger().info(
            'Result from server to this three parameters: for Kp= %d  Ki=%d Kd= %d \n Overshoot= %d d= %d Ess= %d ts= %d' %
            (float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion, response.overshoot,
                                                                                                        response.d, response.ess, response.ts))
    # cuando se termina se destruye la instancia
    # se terminan las comunicaciones
    minimal_client.destroy_node()
    rclpy.shutdown() 
    
if __name__ == '__main__':
    main()
    
    