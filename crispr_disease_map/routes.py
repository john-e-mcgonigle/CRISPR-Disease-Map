from crispr_disease_map import app
from flask import render_template

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/genes.html')
def genes():
    genes = [
        {
            'name': 'ABC',
            'screens_count': '42',
            'samples_count': '4'
        },
        {
            'name': 'DEF',
            'screens_count': '1024',
            'samples_count': '2'
        }
    ]
    return render_template('genes.html', genes=genes)

@app.route('/screens.html')
def screens():
    screens = [
        {
            'name': 'TEST1',
            'genes_count': '9000',
            'samples_count': '3'
        },
        {
            'name': 'TEST2',
            'screens_count': '100500',
            'samples_count': '3'
        }
    ]
    return render_template('screens.html', screens=screens)