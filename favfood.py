from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('Database opened sucessfully!')

connection.execute('CREATE TABLE IF NOT EXISTS food (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
print('Table created sucessfully!')
connection.close()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    name = request.form['name']
    calories = request.form['calories']
    cuisine = request.form['cuisine']
    isvegetarian = request.form['is_vegetarian']
    isglutenfree = request.form['is_gluten_free']
    try:
        cursor.execute('INSERT INTO food(name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name, calories, cuisine, isvegetarian, isglutenfree))
        connection.commit()
        message = 'Record sucessfully added!'
    except:
        connection.rollback()
        message = 'Error in INSERT operation!'
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM food WHERE name = \'mango\'')
    favfood = cursor.fetchall()[0]
    connection.close()
    return jsonify(favfood)

#@app.route('/searchpage')
#def searchpage():
#    return render_template('searchpage.html')

#@app.route('/search', methods=["POST"])
#def search():
#    connection = sqlite3.connect('database.db')
#    name = request.args.get('name')
#    dbQuery = 'SELECT * FROM food WHERE name = "'+ str(name) +'"'
#    cursor = connection.cursor()
#    cursor.execute(dbQuery)
#    foodRequest = cursor.fetchall()
#    connection.close()
#    return jasonify(foodRequest)
