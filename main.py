from website import app

from tryflask.api import api

app.register_blueprint(api,url_prefix="/api")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False, port="5000")
