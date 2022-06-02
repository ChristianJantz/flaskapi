
from email.policy import default
from sqlalchemy import null
from extensions import db


class Todo(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    is_activ = db.Column(db.Boolean(), default=True)
    todos = db.relationship("Comment", backref="Todo")

    @property
    def data(self):
        return {
            "id" : self.id,
            "title" : self.title
        }

    