import kivy    
from kivy.app import App 

     
# this restrict the kivy version i.e   
# below this kivy version you cannot   
# use the app or software   

kivy.require('1.9.0')  
from kivy.uix.gridlayout import GridLayout 
from kivy.config import Config 


Config.set('graphics', 'resizable', 1) 
## Config.set('graphics', 'width', '400') 
## Config.set('graphics', 'height', '400') 


class CalcGridLayout(GridLayout): 

    def calculate(self, calculation): 

        if calculation: 

            try: 


                self.display.text = str(eval(calculation)) 

            except Exception: 

                self.display.text = "Error"

   

class CalculatorApp(App): 

   

    def build(self): 

        return CalcGridLayout() 

calcApp = CalculatorApp() 
calcApp.run() 