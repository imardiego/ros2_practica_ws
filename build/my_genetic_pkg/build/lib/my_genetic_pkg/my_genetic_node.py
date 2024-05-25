import sys
import rclpy
from rclpy.node import Node
from my_messages_control.srv import MySimulatorPID
from std_msgs.msg import String

# clase que declara el nodo
class MyGeneticPIDClient(Node):
    
    # función de inicialización que se ejecuta automáticamente
    # al instanciar  la clase 
    def __init__(self):
       
        super().__init__('my_genetic_client_node_async')
        # creación del  cliente de servicio especificando la estructura de comunicación  
        # y el servidor de servicio 
        self.declare_parameter('my_parameter', 'world')
        # las siguiente es  nueva
        self.subscription = self.create_subscription(String,'miguel', self.listener_callback,10)
        self.cli = self.create_client(MySimulatorPID, '/serv/my_sim_pid')
        # bucle de espera para ser atendido por el servidor
        # da un mensaje de información diciendo  que se está a la espera  de  ser atendido
        # cuando sale del bucle realiza la peticion de servicio
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = MySimulatorPID.Request()

    # función de petición de servicio al servidor con los parámetros
    # de los cuales se quiere saber sus índices de rendimiento
    
    def listener_callback(self, msg):
        self.my_param=msg.data
        
    def send_request(self, kp, ki, kd):
        self.req.kp = kp
        self.req.ki = ki
        self.req.kd = kd
        # se define comunicacion asíncrona
        self.future = self.cli.call_async(self.req)
        # ejecutar hasta que se self.future se complete
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
    
# función principal
def main():
   
    # inicializa comunicaciones
    rclpy.init()
    # instanciacion de la clase declarada arriba
    minimal_client =MyGeneticPIDClient()
    generaciones=2
    # bucle de dos iteraciones para imitiar el algoritmo genético
    # que hará un requerimiento al servidor por cada cromosoma (kp,ki,kd)
    # aquí solo se hará dos  veces
    for generacion in range(generaciones):
        minimal_client.my_param=minimal_client.get_parameter('my_parameter').get_parameter_value().string_value
        # podríamos generar aleatoriamente los parámetros kp, ki y kd
        # pero vamos a probar a introducirlos junto con la ejecución del nodo cliente
        # a partir del primer parámetro ya se genera el segundo en el bucle
        # son valores y operaciones básicas para comprobar la comunicación
        
        # en response, se guarda la respuesta del servidor al que se le mandan
        # kp, ki y kd como parámetros junto con la ejecución del nodo cliente genetic ejemplo: ros2 run genetic_pkg genetic 2.0 3.0 4.0 
        response = minimal_client.send_request(float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion)
        # con la información de la respuesta se genera un mensaje de información 
        # si ponemos un número alto de generaciones me puede dar tiempo a cambiar el parámetro
        minimal_client.get_logger().info('Hello %s!' % minimal_client.my_param)
        #minimal_client.get_logger().info(
        #    'Result from server to this three parameters: for Kp= %d  Ki=%d Kd= %d \n Overshoot= %d d= %d Ess= %d ts= %d \n %s' %
        #    (float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion, response.overshoot, response.d, 
        #                                                                                                   response.ess, response.ts, my_param))
        minimal_client.get_logger().info(
            'Result from server to this three parameters: for Kp= %d  Ki=%d Kd= %d \n Overshoot= %d d= %d Ess= %d ts= %d' %
            (float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion, response.overshoot, response.d, 
                                                                                                                 response.ess, response.ts))

    minimal_client.destroy_node()
    rclpy.shutdown() 
    
    


if __name__ == '__main__':
    main()