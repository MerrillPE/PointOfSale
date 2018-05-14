import kivy
import sqlite3

from PIL import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.factory import Factory

conn = sqlite3.connect('CMPE131.db')  # create a database file
c = conn.cursor()   # a cursor is used for command things

Builder.load_string("""
# Main menu when opening application
#.import Factory kivy.factory.Factory
<MainMenu>:
    BoxLayout:
        padding: [10,50,10,50]
        spacing: 25
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
                size_hint_y: .1                
            #Button:
                #text: 'Sales Report' 
                #on_press:                    
                    #root.manager.transition.direction = "left"
                    #root.manager.transition.duration = .25
                    #root.manager.current = "salesLogin"               
            Button:
                text: 'Schedule' 
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.transition.duration = .25
                    root.manager.current = "schedLogin"        

# Screen switch when processing sale
<SaleProcessing>:
    BoxLayout:
        padding: [10,50,10,50]
        spacing: 50
        
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
                padding: [0,0,0,100]
                
                Button:
                    text: 'Back'
                    on_press:
                        itemPanel.item_strings = ''
                        skuEntry.text = ''
                        qtyEntry.text = ''
                        root.clearSubtotal()
                        root.manager.transition.direction = "right"
                        root.manager.transition.duration = .25
                        root.manager.current = "mainMenu"
                Button: 
                    text: 'Add'
                    on_press:
                        #itemPanel.item_strings.append(root.AcceptEntry(skuEntry.text, qtyEntry.text))
                        root.add(skuEntry.text, qtyEntry.text)
                Button:
                    text: 'Total'
                    on_press:
                        #itemTotal.itemTotalling()
                        #root.printAdj()
                        root.manager.get_screen('itemTotal').setSubtotal(root.subtotal)
                        root.manager.transition.direction = "left"
                        root.manager.transition.duration = .25
                        root.manager.current = "itemTotal"
        
        BoxLayout:
            orientation: 'vertical'
            
            ListView:
                size_hint_y: .8
                id: itemPanel
                item_strings: [""]
                
            Label:
                size_hint_y: .2
                id: subtotalLabel
                text: "Subtotal: "                         

# Item totaling screen after all items are added
<ItemTotalling>:
        
    BoxLayout:
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50
        
        Label:
            text: 'Total'
            font_size: 32
            size_hint_y: .2
            
        #ListView:
            #ListView:
                #size_hint_y: .8
                #id: itemPanel
                #item_strings: [""]
                
        Label:
            id: subtotalLabel
            font_size: 24
        
        Label:
            id: taxLabel
            font_size: 24
            
        Label:
            id: totalLabel
            font_size: 24
    
        BoxLayout:
            orientation: 'horizontal'
            
            Label:
                text: "Tender Amount: $"
                font_size: 24
                
            TextInput:
                id: tenderAmount
                multiline: False
                font_size: 24
                
        Button:
            text: 'Enter'
            on_press:
                root.changeDue(tenderAmount.text)
                root.manager.get_screen('saleProcessing').makeAdj()
                root.manager.get_screen('saleProcessing').clearSubtotal()
                root.manager.get_screen('saleProcessing').clearScreen()
                #root.manager.get_screen('saleProcessing').qtyEntry.text = ''
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "saleProcessing"  
                
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
        padding: [10,50,10,50]
        spacing: 50
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
                padding: [0,0,0,100]
                
                Button:
                    text: 'Back'
                    on_press:
                        itemPanel.item_strings = ''
                        skuEntry.text = ''
                        qtyEntry.text = ''
                        root.manager.transition.direction = "right"
                        root.manager.transition.duration = .25
                        root.manager.current = "mainMenu"
                Button: 
                    text: 'Add'
                    on_press:
                        #itemPanel.item_strings.append(root.AcceptEntry(skuEntry.text, qtyEntry.text))
                        root.add(skuEntry.text, qtyEntry.text)
                Button:
                    text: 'Total'
                    on_press:
                        root.manager.get_screen('returnTotal').setSubtotal(root.subtotal)
                        root.manager.transition.direction = "left"
                        root.manager.transition.duration = .25
                        root.manager.current = "returnTotal"
        BoxLayout:
            orientation: 'vertical'
            
            ListView:
                size_hint_y: .8
                id: itemPanel
                item_strings: [""]
                
            Label:
                size_hint_y: .2
                id: subtotalLabel
                text: "Subtotal: "
                
<OnHandManagement>:
    BoxLayout:
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50
        
        Label:
            text: 'On Hand Management'
            font_size: 32
        
        BoxLayout:
            orientation: "horizontal"
            padding: [50,0,50,0]
            
            Label:
                text: 'SKU: '
                font_size: 24
            TextInput:                
                id: skuEntry
                font_size: 32
                multiline: False
                
        BoxLayout:
            padding: [50,0,50,0]
            
            Button:
                text: 'Back'
                on_press:
                    onHandPanel.item_strings = []
                    skuEntry.text = ''
                    root.manager.transition.direction = "right"
                    root.manager.transition.duration = .25
                    root.manager.current = "mainMenu"
                    
            Button:
                text: 'Enter'
                on_press:
                    onHandPanel.item_strings = []
                    onHandPanel.item_strings.append(root.getOnHands(skuEntry.text))
             
        ListView:
            id: onHandPanel
            item_strings: [""]
                
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


<ScheduleLogin>:
    BoxLayout
        id: sched_login_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50

        Label:
            text: 'Manager Login'
            font_size: 32

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Login'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20

            TextInput:
                id: login
                multiline:False
                font_size: 28

        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 18
                text_size: root.width-20, 20

            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 28

        Button:
            text: 'Login'
            font_size: 24
            on_press: root.do_login(login.text, password.text)
            
<SalesLogin>:
    BoxLayout
        id: sales_login_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50

        Label:
            text: 'Manager Login'
            font_size: 32

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Login'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20

            TextInput:
                id: login
                multiline:False
                font_size: 28

        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 18
                text_size: root.width-20, 20

            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 28

        Button:
            text: 'Login'
            font_size: 24
            on_press: root.do_login(login.text, password.text)
            
<ReturnTotalling>:
    BoxLayout:
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50
        
        Label:
            text: 'Total'
            font_size: 32
            size_hint_y: .2
            
        #ListView:
            #ListView:
                #size_hint_y: .8
                #id: itemPanel
                #item_strings: [""]
                
        Label:
            id: subtotalDueLabel
            font_size: 24
        
        Label:
            id: taxDueLabel
            font_size: 24
            
        Label:
            id: totalDueLabel
            font_size: 24
                
        Button:
            text: 'Enter'
            on_press:
                #root.changeDue(tenderAmount.text)
                root.manager.get_screen('returnProcessing').makeAdj()
                root.manager.get_screen('returnProcessing').clearSubtotal()
                root.manager.get_screen('returnProcessing').clearScreen()
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "returnProcessing"  
                
        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .25
                root.manager.current = "returnProcessing"
""")

