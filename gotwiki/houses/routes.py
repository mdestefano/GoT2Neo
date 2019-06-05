from . import houses

@houses.route('/houses')
def index():
    return '<h1> Houses Index</h1>'