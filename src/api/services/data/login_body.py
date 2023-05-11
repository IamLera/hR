import json


class loginBody():

    def __init__(self, email, password):

        self.email = email
        self.password = password


    def to_json(self):
        return json.dumps({
            'email': self.email,
            'password': self.password
        })

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['email'], data['password'])