alphabets = ["A", "B", "C", "D", "E", "F" ,"G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE"]

list_of_tuples = []
for alphabet in enumerate(alphabets):
    list_of_tuples.append(alphabet)
alphanum_dict = dict((x,y) for x, y in list_of_tuples) 
print(alphanum_dict[9])


   


"""
Output wanted:
[9,10] TO BECOME "J 11"

numeric_first_break_error_coord = [col_index + 2 ,row_index + agent] = [9,10]
#1: Split [9,10] to become [9] and [10]
numeric_first_break_error_coord = [col_index + 2 ,row_index + agent]
middle_index = 1
first_part = numeric_first_break_error_coord[:middle_index] #print(first_part) = [9] ---> We want "J".


We take [9] because it's the one we want to convert to alphabet. Don't care about [10] yet. 
 =============================================================
second_part = numeric_first_break_error_coord[middle_index:]


alphanum_first_break_error_coord = "J 11"


"""
# Print [9,10] as "J 11"
