from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)
from .models import Post
from . import db

@api.route("/health")
def health():
  return jsonify(status="ok")

@api.route("/posts", methods=["GET"])
def posts():
  posts = Post.query.all()
  print(posts)
  return jsonify(posts=[post.to_dict() for post in posts])

@api.route("/posts", methods=["POST"])
def create_post():
  data = request.get_json()
  author = data.get("author")
  body = data.get("body")

  if not author or not body:
    return jsonify({"error: Missing data or body"}), 400

  new_post = Post(author=author, body=body)

  db.session.add(new_post)
  db.session.commit()

  return jsonify(new_post.to_dict()), 201

@api.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
  post = Post.query.get(post_id)
  if not post:
    return jsonify({"error": "Post not found"}), 404

  db.session.delete(post)
  db.session.commit()

  return jsonify({"message": f"Post {post_id} deleted"}), 200

@api.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
  post = Post.query.get(post_id)
  if not post:
    return jsonify({"error": "Post not found"}), 404

  return jsonify(post.to_dict()), 200