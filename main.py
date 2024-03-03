from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
username_helper = """
MDTextField:
    hint_text: "Enter password"
    helper_text: "password is icanmakeapps"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x' :0.5,'center_y' :0.5}
    size_hint_x :None
    width:300
"""
class appApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        screen = Screen()

        self.username = Builder.load_string(username_helper)
        btn = MDRectangleFlatButton(text='click',pos_hint= {'center_x' :0.5,'center_y' :0.4}, on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen
    def show_data(self,obj):
        if self.username.text == "icanmakeapps":
            dialog = MDDialog(title='things i can do',text='make apps',)
            dialog.open()
        else:
            dialog = MDDialog(text='try again', )
            dialog.open()



appApp().run()