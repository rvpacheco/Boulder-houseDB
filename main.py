import pyodbc



class database:
    def __init__(self):

        SERVER='LAPTOP-5KNF7VQH'
        base = 'Muro'
        usuario = 'sa'
        con = '804482817168'

        try:
            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+SERVER+';DATABASE='+base+';UID='+usuario+';PWD='+con)
            self.cursor=self.connection.cursor()
            print("conexion exitosa")



        except:
            print("Error al intentar conectarse")

    def busca_users(self,users):
        cur=self.connection.cursor()
        sql = "SELECT * FROM login_datos WHERE Users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx

    def busca_password(self, password):
        cur=self.connection.cursor()
        sql = "SELECT * FROM login_datos WHERE password = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx

