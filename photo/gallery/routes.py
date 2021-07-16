from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/acrylic')
def acrylic():
   value = "Acrylic Photos "
   return render_template('acrylic.html', value=value,)

@bp.route('/digital')
def digital():
   value = " Digital Photos"
   return render_template('digital.html', value=value,)