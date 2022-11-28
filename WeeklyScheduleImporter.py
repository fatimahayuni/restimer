from datetime import *
from breaktime_str_to_datetime_module import *
import mysql.connector


class WeeklyScheduleImporter:
    # data = list object containing the csv data uploaded from browser.
    def __init__(self, data):
        self.csv_data = data
        self.db = None
        self.cursor = None
        self.convert_num_to_alpha = None

    def weekly_schedule(self, row_index):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="restime"
        )
        self.cursor = self.db.cursor()

        sql = "INSERT INTO schedules (date, agent_name, start, first_break, meal, second_break, end) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        for day in range(5):
            col_index = 1 + (6 * day)
            date_string = self.csv_data[row_index - 1][col_index]
            try:
                date_formatted = datetime.strptime(date_string, "%d %b %y")
            except:
                self.cursor_db_close()
                return "The program died here at the DATE cell."


            for agent in range(11):
                agent_name = self.csv_data[row_index + agent][col_index]

                start_time_string = self.csv_data[row_index + agent][col_index + 1]
                try:
                    start_time_formatted = breaktime_str_to_datetime(date_string, start_time_string)
                except:
                    "Split the numeric coord to 2 parts."
                    first_part = col_index + 1
                    second_part = row_index + agent

                    # Take first_part of the numeric coord and convert it to alphabets
                    self.convert_num_to_alpha(0)

                    # Take second part of the numeric_coord and + 1"
                    num_coord = second_part
                    alphanum_start_time_error_coord = [alpha_coord, num_coord + 1]

                    # Converting the resulting alphanum list to string and printed line by line in terminal.
                    alphanum_start_time_error_coord_str = ""
                    for ele in alphanum_start_time_error_coord:
                        alphanum_start_time_error_coord_str += str(ele)+ ""
                    
                    # String to return to the /schedule after an error is found.
                    start_time_error_message = f"Bad data found in START cell: {[col_index + 1 ,row_index + agent]}."
                    self.cursor_db_close()
                    return start_time_error_message
                
                first_break_string = self.csv_data[row_index + agent][col_index + 2]
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
                        alphanum_first_break_error_coord_str += str(ele)+ ""

                    first_break_error_message = f"Bad data found in FIRST BREAK cell: {alphanum_first_break_error_coord_str}."
                    self.cursor_db_close()
                    return first_break_error_message
                    

                meal_string = self.csv_data[row_index + agent][col_index + 3]
                try:
                    meal_formatted = breaktime_str_to_datetime(date_string, meal_string)
                except:
                    meal_time_error_message = f"Bad data found in MEAL TIME cell: {[col_index + 3 ,row_index + agent]}."
                    self.cursor_db_close()
                    return meal_time_error_message

                second_break_string = self.csv_data[row_index + agent][col_index + 4]
                try:
                    second_break_formatted = breaktime_str_to_datetime(date_string, second_break_string)
                except:
                    second_break_error_message = f"Bad data found in SECOND BREAK cell: {[col_index + 4 ,row_index + agent]}."
                    self.cursor_db_close()
                    return second_break_error_message

                end_time_string = self.csv_data[row_index + agent][col_index + 5]
                try:
                    end_time_formatted = breaktime_str_to_datetime(date_string, end_time_string)
                except:
                    end_time_error_message = f"Bad data found in END TIME cell: {[col_index + 5 ,row_index + agent]}."
                    self.cursor_db_close()
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

                self.cursor.execute(sql, val)
                self.db.commit()

        self.cursor_db_close()

        return "Week OK."


    def convert_num_to_alpha(self, num):
        alphabets = ["A", "B", "C", "D", "E", "F" ,"G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE"]
        alpha_coord = alphabets[num]
        print(alpha_coord)
        return alpha_coord

    def cursor_db_close(self):
        self.cursor.close()
        self.db.close()