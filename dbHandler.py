import mysql.connector

class MySqlConnector:

    connection = 0


    def __init__(self, dbName, user, password):
        try:
            self.connection = mysql.connector.connect(host='localhost', database=dbName, user=user, password=password)

        except Exception as e:
            print("Error creating MySql connection", e)

    


    def queryDb(self, query): 
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        
        data = self.cleanData(data) #returns data as array

        return data
    
    

    def closeConnection(self):
        if self.connection.is_connected():
            self.connection.close()
            self.cursor.close()
        

        
    def cleanData(self, data):
        tempData = []
        singleEle = 0

        for tuple in data: 
            tempSubArr = []
        
            for item in tuple: 

                if len(tuple) != 1: #tuple has more than one item, add items to temp array
                    tempSubArr.append(str(item))
                else: 
                    singleEle = str(item)

            if len(tuple) != 1: #tuple has more than one item, create 2d array
                tempData.append(tempSubArr)
            else: 
                tempData.append(singleEle) #tuple only has one item, create 1d array

        return tempData
