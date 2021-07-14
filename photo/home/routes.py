from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/')
def main():
   value = "Welcome to the Home Page of Maria's Designs"
   return render_template('home.html', value=value,)