from flask import Flask
from flask import request
app = Flask(__name__)

def post_to_kintone(kw):
    import pykintone
    app = pykintone.app('mitou', '90', 'ry4O9PfUuPqoc0uQT75kXu5eaA5dpH6hM1o6Jo0U')
    from pykintone import model
    class Person(model.kintoneModel):
        def __init__(self, kw):
            super(Person, self).__init__()
            self.name = kw['name']
            self.name_en = kw['name_en']
            self.self_intro = kw['SelfIntroduction']
            self.interested_in = kw['InterestedIn']

    app.create(Person(kw))

@app.route("/api/", methods=["POST"])
def api():
    post_to_kintone(request.form)
    return "OK!"

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
