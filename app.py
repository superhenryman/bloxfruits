from flask import Flask, request, render_template, jsonify, send_file, abort
from utils import *
import pandas as pd
from io import BytesIO
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
app = Flask(__name__)
init_db()
API_KEY = os.getenv("API_KEY")
ADMIN_PASSWORD = os.getenv("PASSWORD")
ADMIN_USERNAME = os.getenv("USERNAME")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
def send_message_on_order(order, username):
    webhook = DiscordWebhook(WEBHOOK_URL, content=f"YAO JIN CHOONG!!!!!!!! A NEW ORDER HAS BEEN PLACED!!!, ORDER: {order}, USERNAME: {username}")
    embed = DiscordEmbed(title="Order", description="MOOLAH?!?!?!?!?!? 🤑💲💲💲🤑💲💲💰💸💸", color="FF0000")
    webhook.add_embed(embed=embed)
    webhook.execute()
def require_api_key():
    if request.headers.get('X-API-KEY') != API_KEY:
        ip_addr = request.remote_addr
        print(f"Dumbass forgot his API Key, here's his ip: {ip_addr}")
        abort(403)

def retrieve_data():
    with get_conn() as conn:
       cursor = conn.cursor()
       cursor.execute("SELECT * FROM orders")
       rows = cursor.fetchall()
       jsondata = {index: item for index, item in enumerate(rows)}
    return jsonify(jsondata)

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        json_data = request.form.get("body")
        try:
            insert_order(json_data)
            send_message_on_order(json_data)
        except Exception as e:
            print("Error! Cannot do shit." + e)
        return render_template("info.html", info="Submitted!!!")
    return render_template("index.html")
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
    return f"{squidward}, Yes, you're on the right page."
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
                # login
                pass
        except Exception as e:
            return render_template("login.html", error="Incorrect Username/Password")

        return render_template("info.html", info=f"Your API Key is {API_KEY}, ask the dev on how to use it.")
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
        excelfile = df.to_excel()
        filestream = BytesIO(excelfile.encode())
        return send_file(filestream, None, as_attachment=True, download_name="orders.xlsx")

@app.route("/json", methods=["GET"])
def get_data_json():
    require_api_key()
    return jsonify(retrieve_data())

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)