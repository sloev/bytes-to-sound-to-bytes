from flask import Flask, request, render_template
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static' ,template_folder='.', static_folder = ".")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

import time


@app.route("/")
def hello():

    return render_template('index.html', time=time.time())


if __name__ == "__main__":
    app.run()