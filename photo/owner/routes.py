from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/about')
def about():
   value = "About the Artist"
   return render_template('about.html', value=value,)

@bp.route('/contact')
def contact():
   value = "Contact the Artist"
   return render_template('contact.html', value=value,)