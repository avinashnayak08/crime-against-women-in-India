from utils.db import db

class Report(db.Model):  # Corrected to inherit from db.Model
    Adhaar_Number = db.Column(db.String(20), primary_key=True)  # Part of primary key
    Type_of_Crime = db.Column(db.String(20))  # Part of composite key
    State = db.Column(db.String(50))  # Not part of primary key
    City = db.Column(db.String(50))  # Not part of primary key
    Date_of_Incident = db.Column(db.Date)  # Correct data type for dates
    Description = db.Column(db.Text)