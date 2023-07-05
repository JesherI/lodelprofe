from flask import (Flask, render_template, request,
                   redirect,url_for,flash)
from db.categories import Category

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

@app.route("/")
def home():
    name="Jehser Mednieta Ibarra"
    return render_template('home.html', name=name)

@app.route("/3B/")
def tres():
    alumnos = ['Gaby', 'Adriana','Alicia']
    return render_template('tres.html', alumnos=alumnos)

@app.route("/contact/")
def contact():
    user = 'Jeshersin'
    return render_template('contact.html', user=user)

@app.route("/about/")
def about():
    user = 'Jeshersin'
    return render_template('about.html', user=user)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route('/categories/')
def categories():
    # Consultar Categorias de DB
    categories = Category.get_all()
    return render_template('categories.html', categories=categories)

@app.route('/categories/create/', methods=('GET','POST'))
def create_cat():
    if request.method =='POST':
        category = request.form['category']
        description = request.form['description']
        if not category:
            flash('Debes ingresar la categoria')
        elif not description:
            flash('Debes ingresar la decripción')
        else:
            cat=Category(category,description)
            cat.save()
            return redirect(url_for('categories'))
    
    return render_template('create_cat.html')


if __name__=='__main__' :
    app.run(debug=True)