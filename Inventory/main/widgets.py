from django import forms

place_choices = [
    ('Kitchen', 'Kitchen'),
    ('Bedroom', 'Bedroom'),
    ('Bedroom 2', 'Bedroom 2'),
    ('Bedroom 3', 'Bedroom 3'),
    ('Hall', 'Hall'),
    ('Bathroom', 'Bathroom'),
    ('Toilet', 'Toilet'),
    ("Children's room", "Children's room"),
    ("Cabinet", "Cabinet"),
    ("Garage", "Garage"),
    ("Balcony", "Balcony"),
]
place_choices.sort()
place_choices.append(('Customary', 'Customary'))

class LayoutCreateWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets =(
            forms.Select(attrs={'class': 'form-control'}, choices=place_choices),
            forms.TextInput(attrs={'class':'form-control mt-2', 'style':'display:none'  })
        )
        super(LayoutCreateWidget,self).__init__(widgets,attrs)




    def decompress(self, data):
        if data:
            return data.split("-")
        return [None, None]