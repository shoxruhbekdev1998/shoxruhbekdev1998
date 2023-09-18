import sqlite3

class Database:
    def __init__(self,baza_manzili):
        self.path_to_db = baza_manzili
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql:str,parameters:tuple = None, fetchone = False, fetchall = False, commit = False):
        if not parameters:
            parameters = ()

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    @staticmethod
    def format_args(sql,parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql , tuple(parameters.values())





    def user_qoshish(self, ism:str, tg_id:int, fam: str = None, username: str=None):

        sql = """ 
        INSERT INTO myfiles_subscribe(ism,tg_id,fam,username) Values( ?, ?, ?, ?)
        """
        self.execute(sql,parameters=(ism,tg_id,fam,username),commit=True)


    def natija_qoshish(self, savol_id:int,savol:str,javob:str, tg_id:int,tur:str,status:str):

        sql = """ 
        INSERT INTO myfiles_natijalar(savol_id,savol,javob,tg_id,tur,status) Values( ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql,parameters=(savol_id,savol,javob,tg_id,tur,status),commit=True)
#ru qoshildi
    def natija_qoshishru(self, savol_id:int,savol:str,javob:str, tg_id:int,turru:str,status:str):

        sql = """ 
        INSERT INTO myfiles_natijalarru(savol_id,savol,javob,tg_id,turru,status) Values( ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql,parameters=(savol_id,savol,javob,tg_id,turru,status),commit=True)


    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_subscribe
        """
        return self.execute(sql,fetchall=True)

    def select_user(self,**kwargs):

        #SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
        SELECT * FROM myfiles_menu Where 
        """
        sql,parameters =self.format_args(sql,kwargs)

        return sql.execute(sql,parameters=parameters,fetchone=True)

    def select_types(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT * FROM myfiles_menu Where 
                """
        sql, parameters = self.format_args(sql, kwargs)

        return sql.execute(sql, parameters=parameters, fetchone=True)

    def count_test(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_test_savollar;", fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_subscribe;", fetchone=True)


    def select_test(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT COUNT(*) FROM myfiles_test_savollar Where 
                """
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM myfiles_subscribe WHERE TRUE",commit=True)

    def select_all_menu_uz(self):
        sql = """
        SELECT * FROM myfiles_menu_uz
        """
        return self.execute(sql,fetchall=True)

#ru qoshildi
    def select_all_menu_ru(self):
        sql = """
        SELECT * FROM myfiles_menu_ru
        """
        return self.execute(sql,fetchall=True)


    def select_test_savollar(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT * FROM myfiles_test_savollar Where 
                """
        sql,parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
#ru qoshildi
    def select_test_savollarru(self,**kwargs):
        sql = """
         SELECT * FROM myfiles_test_savollarru Where
        """
        sql,parameters =self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters,fetchall=True)

    def update_test_savollar(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                UPDATE myfiles_natijalar SET status=False Where 
                """
        sql,parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, commit=True)
#ru qoshildi
    def update_test_savollarru(self,**kwargs):
        sql ="""
                   UPDATE myfiles_natijalarru SET status=False Where
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters,commit=True)

    def select_all_test_savollar(self):
        sql = """
        SELECT * FROM myfiles_test_savollar
        """
        return self.execute(sql,fetchall=True)
#ru qoshildi
    def select_all_test_savollarru(self):
        sql = """
             SELECT * FROM myfiles_test_savollarru
        """
        return self.execute(sql,fetchall=True)


    def select_javob(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT javob FROM myfiles_natijalar Where 
                """
        sql,parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
#ru qoshildi
    def select_javobru(self,**kwargs):
        sql = """
        SELECT javob FROM myfiles_natijalarru Where
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters,fetchall=True)






    def select_reklamalar(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT * FROM reklamalar Where
                """
        sql,parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_reklamalar(self):
        sql = """
        SELECT * FROM reklamalar
        """
        return self.execute(sql,fetchall=True)




def logger(statement):
    print(f"""
    _________________________________________________
    Executing:
    {statement}
    ___________________________________________________-
"""


    )