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
    res_Country_total = connection.execute('SELECT COUNT(1) FROM Country').fetchone()
    assert res_Country_total[0] == 11

def test_League_total_records (connection):
    res_League_total = connection.execute('SELECT COUNT(1) FROM League').fetchone()
    assert res_League_total[0] == 11

def test_Country_PK_unique (connection):
    res_Country_PK = len(connection.execute('SELECT id FROM Country GROUP BY id HAVING COUNT(id)>1').fetchall())
    assert res_Country_PK == 0