import os
import argparse
import json
import requests
import re
import pandas as pd
from ast import literal_eval

from flask import Flask, g, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from cdqa.utils.converters import pdf_converter
# from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline

app = Flask(__name__)

api = Api(app)
CORS(app)


@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

@app.errorhandler(500)
def raiseError(error):
    return error


class QASystem(Resource):
    def __init__(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', type=str, required=True)
        args = parser.parse_args()

        df = pdf_converter(directory_path='./data/pdf/')
        cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)

        cdqa_pipeline.fit_retriever(df=df)

        prediction = cdqa_pipeline.predict(args.query)

        return {
            'data': prediction
        }, 200

api.add_resource(QASystem, '/answer')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)