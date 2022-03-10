from src.modules.module import Module as TemplateModule

class Module(TemplateModule):
    def __init__(self, display):
        super().__init__(display)


    
    def draw(self):
        super().draw()

    def update(self):
        super().update()
        print("test")