from application import app
from flask import Flask, render_template, redirect, url_for
from application.model.entity.documento import Documentos


@app.route("/")
def index():
    return render_template("pagtest2.html")