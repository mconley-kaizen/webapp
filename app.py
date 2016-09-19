import importlib, sys
from flask import Flask, request, render_template, jsonify
#import mymodel -- in __main__ function

app = Flask(__name__)

@app.route("/")
def index():
    args = parse_args(mymodel.main)
    return render_template('index.html', arguments=args)

@app.route('/response', methods=['GET', 'POST'])
def response():
    args = request.args
    try:
        data = {key: float(args[key]) if args[key] else False for key in args}
        if all(data.values()):
            result = mymethod(**data)
        else:
            result = 'Enter data!'
    except Exception as e:
        result = repr(e)
    
    return jsonify({'result': result})

def parse_args(function):
    param_count = function.func_code.co_argcount
    params = function.func_code.co_varnames
    args = params[:param_count]
    args = [{'id': arg, 'prompt': 'Enter {}'.format(arg)} for arg in args]
    return args


if __name__ == "__main__":
    port = int(sys.argv[1])
    package = sys.argv[2]
    method_name = sys.argv[3]

    mymodel = importlib.import_module(package)
    mymethod = getattr(mymodel, method_name)

    app.run(host='0.0.0.0', port=port)
