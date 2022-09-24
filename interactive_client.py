import os
import jsonpickle
import requests
import click

CREDENTIAL_FILE_NAME = "credential"

BASE_URL = "http://127.0.0.1:8081/api/v1/"

API_LOGIN = BASE_URL + "login"

API_LIST_PROJECT = BASE_URL + "project"

API_GENERATE = BASE_URL + "generate"


# Utilities
# local


# reader
def file_to_dict(path) -> dict:
    f = open(path, "r")
    data = jsonpickle.loads(f.read())
    return data


def generate_format_params(dirpath, data) -> dict:
    return {
        'path' : dirpath,
        'data' : data
    }


def read_model():
    request_data = list()

    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        for filename in filenames:
            if filename == 'model.json':
                model_path = dirpath + '/' + filename
                data = file_to_dict(model_path)
                format_data = generate_format_params(dirpath, data)
                request_data.append(format_data)

    return request_data


def write_str_to_file(file_name: str, target: str):
    with open(os.path.join(os.getcwd(), file_name), "w") as file:
        file.write(target)


def read_file_to_str(file_name: str) -> str:
    full_path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(full_path):
        with open(full_path, "r") as file:
            return file.read()
    else:
        return ''


def delete_file(file_name: str):
    full_path = os.path.join(os.getcwd(), file_name)
    os.remove(full_path)


def make_dir(parent_path: str, dir_result: str):
    if dir_result:
        path = os.path.join(parent_path, dir_result)
        if not os.path.exists(path):
            os.makedirs(path)
    else:
        path = parent_path
    return path

def is_file_exist(file_name: str) -> bool:
    return os.path.exists(os.path.join(os.getcwd(), file_name))


# API

class RequestObj:

    def __init__(self, method: str, url: str):
        self.method = method
        self.url = url
        self.parameter = {}
        self.headers = {}

    @classmethod
    def get(cls, url):
        return RequestObj(method='get', url=url)

    @classmethod
    def post(cls, url):
        return RequestObj(method='post', url=url)

    def addAuthorization(self, token):
        self.headers['Authorization'] = 'Token ' + token
        return self

    def setParameters(self, parameter: dict):
        self.parameter = parameter
        return self

    def setHeaders(self, headers: dict):
        self.headers = headers
        return self

    def request(self):
        if self.method == 'get':
            return requests.get(url=self.url, data=self.parameter, headers=self.headers)
        else:
            return requests.post(url=self.url, data=self.parameter, headers=self.headers)


def request_post(url, parameter: dict, headers: dict = None):
    response = requests.post(url=url, data=parameter, headers=headers)
    return response


def request_get(url, parameter: dict, headers: dict = None):
    response = requests.get(url=url, data=parameter, headers=headers)
    return response

# Presenter


class LoginPresenter:

    def is_login(self) -> bool:
        return is_file_exist(CREDENTIAL_FILE_NAME)

    def login(self, username, password):
        if is_file_exist(CREDENTIAL_FILE_NAME):
            credential = self.read_credential()
            response = RequestObj.post(API_LOGIN) \
                .setParameters(credential) \
                .request()
            if response.status_code != 200:
                self.logout()
        else:
            response = RequestObj.post(API_LOGIN) \
                .setParameters(parameter={
                'username': username,
                'password': password
            }).request()
            if response.status_code == 200:
                auth_response = response.json()
                self.save_credential(data_json=auth_response['details'])

    def logout(self):
        delete_file(CREDENTIAL_FILE_NAME)

    def delete_credential(self):
        delete_file(CREDENTIAL_FILE_NAME)

    def read_credential(self) -> dict:
        credential_txt = read_file_to_str(CREDENTIAL_FILE_NAME)
        return jsonpickle.loads(credential_txt)

    def save_credential(self, data_json):
        write_str_to_file(CREDENTIAL_FILE_NAME, jsonpickle.dumps(
            data_json
        ))


class MainPresenter:

    def __init__(self, auth_data):
        self.auth_data = auth_data

    def request_list_project(self):
        return RequestObj.get(API_LIST_PROJECT) \
            .setParameters(self.auth_data) \
            .addAuthorization(self.auth_data['token']) \
            .request()

    def request_generate_project(self, project_id):
        data = read_model()
        return RequestObj.post(API_GENERATE) \
            .setParameters(parameter={
                                'array_data' : jsonpickle.dumps(data),
                                'project_id' : project_id,
                              }) \
            .addAuthorization(self.auth_data['token']) \
            .request()

    def write_data(self, data_response):
        for detail in data_response['details']:
            for result_item in detail['result']:
                path = make_dir(detail['path'], result_item['dir_result'])
                file_path = os.path.join(path, result_item['file_name'])
                if os.path.exists(file_path):
                    with open(file_path, "r") as f:
                        content_file = f.read()
                        content_file += "\n\n\n" \
                                        "####################(new generate code)####################\n\n\n"
                        content_file += result_item['code']
                    with open(file_path, "w") as f:
                        f.write(content_file)
                        f.close()
                else:
                    with open(file_path, "w") as f:
                        f.write(result_item['code'])
                        f.close()

# view - command line

@click.command()
def projects():
    login_presenter = LoginPresenter()

    if login_presenter.is_login():
        main_presenter = MainPresenter(login_presenter.read_credential())
        response = main_presenter.request_list_project()
        for index, item in enumerate(response.json()['details']):
            click.echo('' + (index + 1).__str__() + '. Project id : ' + str(item['pk']) + ' Project Name : ' + item['name'] )
    else:
        click.echo('Please login first!')


@click.command()
@click.option('--project_id', prompt='project_id')
def exec(project_id):
    login_presenter = LoginPresenter()

    if login_presenter.is_login():
        main_presenter = MainPresenter(login_presenter.read_credential())
        response = main_presenter.request_generate_project(project_id=project_id)
        print(response.text)
        main_presenter.write_data(data_response=response.json())
    else:
        click.echo('Please login first!')


#
@click.command()
@click.option('--username', prompt='username', help='User name credentials')
@click.option('--password', prompt='password', help='Password user')
def login(username, password):
    login_presenter = LoginPresenter()
    login_presenter.login(username=username, password=password)


@click.command()
def logout():
    login_presenter = LoginPresenter()
    login_presenter.logout()
    click.echo('Logout success!')


@click.group()
def main_app():
    pass


main_app.add_command(login)
main_app.add_command(logout)
main_app.add_command(projects)
main_app.add_command(exec)

if __name__ == '__main__':
    main_app()
