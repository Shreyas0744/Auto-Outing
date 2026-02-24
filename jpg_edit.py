from pdf2image import convert_from_path
from PIL import ImageDraw, ImageFont
import os
import datetime

# Get today's date
today = datetime.date.today()

# Paths
pdf_path = "form.pdf"
poppler_path = r"poppler-25.07.0\Library\bin" 
font_path = "Inkfree.ttf"

# Load font
font = ImageFont.truetype(font_path, 35)
font2 = ImageFont.truetype(font_path, 22)

text_position = (740, 287)
text_position2 = (514, 361)
text_position3 = (961, 362)
text_position4 = (340, 439)
text_position5 = (302,1341)
text_position6 = (550,1510)
text_position7 = (550,1595)
text_position8 = (550,1680)
text_position9 = (890,1510)
text_position10 = (890,1595)
text_position11 = (890,1680)
text_position12 = (1245,1510)
text_position13 = (1245,1595)
text_position14 = (1245,1680)

# Names to fill
name = "Rithwik Reddy Majjigapu"
id ="23WU0101099"
course = "B.Tech"
AY = "2023 - 2027"
date = today.strftime( "%d/%m/%Y")
Fname = "Ravichander Reddy M"
Mname = "Saritha.M "
Sname = "Rithwik Reddy M"
Fmail = "saritham3112@gmail.com"
Mmail="saritham3112@gmail.com"
Smail = "mrithwikreddy3112@gmail.com"
Fph = "7730024642"
Mph = "9010112285"
Sph = "7337347112"

# Loop through each name
images = convert_from_path(
    pdf_path,
    dpi=200,
    first_page=1,
    last_page=1,
    poppler_path=poppler_path  # ✅ Specify poppler path here
    )
    
image = images[0]  # Get the first page as image

# Draw text (name) onto the image
draw = ImageDraw.Draw(image)
draw.text(text_position, name, font=font, fill="black")
draw.text(text_position2, id, font=font, fill="black")
draw.text(text_position3, course, font=font, fill="black")
draw.text(text_position4, AY, font=font, fill="black")
draw.text(text_position5, date, font=font, fill="black")
draw.text(text_position6, Fname, font=font, fill="black")
draw.text(text_position7, Mname, font=font, fill="black")
draw.text(text_position8, Sname, font=font, fill="black")
draw.text(text_position9, Fmail, font=font2, fill="black")
draw.text(text_position10, Mmail, font=font2, fill="black")
draw.text(text_position11, Smail, font=font2, fill="black")
draw.text(text_position12, Fph, font=font, fill="black")
draw.text(text_position13, Mph, font=font, fill="black")
draw.text(text_position14, Sph, font=font, fill="black")

# Save the result as a new PDF
output_filename = f"filled_form_{name}.pdf"
image.save(output_filename, "PDF")
print(f"Saved: {output_filename}")
