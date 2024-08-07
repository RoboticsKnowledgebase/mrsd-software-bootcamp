try:
    import pygame
    from pygame.locals import K_DOWN
    from pygame.locals import K_LEFT
    from pygame.locals import K_RIGHT
    from pygame.locals import K_SPACE
    from pygame.locals import K_UP
    from pygame.locals import K_a
    from pygame.locals import K_d
    from pygame.locals import K_g
    from pygame.locals import K_p
    from pygame.locals import K_q
    from pygame.locals import K_r
    from pygame.locals import K_s
    from pygame.locals import K_w
except ImportError:
    raise RuntimeError('cannot import pygame, make sure pygame package is installed')


import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'


import rclpy
from rclpy.node import Node


from sensor_msgs.msg import Joy
import time


WINDOW_WIDTH = 100
WINDOW_HEIGHT = 100


def _get_keyboard_control(keys):
        """
        Return a VehicleControl message based on the pressed keys. Return None
        if a new episode was requested.
        """
        if keys[K_r]:
            return None
        control = [0.,0.,0,0,0,0,0,0]
        if keys[K_LEFT]:
            control[1] = -1.0
        if keys[K_RIGHT]:
            control[1] = 1.0
        if keys[K_UP]:
            control[0] = 1.0
        if keys[K_DOWN]:
            control[0] = -1.0
        if keys[K_s]:
            control[2] = 1
        if keys[K_w]:
            control[5] = 1
        if keys[K_a]:
            control[4] = 1
        if keys[K_d]:
            control[3] = 1
        if keys[K_p]:
            control[6] = 1
        return control


class MinimalPublisher(Node) :


    def __init__(self) :
        pygame.init()
        self._display = pygame.display.set_mode(
                (WINDOW_WIDTH, WINDOW_HEIGHT),
                pygame.HWSURFACE | pygame.DOUBLEBUF)


        super().__init__('publish_dummy_joy')
        self.publisher_ = self.create_publisher(Joy, '/joy',1)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
   
    def timer_callback(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        msg = Joy()
        msg.header.stamp = rclpy.clock.Clock().now().to_msg()
        control = _get_keyboard_control(pygame.key.get_pressed())
        # print(control)
        # msg.buttons = [1,1,1,1,1,1,1,1,1,1,1,1]
        msg.buttons = [0,0,0,0,control[4],0,0,0,0,0,0,0]#control[2:]#[control[2],0,0,0,0,0,0,0,0,0,0,0]
        msg.axes = [-control[1],-control[1],control[0],1.,1.,-control[0]]
        self.publisher_.publish(msg)
        # print("Published")


def main(args=None) :
    print("Instructions :-")
    print("Keep the generated window active to receive keyboard input")
    print("Use arrow keys to navigate")
    print("a : Gear trigger")
    print("w : Gear up")
    print("s : Gear down")
    print("p : e-stop")
    rclpy.init(args=args)


    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)


    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__' :    
    main()
    pygame.quit()