import psycopg2 as p

class myDB(object):
    def __init__(self, username, password, database, hostname):
        self._conn= p.connect(host=hostname, user=username, password=password, database=database)
        self._cur = self._conn.cursor()

    def query(self, query):
        return self._cur.execute(query)

    def __del__(self):
        self._conn.close()

if __name__ == '__main__':
    pass


