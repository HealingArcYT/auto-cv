import pdfkit

from graphics import AbfrageApp

options = {
    "page-size": "A4",
    "margin-top": "20mm",
    "margin-right": "20mm",
    "margin-left": "20mm",
    "margin-bottom": "20mm",
    "encoding": "utf-8",
    "no-outline": None
}

with open("cv.html", "r", encoding="utf-8") as file:
    cv = file.read()

app = AbfrageApp(cv)
app.run()

pdfkit.from_string(cv, "out.pdf", options=options, css="stylesheet.css")
