from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

from application import routes


