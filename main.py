from flask import Flask, render_template, request
from lcm import find_lcm

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/lcm')
def my_form():
    return render_template('my-form.html')

@app.route('/lcm', methods=['POST'])
def my_form_post():
    text = request.form['text']
    print(type(text))
    a_list = text.split(",")
    
    numbers = []
    
    for i in a_list:
        numbers.append(int(i.replace(" ", "")))

    result = find_lcm(numbers)
    
    result = str(result)
    output = "LCM : " + result
    print(output)
    
    return output

@app.route("/")
def krishna():
    return {
            "message" : "Hare Krishna !"
            }


# @app.route("/thor", methods=['POST','GET'])
# def odin_list():
#     t= request.args.get('Type','')
#     print(t)
#     if t =='cr':
#         return cr+crf
#     else:
#         return 'Invalid input'
    
# cr= "A Reaction in which two or more products combine to form a single product is known as combination reaction"
# crf = "CaO+u'H\u2082O'='Ca(OH)\u2082'+heat"
#
# dr= " A reaction in which a single reactant breaks down to form two or more products is known as decomposition reaction"
#
# disr= " It is atype of reaction in which an element reacts with a compound and takes place of the another element in that compound is known as single displacement reaction"
#
# ddrect = "The reaction in which two different ions or group of atoms in the reactant molecules are diaplaced by each other is called double dispalcement reaction"
