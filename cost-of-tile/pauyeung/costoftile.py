#!/usr/bin/python

import cgi

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers


def ask():
    print '''
    <html>
        <form>
        <table>
            <tr><th><label for="Cost/sqft">Cost/sqft</label></th>
            <td><input type="text" id="Cost/sqft" name="Cost/sqft"/></td></tr>
            <tr><th><label for="Width">Width</label></th>
            <td><input type="text" id="Width" name="Width"/></td></tr>
            <tr><th><label for="Height">Height</label></th>
            <td><input type="text" id="Height" name="Height"/></td></tr>
        </table>
        <button type="submit">Submit Query</button>
        </form>
    </html>
    '''


def main():
    if 'Cost/sqft' in form:
        cost = form.getfirst('Cost/sqft')
        width = form.getfirst('Width')
        height = form.getfirst('Height')

        try:
            total = float(cost) * float(width) * float(height)
        except:
            total = 'error'

        ask()
        print 'Total cost of tiles: $', total
        print '</html>'

    else:
        ask()

if __name__ == "__main__":
        main()
