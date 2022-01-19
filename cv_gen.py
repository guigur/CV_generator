from fpdf import FPDF


pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()
pdf_w=210
pdf_h=297

pdf.set_line_width(1.0)
pdf.line(0,pdf_h/2,210,pdf_h/2)

def titles(self):
    self.set_xy(0.0,0.0)
    self.set_font('Arial', 'B', 16)
    self.set_text_color(220, 50, 50)
    self.cell(w=210.0, h=40.0, align='C', txt="LORD OF THE PDFS", border=0)

def imagex(self):
    self.set_xy(6.0,6.0)
    self.image("profile.png",  link='', type='', w=1586/80, h=1920/80)


def texts(self,name):
    with open(name,'rb') as xy:
        txt=xy.read().decode('latin-1')
    self.set_xy(10.0,80.0)    
    self.set_text_color(76.0, 32.0, 250.0)
    self.set_font('Arial', '', 12)
    self.multi_cell(0,10,txt)

pdf.image('profile.png',10,6,30);

pdf.set_author('guillaume arthaud')
pdf.output('test.pdf','F')