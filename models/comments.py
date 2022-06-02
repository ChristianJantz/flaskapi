from email.policy import default
from extensions import db

class Comment(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    __tabelname__ = "comments"
    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    todo_id = db.Column(db.Integer, db.FoeignKey("Todo"))
    is_activ = db.Column(db.Boolean(), default=False)

    @property
    def data(self):
        return {
            "id" : self.id,
            "body" : self.body,
        }