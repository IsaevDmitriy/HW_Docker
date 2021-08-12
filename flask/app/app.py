from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)


class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    header = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)

    def __str__(self):
        return '<Advertisement {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            "header": self.header,
            'definition': self.definition,
            'created_on': self.created_on
        }

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


@app.route('/api/get/<int:advertisement_id>', methods=['GET', ])
def get_adv(advertisement_id):
    advertisement = Advertisement.query.get(advertisement_id)
    return jsonify(advertisement.to_dict())



@app.route('/api/post', methods=['POST', ])
def post_adv():
    advertisement = Advertisement(**request.json)
    try:
        db.session.add(advertisement)
        db.session.commit()
        return jsonify(advertisement.to_dict())
    except:
        return 'Ошибка'


@app.route('/api/delete/<int:advertisement_id>', methods=['DELETE', ])
def delete_adv(advertisement_id):
    advertisement = Advertisement.query.get(advertisement_id)
    try:
        db.session.delete(advertisement)
        db.session.commit()
        return jsonify(advertisement.to_dict())
    except:
        return 'Ошибка'


@app.route('/api/patch/<int:advertisement_id>', methods=['PATCH', ])
def patch_adv(advertisement_id):
    advertisement = Advertisement.query.get(advertisement_id)
    advertisement.update(**request.json)
    try:
        db.session.commit()
        return jsonify(advertisement.to_dict())
    except:
        return 'Ошибка'


@app.route('/')
def home():
    return 'Оk!'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)