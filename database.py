import mysql.connector

class db:

    def __init__(self, host:str, user:str, password:str, db:str) -> None:
        '''conenct t dabtabsr'''
        self.host = host
        self.user = user
        self.password = password
        #idk if is this the correct way 

    def connect(self):
        '''attempts to connect to teh thing'''
        
        try:
            self.conn = mysql.connector(
                host = self.host,
                user = self.user,
                password = self.password,
                auth_plugin = 'mysql_native_password'
                )
        
        except Exception as e:
            raise ValueError(f"Error while connecting! : {e}")