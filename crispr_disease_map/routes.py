from crispr_disease_map import app

@app.route('/')
@app.route('/index')
def index():
    return "CRISPR - Disease - Map"