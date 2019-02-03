
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, equal_to

app = Flask(__name__)

app.config["SECRET_KEY"] = "nbh3j4tu3orjfio4jnp@$#%$^TU"

class RegisterForm(FlaskForm):
    user_name = StringField(label="userName", validators=[DataRequired()])
    password = PasswordField(label="passWord", validators=[DataRequired()])
    password2 = PasswordField(label="confirm_passWord", validators=[DataRequired(), equal_to("password")])
    submit = SubmitField(label="submit")

# actually: first-time login: register; later: login
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()  # create form object

    if form.validate_on_submit():
        vusername = form.user_name
        vpass = form.password
        vpassc = form.password2
        print (vusername, vpass, vpassc)
        return "register success"
    else:
        if request.method == "GET": # still: request
            return render_template("register.html", form=form, errmsg = "")
        else: # POST, form validate fail: wrong input
            return render_template("register.html", form=form, errmsg = "wrong input")

@app.route("/home")
def home():
    return "home"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)