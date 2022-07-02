'''
Hare Krishna
May the lord Krishna bless us to enlightment
Jai Shri Krishna
'''

from flask import Flask, render_template, request
from lcm import find_lcm

app = Flask(__name__)


@app.route("/")
def krishna():
    return render_template('hello.html')

@app.route('/lcm')
def my_form():
    return render_template('my-form.html')

@app.route('/lcm', methods=['POST'])
def my_form_post():
    text = request.form['text']
    a_list = text.split(",")
    
    numbers = []
    
    for i in a_list:
        numbers.append(int(i.replace(" ", "")))

    result = find_lcm(numbers)
    
    lcm = str(result)
    return render_template('result.html', result=lcm)

