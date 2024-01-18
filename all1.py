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
from det import Details
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
        self.place_button(0.68, 0.33, 'login', 40)
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
            self.delete_widget_by_label("login")
            self.place_button(0.68, 0.33, 'Next', 40)  # red color, font size 18
            self.place_button(0.7, 0.127, 'Delete Account', 60)  # blue color, font size 20
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'New Password')
        if button_label == "Delete Account":
            User_check.delete_account(Username)
            self.show_tost_msg("Account deleted")
        if button_label == "Create Account":
            self.delete_widget_by_label("Next")
            self.delete_widget_by_label("login")
            self.delete_widget_by_label("Create Account")
            self.place_button(0.13, 0.127, 'Back to home', 60)
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'Password')
            self.place_button(0.68, 0.33, 'Create', 40)
        if button_label == "Back to home":
            self.delete_widget_by_label("Create")
            self.delete_widget_by_label("Back to home")
            self.place_button(0.13, 0.127, 'Create Account', 60)
            self.place_button(0.68, 0.33, 'login', 40)
        if button_label == "Create":
            User_check.INSERT(username,password)
            self.show_tost_msg("Account Created")
            self.delete_widget_by_label("Create")
            self.place_button(0.13, 0.127, 'Create Account', 60)
            self.place_button(0.68, 0.33, 'login', 40)
            self.place_button(0.7, 0.127, 'Forgot Password', 60)
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'Password')
        if button_label == "Next":
            self.delete_widget_by_label("Next")
            User_check.Update_user(Username,New_password)
            self.place_button(0.13, 0.127, 'Create Account', 60)  # green color, font size 24
            self.place_button(0.68, 0.33, 'login', 40)  # red color, font size 18
            self.place_button(0.7, 0.127, 'Forgot Password', 60)
            self.add_text_input(0.42, 0.56, 'Username')
            self.add_text_input(0.42, 0.38, 'Password')
        if button_label == 'login' and User_check.check(username,password) == "access granted":
            # Create an instance of NextScreen and switch to it
            next_screen = NextScreen(name='next_screen')
            self.manager.add_widget(next_screen)
            self.manager.current = 'next_screen'
            global page
            page=1
        if button_label == 'login' and User_check.check(username, password) == "access denied":
            self.show_tost_msg("Invalid login credentials")
    #def on_text_input_validate(self, instance):
    #    print(f"Enter key pressed. Text Input string: {instance.text}")

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


data =User_check.test("select * from employee;")
length = len(data)
while len(data) % 6 !=0:
    data.append(("","","","","",""))
    done=True
