from api import API


class HeadHunterAPI(API):

    def get_vacancies(self, name):
        self.name = name
        pass