from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def start():
    return "Стартовая страница"


#@app.route('/list')
#def main_list():
#    return "List-list"


@app.route("/notes/personal")
def personal_list():
    return jsonify({"key": 1, "title:": "TitlePersonal1", "text": "фафафа", "dateOfAdding": "12.05.2019"},
                   {"key": 2, "title:": "TitlePersonal2", "text": "Text2", "dateOfAdding": "13.07.2019"},
                   {"key": 3, "title:": "TitlePersonal3", "text": "JSON IT'S JSON", "dateOfAdding": "14.06.2019"})


@app.route("/notes/work")
def work_list():
    return jsonify({"key": 1, "title:": "TitleWork1", "text": "SimpleText1", "dateOfAdding": "11.05.2019"},
                   {"key": 2, "title:": "TitleWork2", "text": "SimpleText2", "dateOfAdding": "14.07.2019"},
                   {"key": 3, "title:": "TitleWork3", "text": "JSON HAS BEEN JSON", "dateOfAdding": "15.06.2019"})


@app.route("/notes/archived")
def archived_list():
    return jsonify({"key": 1, "title:": "TitleArchive1", "text": "Text1", "dateOfAdding": "14.05.2019"},
                   {"key": 2, "title:": "TitleArchive2", "text": "Text2", "dateOfAdding": "15.07.2019"},
                   {"key": 3, "title:": "TitleArchive3", "text": "JSON WILL BE JSON", "dateOfAdding": "16.06.2019"})


app.run()