global p
p=0
import sys
class NextScreen(Screen):
    shared_id = 1
    def __init__(self, **kwargs):
        super(NextScreen, self).__init__(**kwargs)

        self.add_widget(Image(source='newnew3.png', allow_stretch=True))  # Use your next screen background image
        self.add_widget(Button(text='Go to Home Screen', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                               on_press=self.switch_to_home_screen))

        self.place_button(0.2, 0.473, 'Details', 40, "d1")
        self.place_button(0.28, 0.473, 'Select', 40, "s1")
        self.place_button(0.434, 0.473, 'Details', 40, "d2")
        self.place_button(0.514, 0.473, 'Select', 40, "s2")
        self.place_button(0.664, 0.473, 'Details', 40, "d3")
        self.place_button(0.744, 0.473, 'Select', 40, "s3")
        self.place_button(0.2, 0.186, 'Details', 40, "d4")
        self.place_button(0.28, 0.186, 'Select', 40, "s4")
        self.place_button(0.434, 0.186, 'Details', 40, "d5")
        self.place_button(0.514, 0.186, 'Select', 40, "s5")
        self.place_button(0.664, 0.186, 'Details', 40, "d6")
        self.place_button(0.744, 0.186, 'Select', 40, "s6")
        self.place_button(0.82, 0.2, 'next', 40, "nxt")
        self.place_button(0, 0.2, 'back', 40, "bk")

        self.add_widget(self.create_label("%s" %(data[0+p][0]), 0.3, 0.63,widget= "label1"))
        self.add_widget(self.create_label("%s" %(data[0+p][1]), 0.3, 0.594, widget="label2"))
        self.add_widget(self.create_label("%s" %(data[0+p][2]), 0.3, 0.558, widget="label3"))
        self.add_widget(self.create_label("%s"%(data[1+p][0]), 0.53, 0.63,widget= "label4"))
        self.add_widget(self.create_label("%s"%(data[1+p][1]), 0.53, 0.594,widget= "label5"))
        self.add_widget(self.create_label("%s"%(data[1+p][2]), 0.53, 0.558, widget="label6"))
        self.add_widget(self.create_label("%s"%(data[2+p][0]), 0.76, 0.63, widget="label7"))
        self.add_widget(self.create_label("%s"%(data[2+p][1]), 0.76, 0.594,widget= "label8"))
        self.add_widget(self.create_label("%s"%(data[2+p][2]), 0.76, 0.558,widget= "label9"))
        self.add_widget(self.create_label("%s"%(data[3+p][0]), 0.3, 0.34, widget="label10"))
        self.add_widget(self.create_label("%s"%(data[3+p][1]), 0.3, 0.302, widget="label11"))
        self.add_widget(self.create_label("%s"%(data[3+p][2]), 0.3, 0.267, widget="label12"))
        self.add_widget(self.create_label("%s"%(data[4+p][0]), 0.53, 0.34, widget="label13"))
        self.add_widget(self.create_label("%s"%(data[4+p][1]), 0.53, 0.302,widget="label14"))
        self.add_widget(self.create_label("%s"%(data[4+p][2]), 0.53, 0.267, widget="label15"))
        self.add_widget(self.create_label("%s"%(data[5+p][0]), 0.76, 0.34, widget="label16"))
        self.add_widget(self.create_label("%s"%(data[5+p][1]), 0.76, 0.302,widget= "label17"))
        self.add_widget(self.create_label("%s"%(data[5+p][2]), 0.76, 0.267, widget="label18"))




    def create_label(self, message, x_rel, y_rel, font_size=50, halign='center', valign='middle', widget=None):
        label_pos_rel = {'center_x': x_rel, 'center_y': y_rel}
        label = Label(text=message, font_size=font_size, halign=halign, valign=valign, pos_hint=label_pos_rel,
                      color=(0, 0, 0, 1))
        label.bind(on_press=lambda instance: self.on_widget_press(instance, widget))
        return label

    def place_button(self, x, y, button_label, font_size, widget_name):
        if button_label == "next" or button_label == "back":
            button = Button(
                text=button_label,
                size_hint=(None, None),
                size=(667, 150),
                pos_hint={'x': x, 'y': y},
                font_size=font_size,
                background_color=(1, 1, 1, 0),
                background_normal='',
                color=(0, 0, 0, 1)
            )
            if button_label == "next":
                button.bind(on_release=lambda instance: self.on_widget_press(instance, 'nxt'))
                self.add_widget(button)
            else:
                button.bind(on_release=lambda instance: self.on_widget_press(instance, 'bk'))
                self.add_widget(button)

        else:
            button = Button(text=button_label, size_hint=(None, None), size=(200, 50),
                            pos_hint={'x': x, 'y': y}, font_size=font_size, background_normal='bg_button.png',
                            color=(0, 0, 0, 1))

            button.bind(on_release=lambda instance: self.on_widget_press(instance, widget_name))
            setattr(self, widget_name, button)  # Set the attribute dynamically
            self.add_widget(button)
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
    def on_widget_press(self, instance, widget):
        if widget is not None:
            if widget == "nxt":
                 #self.manager.current = 'home_screen'
                self.manager.current= "next_screen"
                global p
                p+=6
                self.clear_labels()
                self.add_widget(self.create_label("%s" % (data[0 + p][0]), 0.3, 0.63, widget="label1"))
                self.add_widget(self.create_label("%s" % (data[0 + p][1]), 0.3, 0.594, widget="label2"))
                self.add_widget(self.create_label("%s" % (data[0 + p][2]), 0.3, 0.558, widget="label3"))
                self.add_widget(self.create_label("%s" % (data[1 + p][0]), 0.53, 0.63, widget="label4"))
                self.add_widget(self.create_label("%s" % (data[1 + p][1]), 0.53, 0.594, widget="label5"))
                self.add_widget(self.create_label("%s" % (data[1 + p][2]), 0.53, 0.558, widget="label6"))
                self.add_widget(self.create_label("%s" % (data[2 + p][0]), 0.76, 0.63, widget="label7"))
                self.add_widget(self.create_label("%s" % (data[2 + p][1]), 0.76, 0.594, widget="label8"))
                self.add_widget(self.create_label("%s" % (data[2 + p][2]), 0.76, 0.558, widget="label9"))
                self.add_widget(self.create_label("%s" % (data[3 + p][0]), 0.3, 0.34, widget="label10"))
                self.add_widget(self.create_label("%s" % (data[3 + p][1]), 0.3, 0.302, widget="label11"))
                self.add_widget(self.create_label("%s" % (data[3 + p][2]), 0.3, 0.267, widget="label12"))
                self.add_widget(self.create_label("%s" % (data[4 + p][0]), 0.53, 0.34, widget="label13"))
                self.add_widget(self.create_label("%s" % (data[4 + p][1]), 0.53, 0.302, widget="label14"))
                self.add_widget(self.create_label("%s" % (data[4 + p][2]), 0.53, 0.267, widget="label15"))
                self.add_widget(self.create_label("%s" % (data[5 + p][0]), 0.76, 0.34, widget="label16"))
                self.add_widget(self.create_label("%s" % (data[5 + p][1]), 0.76, 0.302, widget="label17"))
                self.add_widget(self.create_label("%s" % (data[5 + p][2]), 0.76, 0.267, widget="label18"))
                self.add_widget(
                    Button(text='Go to Home Screen', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                           on_press=self.switch_to_home_screen))

                self.place_button(0.2, 0.473, 'Details', 40, "d1")
                self.place_button(0.28, 0.473, 'Select', 40, "s1")
                self.place_button(0.434, 0.473, 'Details', 40, "d2")
                self.place_button(0.514, 0.473, 'Select', 40, "s2")
                self.place_button(0.664, 0.473, 'Details', 40, "d3")
                self.place_button(0.744, 0.473, 'Select', 40, "s3")
                self.place_button(0.2, 0.186, 'Details', 40, "d4")
                self.place_button(0.28, 0.186, 'Select', 40, "s4")
                self.place_button(0.434, 0.186, 'Details', 40, "d5")
                self.place_button(0.514, 0.186, 'Select', 40, "s5")
                self.place_button(0.664, 0.186, 'Details', 40, "d6")
                self.place_button(0.744, 0.186, 'Select', 40, "s6")
                self.place_button(0, 0.2, 'back', 40, "bk")
                if done == False:
                    self.place_button(0.82, 0.2, 'next', 40, "nxt")
                # Do something for Button 12
        if widget in ["s1", "s2", "s3", "s4", "s5", "s6"]:
            #ssid=int(widget[1])+p
            ssid=data[0][1]
            if ssid > length or data[int(widget[1])-1+p][1] == "":
                NextScreen.shared_id = 111
                #self.shared_id = 1
                sys.stdout.write(str(self.shared_id)+"hello test ssid:"+str(ssid))
                try:
                    details_screen = self.manager.get_screen('details')
                    pass
                except:
                    details = Details(name='details')
                    self.manager.add_widget(details)
                self.manager.current = "details"

            else:
                ssid=data[int(widget[1])-1+p][1]
                data1=User_check.info(ssid)
                c = []
                for i in data1:
                    for j in i:
                        c.append(j)
                print(c)
                c.pop(2)
                c = [0] + c
                #tax.tax_calc(c,ssid)
                self.show_tost_msg("Tax calculated for: "+str(ssid))
        if widget in ["d1","d2","d3","d4","d5","d6"]:
            sys.stdout.write("hello there the shared id is :"+str(data[int(widget[1])-1+p][1]))
            NextScreen.shared_id = data[int(widget[1])-1+p][1]# please use data insted of widget and then it will e fine use dtat[widge[1]-1][1] shared id will also change !
            #sys.stdout.write(str(shared_id)+" "+widget[1]+str(p)+"helooooooooooo\n\n")
            try:
                details_screen = self.manager.get_screen('details')
                pass
            except:
                details = Details(name='details')
                self.manager.add_widget(details)

            # Switch to the "details" screen
            #self.manager.current = "details"
            #details = Details(name='details')
            #self.manager.add_widget(details)
            self.manager.current = "details"



        if widget == "bk" :
            # self.manager.current = 'home_screen'
            self.manager.current = "next_screen"
            p -= 6
            self.clear_labels()
            self.add_widget(self.create_label("%s" % (data[0 + p][0]), 0.3, 0.63, widget="label1"))
            self.add_widget(self.create_label("%s" % (data[0 + p][1]), 0.3, 0.594, widget="label2"))
            self.add_widget(self.create_label("%s" % (data[0 + p][2]), 0.3, 0.558, widget="label3"))
            self.add_widget(self.create_label("%s" % (data[1 + p][0]), 0.53, 0.63, widget="label4"))
            self.add_widget(self.create_label("%s" % (data[1 + p][1]), 0.53, 0.594, widget="label5"))
            self.add_widget(self.create_label("%s" % (data[1 + p][2]), 0.53, 0.558, widget="label6"))
            self.add_widget(self.create_label("%s" % (data[2 + p][0]), 0.76, 0.63, widget="label7"))
            self.add_widget(self.create_label("%s" % (data[2 + p][1]), 0.76, 0.594, widget="label8"))
            self.add_widget(self.create_label("%s" % (data[2 + p][2]), 0.76, 0.558, widget="label9"))
            self.add_widget(self.create_label("%s" % (data[3 + p][0]), 0.3, 0.34, widget="label10"))
            self.add_widget(self.create_label("%s" % (data[3 + p][1]), 0.3, 0.302, widget="label11"))
            self.add_widget(self.create_label("%s" % (data[3 + p][2]), 0.3, 0.267, widget="label12"))
            self.add_widget(self.create_label("%s" % (data[4 + p][0]), 0.53, 0.34, widget="label13"))
            self.add_widget(self.create_label("%s" % (data[4 + p][1]), 0.53, 0.302, widget="label14"))
            self.add_widget(self.create_label("%s" % (data[4 + p][2]), 0.53, 0.267, widget="label15"))
            self.add_widget(self.create_label("%s" % (data[5 + p][0]), 0.76, 0.34, widget="label16"))
            self.add_widget(self.create_label("%s" % (data[5 + p][1]), 0.76, 0.302, widget="label17"))
            self.add_widget(self.create_label("%s" % (data[5 + p][2]), 0.76, 0.267, widget="label18"))
            self.add_widget(
                Button(text='Go to Home Screen', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                       on_press=self.switch_to_home_screen))

            self.place_button(0.2, 0.473, 'Details', 40, "d1")
            self.place_button(0.28, 0.473, 'Select', 40, "s1")
            self.place_button(0.434, 0.473, 'Details', 40, "d2")
            self.place_button(0.514, 0.473, 'Select', 40, "s2")
            self.place_button(0.664, 0.473, 'Details', 40, "d3")
            self.place_button(0.744, 0.473, 'Select', 40, "s3")
            self.place_button(0.2, 0.186, 'Details', 40, "d4")
            self.place_button(0.28, 0.186, 'Select', 40, "s4")
            self.place_button(0.434, 0.186, 'Details', 40, "d5")
            self.place_button(0.514, 0.186, 'Select', 40, "s5")
            self.place_button(0.664, 0.186, 'Details', 40, "d6")
            self.place_button(0.744, 0.186, 'Select', 40, "s6")
            self.place_button(0, 0.2, 'back', 40, "bk")
            self.place_button(0.82, 0.2, 'next', 40, "nxt")

    def clear_labels(self):
        # Clear only label widgets from the screen
        widgets_to_remove = [widget for widget in self.children if isinstance(widget, Label)]
        for widget in widgets_to_remove:
            self.remove_widget(widget)
    def switch_to_home_screen(self, instance):
        # Switch to the "HomeScreen"
        self.manager.current = 'home_screen'
        details_screen = self.manager.get_screen('next_screen')
        self.manager.remove_widget(details_screen)
        #sys.stdout.write("deleted next screen\n")

