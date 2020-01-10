from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from wtforms import Form,StringField,TextAreaField,validators,SelectField,IntegerField,FloatField
app=Flask(__name__)
app.secret_key = "12345"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL

_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventory'  
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Intialize MySQL
mysql = MySQL(app)


class InsertMPNForm(Form):
    productid=StringField('MPN',[validators.Length(min=1,max=50),validators.required()])
    no=IntegerField('Quantity',[validators.required()])

class AttribForm(Form):
    package=StringField('Package',[validators.Length(min=4,max=25),validators.required()])
    value=FloatField('Value',[validators.required(),validators.required()])
    units=StringField('Units',[validators.Length(min=3,max=5),validators.required()])
    types=StringField('Types',[validators.Length(min=4,max=25),validators.required()])

@app.route('/searchMPN',methods=['GET','POST'])
def search():
    form=InsertMPNForm(request.form)
    
    if request.method=='POST' and form.validate():
        productid=form.productid.data
        cursor = mysql.connection.cursor()
        result=cursor.execute('SELECT * FROM data1 WHERE productid = %s',[ productid])
        if result>0:
            flash()
            cursor.close()
        
        else:

            flash('No data found !')
            cursor.close()
            
@app.route('/srcattrib',methods=['GET','POST'])  
def srchAttrib():
    form=AttribForm(request.form)

    if request.method=='POST' and form.validate():
        package=form.package.data
        value=form.value.data
        units=form.units.data
        types=form.types.data
        cursor = mysql.connection.cursor()
        result=cursor.execute('SELECT * FROM data1 WHERE package = %s,value=%s,units=%s,types=%s',[ package,value,units,types])
        if result>0:
            flash()
            cursor.close()
        
        else:

            flash('No data found !')
            cursor.close()



if __name__=='__main__':
    app.run(debug=True)