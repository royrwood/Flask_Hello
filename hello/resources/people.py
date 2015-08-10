from __future__ import print_function

from flask_restful import Resource
##from myproject.common.db import query_db


class People(Resource):
    def get(self,**kwargs):
        print("In People.get")
        return "People.get()"
    
    def post(self,id,**kwargs):
        print("In People.post; id = {}".format(id))
        return "People.post(); id = {}".format(id)