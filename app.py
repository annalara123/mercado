from flask import *
import dao

app = Flask(__name__)
app.secret_key = 'ASsadlkjasdAJS54$5sdSA21'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)