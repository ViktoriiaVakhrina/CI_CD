import pytest
import sqlite3

@pytest.fixture(scope="session")
def connection():
    conn = sqlite3.connect('C:/Users/Viktoriia_Vakhrina/PycharmProjects/CICD/database.sqlite')
    curs = conn.cursor()
    return curs

def test_Tables(connection):
    res_FK = connection.execute('SELECT name from sqlite_master where type= "table"').fetchall()
    res_list = [t[0] for t in res_FK]
    assert res_list == ['Player_Attributes','Player','Match','League','Country',
                      'Team','Team_Attributes']

