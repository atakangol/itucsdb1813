from flask import Flask
import admin
#import flights
import general
#import tickets
import user

app = Flask(__name__)
app.debug = True

dsn = """user='ddzwibxvysqwgx' password='9e0edae8756536ffdba78314ebde69e2d019e58a2c05dfbad508b5eb657ac9e7'
         host='ec2-54-247-101-205.eu-west-1.compute.amazonaws.com' port=5432 dbname='d8o6dthnk5anke'"""

def create_app():
    app = Flask(__name__)

    #General Definitions
    app.add_url_rule("/errorpage/<message>", view_func=general.errorpage) #Enes
    app.add_url_rule("/about", view_func=general.about) #Enes
    app.add_url_rule("/news", view_func=general.news) #Enes

    #Admin Definitions
    app.add_url_rule("/adm_sendpost", view_func=admin.adm_sendpost, methods = ['GET', 'POST']) #Enes
    app.add_url_rule("/adm_pymreqs", view_func=admin.adm_pymreqs, methods = ['GET', 'POST']) #Enes
    app.add_url_rule("/deleteuser/<username>", view_func=admin.deleteuser, methods = ['POST']) #Enes
    app.add_url_rule("/adm_updateuser/<username>", view_func=admin.adm_updateuser, methods = ['POST']) #Enes
    app.add_url_rule("/adm_users/<username>", view_func=admin.updateuser) #Enes
    app.add_url_rule("/adminpage", view_func=admin.adminpage) #Enes
    app.add_url_rule("/adm_users", view_func=admin.adm_users) #Enes
    app.add_url_rule("/adm_fabrika_ayarlari", view_func=admin.adm_fabrika_ayarlari) #Enes

    #User Definitons
    app.add_url_rule("/login", view_func=user.login, methods = ['POST']) #Enes
    app.add_url_rule("/register", view_func=user.register, methods = ['POST']) #Enes
    app.add_url_rule("/userpage", view_func=user.userpage) #Enes
    app.add_url_rule("/logout", view_func=user.logout) #Enes
    app.add_url_rule("/buycoins", view_func=user.buycoins, methods = ['GET', 'POST']) #Enes
    app.add_url_rule("/edituser", view_func=user.edituser, methods = ['GET', 'POST']) #Enes
    app.add_url_rule("/forgotpassword", view_func=user.forgotpassword, methods = ['GET', 'POST']) #Enes

    return app

if __name__ == "__main__":
    app = create_app()
    app.config.update(dict(
    SECRET_KEY="pnBM(@?&#p]l~eI%L&$@#9f)T^uK7U",
    WTF_CSRF_SECRET_KEY="N4<*$83/[[{)ZO&X2yL_qN68+{;;Xo"
    ))
    app.run()