class MainMenu(Screen):
    pass

class SaleProcessing(Screen):

    subtotal = 0
    onHandAdj = {}

    def add(self, sku, quantity):
        #self.ids['itemPanel'].adapter.data.append(sku + '@' + quantity)
        t = (sku,)
        c.execute("SELECT * FROM my_stock WHERE ID = ?", t)

        if c.fetchone() != None and quantity != '' and int(quantity) > 0:
            t = (sku,)
            c.execute("SELECT * FROM my_stock WHERE ID = ?", t)
            entry = self.buildEntry(str(c.fetchone()), quantity)
            self.ids['itemPanel'].adapter.data.append(entry)
            self.onHandAdj[sku] = quantity

        elif quantity == '' or int(quantity) <= 0:
            self.qtyPopup()
        else:
            self.skuPopup()

    def buildEntry(self, dataEntry, quantity):

        parsedList = dataEntry.split(',')
        entry = self.parseName(parsedList) + '@' + quantity + ': $' + '%0.2f' % self.calcPrice(parsedList, quantity)
        return entry

    def parseName(self, list):

        return list[1].replace("'", "")

    def calcPrice(self, list, qty):

        price = float(list[2].replace(' ', ''))
        quantity = int(qty)
        itemTotal = price * quantity
        self.calcSubtotal(itemTotal)
        return itemTotal

    def calcSubtotal(self, price):

        self.subtotal += price
        self.ids['subtotalLabel'].text = 'Subtotal: $' + '%0.2f' % self.subtotal

    def clearSubtotal(self):

        self.subtotal = 0
        self.ids['subtotalLabel'].text = 'Subtotal: '

    def clearScreen(self):

        self.ids['skuEntry'].text = ''
        self.ids['qtyEntry'].text = ''
        self.ids['itemPanel'].adapter.data = []
        self.onHandAdj = {}

    def totalItems(self):
        list = self.ids['itemPanel'].adapter.data
        ItemTotalling.itemTotalling(self.ids['itemPanel'].adapter.data[1])

    def sendSubtotal(self):
        ItemTotalling.getSubtotal()

    def printAdj(self):
        print(self.onHandAdj)

    def makeAdj(self):

        for sku in self.onHandAdj:
            adjust = self.onHandAdj[sku]

            t = (adjust, sku)
            c.execute("UPDATE my_stock SET Quantity = Quantity - ? WHERE ID = ?", t)

    def skuPopup(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='OK', size_hint_y=.1)
        box.add_widget(Label(text='SKU not found'))
        box.add_widget(button)

        popup = Popup(title='Not Found',
                      content=box, size=(400, 400))

        popup.open()
        button.bind(on_press=popup.dismiss)

    def qtyPopup(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='OK', size_hint_y=.1)
        box.add_widget(Label(text='Not a valid quantity'))
        box.add_widget(button)

        popup = Popup(title='Not Found',
                      content=box, size=(400, 400))

        popup.open()
        button.bind(on_press=popup.dismiss)

