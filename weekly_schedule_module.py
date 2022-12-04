from datetime import *
from breaktime_str_to_datetime_module import *
import mysql.connector


elements_csvdata = []

"""Data parsing is done here."""
def weekly_schedule(row_index, cursor):

    sql = "INSERT INTO schedules (date, agent_name, start, first_break, meal, second_break, end) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    for day in range(5):
        col_index = 1 + (6 * day)
        date_string = elements_csvdata[row_index - 1][col_index]
        try:
            date_formatted = datetime.strptime(date_string, "%d %b %y")
        except:
            return "The program died here at the DATE cell."
        # else:
        #     week_ok = f"Week {} OK."


        for agent in range(11):
            # AGENT NAME
            agent_name = elements_csvdata[row_index + agent][col_index]





            # START TIME
            start_time_string = elements_csvdata[row_index + agent][col_index + 1]
            try:
                start_time_formatted = breaktime_str_to_datetime(date_string, start_time_string)
            except:
                start_time_error_message = f"Bad data found in START cell: {[col_index + 1 ,row_index + agent]}."
                return start_time_error_message
            




            # FIRST BREAK
            first_break_string = elements_csvdata[row_index + agent][col_index + 2]
            try: 
                first_break_formatted = breaktime_str_to_datetime(date_string, first_break_string)
            except:
                "Split the numeric coord [9, 10] to 2 parts: [9] and [10]"
                first_part = col_index + 2
                second_part = row_index + agent

                "Take first_part of the numeric coord and convert it to alphabets"
                alphabets = ["A", "B", "C", "D", "E", "F" ,"G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE"]
                alpha_coord = alphabets[first_part]
            
                "Take second_part of the numeric_coord and + 1"
                num_coord = second_part
                alphanum_first_break_error_coord = [alpha_coord, num_coord + 1]
                alphanum_first_break_error_coord_str = ""
                for ele in alphanum_first_break_error_coord:
                    alphanum_first_break_error_coord_str += str(ele) + ""
                first_break_error_message = f"Bad data found in FIRST BREAK cell: {alphanum_first_break_error_coord_str}."
                return first_break_error_message




            # MEAL TIME
            meal_string = elements_csvdata[row_index + agent][col_index + 3]
            try:
                meal_formatted = breaktime_str_to_datetime(date_string, meal_string)
            except:
                meal_time_error_message = f"Bad data found in MEAL TIME cell: {[col_index + 3 ,row_index + agent]}."
                return meal_time_error_message





            # SECOND BREAK
            second_break_string = elements_csvdata[row_index + agent][col_index + 4]
            try:
                second_break_formatted = breaktime_str_to_datetime(date_string, second_break_string)
            except:
                second_break_error_message = f"Bad data found in SECOND BREAK cell: {[col_index + 4 ,row_index + agent]}."
                return second_break_error_message





            # END TIME
            end_time_string = elements_csvdata[row_index + agent][col_index + 5]
            try:
                end_time_formatted = breaktime_str_to_datetime(date_string, end_time_string)
            except:
                end_time_error_message = f"Bad data found in END TIME cell: {[col_index + 5 ,row_index + agent]}."
                return end_time_error_message
        



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

    return "Week OK."

        
