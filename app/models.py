from . import db

class Post(db.Model):
  __tablename__ = "posts"
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.String(100), nullable=False)
  body = db.Column(db.Text, nullable=False)
  likes = db.Column(db.Integer, default=0, server_default="0")

  def to_dict(self):
      return {
          'id': self.id,
          'author': self.author,
          'body': self.body,
          'likes': self.likes
      }