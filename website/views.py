from flask import Blueprint, render_template, request, flash, jsonify # this  mean have buch of root inside & and render template html
from flask_login import login_user, login_required, logout_user, current_user
from . import db
import json
from datetime import datetime
from .models import RentUser, Note, ReportUser  # call database form model.py


views = Blueprint('views', __name__ ) 

@views.route('/')
@login_required
def home():
    receipts = [
        {"date": "Jan 2025", "amount": "Paid", "approved": "Yes", "note": "Noted"},
        {"date": "Dec 2024", "amount": "Given", "approved": "Yes", "note": "Noted"},
        {"date": "Nov 24", "amount": "Given", "approved": "Yes", "note": "Noted"}
    ]
    
    return render_template(
        "home.html",
        user=current_user,
        receipts=receipts,
        current_date=datetime.now().strftime('%Y-%m-%d'),
        current_time=datetime.now().strftime('%H:%M'),
        announcement_text="Lorem ipsum dolor sit amet..."
    )

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note= json.loads(request.data)
    noteId= note['noteId']
    note= Note.query.get(noteId)
    if note:
      if note.user_id==current_user.id:
        db.session.delete(note)
        db.session.commit()
    return jsonify({})
 

@views.route('/rent', methods=['GET', 'POST'])
@login_required
def rent():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        note = request.form.get('note')
        rent_file = request.files.get('rent_file')
        
        new_rent = RentUser(
            file_name=file_name,
            note=note,
            user_id=current_user.id,
            status='Pending'
        )
        
        db.session.add(new_rent)
        db.session.commit()
        flash('Rent record added!', category='success')
        
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M')
    
    return render_template(
        "RentUser.html",
        user=current_user,
        current_date=current_date,
        current_time=current_time,
        rent_status="Active",
        overdue=False
    )

@views.route('/news')
@login_required
def news():
    return render_template("NewsUser.html",  # Changed from news.html
        user=current_user,
        current_date=datetime.now().strftime('%Y-%m-%d'),
        current_time=datetime.now().strftime('%H:%M'),
        latest_news={"content": "Lorem ipsum..."},
        previous_news=[...]
    )

@views.route('/report', methods=['GET', 'POST'])
@login_required
def report():
    if request.method == 'POST':
        new_report = ReportUser(
            name=request.form.get('name'),
            email=request.form.get('email'),
            request=request.form.get('request'),
            user_id=current_user.id
        )
        db.session.add(new_report)
        db.session.commit()
        flash('Report submitted!', category='success')
        
    return render_template("ReportUser.html",
        user=current_user,
        current_date=datetime.now().strftime('%Y-%m-%d'),
        current_time=datetime.now().strftime('%H:%M')
    )

@views.route('/faq')
@login_required
def faq():
    faqs = [
        {"id": 1, "question": "Question", "answer": "Lorem ipsum..."},
        {"id": 2, "question": "Question", "answer": "Lorem ipsum..."},
        {"id": 3, "question": "Question", "answer": "Lorem ipsum..."}
    ]
    return render_template(
        "FAQs.html",
        user=current_user,
        current_date=datetime.now().strftime('%Y-%m-%d'),
        current_time=datetime.now().strftime('%H:%M'),
        faqs=faqs
    )