data3 =User_check.test("select * from employee;")
length = len(data3)
p=0
#print(User_check.info(1))
ename=""
CTC=0
DOJ=""
C80=0
D80=0
rent=0
class Details(Screen):
    switch = False
    def __init__(self, **kwargs):
        super(Details, self).__init__(**kwargs)

        global sid1
        from tab import NextScreen
        sid1 = NextScreen.shared_id
        #sys.stdout.write("\ntesting plz plz :"+str(sid1))
        if sid1 == "" or sid1 == 111:
            self.add_widget(Image(source='details.png', allow_stretch=True))
            self.add_widget(Button(text='Go Back', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                                   on_press=self.switch_to_tables))
            self.add_styled_text_input(0.34, 0.6, 'Employee Name')
            self.add_styled_text_input(0.34, 0.48, 'DOJ')
            self.add_styled_text_input(0.74, 0.638, 'CTC')
            self.add_styled_text_input(0.74, 0.5, '80C')
            self.add_styled_text_input(0.74, 0.42, '80D')
            self.add_styled_text_input(0.74, 0.37, 'Rent')
            self.place_button(0.74, 0.10, 'ADD PERSON', 60)

        else:
            print("just why:")
            data = User_check.info(sid1)
            sys.stdout.write(str(sid1))
            self.add_widget(Image(source='details.png', allow_stretch=True))
            self.add_widget(Button(text='Go Back', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                                   on_press=self.switch_to_tables))
            self.place_button(0.16, 0.21, 'Del', 1)  # green color, font size 24
            self.place_button(0.32, 0.21, 'Up', 1)  # red color, font size 18
            self.place_button(0.68, 0.21, 'Calc', 1)  # blue color, font size 20

            self.add_widget(self.create_label("%s" % (data[0][0]), 0.34, 0.64, widget="label1"))
            self.add_widget(self.create_label("%s" % (data[0][1]), 0.34, 0.58, widget="label2"))
            self.add_widget(self.create_label("%s" % (data[0][2]), 0.34, 0.514, widget="label3"))
            self.add_widget(self.create_label("%s" % (data[0][3]), 0.74, 0.638, widget="label4"))
            self.add_widget(self.create_label("%s" % (data[0][4]), 0.74, 0.582, widget="label5"))
            self.add_widget(self.create_label("%s" % (data[0][5]), 0.74, 0.53, widget="label6"))
            self.add_widget(self.create_label("%s" % (data[0][6]), 0.74, 0.47, widget="label7"))
    def Tost(self,text):
        background_layout = BoxLayout(
            orientation='horizontal',
            pos_hint={'center_x': 0.5, 'top': 0.93},  # Centered at the top of the screen
            size_hint=(None, None),
            size=(500, 60),  # Set the size based on your background image
        )
        background_layout.background = 'button_bg.png'
        invalid_label = Label(
            text=text,
            font_size=100,
            color=(0, 0, 0, 1),  # Black text color
        )

        background_layout.add_widget(invalid_label)
        self.add_widget(background_layout)

        # Schedule the removal of the label and background after 3 seconds
        Clock.schedule_once(lambda dt: self.remove_widget(background_layout), 3)
    def create_label(self, message, x_rel, y_rel, font_size=50, halign='center', valign='middle', widget=None):
        label_pos_rel = {'center_x': x_rel, 'center_y': y_rel}
        label = Label(text=message, font_size=font_size, halign=halign, valign=valign, pos_hint=label_pos_rel,
                      color=(0, 0, 0, 1))
        label.bind(on_press=lambda instance: self.on_widget_press(instance, widget))
        return label

    def add_styled_text_input(self, x, y, text_input_name):
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
        global ename, CTC , DOJ , C80, D80 , rent
        sys.stdout.write(f"Enter key pressed for {text_input_name}. Text Input string: {instance.text}")

        if text_input_name == "Employee Name":
            ename=instance.text
        if text_input_name == "CTC":
            CTC=instance.text
        if text_input_name == "DOJ":
            DOJ=instance.text
        if text_input_name == "80C":
            C80 = instance.text
        if text_input_name == "80D":
            D80 = instance.text
        if text_input_name == "Rent":
            rent= instance.text


    def place_button(self, x, y, button_label, font_size):
        if font_size == 60:
            button = Button(
                text=button_label,
                size_hint=(None, None),
                size=(667, 150),
                pos_hint={'x': x, 'y': y},
                font_size=font_size,
                background_color=(1, 1, 1, 0),
                background_normal='bg_button.png',
                color=(0, 0, 0, 1)  # Text color
            )
            button.bind(on_press=lambda instance: self.on_button_press(instance, button_label))
            self.add_widget(button)

        else:
            button = Button(
                text=button_label,
                size_hint=(None, None),
                size=(667, 150),
                pos_hint={'x': x, 'y': y},
                font_size=font_size,
                background_color=(1, 1, 1, 0),  # Fully transparent background color
                background_normal='',  # No background image
                #color=(0, 0, 0, 1)  # Text color
                )
            button.bind(on_press=lambda instance: self.on_button_press(instance, button_label))
            self.add_widget(button)

    def delete_widget_by_label(self):
        text_inputs_to_remove = [widget for widget in self.children if isinstance(widget, BoxLayout) and
                                 isinstance(widget.children[0], TextInput)]
        for box_layout in text_inputs_to_remove:
            self.remove_widget(box_layout)

    def on_button_press(self, instance, button_label):
        print(f"{button_label} pressed!")

        if button_label == "Del":
            self.Tost("User deleted")
            User_check.del_employee(sid1)
            sys.stdout.write("deleated my guy especiall: "+str(sid1))
        if button_label == "Calc":
            self.Tost("Tax Calculated")
            data = User_check.info(sid1)
            c=[]
            for i in data:
                for j in i:
                    c.append(j)
            print(c)
            c.pop(2)
            c=[0]+c
            print(c)
            print(data)
            #sys.stdout.write(data)
            #tax.tax_calc(c,sid1)
        if button_label == "Up":
            self.add_styled_text_input(0.34, 0.6, 'Employee Name')
            #self.add_styled_text_input(0.34, 0.59, 'Password')
            #self.add_styled_text_input(0.34, 0.48, 'DOJ')
            self.add_styled_text_input(0.74, 0.638, 'CTC')
            self.add_styled_text_input(0.74, 0.5, '80C')
            self.add_styled_text_input(0.74, 0.42, '80D')
            self.add_styled_text_input(0.74, 0.37, 'Rent')
            self.place_button(0.74, 0.10, 'UPDATE', 60)
        if button_label == "UPDATE":
            sys.stdout.write(ename+"id:"+str(sid1)+"\ndoj:"+DOJ+"\n"+str(CTC)+"\n"+str(C80)+str(D80)+str(rent))
            User_check.update_employee(ename,sid1,CTC,C80,D80,rent)
        if button_label == "ADD PERSON":
            User_check.add_employee(ename,length+1,DOJ,CTC,C80,D80,rent)
            self.switch_to_tables()
    def switch_to_tables(self, instance):
        Details.switch=True
        self.delete_widget_by_label()
        #next_screen = NextScreen(name='next_screen')
        #self.manager.add_widget(next_screen)
        self.manager.current = 'next_screen'
        details_screen = self.manager.get_screen('details')
        self.manager.remove_widget(details_screen)

if __name__ == '__main__':
    MyApp().run()
