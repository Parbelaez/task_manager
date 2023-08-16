from flask import render_template, request, redirect, url_for, flash
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route('/')
def home():
    return render_template('tasks.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category = Category(category_name=request.form.get['category_name'])
        db.session.add(category)
        db.session.commit()
        flash('New category was successfully added')
        return redirect(url_for('categories'))
    return render_template('add_category.html')