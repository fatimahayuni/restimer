import traceback
from flask import Flask, render_template, request
import mysql.connector
from weekly_schedule_module import *
import datetime

app = Flask(__name__)

"""Endpoint to return upload.html"""
@app.route("/upload", methods=['GET'])
def upload():
    return render_template("upload.html")

"""To save a file of csv data to pass to MySQL"""
@app.route("/schedule", methods=['POST'])
def schedule():
    try:
        uploaded_file = request.files['filename']
        csvdata = uploaded_file.read()

        string_csvdata = str(csvdata)

        list_csvdata = string_csvdata.split("\\r\\n")

        for index in range(0,73):
            split_listcsvdata = list_csvdata[index].split(",")
            elements_csvdata.append(split_listcsvdata)

        w1 = weekly_schedule(3)
        w2 = weekly_schedule(18)
        w3 = weekly_schedule(32)
        w4 = weekly_schedule(47)
        w5 = weekly_schedule(61)
        
        if w1 == "Week OK." and w2 == "Week OK." and w3 == "Week OK." and w4 == "Week OK." and w5 == "Week OK.":
            return "Thanks for uploading a good file."
        a = w1 + "\n" + w2 + "\n" + w3 + "\n" + w4 + "\n" + w5
        return a
        

    except Exception as e:
        my_string = str(e)
        print(my_string)
        traceback.print_exc()
        

"""This endpoint retrieves agent times from the database using the agent name and date sent from client."""
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

    val = (agent,date)

    """Agent and date name input"""
    cursor.execute("SELECT start, first_break, meal, second_break, end FROM schedules WHERE agent_name = %s AND date =%s", val)

    result = cursor.fetchall()
    [unpacked_list] = result
    (start_unpacked, first_break_unpacked, meal_unpacked, second_break_unpacked, end_unpacked) = unpacked_list
    
    unix_start_unpacked = datetime.datetime.timestamp(start_unpacked)
    unix_start_formatted = int(unix_start_unpacked)

    unix_first_break_unpacked = datetime.datetime.timestamp(first_break_unpacked)
    unix_first_break_formatted = int(unix_first_break_unpacked)

    unix_meal_unpacked = datetime.datetime.timestamp(meal_unpacked)
    unix_meal_formatted = int(unix_meal_unpacked)

    unix_second_break_unpacked = datetime.datetime.timestamp(second_break_unpacked)
    unix_second_break_formatted = int(unix_second_break_unpacked)

    unix_end_unpacked = datetime.datetime.timestamp(end_unpacked)
    unix_end_formatted = int(unix_end_unpacked)
  
    unix_all = [unix_start_formatted, unix_first_break_formatted, unix_meal_formatted, unix_second_break_formatted, unix_end_formatted]
    
    cursor.close()
    db.close()
    return unix_all


"""Endpoint to return AgentFetch.html"""
@app.route("/timer_test", methods=['GET'])
def timer_test():
    return render_template("AgentFetch.html")


app.run(host='0.0.0.0', port=8080)


