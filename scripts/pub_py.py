#!/usr/bin/env python3.6

import rospy

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.slider import Slider


from std_msgs.msg import String

class TutorialApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("debug")
        self.password = "0"
        self.screen = Builder.load_file('/home/csw/catkin_ws/src/umbot_gui/umbot.kv')
        #self.screen = Builder.load_file('/home/csw/rosgui.kv')
        #print("debug22222222222222")

    def build(self):
        return self.screen
        #return Label(text="Hello, World")

    def buttonExplore_pressed(self, *args):
        print("button pressed")
        # msg = "Hello GUI"
        # self.screen.ids.labelDestination.text = "button pressed"
        # pub.publish(msg)
        print("Explore")

    def buttonDisinfection_pressed(self, *args):
        print("button pressed")
        # msg = "Hello GUI"
        # self.screen.ids.labelDestination.text = "button pressed"
        # pub.publish(msg)
        print("Disinfection")

    def buttonCleaning_pressed(self, *args):
        print("button pressed")
        # msg = "Hello GUI"
        # self.screen.ids.labelDestination.text = "button pressed"
        # pub.publish(msg)
        print("Cleaning")

    def buttonOpen_pressed(self, *args):
        print("button pressed")
        # msg = "Hello GUI"
        # self.screen.ids.labelDestination.text = "button pressed"
        # pub.publish(msg)
        if( self.password == self.screen.ids.textPassword.text):
            print("Open")
        else:
            print("Password error!")

    def buttonClose_pressed(self, *args):
        print("button pressed")
        # msg = "Hello GUI"
        # self.screen.ids.labelDestination.text = "button pressed"
        # pub.publish(msg)
        print("Close")

    def buttonDelivery_pressed(self, *args):
        self.password = self.screen.ids.textPassword.text
        print("button pressed")
        # msg = "Hello GUI"
        # self.screen.ids.labelDestination.text = "button pressed"
        # pub.publish(msg)
        print("Delivery")
        # print(self.screen.ids.textPassword.text)
        print(self.screen.ids.textDestination.text)

    def slider_touch_move(self, value):
        print(value)


if __name__ == '__main__':
    rospy.init_node('simple_gui',anonymous=True)

    pub = rospy.Publisher('/button', String, queue_size=10)

    TutorialApp().run()
