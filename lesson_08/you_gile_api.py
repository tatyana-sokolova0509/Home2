import requests


class YouGileApi:
    def __init__(self, url):
        self.url = url

    def get_id_company(self, login, password):
        my_json = {"login": login,
                   "password": password}
        my_headers = {"Content-Type": "application/json"}
        resp = requests.post(self.url + '/auth/companies',
                             headers=my_headers, json=my_json)
        id_company = resp.json()['content'][0]['id']
        return id_company

    def get_key(self, login, password):
        my_json = {"login": login,
                   "password": password,
                   "companyId": self.get_id_company(login, password)}
        my_headers = {"Content-Type": "application/json"}
        resp = requests.post(self.url + '/auth/keys/get',
                             headers=my_headers, json=my_json)
        key = resp.json()[0]['key']
        return key

    def create_project(self, login, password, title):
        my_json = {"title": title}
        my_headers = {"Content-Type": "application/json",
                      "Authorization": "Bearer " +
                                       self.get_key(login, password)}
        resp = requests.post(self.url + '/projects',
                             headers=my_headers, json=my_json).json()
        return resp

    def get_list_projects(self, login, password):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + self.get_key(login, password)}
        resp = requests.get(self.url + '/projects', headers=headers)
        projects = resp.json()
        return projects

    def get_project_by_id(self, login, password, id_project):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + self.get_key(login, password)}
        resp = requests.get(self.url + '/projects/' + id_project,
                            headers=headers)
        return resp.json()

    def get_projects_count(self, login, password):
        count = self.get_list_projects(login, password)['paging']['count']
        return count

    def edit_title_project_by_id(self, login, password, id_project, title):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + self.get_key(login, password)}
        my_json = {"title": title}
        resp = requests.put(self.url + '/projects/' + id_project,
                            headers=headers, json=my_json)
        return resp.json()

    def delete_project_by_id(self, login, password, id_project):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + self.get_key(login, password)}
        my_json = {"deleted": True}
        resp = requests.put(self.url + '/projects/' + id_project,
                            headers=headers, json=my_json)
        return resp.json()
