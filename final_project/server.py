import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    fr_text = translator.englishtofrench(textToTranslate)
    return fr_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    en_text = translator.frenchtoenglish(textToTranslate)
    return en_text

@app.route("/")
def renderIndexPage():
    app.run(debug=True) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
