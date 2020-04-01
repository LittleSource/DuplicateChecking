from flask import Flask, request, render_template ,json,jsonify
from core import Dataer
app = Flask(__name__)

dataer = Dataer()
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    str1 = request.form.get('word')
    befurl = request.form.get('befurl')
    floatRedLie = float(request.form.get('floatRedLie')) * 30
    strList = []
    for i in range(0,len(str1),30):
        strList.append(str1[i:i+30])
    if befurl == '1':
        return jsonify(dataer.baidu(strList,floatRedLie))
    elif befurl == '2':
        return jsonify(dataer.q360(strList,floatRedLie))
    else:
        return jsonify(dataer.sougou(strList,floatRedLie))
if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0', port=5000, debug = False)