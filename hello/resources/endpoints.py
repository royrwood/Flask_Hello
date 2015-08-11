from __future__ import print_function

from flask_restful import Resource

# print("--> endpoints.py: import hello.models.people before")
# import hello.models.people
# print("--> endpoints.py: import hello.models.people after")
# print("dir(hello.models.people) = {}".format(dir(hello.models)))

print("--> endpoints.py: hello.models.people import People before")
from hello.models.people import People
# print("dir(People) = {}".format(dir(People)))
print("--> endpoints.py: import hello.models.people after")


class PeopleEndpoint(Resource):
    def get(self,**kwargs):
        print("In People.get")
        
        result = {}
        
        for i,p in enumerate(People.query.all()):
            result[str(i)] = str(p)

        return result
    
    def post(self,id,**kwargs):
        print("In People.post; id = {}".format(id))
        return "People.post(); id = {}".format(id)

    
if (__name__ == '__main__'):
    print("Hello endpoints.py")