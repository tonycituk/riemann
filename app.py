from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
import riemann as rmnn
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('root.html')


@app.route('/mid')
def midpoint():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    n = int(request.args.get('n'))
    ax = float(request.args.get('ax'))
    bx = float(request.args.get('bx'))
    cx = float(request.args.get('cx'))
    d = float(request.args.get('d'))

    f = lambda x: ax*(x**3) + bx*(x**2) + cx*x + d
    res = rmnn.riemannsSumMidpoint(a, b, n, f)
    fig = px.line(x=res["xi"], y=res["yi"], title="Área total: "+str(res["totalArea"]))
    for i, y in enumerate(res["yi_midpoints"]):

        fig.add_shape(type="rect",
                      x0=res["xi"][i], y0=0, x1=res["xi"][i+1], y1=y,
                      line=dict(
                          color="RoyalBlue",
                          width=2,
                      ),
                      fillcolor="LightSkyBlue",
                      opacity=0.5)
    
    converted_list = [str(element) for element in res["xi"]]
    elementosParticion = ", ".join(converted_list)

    converted_list = [str(element) for element in res["x_midpoints"]]
    puntosMedios = ", ".join(converted_list)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('notdash.html', graphJSON=graphJSON, title="Punto Medio", color="is-link", elementosParticion=elementosParticion, puntosMedios=puntosMedios, dx=str(res["dx"]))

@app.route('/left')
def leftpoint():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    n = int(request.args.get('n'))
    ax = float(request.args.get('ax'))
    bx = float(request.args.get('bx'))
    cx = float(request.args.get('cx'))
    d = float(request.args.get('d'))

    f = lambda x: ax*(x**3) + bx*(x**2) + cx*x + d
    res = rmnn.riemannsSumLeftpoint(a, b, n, f)
    fig = px.line(x=res["xi"], y=res["yi"], title="Área total: "+str(res["totalArea"]))
    for i, y in enumerate(res["yi_leftpoints"]):

        fig.add_shape(type="rect",
                      x0=res["xi"][i], y0=0, x1=res["xi"][i+1], y1=y,
                      line=dict(
                          color="RoyalBlue",
                          width=2,
                      ),
                      fillcolor="LightSkyBlue",
                      opacity=0.5)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('notdash.html', graphJSON=graphJSON, title="Por la izquierda", color="is-warning")

@app.route('/right')
def rightpoint():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    n = int(request.args.get('n'))
    ax = float(request.args.get('ax'))
    bx = float(request.args.get('bx'))
    cx = float(request.args.get('cx'))
    d = float(request.args.get('d'))

    f = lambda x: ax*(x**3) + bx*(x**2) + cx*x + d
    res = rmnn.riemannsSumRightpoint(a, b, n, f)
    fig = px.line(x=res["xi"], y=res["yi"], title="Área total: "+str(res["totalArea"]))
    for i, y in enumerate(res["yi_rightpoints"]):

        fig.add_shape(type="rect",
                      x0=res["xi"][i], y0=0, x1=res["xi"][i+1], y1=y,
                      line=dict(
                          color="RoyalBlue",
                          width=2,
                      ),
                      fillcolor="LightSkyBlue",
                      opacity=0.5)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('notdash.html', graphJSON=graphJSON, title="Por la derecha", color="is-primary")
