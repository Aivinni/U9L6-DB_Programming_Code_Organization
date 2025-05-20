import mysql.connector




def makeQuery(query):
   connection = mysql.connector.connect(user='aivinn',
                                        password='204411003',
                                        host='10.8.37.226',
                                        database='aivinn_db')


   cursor = connection.cursor()
   cursor.execute(query)


   schedule = []
   for row in cursor:
       schedule.append(row)


   cursor.close()
   connection.close()
   return schedule




def printSchedule(array):
   for row in array:
       print(f"Period: {row[6]}")
       print(f"Course: {row[4]}")
       print(f"Row: {row[3]}")
       print(f"Teacher: {row[5]}")
       print()




response = makeQuery("call GetStudentSchedule(1);")
printSchedule(response)


