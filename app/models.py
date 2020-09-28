from app import db

class Dev_events(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), index=True)
    date_from = db.Column(db.DateTime)
    date_to = db.Column(db.DateTime)

    def __repr__(self):
        return '<Event {}>'.format(self.title) 