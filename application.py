# file copied from CS50 Finance PSet
import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "2)Wkrv%b`BG&4P."

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


@app.route("/")
def index():
    """Main Page; make cool unlocking thing"""
    return render_template("index.html")


@app.route("/afrofuturism", methods=["GET", "POST"])
def afrofuturism():
    """Abt Afrofuturism"""
    return render_template("afrofuturism.html")


@app.route("/africanfuturism", methods=["GET", "POST"])
def africanfuturism():
    """Abt Afrofuturism in Africa"""
    return render_template("africanfuturism.html")


@app.route("/explore", methods=["GET", "POST"])
def explore():
    """Create Black Speculative Fiction World"""

    genres = ['Afrofuturism', 'Africanfuturism', 'Africanjujuism']
    times =  ['Past', 'Present', 'Future']
    themes = ['Gender/Sexuality', 'Religion', 'Class/Politics']
    mediums = ['Short Story', 'Book', 'Movie']

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        session['genre'] = request.form["g"]
        session['time'] = request.form["t"]
        session['theme'] = request.form["h"]
        session['medium'] = request.form["m"]

        if session['medium'] == None:
            return render_template("explore.html", genres=genres, times=times, themes=themes, mediums=mediums)
        # Redirect user to result page
        return redirect("/result")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("explore.html", genres=genres, times=times, themes=themes, mediums=mediums)

@app.route("/result", methods=['POST','GET'])
def result():
    """Results"""
    genre = session['genre']
    time = session['time']
    theme = session['theme']
    medium = session['medium']

    if genre=="Afrofuturism":
        if time=="Past":
            if theme=="Gender/Sexuality": #done
                if medium=="Short Story":
                    result='"The Princess Steel" by W.E.B. DuBois'
                elif medium=="Book":
                    result='"The Fifth Season" by N.K. Jemisin'
                else:
                    result="af p g/s movie"

            elif theme=="Religion":
                if medium=="Short Story":
                   result='"Lalibela" by Gabriel Teodros'
                elif medium=="Book":
                    result="af p r bk"
                else:
                    result="af p r movie"

            else: # class, done
                if medium=="Short Story":
                    result='"Fire on the Mountain" by Terry Bisson'
                elif medium=="Book":
                    result='"Kindred" by Octavia Butler'
                else:
                    result="af p c movie"

        elif time=="Present":
            if theme=="Gender/Sexuality":
                if medium=="Short Story":
                    result="af pr g/s ss"
                elif medium=="Book":
                    result="af pr g/s bk"
                else:
                    result="af pr g/s movie"

            elif theme=="Religion":
                if medium=="Short Story":
                    result='"Black Angel" by Walidah Imarisha'
                elif medium=="Book":
                    result="af pr r bk"
                else:
                    result="af pr r movie"

            else: # class, done
                if medium=="Short Story":
                    result='"the river" by adrienne maree brown'
                elif medium=="Book":
                    result='"Aftermath" by LeVar Burton'
                else:
                    result='"See You Yesterday" dir. Stefon Bristol'

        else: # future, done
            if theme=="Gender/Sexuality":
                if medium=="Short Story":
                    result='"Manhunters" by Kalamu ya Salaam'
                elif medium=="Book":
                    result='"Trouble on Triton: An Ambiguous Heterotopia" by Samuel R. Delany'
                else:
                    result="af f g/s movie"

            elif theme=="Religion":
                if medium=="Short Story":
                    result="af f r ss"
                elif medium=="Book":
                    result='"Parable of the Sower" by Octavia Butler'
                else:
                    result="af f r movie"

            else: # class, done
                if medium=="Short Story":
                    result='"The Ones Who Stay and Fight" by N.K. Jemisin'
                elif medium=="Book":
                    result='"Race After Technology" by Ruha Benjamin'
                else:
                    result="af f c movie"


    elif genre=="Africanfuturism":
        if time=="Past":
            result="Africanfuturism"
            return render_template("exploreapology.html", result=result)

        elif time=="Present": #done
            if theme=="Gender/Sexuality":
                if medium=="Short Story":
                    result='"Egoli" by T.L. Hutchu'
                elif medium=="Book":
                    result='"Lagoon" by Nnedi Okorafor'
                else:
                    result="afr pr g/s movie"

            elif theme=="Religion":
                if medium=="Short Story":
                    result='"Sunrise" by Nnedi Okorafor'
                elif medium=="Book":
                    result='"Lagoon" by Nnedi Okorafor'
                else:
                    result="afr pr r movie"

            else: # class
                if medium=="Short Story":
                    result='"Yat Madit" by Dilman Dila'
                elif medium=="Book":
                    result='"Pet" by Akwaeke Emezi'
                else:
                    result='"The Last Angel of History" dir. by John Akomfrah'

        else: # future, done
            if theme=="Gender/Sexuality":
                if medium=="Short Story":
                    result='"Fruit of the Calabash" by Rafeeat Aliyu'
                elif medium=="Book":
                    result='"War Girls" by Tochi Onyebuchi'
                else:
                    result="afr f g/s movie"

            elif theme=="Religion":
                if medium=="Short Story":
                    result='"Sunrise" by Nnedi Okorafor'
                elif medium=="Book":
                    result="afr f r bk"
                else:
                    result='"Pumzi" dir. by Wanuri Kahiu'

            else: # class
                if medium=="Short Story":
                    result='"Fort Kwame" by Derek Lubangakene'
                elif medium=="Book":
                    result='"The Rape of Shavi" by Buchi Emecheta'
                else:
                    result='"The Last Angel of History" dir. by John Akomfrah'


    else: # "Africanjujuism"
        if time=="Past":
            result="Africanjujuism"
            return render_template("exploreapology.html", result=result)

        elif time=="Present":
            if theme=="Gender/Sexuality":
                if medium=="Short Story":
                    result="juju pr g/s ss"
                elif medium=="Book":
                    result='"The Deep" by Rivers Solomon'
                else:
                    result="juju pr g/s movie"

            elif theme=="Religion":
                if medium=="Short Story":
                    result="juju pr r ss"
                elif medium=="Book":
                    result='"Children of Blood and Bone" by Tomi Adeyemi'
                else:
                    result="juju pr r movie"

            else: # class
                if medium=="Short Story":
                    result="juju pr c ss"
                elif medium=="Book":
                    result='"Pet" by Akwaeke Emezi'
                else:
                    result='The Last Angel of History" dir. by John Akomfrah'

        else: # future
            if theme=="Gender/Sexuality":
                if medium=="Short Story":
                    result="juju f g/s ss"
                elif medium=="Book":
                    result='"The Deep" by Rivers Solomon'
                else:
                    result="juju f g/s movie"

            elif theme=="Religion":
                if medium=="Short Story":
                    result="juju f r ss"
                elif medium=="Book":
                    result='"Children of Blood and Bone" by Tomi Adeyemi'
                else:
                    result="juju f r movie"

            else: # class
                if medium=="Short Story":
                    result="juju f c ss"
                elif medium=="Book":
                    result='"Zoo City" by Lauren Beukes'
                else:
                    result="juju f c movie"


    return render_template("result.html", result=result)

@app.route("/diaspora")
def diaspora():
    """African Diaspora in Africanfuturism"""
    return render_template("diaspora.html")


@app.route("/about")
def about():
    """About Me/Classes"""
    return render_template("about.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
