"""
Simple Calculator App using KivyMD
A Material Design calculator with a clean, intuitive interface
"""

from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.color_definitions import colors
Window.fullscreen="auto"
class Calculator(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expression = ""
        self.result_display = None
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
    
    # Main container - remove title, use full height
        main_box = MDBoxLayout(
        orientation='vertical',
        padding='10dp',
        spacing='10dp',
        size_hint=(1, 1)
    )
    
    # Display - bigger
        self.result_display = MDTextField(
        mode='rectangle',
        multiline=False,
        readonly=True,
        size_hint_y=0.2,  # Increased from 0.12
        font_size='48sp',  # Bigger font
        hint_text='0',
        line_color_focus=(0.2, 0.6, 1, 1),
        line_color_normal=(0.8, 0.8, 0.8, 1)
    )
        self.result_display.text = '0'
        main_box.add_widget(self.result_display)
    
    # Button grid - use remaining space
        button_grid = MDGridLayout(
        cols=4,
        spacing='6dp',
        size_hint_y=0.8,
        padding='0dp'
    )
    
    # ... keep your buttons code same ...
        
        # Define buttons: (label, action)
        buttons = [
            ('C', self.clear),
            ('(', self.add_character),
            (')', self.add_character),
            ('/', self.add_character),
            
            ('7', self.add_character),
            ('8', self.add_character),
            ('9', self.add_character),
            ('×', self.add_character),
            
            ('4', self.add_character),
            ('5', self.add_character),
            ('6', self.add_character),
            ('−', self.add_character),
            
            ('1', self.add_character),
            ('2', self.add_character),
            ('3', self.add_character),
            ('+', self.add_character),
            
            ('0', self.add_character),
            ('.', self.add_character),
            ('=', self.calculate),
            ('⌫', self.backspace),
        ]
        
        # Create buttons with styling
        for label, action in buttons:
            if label == '=':
                btn = MDRaisedButton(
                    text=label,
                    size_hint_y=None,
                    height='70dp',
                    md_bg_color=(0.2, 0.8, 0.4, 1),  # Green
                    on_press=action
                )
            elif label == 'C':
                btn = MDRaisedButton(
                    text=label,
                    size_hint_y=None,
                    height='70dp',
                    md_bg_color=(1, 0.4, 0.4, 1),  # Red
                    on_press=action
                )
            elif label in ['/', '×', '−', '+', '⌫']:
                btn = MDRaisedButton(
                    text=label,
                    size_hint_y=None,
                    height='70dp',
                    md_bg_color=(0.2, 0.6, 1, 1),  # Blue
                    on_press=action
                )
            else:
                btn = MDRaisedButton(
                    text=label,
                    size_hint_y=None,
                    height='70dp',
                    md_bg_color=(0.9, 0.9, 0.9, 1),  # Light gray
                    text_color=(0.2, 0.2, 0.2, 1),  # Dark text
                    on_press=action
                )
            
            button_grid.add_widget(btn)
        
        main_box.add_widget(button_grid)
        
        return main_box
    
    def add_character(self, instance):
        """Add a character to the expression"""
        char = instance.text
        
        # Replace display symbols with mathematical symbols
        if char == '×':
            char = '*'
        elif char == '−':
            char = '-'
        
        # Handle first character
        if self.result_display.text == '0':
            if char == '.':
                self.result_display.text = '0.'
                self.expression = '0.'
            elif char not in ['+', '-', '*', '/', '(', ')']:
                self.result_display.text = char
                self.expression = char
            else:
                self.result_display.text = '0' + char
                self.expression = '0' + char
        else:
            self.expression += char
            self.result_display.text = self.expression
    
    def clear(self, instance):
        """Clear the calculator"""
        self.expression = ""
        self.result_display.text = '0'
    
    def backspace(self, instance):
        """Remove the last character"""
        if self.expression:
            self.expression = self.expression[:-1]
            self.result_display.text = self.expression if self.expression else '0'
    
    def calculate(self, instance):
        """Calculate the result"""
        try:
            # Replace display symbols
            expression = self.expression.replace('×', '*').replace('−', '-')
            result = eval(expression)
            
            # Format result to remove unnecessary decimals
            if isinstance(result, float):
                if result == int(result):
                    result = int(result)
            
            self.result_display.text = str(result)
            self.expression = str(result)
        except ZeroDivisionError:
            self.result_display.text = 'Error: Division by 0'
            self.expression = ""
        except Exception as e:
            self.result_display.text = 'Error'
            self.expression = ""

if __name__ == '__main__':
    Calculator().run()
