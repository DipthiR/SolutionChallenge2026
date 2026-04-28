from flask import Flask, render_template, request
import pandas as pd
from bias import detect_bias
from utils import create_chart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']

    if not file:
        return "No file uploaded"

    df = pd.read_csv(file)

    result = detect_bias(df)

    chart_path = create_chart(result['group_stats'])

    return render_template(
        'result.html',
        result=result,
        chart=chart_path
    )

if __name__ == '__main__':
    app.run(debug=True)
