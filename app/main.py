from flask import Flask, render_template, jsonify      

app = Flask(__name__)

page = [
    {
        'id': 1,
        'title': u'page-one',
        'success': u'true'
    }
]
@app.route("/")
def home():
    return render_template("page-one.html")
    
@app.route("/page-two")
def page_two():
    return render_template("page-two.html")

@app.route('/api/page', methods=['GET'])
def get_tasks():
    return jsonify({'page': page})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)