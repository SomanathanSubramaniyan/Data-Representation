import mysql.connector
class AccidentDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Somu@1975",
        database="Accidents"
        )
                
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into accidents (id,province,VehicleType,DriverAge,DriverSex, MonthYear) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (values))
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from accidents"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from accidents where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update accidents set province=%s,VehicleType=%s,DriverAge=%s,DriverSex=%s, MonthYear=%s where id=%s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from accidents where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','province','VehicleType','DriverAge','DriverSex', 'MonthYear']
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item
        
AccidentDAO = AccidentDAO()