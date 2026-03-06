from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Guide(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), unique=False)
  content = db.Column(db.String(144), unique=False)

  def __init__(self, title, content):
    self.title = title
    self.content = content

# # Este codigo de profe se cambio, ya no es correcto
# class GuideSchema(ma.Schema):
#   class Meta:
#     field = ("id","title", "content")

class GuideSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Guide
        load_instance = True


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)

# End point for CREATE new entry
@app.route("/guide", methods=["POST"])
def add_guide():
  title = request.json["title"]
  content = request.json["content"]

  new_guide = Guide(title, content)

  db.session.add(new_guide)
  db.session.commit()

  guide = Guide.query.get(new_guide.id)
  return guide_schema.jsonify(guide)

# Endpoint to GET ALL ENTREES
@app.route("/guides", methods=["GET"] )
def get_guides():
   all_guides = Guide.query.all()
   result = guides_schema.dump(all_guides)
   return jsonify(result)

# Endpoint for GET single guide
@app.route("/guide/<id>", methods=["GET"] )
def get_guide(id):
   guide = Guide.query.get(id)
   return guide_schema.jsonify(guide)

# Endpoint to edit entree with "PUT"
@app.route("/guide/<id>", methods=["PUT"])
def update_guide(id):
   guide = Guide.query.get(id)
   title = request.json["title"]
   content = request.json["content"]

   guide.title = title
   guide.content = content

   db.session.commit()
   return guide_schema.jsonify(guide)



if __name__ == "__main__":
  app.run(debug=True)

# ### ESO HAY QUE EJECUTAR EN TERMINAL PARA QUE SE CREA la "APP.SQLITE" FILE Y SE CREA/actualiza la SQL SCHEMA
# python3
# from app import app, db
# with app.app_context():
#     db.create_all()
