import os

from flask import Flask
from requests import get

app = Flask(__name__)


@app.route('/')
def check_myip():
    response = get("http://ifconfig.io/ip")
    return 'My ip address is {} \n'.format(response.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
