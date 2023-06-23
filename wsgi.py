from api.app import app

if __name__ == "__main__":
    app.run()
    

#run = app.create_app()
#print(run.url_map)
#run.run()

# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# run = Flask(__name__)

# db_uri = 'mysql+pymysql://flaskuser:flaskpass@localhost/flasktest?charset=utf8mb4'
# run.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# db = SQLAlchemy(run)

# class Item(db.Model):
#     __tablename__ = 'item'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.Text())
#     price = db.Column(db.Integer)


# @run.route("/")
# @run.route("/index")
# def index():
#     name = request.args.get('name')
#     books = ["化学", "物理", "数学", "情報"]
#     items = Item.query.all()
#     return render_template("index.html", name = name, books = books, items = items)

# @run.route("/index", methods=["post"])
# def post():
#     name = request.form["name"]
#     books = ["化学", "物理", "数学", "情報"]
#     return render_template("index.html", name = name, books = books)


# if __name__ == "__main__":
#     run.run(debug=True)