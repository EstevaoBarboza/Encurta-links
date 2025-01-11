import re
import pyshorteners
from flask import Flask, request, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.secret_key = 'Encurta_Links'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




def validar_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' 
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

@app.route('/', methods=['GET', 'POST'])
def encurtar():
    link_curto = None

    if request.method == 'POST':
        url_longa = request.form.get('link_input')

        if not url_longa or not validar_url(url_longa):
            flash("URL inválida. Por favor, insira uma URL válida.", "error")
        else:
            type_tiny = pyshorteners.Shortener()
            link_curto = type_tiny.tinyurl.short(url_longa)

   
            session['link_curto'] = link_curto



    return render_template('index.html', link_curto=link_curto)

if __name__ == '__main__':
    app.run(debug=True)
