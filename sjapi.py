from api import API


class SuperJobAPI(API):

    def get_vacancies(self, name):
        self.name = name
        pass