from rollforbugs_website import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, default='GETDATE()', nullable=False)
    edited = db.Column(db.DateTime, default='GETDATE()', nullable=False)
    body = db.Column(db.UnicodeText)

    def __repr__(self):
        return '<Post %r>' % self.id


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, default='GETDATE()', nullable=False)
    edited = db.Column(db.DateTime, default='GETDATE()', nullable=False)
    body = db.Column(db.UnicodeText)

    def __repr__(self):
        return '<Comment %r>' % self.id
