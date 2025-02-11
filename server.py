''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from sentiment_analysis import sentiment_analyzer

app = Flask(__name__)


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    body = request.args.get('textToAnalyze')
    if not body:
        return ({'message': 'Parameter not found'}, 400)

    result = sentiment_analyzer(body.strip())
    print(result)
    return {result}


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''  # TODO
    app.run(debug=True, port=5000)
