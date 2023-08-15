users = [{"id": 1, "name": "Talismar", "age": 24}]


class UserRepository:
    def list_all(self):
        return users

    def create(self, user):
        users.append(user)
        return user
