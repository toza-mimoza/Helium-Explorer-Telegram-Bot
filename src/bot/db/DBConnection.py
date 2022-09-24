class DBConnection: 
    connection = None
    
    @staticmethod
    def set_connection(conn):
        DBConnection.connection = conn