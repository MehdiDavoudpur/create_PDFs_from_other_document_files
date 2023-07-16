import glob
from fpdf import FPDF
from pathlib import Path

# set format of PDFs
pdf = FPDF(orientation="p", unit='mm', format='a4')

# create a list of filepaths:
files_path = glob.glob("Text-Files/*.txt")

# create title of each page in PDF by name of each text file:
for path in files_path:
    file_name = Path(path).stem.title()
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=18)
    pdf.cell(w=50, h=10, txt=file_name, ln=1)

#   extract the text in ech text file and save them word by word:
    with open(path, 'r') as file:
        text = file.readline()
        words = text.split(" ")

#       combine each 12 words together to make a text for one line:
        split_length = 12
        line_text = ''
        for i in range(0, len(words), split_length):
            split_words = words[i:i + split_length]
            for word in split_words:
                line_text = line_text + word + ' '
            pdf.set_font(family='Times', size=14)
            pdf.cell(w=200, h=10, txt=line_text, ln=1)
            line_text = ''

        # convert all text to pdf body by multi cell function:
        pdf.ln(25)
        pdf.multi_cell(w=0, h=10, txt=text)

pdf.output('PDFs/animals.pdf')
