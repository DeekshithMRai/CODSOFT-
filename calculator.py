from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json['expression']
    try:
        result = eval(expression)
    except:
        result = 'Error'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
