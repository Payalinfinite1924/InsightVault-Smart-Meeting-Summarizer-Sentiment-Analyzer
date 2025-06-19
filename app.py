from flask import Flask, render_template, request
import os
from summarize import process_meeting

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
LOG_FOLDER = 'meeting_logs'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['meeting']
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            report = process_meeting(path)
            return render_template('index.html', report=report, uploaded=True)
    return render_template('index.html', uploaded=False)

if __name__ == '__main__':
    app.run(debug=True)
