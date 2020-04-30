from flask_restful import Resource, reqparse, abort

from App.apis.movie_user.model_utils import get_user

parse = reqparse.RequestParser()
parse.add_argument("token", required =True, help="请登录")

class MovieOrderResource(Resource):

    def post(self):

        args = parse.parse_args()

        token = args.get("token")

        user_id = cache.get(token)

        user = get_user(user_id)

        if not user:
            abort(401,msg="请登录")

        return {"msg":"post order ok"}