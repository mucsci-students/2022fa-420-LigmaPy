from tkinter import Tk, Canvas, Frame, BOTH
import json
class Plot(Frame):
    def __init__(self):
        super().__init__()
        self.Draw()
        
    def Draw(self):
        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)
        f = open('UMLsavefiles/testfile.json')
        data=json.load(f)
        x0=0
        x1=0
        y0=0
        y1=0
        classlocation=[]
        canvas = Canvas(self)
        for items in data['classes']:
            print(items['name'])
            classid=canvas.create_rectangle(x0+10, x1+10, y0+10, y1+10, outline="#f11",
            fill="#1f1", width=10)
            x0=x0+20
            x1=x1+10
            y0=y0+20
            y1=y1+10
            # we need to store the instances to access the location later
            classlocation.append((canvas.coords(classid),items['name']))
        for items in data['relationships']:
            for names in data['classes']:
                if names['name']==items['source']:
                    canvas.create_line(classlocation[0][0], classlocation[1][0])
                    
        canvas.pack(fill=BOTH, expand=True)
def main():

    root = Tk()
    ex = Plot()
    root.geometry("330x220+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()