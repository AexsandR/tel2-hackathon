from flask import *
from data import db_session
from flask_restful import reqparse, abort, Api, Resource
from api_tele2 import Api_tele2
import requests
from data.__all_models import *


app = Flask(__name__)
api = Api(app)
app.config[
    'SECRET_KEY'] = "7fm0UzncQc?CVjxdYePDPz=ydg!-LKIw9u8z20hRsxWTwiGjnxFZVsiy1deUIINzbgJqk48yUpR6zn=v8k2zCqO099bTc" \
                    "!4!chtyIAMbB5-ld/zCezXakibhMuOEDT62qYVIhuD26gk7ICVoW8sCooojso6XVgI/8Usvr9IcIalP-Gse0MN=B5kpvQm" \
                    "U/?leMB7D/Hw1mlDDs9e?vZwF-xSjeCssGfZNHq?cNcQJx1zc6uJEK0qffpxT!vy1vvyg"


@app.before_request
def search():
    if request.method == 'POST':
        if 'tildaspec-phone-part[]' in request.form:
            db_sess = db_session.create_session()
            number = "8" + request.form['tildaspec-phone-part[]']
            try:
                user = db_sess.query(Users).filter(Users.number == int(number)).first()
            except Exception as er:
                ...
            else:
                return redirect(f"/statics/8{request.form['tildaspec-phone-part[]']}")


@app.route("/", methods=['GET', 'POST'])
def main_page():
    return render_template('TELE 2.html')


@app.route("/statics/<int:number>")
def number_page(number):
    print(f"http://127.0.0.1:5000/api_tele2/{number}")
    res = requests.get(f"http://127.0.0.1:5000/api_tele2/{number}").json()
    text = ""
    if res['buy_gb'] != 0 or res['buy_min'] != 0:
        text = "Для наибольшей выгоды к тарифу вам нужно купить следующие услуги"
        if res['buy_gb']:
            text += f"\n {res['buy_gb']} гб"
            if res['buy_min'] != 0:
                text += f" и {res['buy_min']} мин"
        else:
            text += f"\n {res['buy_min']} мин"

    return render_template(f"{res['tariff'].lower()}.html", name=res['name'], gigs=res['gigabyte'],
                           minutes=res['minutes'],
                           text=text)


if __name__ == "__main__":
    db_session.global_init("db/database.db")
    parser = reqparse.RequestParser()
    parser.add_argument("number", required=True, type=int)
    api.add_resource(Api_tele2, "/api_tele2/<int:number>")
    app.run()
    # http://127.0.0.1:5000/api_tele2/89092556770
