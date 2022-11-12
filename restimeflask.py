from flask import Flask, render_template, request
import mysql.connector
from weekly_schedule_module import *

app = Flask(__name__)

@app.route("/upload", methods=['GET'])
def upload():
    return render_template("upload.html")

@app.route("/schedule", methods=['POST'])
def schedule():
    uploaded_file = request.files['filename']
    csvdata = uploaded_file.read()

    string_csvdata = str(csvdata)

    list_csvdata = string_csvdata.split("\\r\\n")

    for index in range(0,73):
        split_listcsvdata = list_csvdata[index].split(",")
        elements_csvdata.append(split_listcsvdata)


    weekly_schedule(3)
    weekly_schedule(18)
    weekly_schedule(32)
    weekly_schedule(47)
    weekly_schedule(61)

    return "Thanks for the file!"

"""This runs the GET TIMES button in AgentFetch.html"""
@app.route("/times", methods=['GET'])
def times():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="restime"
    )
    cursor = db.cursor()

    agent = request.args.get("agent")
    date = request.args.get("date")

    val = (agent, date)

    cursor.execute("SELECT start, first_break, meal, second_break, end FROM schedules WHERE agent_name = %s AND date =%s", val)

    result = cursor.fetchall()

    cursor.close()
    db.close()

    return result

@app.route("/timer_test", methods=['GET'])
def timer_test():
    return render_template("AgentFetch.html")


app.run(host='0.0.0.0', port=8080)

