from db import Database
from test import isvalid_email

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] ='5a2414632370aaca4f6dec257eccc6602d1531399983871c35cd48b30a6ae899'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Database()
        db.create_table('User', id='int auto_increment primary key',
                        name='varchar(100)',
                        email='varchar(40)',
                        password='text')
        if isvalid_email(request.form.get('email'),db.query_email('User',request.form.get('email'))):
            db.insert_data('User', {'name': request.form.get('name'),
                                'email': request.form.get('email'),
                                'password': request.form.get('psw')})
            flash('Пользователь создан')
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
