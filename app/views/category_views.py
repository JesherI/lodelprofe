from flask import Blueprint, render_template, request, redirect, flash, url_for

from models.categories import Category

category_views = Blueprint('category',__name__)

@category_views .route('/categories/')
def categories():
    # Consultar Categorias de DB
    categories = Category.get_all()
    return render_template('category/categories.html', categories=categories)

@category_views .route('/categories/create/', methods=('GET','POST'))
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
            return redirect(url_for('category.categories'))
    
    return render_template('category/create_cat.html')

@category_views .route('/categories/<int:id>/update/')
def update_cat(id):
    return "Vamos a Actualizar"

@category_views .route('/categories/<int:id>/delete/')
def delete_cat(id):
    cat = Category.get(id)
    cat.delete()
    return redirect(url_for('category.categories'))