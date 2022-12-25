from flask_restful import *
from data import db_session
from data.__all_models import *
from price import price
from flask import jsonify


class Api_tele2(Resource):
    def get(self, number):
        prices_tariff = {
            1: 700,
            2: 500,
            3: 450,
            4: 400,
            5: 300,
            6: 890}
        db_sess = db_session.create_session()
        user = db_sess.query(Users).filter(Users.number == int(number)).first()
        print(user.id)
        statistic_user = db_sess.query(Statistics).filter(Statistics.id_users == user.id).first()
        tariff_user = db_sess.query(Tariffs).filter(Tariffs.id == statistic_user.id_tariff).first()
        spent = statistic_user.gigabyte
        if tariff_user.social:
            ...
        else:
            spent += statistic_user.social

        if tariff_user.messanger:
            ...
        else:
            spent += statistic_user.messanger

        if tariff_user.youtube:
            ...
        else:
            spent += statistic_user.internet
        res = []
        for i in range(1, 7):
            tariff = db_sess.query(Tariffs).filter(Tariffs.id == i).first()
            gb = tariff.gigabyte - statistic_user.gigabyte
            minutes = tariff.minutes - statistic_user.minutes
            res.append([gb, minutes, i])
        print(res)
        res = sorted(res, key=lambda x: x[0] and x[1])

        for i in res:
            tariff = db_sess.query(Tariffs).filter(Tariffs.id == i[2]).first()

            if tariff.social:
                ...
            else:
                i[0] -= statistic_user.social

            if tariff.messanger:
                ...
            else:
                i[0] -= statistic_user.messanger

            if tariff.youtube:
                ...
            else:
                i[0] -= statistic_user.internet
            balance = False
            if i[0] < 0:
                gb_plus = abs(i[0]) * 15
                if price(i[2]):
                    if i[2] != 1 and gb_plus < prices_tariff[price(i[2])] - prices_tariff[i[2]]:
                        i[0] = 0
                        i.append(gb_plus // 15)
                        balance = prices_tariff[price(i[2])] - prices_tariff[i[2]] - gb_plus
                    elif i[2] == 1:
                        i[0] = 0
                        i.append(gb_plus // 15)
            else:
                i.append(0)
            if i[1] < 0:
                if price(i[2]):
                    minutes = min_price = abs(i[1])
                    min_price = (lambda x: x - 1 if x % 10 == 5 else x)(min_price)
                    min_price = (lambda x: x + 1 if x % 10 == 9 else x)(min_price)
                    min_price = ((lambda x: 1 if min_price // 50 > 0 else 0)(i) * min_price - 40) + 40
                    min_price -= min_price // 10 * 2
                    if balance is False and balance != 0 and i[2] != 1:
                        if min_price < prices_tariff[price(i[2])] - prices_tariff[i[2]]:
                            i.append(minutes)
                            i[1] = 0
                    elif i[2] == 1:
                        i[1] = 0
                        i.append(minutes)
                    elif balance:
                        if balance >= min_price:
                            i[1] = 0
                            i.append(minutes)

            else:
                i.append(0)
        print(res)
        res = list(filter(lambda x: x[0] >= 0 and x[1] >= 0 and len(x) > 3, res))
        print(res)
        res = sorted(res, key=lambda x: x[0] and x[1] and x[3] and x[4])[0]
        print(res)

        tariff = db_sess.query(Tariffs).filter(Tariffs.id == res[2]).first()
        tariff_name = tariff.tariff

        return jsonify({"number": user.number,
                        'name': user.name,
                        'tariff': tariff_name,
                        'minutes': statistic_user.minutes,
                        'gigabyte': spent,
                        'buy_gb': res[-2],
                        'buy_min': res[-1]})
