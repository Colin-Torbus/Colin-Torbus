import openpyxl
from openpyxl import Workbook
from pathlib import Path
import os
from openpyxl import load_workbook


fpath = Path(__file__)
os.chdir(fpath.parent)


# I found a good way to cut out a layer of the dict, now we only go 3 deep.
items = {
    'projector': {
        'p60' : {
            'manufacturer' : 'norxe',
            'country of origin' : 'norway',
            'description' : 'cool rectangle' ,
        },
        'p10' : {
            'manufacturer' : 'norxe',
            'country of origin' : 'norway',
            'description' : 'not as cool rectangle',
            },
        },
    'monitor' : {
        'lg50' : {
            'manufacturer' : 'lg',
            'country of origin' : 'zimbabwe',
            'description' : 'crt tv',
        },
        'samsung69' : {
            'manufacturer' : 'samsung',
            'country of origin' : 'constantinople',
            'description' : '69 in tv',
        }
    }
}
 

# Down the line make sure that one of the fields in the model subcategory can be blank/none
# We may need to remove TAA compliance later and make it part of the description, unless we make 2 quote forms.
def new_item(category, manufacturer, model, origin, description, warranty, taa):
    if category in items:
        items[category][model] = {
            'manufacturer': manufacturer,
            'country of origin': origin,
            'description': description,
            'warranty' : warranty,
            'taa' : taa,
        }
    else:
        items[category] = {
            model: {
                'manufacturer': manufacturer,
                'country of origin': origin,
                'description': description,
                'warranty' : warranty,
                'taa' : taa,
            }
        }


def abom_update():
    pass