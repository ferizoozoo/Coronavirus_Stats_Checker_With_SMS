import ghasedak
from flask import Flask
from scraper import eachCountry
import os

app = Flask(__name__)
sms = ghasedak.Ghasedak(os.environ.get('SMS_API_KEY', ' '))

@app.route('/stats/<country>')
def getCountryStats(country):
    """Return the statistics of each country.
    """
    countryStats = eachCountry(country)
    sms.send({
        'message': countryStat['Deaths'],
        'receptor': '09056368477',
        'linenumber': '10008566'
        })
    return 'SMS sent.'