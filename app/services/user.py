from fastapi import Depends
from ..repositories.user import UserRepository


class UserService:
    userRepository: UserRepository

    def __init__(self, userRepository: UserRepository = Depends()):
        self.userRepository = userRepository

    def list_all(self):
        return self.userRepository.list_all()

    def create(self, user):
        return self.userRepository.create(user)

    def get_by_id(self, user_id):
        return self.userRepository[user_id]
