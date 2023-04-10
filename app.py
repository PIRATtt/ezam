from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('db.db')
c = db.cursor()

c.execute("""
SELECT * FROM rooms""")
all_rooms = c.fetchall()

c.execute("""
SELECT * FROM booking""")
all_booking = c.fetchall()

db.close()


list_code=[]
for b in all_booking:
        list_code.append(b[1])

# Список для проверки этажей
floors=[]
for r in all_rooms:
        floors.append(r[2])

@app.route('/')
def index():
    return render_template('base.html')

# @app.route('/auth')
# def auth():
#     code=request.form.get('code', type=str)
#     if code in list_code:
#         check_code=True
#         print(check_code)
#     return render_template('auth.html')

# @app.route('/append', methods=['POST', 'GET'])
# def append():
#     if request.method == "POST":
#         name=request.form.get('name', type=str)
#         age=request.form.get('age', type=int)
#         address=request.form.get('address', type=str)

#         name_horse=request.form.get('name_horse', type=str)
#         age_horse=request.form.get('age_horse', type=int)
#         pol=request.form.get('pol', type=str)

#         battle=request.form.get('battle', type=str)
#         hippodrome=request.form.get('hippodrome', type=str)
#         date=request.form.get('date', type=str)
#         if name and age and address:
#             with sqlite3.connect('skachki.db') as db:
#                 c = db.cursor()
#                 # Добавь блок трай, для добавления в бд
#                 # хотя пох
#                 c.execute('INSERT INTO jockeys (name,address,age) VALUES (?,?,?)',
#                 (name,address,age)          
#                 )
#                 db.commit()
#                 flash="Успешно добавили жокея!"
#             return redirect('jockeys')
#         if name_horse and age_horse and pol:
#             with sqlite3.connect('skachki.db') as db:
#                 c = db.cursor()
#                 c.execute('INSERT INTO horses (name,pol,age) VALUES (?,?,?)',
#                 (name_horse,pol,age_horse)          
#                 )
#                 db.commit()
#             return redirect('horses')
#         if battle and hippodrome and date:
#             with sqlite3.connect('skachki.db') as db:
#                 c = db.cursor()
#                 c.execute('INSERT INTO battles (battle,date,hippodrome) VALUES (?,?,?)',
#                 (battle,date,hippodrome)          
#                 )
#                 db.commit()
#             return redirect('battles')
#     else:
#         return render_template('append.html')

@app.route('/rooms')
def rooms():
    rooms=[]
    for r in all_rooms:
        rooms.append({"id": r[0], "name":r[1], "floor":r[2]})
    return render_template('rooms.html', rooms=rooms)

@app.route('/booking')
def booking():
    booking=[]
    for b in all_booking:
        if b[4] in floors:
            booking.append({"id": b[0], "name":b[2], "time":b[3], "floor":b[4]})
        else:
            booking.append({"id": b[0], "name":b[2], "time":b[3], "floor":'Fake floor!'})
    return render_template('booking.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5010')