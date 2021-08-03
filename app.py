from flask import Flask
from flask_restful import Resource, Api, reqparse
import scale_builder
import chord_builder
from notes import notesSharps, notesFlats

app = Flask(__name__)
api = Api(app)

allNotes = set(notesSharps).union(set(notesFlats))

class Scales(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('scale', required=True)
        parser.add_argument('root', required=True)
        args = parser.parse_args()

        if scale_builder.scales.get(args['scale']) and args['root'] in allNotes:
            return {'data': scale_builder.process(args['scale'], args['root'])}, 200
        else:
            return {'error': 'Wrong argument supplied', 'arguments': args}, 400

class Chords(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('chord', required=True)
        parser.add_argument('root', required=True)
        args = parser.parse_args()

        if chord_builder.chords.get(args['chord']) and args['root'] in allNotes:
            return {'data': chord_builder.process(args['chord'], args['root'])}, 200
        else:
            return {'error': 'Wrong argument supplied', 'arguments': args}, 400

api.add_resource(Scales, '/scales')
api.add_resource(Chords, '/chords')

if __name__ == '__main__':
    app.run()
