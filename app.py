from flask import Flask, request, render_template, jsonify, send_file, abort, redirect
from utils import *
import pandas as pd
from io import BytesIO
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
# TODO: Add Captcha, fix checkout.

app = Flask(__name__)
init_db()
API_KEY = os.getenv("API_KEY")
ADMIN_PASSWORD = os.getenv("PASSWORD")
ADMIN_USERNAME = os.getenv("USERNAME")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

def verify_recaptcha(response_token):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': SECRET_KEY,
        'response': response_token
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result.get('success')
def send_message_on_order(order, username):
    webhook = DiscordWebhook(WEBHOOK_URL, content=f"YAO JIN CHOONG!!!!!!!! A NEW ORDER HAS BEEN PLACED!!!, ORDER: {order}, USERNAME: {username}")
    embed = DiscordEmbed(title="Order", description="MOOLAH?!?!?!?!?!? 🤑💲💲💲🤑💲💲💰💸💸", color="FF0000")
    webhook.add_embed(embed=embed)
    webhook.execute()

def require_api_key():
    if request.headers.get('X-API-KEY') != API_KEY:
        ip_addr = request.remote_addr
        print(ip_addr)
        return f"This you lil bro? {ip_addr}"

@app.route("/gotologin")
def redirecttologin():
    return redirect("/login")

def retrieve_data():
    with get_conn() as conn:
       cursor = conn.cursor()
       cursor.execute("SELECT * FROM orders")
       rows = cursor.fetchall()
       jsondata = {index: item for index, item in enumerate(rows)}
    return jsonify(jsondata)


@app.route("/squidward", methods=["GET"])
def squidward():
    squidward_handsome = r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣤⣄⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡤⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠀⡀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠘⡆⡜⠁⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⣀⣤⡂⠀⠇⠱⠀⡀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⡀⢠⣟⢭⣥⣤⠽⡆⠀⡶⣊⣉⣲⣤⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⡀⠀⠐⠂⠘⠄⣈⣙⡡⡴⠀⠀⠙⣄⠙⣛⠜⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠄⠊⠀⠀⠀⠀⡸⠛⠀⠀⠀⢸⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⢄⣘⣄⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⣇⡀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠈⡟⠒⠲⣄⠀⠀⡰⠇⠖⢄⠀⠀⡹⡇⢀⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⡇⠀⠀⠹⠀⡞⠀⠀⢀⠤⣍⠭⡀⢱⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⠞⠀⠀⢠⡇⠀⠀⠀⠀⠁⠀⢴⠥⠤⠦⠦⡼⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣤⣴⣶⣿⣿⡟⠁⠀⠋⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠑⣠⢤⠐⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠬⠥⣄⠀⠀⠈⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⢀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠦⠤⢤⣄⣀⣠⠤⢿⣶⣶⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀


        """
    return f"{squidward_handsome}, Yes, you're on the right page."

# admin stuff
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        realhashusername = hash(ADMIN_USERNAME)
        realhashpassword = hash(ADMIN_PASSWORD)
        try:
            if verify(username, realhashusername) and verify(password, realhashpassword):
                return render_template("info.html", info=f"Your API Key is {API_KEY}, ask the dev on how to use it.")
        except Exception as e:
            return render_template("login.html", error="Incorrect Username/Password")
    return render_template("login.html")

@app.route("/excel", methods=["GET"])
def retrieve_and_save_data_as_excel():
    """
    note: to use this u gotta use the requests module with this code: 
    url = "thedomain.com/excel"
    or:
    url = "thedomain.com/json"
    # Headers with API key
    headers = {
    	"X-API-KEY": "your_secret_api_key"
    }

    # Send GET request
    response = requests.get(url, headers=headers)

    # Print response
    print(response.status_code)
    print(response.text)  
    """
    require_api_key()
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=["id", "order"])
        excelfile = BytesIO()
        df.to_excel(excelfile, index=False)
        excelfile.seek(0)  # Move to the beginning of the file after writing
    return send_file(
        excelfile,
        as_attachment=True,
        download_name="data.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.route("/json", methods=["GET"])
def get_data_json():
    require_api_key()
    return retrieve_data()

@app.route("/checkout", methods=["POST"])
def checkout():
    response_token = request.form.get('g-recaptcha-response')
    if verify_recaptcha(response_token):     
        json_data = request.form.get("body")
        print(json_data)
        try:
            insert_order(json_data)
            send_message_on_order(json_data)
        except Exception as e:
            return render_template("info.html", info="Error while submitting.")
    else:
        return render_template("info.html", info="Invalid Captcha")
    
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)