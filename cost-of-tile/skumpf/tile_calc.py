#!/usr/bin/env python2.7

from bottle import route, run, Bottle, request
import random

''' Define the app '''
tile_calc_app = Bottle()

@tile_calc_app.get('/')
@tile_calc_app.get('/tilecalc')
def main_page():
    ''' Display main form '''
    html = '''
           <h1>Welcome to Tile Calc</h1>
           <p>Enter the width, length, and price per unit</p>
           <form action="/tilecalc" method="post">
                Width: <input name="width" type="text" /><br /><br />
                Length: <input name="length" type="text" /><br /><br />
                Cost Per Unit: <input name="cost_per_unit" type="text" /><br /><br />
                <input value="Calculate" type="submit" />
            </form>
            <p>Testimonial from our customers: <i><b>%s</b></i></p>
            '''
    return html % get_cust_feedback()

@tile_calc_app.post('/')
@tile_calc_app.post('/tilecalc')
def result_page():
    ''' Display the error or results page '''
    try:
        width = float(request.forms.get('width'))
        length = float(request.forms.get('length'))
        cost_per_unit = float(request.forms.get('cost_per_unit'))
        html = '''
               <h2>Total cost: %s</h2>
               <a href="/">Go back</a>
               ''' % (width * length * cost_per_unit)

    except:
        html = '''
               <h1>ERROR: All inputs must be ints or floats</h1>
               <a href="/">Go back</a>
               '''
    return html

def get_cust_feedback():
    ''' Teen talk barbie really likes our app! '''
    cust_feedback = (
                      "Will we ever have enough clothes?",
                      "I love shopping!",
                      "Wanna have a pizza party?",
                      "Math class is tough!"
                    )
    return random.choice(cust_feedback)

''' Run the app '''
run(tile_calc_app, host='localhost', port=8081, debug=True)
