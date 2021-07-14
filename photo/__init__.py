from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session
# from flask_admin import Admin, AdminIndexView
# from flask_admin.contrib.sqla import ModelView
from config import KEY, SQL


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = KEY

    app.config['SQLALCHEMY_DATABASE_URI'] = SQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)

    # flask admin config

    # from knit.db_knit import TblUsers

    # from knit.db_knit import TblProducts


    # def check_admin():
    #     try:
    #         user = session["USER_ID"]
    #         print (user)
    #         if user == "miha_123@gmail.com":
    #             return True
    #     except:
    #         return False


    # # this will allow tables
    # class MyModelView(ModelView):
    #     page_size    = 1000
    #     can_view_details = True
    #     column_exclude_list = ['passwd', ]
    #     def is_accessible(self):
    #         return check_admin()

    # class MyAdminView(AdminIndexView):
    #     def is_accessible(self):
    #         return check_admin()

    # admin = Admin(app, index_view=MyAdminView(), template_mode='bootstrap4', name='WebTools')
    # admin.add_view(MyModelView    (TblUsers,  db.session))
    # admin.add_view(MyModelView    (TblProducts,  db.session))



    # home BP
    from photo.home import bp as home
    app.register_blueprint(home)

    # # # My gallery Blueprint
    # from photo.gallery import bp as gallery
    # app.register_blueprint(gallery)

    # # # # owner Blueprint
    # from photo.owner import bp as owner
    # app.register_blueprint(owner)
    

    return app