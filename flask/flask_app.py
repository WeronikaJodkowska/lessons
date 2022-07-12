import json
import logging

from flask import Flask, request, Response
from sqlalchemy.orm import sessionmaker

from utils import create_database_if_not_exists, setup_db_engine
from models import Base, User, Profile, Address, Product, Purchase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    data = {"message": "Index page"}
    return Response(json.dumps(data), content_type="application/json")


@app.route("/user/", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        data = request.json
        if not data.get("email") or not data.get("password"):
            return Response(status=400)

        new_user = User(email=data.get("email"), password=data.get("password"))
        app.current_session.add(new_user)
        app.current_session.commit()

        return Response(new_user.json(), status=201, content_type="application/json")

    data = {"users": list(
        map(lambda x: x.serialize(), app.current_session.query(User).all())
    )}
    return Response(json.dumps(data), content_type="application/json")


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    app.current_session = CurrentSession()

    app.run()