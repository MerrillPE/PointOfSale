import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
# Main menu when opening application
<MainMenu>:
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: 'Sales Menu'
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
        BoxLayout:
            orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'
                BoxLayout:
                    orientation: 'horizontal'
                    Label:
                        text: 'SKU:' 
                    TextInput:
                        id: skuEntry
                        font_size: 32
                        multiline: False
                BoxLayout:
                    orientation: 'horizontal'
                    Label:
                        text: 'Quantity:'
                    TextInput:
                        id: qtyEntry
                        font_size: 32
                        multiline: False
            
            BoxLayout:
                Button:
                    text: 'Back'
                    on_press:
                        #itemPanel.text = ''
                        root.manager.transition.direction = "right"
                        root.manager.transition.duration = .25
                        root.manager.current = "mainMenu"
                Button: 
                    text: 'Add'
                    on_press:
                        itemPanel.item_strings.append(root.AcceptEntry(skuEntry.text, qtyEntry.text))
                Button:
                    text: 'Total'
                    on_press:
                        root.manager.transition.direction = "left"
                        root.manager.transition.duration = .25
                        root.manager.current = "itemTotal"
        AnchorLayout:
            ListView:
                id: itemPanel
                item_strings: ["Items"]                         

# Item totaling screen after all items are added
<ItemTotalling>:
    Button:
        text: 'Back'
        on_press:
            root.manager.transition.direction = "right"
            root.manager.transition.duration = .25
            root.manager.current = "saleProcessing"

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

    def AcceptEntry(self, sku, quantity):
        entry = "\n" + sku + "@" + quantity
        return entry

class ReturnProcessing(Screen):
    pass

class OnHandManagement(Screen):
    pass

class SalesReport(Screen):
    pass

class Schedule(Screen):
    pass

class ItemTotalling(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(MainMenu(name="mainMenu"))
screen_manager.add_widget(SaleProcessing(name="saleProcessing"))
screen_manager.add_widget(ReturnProcessing(name="returnProcessing"))
screen_manager.add_widget(OnHandManagement(name="onHands"))
screen_manager.add_widget(SalesReport(name="salesReport"))
screen_manager.add_widget(Schedule(name="schedule"))
screen_manager.add_widget(ItemTotalling(name="itemTotal"))



class PoSApp(App):

    def build(self):
        return screen_manager

PoSGUI_App = PoSApp()
PoSGUI_App.run()