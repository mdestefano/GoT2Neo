# app.py - a minimal flask api using flask_restful
from gotwiki import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')