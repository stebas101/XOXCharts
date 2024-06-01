from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev' # For development only - new key using secrets

from xox_pnf import routes