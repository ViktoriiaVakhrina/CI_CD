import pytest
import sqlite3

@pytest.fixture(scope="session")
def connection():
    conn = sqlite3.connect('database.sqlite')
    curs = conn.cursor()
    return curs

def test_Tables(connection):
    res_FK = connection.execute('SELECT name from sqlite_master where type= "table"').fetchall()
    res_list = [t[0] for t in res_FK]
    assert res_list == ['sqlite_sequence','Player_Attributes','Player','Match','League','Country',
                      'Team','Team_Attributes']

def test_County_total_records (connection):
    res_Country_total = connection.execute('SELECT COUNT(1) FROM Country').fentone()
    assert res_Country_total == 10
