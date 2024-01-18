import sys

import mysql.connector as connection
con = connection.connect(host="localhost", user="root", database="test", password="password")
def execute(q):
    cursor = con.cursor()
    cursor.execute(q)
    con.commit()

def test(q):
    cursor = con.cursor()
    cursor.execute(q)
    data = cursor.fetchall()
    for i in data:
        pass
        # print(i)
    return data


def INSERT(username, password):
    values_query = '''
    INSERT INTO login
    values("%s","%s");''' % (username, password)
    print(values_query)
    execute(values_query)



#########################################################
'''initial_query=
CREATE TABLE login
(username varchar(20) primary key,
password varchar(20));
initial_query=
CREATE TABLE EMPLOYEE
(employee_name varchar(20),
employee_id int primary key,
doj date,
Cost_to_Company int,
80C int,
80D int,
rent int);
CREATE TABLE Tax
(employee_name varchar(20),
employee_id int primary key,
Basic int,
HRA int,
Sp_Allow int,
Total_Earning int,
Net_pay int,
PF int,
IT int,
Tot_Detuct int);
'''
#execute(initial_query)

def create_new_user(username, password):
    # Y=check(username)
    # if Y == "access "
    INSERT(username, password)

def delete_account(username):
    query='''DELETE FROM LOGIN WHERE USERNAME = "%s";'''%username
    execute(query)

def Update_user(username,new_password):
    q="""UPDATE LOGIN SET password = "%s" where username = "%s" ;"""%(new_password,username)
    execute(q)

def check(USERNAME, passw):
    q = "SELECT PASSWORD FROM LOGIN WHERE USERNAME = '%s';" % USERNAME
    y = test(q)
    # print(y)
    if [(passw,)] == y:
        return "access granted"
    else:
        return "access denied"
    # return q
# INSERT("a","p")

def add_employee(name,id,doj,ctc,C_80Exemption,D_80Exemption,rent):
    values_query = '''
    INSERT INTO EMPLOYEE
    values("%s","%s","%s","%s","%s","%s","%s");''' % (name,id,doj,ctc,C_80Exemption,D_80Exemption,rent)
    execute(values_query)
    with open('log', 'a+') as f:
        a = id
        b = 'Employee ' + str(a) + ' added' + '\n'
        f.write(b)
def del_employee(sid):
    q='''delete from employee where employee_id = %s;'''%(sid)
    execute(q)
    with open('log', 'a+') as f:
        a = sid
        b = 'Employee ' + str(a) + ' deleted' + '\n'
        f.write(b)

def update_employee(name,id,ctc,C_80Exemption,D_80Exemption,rent):
    q="""UPDATE employee SET employee_name = "%s",
                Cost_to_company = %s,
                80C = %s,
                80D = %s,
                rent = %s
            WHERE employee_id = %s;
        """%(name,ctc,C_80Exemption,D_80Exemption,rent,id)
    sys.stdout.write(q)
    execute(q)
    with open('log', 'a+') as f:
        a = id
        b = 'Employee ' + str(a) + ' updated' + '\n'
        f.write(b)
def info(id):
    q = "Select * from EMPLOYEE where employee_id = '%s';" % id
    y = test(q)
    return y

def tax_add(name,id,b,hra,sa,te,np,pf,it,td):
    q1='''delete from tax where employee_id = %s'''%(id)
    q="""INSERT INTO TAX
    values("%s",%s,%s,%s,%s,%s,%s,%s,%s,%s);"""%(name,id,b,hra,sa,te,np,pf,it,td)
    execute(q1)
    execute(q)
    with open('log', 'a+') as f:
        a = id
        b = 'Tax calculated for Employee ' + str(a) + '\n'
        f.write(b)
def maax():
    q="""select max(employee_id) from employee;"""
    return test(q)
#print(test("select * from employee;"))
#add_employee("Nakul",5,"2007-3-12",25000,600,780,3000)
