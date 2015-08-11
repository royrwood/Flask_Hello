from __future__ import print_function

from flask_restful import Resource
#from myproject.common.db import query_db

print("--> endpoints.py")

print("--> endpoints.py: import hello.models.people before")
import hello.models.people
print("--> endpoints.py: import hello.models.people after")
# print("dir(hello.models.people) = {}".format(dir(hello.models)))

# from hello.models.people import People
# print("dir(People) = {}".format(dir(People)))

class PeopleEndpoint(Resource):
    def get(self,**kwargs):
        print("In People.get")
        
        result_str = "People.get():\n"
        
        # for i,p in enumerate(People.query.all()):
            # result_str += "{}: {}\n".format(i, p)

        return result_str
    
    def post(self,id,**kwargs):
        print("In People.post; id = {}".format(id))
        return "People.post(); id = {}".format(id)

    
if (__name__ == '__main__'):
    print("Hello endpoints.py")