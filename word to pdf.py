import kivy
from kivy.app import App
from kivy.lang import  Builder
from plyer import  filechooser
from docx2pdf import convert


kv = """

BoxLayout:
    
    Button:
        color: "black"
        background_color: 255, 255, 255
        size_hint: None, None
        pos_hint: {'x': 0.2, 'y':0.8}
        size: dp(120), dp(40)
        text: "select .Docx"
        on_release:
            app.file_chooser()
            
            
  
       
    
"""
class FileChooser(App):
    def build(self):
        return Builder.load_string(kv)
    
    def file_chooser(self):
        filechooser.open_file(on_selection = self.selected)
        
    def selected(self, selection):
        convert(selection[0])
        

        
        
if __name__ == "__main__":
    FileChooser().run()
        