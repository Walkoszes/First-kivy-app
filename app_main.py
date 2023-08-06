from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from add import *
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

name = ''

class Main(Screen):
    def __init__(self, name='main'):
        super().__init__(name='main')
        button1 = Button(text="1")
        button2 = Button(text="2")
        button3 = Button(text="3")
        button4 = Button(text="4")
        label = Label(text="Вибери екран")

        main_layout = BoxLayout(orientation="horizontal")
        layout_right = BoxLayout(orientation="vertical", spacing=20, padding=10)
        layout_left = BoxLayout(orientation="vertical")

        layout_left.add_widget(label)

        layout_right.add_widget(button1)
        layout_right.add_widget(button2)
        layout_right.add_widget(button3)
        layout_right.add_widget(button4)

        main_layout.add_widget(layout_left)
        main_layout.add_widget(layout_right)

        button1.on_press = self.next
        button2.on_press = self.next2
        button3.on_press = self.next3
        button4.on_press = self.next4

        self.add_widget(main_layout)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'

    def next2(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

    def next3(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'

    def next4(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'forth'

class FirstScreen(Screen):
    def __init__(self, name='first'):
        super().__init__(name='first')
        btn1 = Button(text='Вибір: 1')
        btn2 = Button(text='Назад')

        layout_central = BoxLayout(orientation="horizontal", size_hint=(None, 0.5), width="400", pos_hint={"center_x": 0.5, "center_y": 0.5})
        layout_right = BoxLayout(orientation="vertical", size_hint=(0.5, 0.5), width="200", pos_hint={"y": 0.5})
        layout_left = BoxLayout(orientation="vertical", size_hint=(0.5, 0.5), width="200", pos_hint={"y": 0})

        layout_right.add_widget(btn1)
        layout_left.add_widget(btn2)

        btn2.on_press = self.next

        layout_central.add_widget(layout_right)
        layout_central.add_widget(layout_left)

        self.add_widget(layout_central)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class SecondScreen(Screen):
    def __init__(self, name="second"):
        super().__init__(name="second")
        label = Label(text="Вибір: 2")
        label1 = Label(text="Введіть пароль:")
        inputing = TextInput(text=" ")
        btn_ok = Button(text="ОК!")
        btn_back = Button(text="Назад")

        layout_main = BoxLayout(orientation="vertical")
        layout_up = BoxLayout(orientation="horizontal")
        layout_middle = BoxLayout(orientation="horizontal", size_hint=(0.9, 0.1), width="800", pos_hint={"x": 0.0, "centre_y": 0.3})
        layout_buttons = BoxLayout(orientation="horizontal", size_hint=(None, 0.3), width="600", pos_hint={"x": 0.2, "centre_y": 0.3})

        layout_up.add_widget(label)

        layout_middle.add_widget(label1)
        layout_middle.add_widget(inputing)

        layout_buttons.add_widget(btn_ok)
        layout_buttons.add_widget(btn_back)

        layout_main.add_widget(layout_up)
        layout_main.add_widget(layout_middle)
        layout_main.add_widget(layout_buttons)

        btn_back.on_press = self.next

        self.add_widget(layout_main)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class ThirdScreen(Screen):
    def __init__(self, name="third"):
        super().__init__(name="third")
        slider1 = Slider(orientation='horizontal')
        slider2 = Slider(orientation='horizontal')
        slider3 = Slider(orientation='horizontal')
        slider1_ver = Slider(orientation='vertical')
        slider2_ver = Slider(orientation='vertical')
        btn_back = Button(text="Назад")

        layout_main = BoxLayout(orientation="vertical")
        layout_sliders = BoxLayout(orientation="horizontal")
        layout_horyzontal_sliders = BoxLayout(orientation="vertical", size_hint=(None, 0.9), width="500", pos_hint={"centre_y": 0.3})
        layout_vertical_sliders = BoxLayout(orientation="horizontal", size_hint=(0.8, 0.9), width="200", pos_hint={"x": 0.8, "centre_y": 0.9})
        layout_button = BoxLayout(orientation="horizontal", size_hint=(None, 0.1), width="1000", pos_hint={"centre_y": 0.1})

        layout_horyzontal_sliders.add_widget(slider1)
        layout_horyzontal_sliders.add_widget(slider2)
        layout_horyzontal_sliders.add_widget(slider3)

        layout_vertical_sliders.add_widget(slider1_ver)
        layout_vertical_sliders.add_widget(slider2_ver)

        layout_button.add_widget(btn_back)

        layout_sliders.add_widget(layout_horyzontal_sliders)
        layout_sliders.add_widget(layout_vertical_sliders)
        layout_main.add_widget(layout_sliders)
        layout_main.add_widget(layout_button)

        btn_back.on_press = self.next

        self.add_widget(layout_main)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class ForthScreen(Screen):
    def __init__(self, name='forth'):
        super().__init__(name='forth')
        additional_label = Label(text='Додаткове завдання')
        btn2 = Button(text='Назад')
        long_text = Label(text= long_text1 , size_hint=(1, None), height=900, font_size = 24)

        scroll_view = ScrollView(do_scroll_x=False)
        scroll_view.add_widget(long_text)

        layout_central = BoxLayout(orientation="vertical")
        layout_look = BoxLayout(orientation="vertical", size_hint=(None, 0.3), width="300", pos_hint={"x": 0.0, "y": 0.4})
        layout_look1 = BoxLayout(orientation="vertical", size_hint=(None, 0.2), width="1000", pos_hint={"x": 0.0, "y": 0.3})
        layout_text = BoxLayout(orientation="vertical")

        layout_look.add_widget(additional_label)
        layout_look1.add_widget(btn2)
        layout_text.add_widget(scroll_view)

        btn2.on_press = self.next

        layout_central.add_widget(layout_look)
        layout_central.add_widget(layout_look1)
        layout_central.add_widget(layout_text)

        self.add_widget(layout_central)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class Application(App):
    def build(self):
        sm = ScreenManager()
        m = Main()
        sm.add_widget(m)
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(ForthScreen())
        return sm

app = Application()
app.run()