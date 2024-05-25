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
        # y el parámetro num_generaciones con valor 3, aunque no nos sirve de mucho
        self.declare_parameter('my_parameter', 'world')
        self.declare_parameter('num_generaciones', 2)
        # bucle de espera para ser atendido por el servidor
        # da un mensaje de información diciendo que se está a la espera de  
        # ser atendido , cuando se sale del bucle se realiza la petición de servicio
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = MySimulatorPID.Request()

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
 
    # bucle del número de iteraciones que tenga el parámetro generaciones
    # si no se ha cambiado serán 2, es para imitar el funcionamiento del algoritmo genético
    # si no hay cambio del valor del parámetro param_generaciones vale 2   
    param_generaciones= minimal_client.get_parameter('num_generaciones').get_parameter_value().integer_value
    print("El número de generaciones es de ", param_generaciones,".")
    respuesta=input('¿Quieres cambiar el número de generaciones? (s/n)')
    if(respuesta=='s'):
        print('Mientras se ejcuta el for, cambia my_param mediante el servidor de parámetros, desde otro terminal.')
        respuesta_generaciones=input('Introduce un número de generaciones muy alto: ')
        param_generaciones= int(respuesta_generaciones)
                
    print("El número de generaciones es de ", param_generaciones,".")
    for generacion in range(param_generaciones):
        
        my_param = minimal_client.get_parameter('my_parameter').get_parameter_value().string_value
        # podríamos generar aleatoriamente los parámetros kp, ki y kd
        # pero vamos a probar a introducirlos junto con la ejecución del nodo cliente
        # a partir del primer parámetro ya se genera el segundo en el bucle
        # son valores y operaciones básicas para comprobar la comunicación
        
        # en response, se guarda la respuesta del servidor al que se le mandan
        # kp, ki y kd como parámetros junto con la ejecución del nodo cliente genetic ejemplo: ros2 run genetic_pkg genetic 2.0 3.0 4.0 
        response = minimal_client.send_request(float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion)
        
        # con la información de la respuesta se genera un mensaje de información 
        # si ponemos un número alto de generaciones me puede dar tiempo a cambiar el parámetro
        minimal_client.get_logger().info('Hello %s!' % my_param)
        minimal_client.get_logger().info(
            'Result from server to this three parameters: for Kp= %d  Ki=%d Kd= %d \n Overshoot= %d d= %d Ess= %d ts= %d' %
            (float(sys.argv[1])+ generacion, float(sys.argv[2])+ generacion, float(sys.argv[3])+ generacion, response.overshoot,
                                                                                                        response.d, response.ess, response.ts))
    # cuando se termina se destruye la instancia
    # se terminan las comunicaciones
    # aquí debería preguntar si cerramos nodo 
    # o si hacemos una nueva ejecución con cambio previo de parámetros
    minimal_client.destroy_node()
    rclpy.shutdown() 
    
if __name__ == '__main__':
    main()
    
    