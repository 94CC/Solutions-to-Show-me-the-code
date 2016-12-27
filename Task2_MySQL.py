"""
Task0002: store the unique codes generated from task 0001 into MySQL database.
"""
import Task1_ActivationCodes
import pymysql

def record(passwd,mycodes):
    try:
        con=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd=passwd,db='mysql')
        cursor=con.cursor()
        cursor.execute('CREATE DATABASE activation_code')
        cursor.execute('USE activation_code')
        cursor.execute('CREATE TABLE activ_codes(id SMALLINT NOT NULL auto_increment PRIMARY KEY,\
        codes VARCHAR(20))')
        for code in mycodes:
            command="INSERT INTO activ_codes(codes) VALUES ('%s')" %code
            cursor.execute(command)
            con.commit()
    except Exception as e:
        con.rollback()
        print ('error:',repr(e))
    finally:        
        cursor.close()
        con.close()
        
def main():
    mycodes=Task1_ActivationCodes.main()
    passwd=input('enter your password for mysql database: ')
    record(passwd,mycodes)

if __name__=='__main__':
    main()
