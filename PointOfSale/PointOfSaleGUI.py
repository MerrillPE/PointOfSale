import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
# Main menu when opening application
<MainMenu>:
    BoxLayout:
    
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Cashier'
                size_hint_y: .3                
            Button:
                text: 'Sale' 
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.transition.duration = .25
                    root.manager.current = "saleProcessing"                
            Button:
                text: 'Return' 
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.transition.duration = .25
                    root.manager.current = "returnProcessing"                
            Button:
                text: 'On Hand Count' 
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.transition.duration = .25
                    root.manager.current = "onHands"
                    
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Manager'
                size_hint_y: .2                
            Button:
                text: 'Sales Report' 
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.transition.duration = .25
                    root.manager.current = "salesReport"                
            Button:
                text: 'Schedule' 
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.transition.duration = .25
                    root.manager.current = "schedule"        

# Screen switch when processing sale
<SaleProcessing>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "mainMenu"

# Item totaling screen after all items are added
#<ItemTotaling>:

# Receipt shown after amount is paid
#<Receipt>:

<ReturnProcessing>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "mainMenu"
                
<OnHandManagement>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "mainMenu"
                
<SalesReport>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "mainMenu"
                
<Schedule>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "mainMenu"

""")

class MainMenu(Screen):
    pass

class SaleProcessing(Screen):
    pass

class ReturnProcessing(Screen):
    pass

class OnHandManagement(Screen):
    pass

class SalesReport(Screen):
    pass

class Schedule(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(MainMenu(name="mainMenu"))
screen_manager.add_widget(SaleProcessing(name="saleProcessing"))
screen_manager.add_widget(ReturnProcessing(name="returnProcessing"))
screen_manager.add_widget(OnHandManagement(name="onHands"))
screen_manager.add_widget(SalesReport(name="salesReport"))
screen_manager.add_widget(Schedule(name="schedule"))

class PoSApp(App):

    def build(self):
        return screen_manager

PoSGUI_App = PoSApp()
PoSGUI_App.run()