class ReturnProcessing(Screen):

    subtotal = 0
    onHandAdj = {}

    def add(self, sku, quantity):
        t = (sku,)
        c.execute("SELECT * FROM my_stock WHERE ID = ?", t)

        if c.fetchone() != None and quantity != '' and int(quantity) > 0:
            t = (sku,)
            c.execute("SELECT * FROM my_stock WHERE ID = ?", t)
            entry = self.buildEntry(str(c.fetchone()), quantity)
            self.ids['itemPanel'].adapter.data.append(entry)
            self.onHandAdj[sku] = quantity


        elif quantity == '' or int(quantity) <= 0:
            self.qtyPopup()
        else:
            self.skuPopup()

    def buildEntry(self, dataEntry, quantity):

        parsedList = dataEntry.split(',')
        entry = self.parseName(parsedList) + '@' + quantity + ': -$' + '%0.2f' % self.calcPrice(parsedList, quantity)
        return entry

    def parseName(self, list):

        return list[1].replace("'", "")

    def calcPrice(self, list, qty):

        price = float(list[2].replace(' ', ''))
        quantity = int(qty)
        itemTotal = price * quantity
        self.calcSubtotal(itemTotal)
        return itemTotal

    def calcSubtotal(self, price):

        self.subtotal += price
        self.ids['subtotalLabel'].text = 'Subtotal: -$' + '%0.2f' % self.subtotal

    def clearSubtotal(self):

        self.subtotal = 0
        self.ids['subtotalLabel'].text = 'Subtotal: '

    def clearScreen(self):

        self.ids['skuEntry'].text = ''
        self.ids['qtyEntry'].text = ''
        self.ids['itemPanel'].adapter.data = []
        self.onHandAdj = {}

    def makeAdj(self):

        for sku in self.onHandAdj:
            adjust = self.onHandAdj[sku]

            t = (adjust, sku)
            c.execute("UPDATE my_stock SET Quantity = Quantity + ? WHERE ID = ?", t)

    def skuPopup(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='OK', size_hint_y=.1)
        box.add_widget(Label(text='SKU not found'))
        box.add_widget(button)

        popup = Popup(title='Not Found',
                      content=box, size=(400, 400))

        popup.open()
        button.bind(on_press=popup.dismiss)

    def qtyPopup(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='OK', size_hint_y=.1)
        box.add_widget(Label(text='Not a valid quantity'))
        box.add_widget(button)

        popup = Popup(title='Not Found',
                      content=box, size=(400, 400))

        popup.open()
        button.bind(on_press=popup.dismiss)

