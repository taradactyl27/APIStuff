from flask import Flask, render_template
import json, urllib2

myapp = Flask(__name__)
url = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=jz8lQAEvIoLQ0hYmCHT8b6kTBkKRzu2jDW2UsOk9")
jcode = json.loads(url.read())
@myapp.route('/')
def root():
    return render_template('template.html', stuff = jcode["explanation"], picture = jcode["url"])

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
