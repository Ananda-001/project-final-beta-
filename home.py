from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from tab import NextScreen
import User_check
username=""
password=""
Username=""
New_password=""
class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        background_image = Image(source='2.png', allow_stretch=True)
        self.add_widget(background_image)

        # Place buttons
        self.place_button(0.13, 0.127, 'Create Account',60)
        self.place_button(0.68, 0.33, ' ', 40)
        self.place_button(0.7, 0.127, 'Forgot Password',60)

        # Add text input boxes
        self.add_text_input(0.42, 0.56, 'Username')
        self.add_text_input(0.42, 0.38, 'Password')

    def show_tost_msg(self,text):  # shows tost messages
        background_layout = BoxLayout(
            orientation='horizontal',
            pos_hint={'center_x': 0.5, 'top': 0.93},  # Centered at the top of the screen
            size_hint=(None, None),
            size=(500, 60),
        )
        background_layout.background = 'button_bg.png'
        invalid_label = Label(
            text=text,
            font_size=100,
            color=(0, 0, 0, 1),  # Black text color
        )

        background_layout.add_widget(invalid_label)
        self.add_widget(background_layout)

        # removal of the label and background after 3 seconds
        Clock.schedule_once(lambda dt: self.remove_widget(background_layout), 3)

    def place_button(self, x, y, button_label, font_size):
        if font_size == 40:
            button = Button(
                text=button_label,
                size_hint=(None, None),
                size=(667, 150),
                pos_hint={'x': x, 'y': y},
                font_size=font_size,
                background_color=(1, 1, 1, 0),  # Fully transparent background color
                background_normal='',  # No background image
                color=(0, 0, 0, 1)  # Text color
            )
            button.bind(on_press=lambda instance: self.on_button_press(instance, button_label))
            self.add_widget(button)
        else:
            button = Button(text=button_label, size_hint=(None, None), size=(667, 150),
                            pos_hint={'x': x, 'y': y}, font_size=font_size,background_normal='button_bg.png',color=(0, 0, 0, 1))
            button.bind(on_press=lambda instance: self.on_button_press(instance, button_label))

            self.add_widget(button)

    def add_text_input(self, x, y, text_input_name):
        box_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(None, None), size=(600, 150),
                               pos_hint={'x': x, 'y': y})

        text_input = TextInput(
            multiline=False,
            background_normal="normal_bg_text_box.png",
            background_active='active_bg_text_box.png',
            foreground_color=(0, 0, 0, 1),  # Text color
            cursor_color=(0, 0, 0, 1),  # Cursor color
            hint_text=f'{text_input_name}...',
            hint_text_color=(0.5, 0.5, 0.5, 1),  # Hint text color
            padding=(20, 10),
            font_size=50,
            size=(600, 150),
            on_text_validate=lambda instance: self.on_text_input_validate(instance, text_input_name)
        )

        box_layout.add_widget(text_input)
        self.add_widget(box_layout)

    def on_text_input_validate(self, instance, text_input_name):
        global username, password , Username , New_password
        print(f"Enter key pressed for {text_input_name}. Text Input string: {instance.text}")
        if text_input_name == "Username":
            username=instance.text
        if text_input_name == "Password":
            password=instance.text
        if text_input_name == "Username":
            Username=instance.text
        if text_input_name == "New Password":
            New_password = instance.text

    def delete_widget_by_label(self, label):
        for widget in self.children:
            if isinstance(widget, Button) and widget.text == label:
                self.remove_widget(widget)
                print(f"Widget with label '{label}' deleted.")
                break
    def on_button_press(self, instance, button_label):
        print(f"{button_label} pressed!")
        if button_label == "Forgot Password":
            self.delete_widget_by_label(" ")
            self.place_button(0.68, 0.33, 'Next', 40)  # red color, font size 18
            self.place_button(0.7, 0.127, 'Delete Account', 60)  # blue color, font size 20
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'New Password')
        if button_label == "Delete Account":
            User_check.delete_account(Username)
            self.show_tost_msg("Account deleted")
        if button_label == "Create Account":
            self.delete_widget_by_label("Next")
            self.delete_widget_by_label(" ")
            self.delete_widget_by_label("Create Account")
            self.place_button(0.13, 0.127, 'Back to home', 60)
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'Password')
            self.place_button(0.68, 0.33, 'Create', 40)
        if button_label == "Back to home":
            self.delete_widget_by_label("Create")
            self.delete_widget_by_label("Back to home")
            self.place_button(0.13, 0.127, 'Create Account', 60)
            self.place_button(0.68, 0.33, ' ', 40)
        if button_label == "Create":
            User_check.INSERT(username,password)
            self.show_tost_msg("Account Created")
            self.delete_widget_by_label("Create")
            self.place_button(0.13, 0.127, 'Create Account', 60)
            self.place_button(0.68, 0.33, ' ', 40)
            self.place_button(0.7, 0.127, 'Forgot Password', 60)
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'Password')
        if button_label == "Next":
            self.delete_widget_by_label("Next")
            User_check.Update_user(Username,New_password)
            self.place_button(0.13, 0.127, 'Create Account', 60)  # green color, font size 24
            self.place_button(0.68, 0.33, ' ', 40)  # red color, font size 18
            self.place_button(0.7, 0.127, 'Forgot Password', 60)
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'Password')
        if button_label == ' ' and User_check.check(username,password) == "access granted":
            # Create an instance of NextScreen and switch to it
            next_screen = NextScreen(name='next_screen')
            self.manager.add_widget(next_screen)
            self.manager.current = 'next_screen'
            global page
            page=1
        if button_label == ' ' and User_check.check(username, password) == "access denied":
            self.show_tost_msg("Invalid login credentials")


class MyApp(App):
    def build(self):
        global username, password
        # Create the screen manager
        sm = ScreenManager()
        # Add the home screen to the screen manager
        home_screen = HomeScreen(name='home_screen')
        sm.add_widget(home_screen)

        # Add the screen manager to the layout
        layout = RelativeLayout()
        layout.add_widget(sm)
        return layout


if __name__ == '__main__':
    MyApp().run()
