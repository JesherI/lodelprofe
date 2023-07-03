from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name="Jehser Mednieta Ibarra"
    return render_template('home.html', name=name)

@app.route("/3B")
def tres():
    alumnos = ['Gaby', 'Adriana','Alicia']
    return render_template('tres.html', alumnos=alumnos)

@app.route("/contact")
def contact():
    user = 'Jeshersin'
    return render_template('contact.html', user=user)

@app.route("/about")
def about():
    user = 'Jeshersin'
    return render_template('about.html', user=user)


if __name__=='__main__' :
    app.run(debug=True)