from app import app
from app.models import Accounts, Account_History

@app.route("/")
@app.route("/home")
def home():
    return 'hello world'