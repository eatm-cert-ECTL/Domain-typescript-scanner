from mainApp import MainApp

import sqlite3

def insertIntoDatabase(domainList : list, mainA : MainApp) -> None:
    query = "INSERT INTO {} (domains) VALUES ".format(mainA.typosquatDomainTableName)
    for elt in domainList:
        query += '("{}"),'.format(elt)
    query = query[:len(query)-1]
    query += ';'
    con = sqlite3.connect(mainA.databaseName)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()
    mainA.model.select()

def insertIntoDatabase2(elements : list, dbName: str, tableName: str):
    query = f"INSERT INTO {tableName} VALUES "
    for elt in elements:
        query += '("{}"),'.format(elt)
    query = query[:len(query)-1]
    query += ';'
    con = sqlite3.connect(dbName)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()