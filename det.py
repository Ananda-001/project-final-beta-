from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import User_check
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import tax
from datetime import datetime
import sys
data3 =User_check.test("select * from employee;")
length = len(data3)

p=0
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
        if sid1 == "" or sid1 == 111 or  User_check.info(sid1) == "":
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
            data = User_check.info(sid1)
            #sys.stdout.write(str(sid1))
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
        #sys.stdout.write(f"Enter key pressed for {text_input_name}. Text Input string: {instance.text}")

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
            #sys.stdout.write("deleated my guy especiall: "+str(sid1))
        if button_label == "Calc":
            self.Tost("Tax Calculated")
            data = User_check.info(sid1)
            c=[]
            for i in data:
                for j in i:
                    c.append(j)
            c.pop(2)
            c=[0]+c
            #sys.stdout.write("c is :"+str(c))
            tax.tax_calc(c,sid1)
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
            if CTC.isdigit() and C80.isdigit() and D80.isdigit() and rent.isdigit() and int(C80) < int(CTC) and int(D80)<int(CTC) and int(C80) <150000 and int(D80) < 25000:
                User_check.update_employee(ename, sid1, CTC, C80, D80, rent)
                self.Tost("Updated")
            if int(C80) > int(CTC):
                self.Tost("80 C value is higher than Cost to company!")
            if int(D80)>int(CTC):
                self.Tost("80 D value is higher than Cost to company!")
            if int(C80) >150000:
                self.Tost("80 C value is higher than 1,50,000 limit!")
            if int(D80) > 25000:
                self.Tost("80 D value is higher than 25,000 limit!")
        if button_label == "ADD PERSON":

            currentDay = datetime.now().day
            currentMonth = datetime.now().month
            currentYear = datetime.now().year
            tod = str(currentYear) + "-" + str(currentMonth) + "-" + str(currentDay)
            t=tod.split("-")
            d=DOJ.split("-")

            if d[0] < t[0]:
                iid = User_check.maax()[0][0]
                User_check.add_employee(ename, iid + 1, DOJ, CTC, C80, D80, rent)
                self.switch_to_tables(self)

            elif d[0] == t[0] :
                if  d[1] < t[1]:
                    iid = User_check.maax()[0][0]
                    User_check.add_employee(ename, iid + 1, DOJ, CTC, C80, D80, rent)
                    self.switch_to_tables(self)
                elif d[1] == t[1]:
                    if d[2] <= t[2]:
                        iid = User_check.maax()[0][0]
                        User_check.add_employee(ename, iid + 1, DOJ, CTC, C80, D80, rent)
                        self.switch_to_tables(self)
                    else:
                        self.Tost("invalid date")
                else:
                    self.Tost("invalid date")
            else:
                self.Tost("invalid date")



    def switch_to_tables(self, instance):
        Details.switch=True
        self.delete_widget_by_label()
        #next_screen = NextScreen(name='next_screen')
        #self.manager.add_widget(next_screen)
        self.manager.current = 'next_screen'
        details_screen = self.manager.get_screen('details')
        self.manager.remove_widget(details_screen)
