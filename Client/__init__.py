from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
@app.route('/<string:page_name>/')
def render_static(page_name):
return render_template('%s.html' % page_name)</string:page_name>






if __name__ == '__main__':
   app.run()

