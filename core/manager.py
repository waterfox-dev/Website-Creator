from rich.console import Console

from core.template import html_template
import os

class Manager() :
    
    def __init__(self) -> None:
        self.console = Console()
        self.title("Console Manager")
        self.running = True
        
        while self.running :
            command = input('>>>')
            self.executor(command)
       
    def center(self, text : str) -> None :
        self.console.rule(text)
    
    def title(self, text : str) -> None :
        self.console.rule(f'[bold red] {text}')
    
    def error(self, text : str) -> None :
        self.console.print(f'[bold red] {text}')
    
    def executor(self, command : str) -> any :
      
        if command == 'exit' :
            self.center('Goodbye')
            self.running = False
            
        elif command[0:6] == 'create' :
            if command[7:] == 'view' :
                
                name = input('name : ')
                
                with open(f"templates/{name}.html", 'w', encoding='utf8') as n_file :
                    n_file.write(html_template(name))
                    
                with open(f"static/{name}.css", "w", encoding='utf8') as n_file :
                    n_file.write('')
                
                with open(f'main.py', 'r', encoding='utf8') as p_file :
                    p_file = p_file.read()
                    n_file += f"@app.route('{name}')\n def {name}() : \n    return render_template({name}.html)"


        elif command[0:6] == 'delete' :
            if command[7:] == 'view' :
                name = input('name : ')
                try :
                    os.remove(f'app/templates/{name}.html')
                    os.remove(f'app/static/{name}.css')
                except FileNotFoundError :
                    self.error('Files not found')
        