#!/usr/bin/python

import web
from web import form

render = web.template.render('templates/')


urls = ('/', 'index')

app = web.application(urls, globals())


myform = form.Form(
    form.Textbox("Cost/sqft"),
    form.Textbox("Width"),
    form.Textbox("Height"),
)


class index:
    def GET(self):
        form = myform()
        return render.formtest(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.formtest(form)
        else:
            cost = form['Cost/sqft'].value
            width = form['Width'].value
            height = form['Height'].value
            total = float(cost) * float(width) * float(height)
            return "%s  Total cost of tiles: $ %s" % (render.formtest(form), total)


if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
