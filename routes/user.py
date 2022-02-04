from flask import request, Blueprint
from flask_restx import Resource
from models.user import User, UserDto, UserInsertDto, UserUpdateDto
from app import db, api

user_module = Blueprint('user_module', __name__)


@api.route('/user')
class Route(Resource):
    @api.marshal_list_with(UserDto)
    def get(self):
        """ 全レコードを取得します """
        users = db.session.query(User).all()
        return users

    @api.expect(UserInsertDto)
    @api.marshal_with(UserDto)
    def post(self):
        """ レコードを１件追加します """
        json_body = request.json

        new_user = User(**json_body)
        db.session.add(new_user)
        db.session.commit()

        return new_user


@api.route('/user/<int:id>')
class RouteWithId(Resource):
    @api.marshal_with(UserDto)
    def get(self, id: int):
        """ IDを指定してレコードを１件取得します """
        user = db.session.query(User).filter(User.id == id).one()
        return user

    @api.expect(UserUpdateDto)
    @api.marshal_with(UserDto)
    def patch(self, id: int):
        """ IDを指定してレコードを１件更新します """
        json_body = request.json
        update_user = db.session.query(User).filter(User.id == id).one()
        for k, v in json_body.items():
            setattr(update_user, k, v)
        db.session.commit()
        return update_user

    @api.marshal_with(UserDto)
    def delete(self, id: int):
        """ IDを指定してレコードを１件削除します """
        delete_user = db.session.query(User).filter(User.id == id).one()
        db.session.delete(delete_user)
        db.session.commit()
        return delete_user
