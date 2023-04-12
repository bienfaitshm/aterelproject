from fpdf import Template
#this will define the ELEMENTS that will compose the template.
elements = [
    { 
        'name': 'company_logo', 
        'type': 'I', 
        'x1': 20.0, 
        'y1': 17.0, 
        'x2': 78.0,
        'y2': 30.0,
        'font': None,
        'size': 0.0,
        'bold': 0,
        'italic': 0,
        'underline': 0,
        'align': 'C',
        'text': 'logo',
        'priority': 2, 
        'multiline': False
    },
    {
        'name': 'company_name',
        'type': 'T',
        'x1': 17.0,
        'y1': 32.5,
        'x2': 115.0,
        'y2': 37.5,
        'font':'helvetica',
        'size': 12.0,
        'bold': 1,
        'italic': 0,
        'underline': 0,
        'align': 'C',
        'text': '',
        'priority': 2,
        'multiline': False
    },
    {
        'name': 'multline_text',
        'type': 'T', 
        'x1': 20, 
        'y1': 100, 
        'x2': 40, 
        'y2': 105, 
        'font': 'helvetica', 
        'size': 12, 
        'bold': 0, 
        'italic': 0, 
        'underline': 0,
        'background': 0x88ff00, 
        'align': 'C', 
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisici elit', 
        'priority': 2, 
        'multiline': True
    },
    {
        'name': 'box',
        'type': 'B',
        'x1': 15.0,
        'y1': 15.0,
        'x2': 185.0,
        'y2': 260.0, 
        'font': 'helvetica',
        'size': 0.0,
        'bold': 0, 
        'italic': 0, 
        'underline': 0,
        'align': 'C', 
        'text': None, 
        'priority': 0, 
        'multiline': False
    },
{ 'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'helvetica', 'size': 0.0, 'bold': 1, 'italic': 0, 'underline': 0,
'align': 'C', 'text': None, 'priority': 2, 'multiline': False},
{ 'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'helvetica', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0,
'align': 'C', 'text': None, 'priority': 3, 'multiline': False},
{ 'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 246.5, 'x2': 140.0, 'y2': 254.0, 'font': 'Interleaved 2of5 NT', 'size': 0.75, 'bold': 0, 'italic': 0,
'underline': 0, 'align': 'C', 'text': '200000000001000159053338016581200810081', 'priority': 3, 'multiline': False},
]

#here we instantiate the template
f = Template(format="A4", elements=elements,
title="Sample Invoice")
f.add_page()
#we FILL some of the fields of the template with the information we want
#note we access the elements treating the template instance as a "dict"
f["company_name"] = "Sample Company"
f["company_logo"] = "./medias/img.jpg"
#and now we render the page
f.render("./template.pdf")