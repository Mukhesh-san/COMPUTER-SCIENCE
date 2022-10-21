from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        Firstname = request.form.get('Firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 3:
            flash("Email must me greater than 2 characters.", category='error')
        elif len(Firstname) < 2:
            flash("Firstname must me greater than 1 characters.", category='error')
        elif password1 != password2:
            flash("Your paswords dont match.", category='error')
        elif len(password1) < 7:
            flash("Password must me greater than 6 characters.", category='error')
        else:
            flash("Account Created!.", category='success')
    
    return render_template("sign_up.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"