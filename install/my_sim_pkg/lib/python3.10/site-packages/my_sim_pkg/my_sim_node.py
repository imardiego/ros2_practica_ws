import rclpy
from rclpy.node import Node
from my_messages_control.srv import MySimulatorPID

# clase que contiene al nodo
class MySimPIDService(Node):
    
    # inicialización automática del nodo cuando se instancia
    def __init__(self):
        super().__init__('my_sim_pid_node')
        # se crea el servicio con un interface, un nombre de servicio y una función callback
        self.srv = self.create_service(MySimulatorPID, '/serv/my_sim_pid', self.my_sim_pid_callback)
               
    # función a  realizar despues de inicializar y crear el servicio           
    def my_sim_pid_callback(self, request, response):
        # se emite por pantalla que se ha recibido una petición y se pintan los parámetros
        # recibidos junto con la petición de servicio 
        self.get_logger().info('Incoming request\nkp: %f ki %f kd: %f' % (request.kp, request.ki, request.kd))
        
        # forma sencilla de simular que utilizamos los parámetros de 
        # la petición de servicio para calcular los indexes
        response.overshoot = request.kp*1
        response.d = request.kp*2
        response.ess = request.ki*3
        response.ts = request.kd*4
        #calculados los indexes, se envian con return      
        return response

# función principal
def main(args=None):
    rclpy.init(args=args)
    manager = None
    # mientras no se produzca una interrupción de teclado
    # se crea ina instancia de la clase declarada arriba
    # se la pone a funcionar ejecutando su callback
    try:
        manager = MySimPIDService()
        rclpy.spin(manager) 
        
    except KeyboardInterrupt:
        print(f'{manager.get_name()}: Keyboard interrupt')
        manager.destroy_node()
        rclpy.try_shutdown()
        
    except Exception:
        print(format_exc())

if __name__ == '__main__':
    main()
