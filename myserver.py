from flask import Flask , render_template , request , redirect, url_for
import csv

app = Flask(__name__)

@app.route('/<string:page_name>') #making url variable
def my_page(page_name):
    return render_template(page_name)

@app.route('/') #setting routes to dynamically
def my_home():
    return render_template('index.html')        
       
def write_to_csv(data):
    with open('./mydatabase/bd.csv', mode='a', newline='') as database:
        fieldnames = ['subject','email','message']
        csv_writer= csv.DictWriter(database , fieldnames =fieldnames)
        # csv_writer.writeheader()
        csv_writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('submit_form.html') 
    else:
        return 'Something went wrong, Try again!'        






