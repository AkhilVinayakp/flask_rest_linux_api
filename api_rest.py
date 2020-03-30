from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os
import shlex
import subprocess
app = Flask(__name__)
api = Api(app)

# adding a class that will resolve according to that


class Hello_world(Resource):
    def get(self):
        return {'hello': 'world'}


@app.route('/linapi', methods=['GET'])
def resolve():
    cmd = request.args.get('cmd')
    cmd = shlex.split(cmd)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    stdout = str(stdout).replace('\\n', '<br>')
    return "command <br>{} output <br> {} <br>error<br> {} ".format(cmd,stdout,stderr)


api.add_resource(Hello_world, '/')
#api.add_resource(Api_call, '/lin_api')


if __name__ == '__main__':
    app.run(debug='true')
