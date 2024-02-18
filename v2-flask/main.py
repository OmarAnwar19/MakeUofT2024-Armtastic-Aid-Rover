from flask import Flask, render_template
from mobility import mobility
from arm import arm

app = Flask(__name__)
app.register_blueprint(mobility)
app.register_blueprint(arm)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    arm.init()
    app.run(debug=True)