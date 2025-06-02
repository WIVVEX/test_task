from flask import Flask, render_template, request, redirect, jsonify
from req import weather, icon
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    num = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'num': self.num}



@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None

    
    city_name = request.form.get('city')


    weather_data = weather(city_name)
    if weather_data == "error":
        return redirect("/error")
    icon_path = icon(weather_data["description"])


    if city_name: 
        city_name = city_name.title()
        existing_city = City.query.filter_by(city=city_name).first()
        if existing_city:
            existing_city.num += 1
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                redirect ("/error")
        else:
            new_city = City(city=city_name.title(), num=1)
            try:
                db.session.add(new_city)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                redirect("/error")

    return render_template("index.html", wd = weather_data, icon_path = icon_path)

@app.route("/stats")
def stats():
    cities = City.query.all()
    return render_template("stats.html", cities = cities)





@app.route("/error")
def error():
    return render_template("error.html")



@app.route("/api")
def apii():
    return render_template("api.html")




class Main(Resource):
    def get(self, name):
        if name == "all":
            cities = City.query.all()
            return jsonify([city.to_dict() for city in cities])
        else:
            city = City.query.filter_by(city=name).first()
            if city:
                return jsonify(city.to_dict())
            else:
                return {"error": "City not found"}, 404
api.add_resource(Main, "/api/cities/<name>")
api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=3213, host="127.0.0.1")