class OnHandManagement(Screen):

    def getOnHands(self, sku):

        t = (sku,)
        c.execute("SELECT * FROM my_stock WHERE ID = ?", t)

        if c.fetchone() != None:
            t = (sku,)
            c.execute("SELECT * FROM my_stock WHERE ID = ?", t)
            entry = self.buildEntry(str(c.fetchone()))
            return entry

        else:
            self.skuPopup()

        #self.ids['onHandPanel'].adapter.data = []
        #t = (sku,)
        #c.execute("SELECT * FROM my_stock WHERE ID = ?", t)
        #entry = self.buildEntry(str(c.fetchone()))
        #entry = "\n" + sku + ": 5"
        #return entry

    def buildEntry(self, dataEntry):

        parsedList = dataEntry.split(',')
        entry = self.parseName(parsedList) + ": %0.0f" % float(self.parseOnHand(parsedList))
        return entry

    def parseName(self, list):

        return list[1].replace("'", "")

    def parseOnHand(self, list):

        return list[3].replace(')', '')

    def skuPopup(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='OK', size_hint_y=.1)
        box.add_widget(Label(text='SKU not found'))
        box.add_widget(button)

        popup = Popup(title='Not Found',
                      content=box, size=(400, 400))

        popup.open()
        button.bind(on_press=popup.dismiss)

class SalesReport(Screen):
    pass

class Schedule(Screen):
    pass

class ItemTotalling(Screen):
    total = 0

    def itemTotalling(self):
        self.ids['itemPanel'].adapter.data.append('')

    def setSubtotal(self, amount):
        self.ids['subtotalLabel'].text = 'Subtotal: $%0.2f' % amount
        self.setLabels(amount)

    def setLabels(self, subtotal):
        tax = subtotal * .09
        self.total = subtotal + tax

        self.ids['taxLabel'].text = 'Tax: $%0.2f' % tax
        self.ids['totalLabel'].text = 'Total: $%0.2f' % self.total

    def changeDue(self, tender):

        amountDue = float(tender) - self.total

        box = BoxLayout()
        button = Button(text='OK')
        box.add_widget(Label(text='Change Due: $%0.2f' % amountDue))
        box.add_widget(button)

        popup = Popup(title='Amount Due',
                      content=box, size=(400,400))

        popup.open()
        button.bind(on_press=popup.dismiss)

class ScheduleLogin(Screen):

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        if loginText == 'admin' and passwordText == 'password':
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'schedule'

            image = Image.open('schedule.png')
            image.show()

        else:
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'mainMenu'

        app.config.read(app.get_application_config())
        app.config.write()

class SalesLogin(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        if loginText == 'admin' and passwordText == 'password':
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'salesReport'

        else:
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'mainMenu'

        app.config.read(app.get_application_config())
        app.config.write()

class ReturnTotalling(Screen):
    total = 0

    def itemTotalling(self):
        self.ids['itemPanel'].adapter.data.append('')

    def setSubtotal(self, amount):
        self.ids['subtotalDueLabel'].text = 'Subtotal: -$%0.2f' % amount
        self.setLabels(amount)

    def setLabels(self, subtotal):
        tax = subtotal * .09
        self.total = subtotal + tax

        self.ids['taxDueLabel'].text = 'Tax: -$%0.2f' % tax
        self.ids['totalDueLabel'].text = 'Total: -$%0.2f' % self.total

screen_manager = ScreenManager()
screen_manager.add_widget(MainMenu(name="mainMenu"))
screen_manager.add_widget(SaleProcessing(name="saleProcessing"))
screen_manager.add_widget(ReturnProcessing(name="returnProcessing"))
screen_manager.add_widget(OnHandManagement(name="onHands"))
screen_manager.add_widget(SalesReport(name="salesReport"))
screen_manager.add_widget(Schedule(name="schedule"))
screen_manager.add_widget(ItemTotalling(name="itemTotal"))
screen_manager.add_widget(ScheduleLogin(name='schedLogin'))
screen_manager.add_widget(SalesLogin(name='salesLogin'))
screen_manager.add_widget(ReturnTotalling(name='returnTotal'))

class PoSApp(App):

    def build(self):
        return screen_manager

PoSGUI_App = PoSApp()
PoSGUI_App.run()

c.close()
conn.close()