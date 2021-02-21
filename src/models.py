from confdb import db


class Pad(db.Model):
    __tablename__ = 'pad'
    id = db.Column(
            db.Integer,
            db.Sequence('user_id_seq'),
            primary_key=True,
            nullable=False
            )
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def to_json(self):
        return {
                "id": self.id,
                "title": self.title,
                "content": self.content
                }
