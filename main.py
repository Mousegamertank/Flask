from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=False)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=False)

video_update_args = reqparse.RequestParser()
video_update_args.add_arguments("")
video_update_args.add_argument("likes", type=int, help="Likes of the video")
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer, 
    'likes': fields.Integer,
    }

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def patch(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video does't exist, cannot update")
        


    # def delete(self, video_id):
    #     abort_if_video_doesnt_exist(video_id)
    #     del videos[video_id]
    #     return '', 204

api.add_resource(Video, "//video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

# videos = {}

# def abort_if_video_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, message="Video id is not valid...")

# def abort_if_video_exists(video_id):
#     if video_id in videos:
#         abort(409, message="Video already exists with an ID")


# names = {"Pedro":{"age": 19, "gender": "male"},
#          "bill": {"age": 70, "gender": "male"}}

# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]