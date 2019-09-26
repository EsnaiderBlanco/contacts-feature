from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import Session, Base
from models import Contact

app = Flask(__name__)
app.secret_key = "super secret key"

def _get_all_contacs(db_session):
    try:
        contacts = db_session.query(Contact).order_by(Contact.id)
    except:
        db_session.rollback()
        raise
    finally:
        db_session.close()
        return contacts

def _insert_contact(db_session, contact_info):
    status = False
    try:
        db_session.add(contact_info)
        db_session.commit()
        status = True
    except:
        db_session.rollback()        
        raise
    finally:
        db_session.close()
        return status        

def _update_contact(db_session, contact_info, contact_id):
    status = False
    try:
        obj_to_update = db_session.query(Contact).filter_by(id=contact_id).first()
        obj_to_update.name = contact_info.name
        obj_to_update.phone_number = contact_info.phone_number
        obj_to_update.email = contact_info.email
        obj_to_update.description = contact_info.description
        db_session.commit()        
        print("contact updated")
        status = True
    except:
        db_session.rollback()        
        raise
    finally:
        db_session.close()
        return status
    
def _delete_contac(db_session, contact_id):
    status = False
    try:
        obj_to_delete = db_session.query(Contact).filter_by(id=contact_id).first()
        db_session.delete(obj_to_delete)        
        db_session.commit()        
        print("contact deleted")
        status = True
    except:
        db_session.rollback()        
        raise
    finally:
        db_session.close()
        return status      

@app.route("/")
def display_index():
    return render_template('base.html')

@app.route("/contacts")
def get_contacts():
    print("Displaying table")
    db_session = Session()
    data = _get_all_contacs(db_session)
    return render_template('contacts.html', data=data)

@app.route("/submit", methods=['POST'])
def new_contact():
    if request.method == 'POST':
        name = request.form['name']        
        phone_number = request.form['phone_number']
        email = request.form['email']
        description = request.form['description']        
        contact_info = Contact(name,phone_number,email,description)        
        db_session = Session()
        result = _insert_contact(db_session,contact_info)        
        return redirect(url_for('get_contacts'))
    
@app.route("/edit-contact", methods=["POST"])
def edit_contact():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']        
        phone_number = request.form['phone_number']
        email = request.form['email']
        description = request.form['description']        
        contact_info = Contact(name,phone_number,email,description)        
        db_session = Session()
        data = _update_contact(db_session, contact_info, id)
        return redirect(url_for('get_contacts'))      

@app.route("/delete-contact", methods=["POST"])
def delete_contact():
    if request.method == 'POST':
        id = request.form['id']               
        db_session = Session()
        data = _delete_contac(db_session, id)
        return redirect(url_for('get_contacts'))  
    
if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()