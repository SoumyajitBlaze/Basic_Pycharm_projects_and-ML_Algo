from flask import Flask,request,jsonify,render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/',methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def index1():
    return render_template('index1.html')


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

    '''add->POST......search->GET....update->PUT....Delete->DELETE'''