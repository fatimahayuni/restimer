from datetime import *
from breaktime_str_to_datetime_module import *
import mysql.connector


elements_csvdata = []


def weekly_schedule(row_index):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="restime"
    )
    cursor = db.cursor()


    sql = "INSERT INTO schedules (date, agent_name, start, first_break, meal, second_break, end) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    for day in range(5):
        col_index = 1 + (6 * day)
        date_string = elements_csvdata[row_index - 1][col_index]
        date_formatted = datetime.strptime(date_string, "%d %b %y")
        print(date_formatted)
        

        for agent in range(11):
            agent_name = elements_csvdata[row_index + agent][col_index]
            print(agent_name)

            start_time_string = elements_csvdata[row_index + agent][col_index + 1]
            start_time_formatted = breaktime_str_to_datetime(date_string, start_time_string)
            
            first_break_string = elements_csvdata[row_index + agent][col_index + 2]
            first_break_formatted = breaktime_str_to_datetime(date_string, first_break_string)
            print(first_break_formatted)

            meal_string = elements_csvdata[row_index + agent][col_index + 3]
            meal_formatted = breaktime_str_to_datetime(date_string, meal_string)
            print(meal_formatted)

            second_break_string = elements_csvdata[row_index + agent][col_index + 4]
            second_break_formatted = breaktime_str_to_datetime(date_string, second_break_string)
            print(second_break_formatted)

            end_time_string = elements_csvdata[row_index + agent][col_index + 5]
            end_time_formatted = breaktime_str_to_datetime(date_string, end_time_string)
            print(end_time_formatted)

            val = (
                date_formatted,
                agent_name, 
                start_time_formatted, 
                first_break_formatted, 
                meal_formatted, 
                second_break_formatted, 
                end_time_formatted
                )

            cursor.execute(sql, val)

            db.commit()

    cursor.close()
    db.close()

           
