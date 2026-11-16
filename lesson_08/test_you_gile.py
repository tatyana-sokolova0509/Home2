from you_gile_api import YouGileApi
from faker import Faker
import pytest
import config
import random

base_url = config.BASE_URL
login = config.LOGIN
password = config.PASSWORD
fake = Faker()
fake_ru = Faker('ru_RU')
random_index = random.randint(1, (
        YouGileApi(base_url).get_projects_count(login, password) - 1))


def test_auth():
    api = YouGileApi(base_url)
    id_company = api.get_id_company(login, password)
    assert len(id_company) > 0


def test_get_key():
    api = YouGileApi(base_url)
    key = api.get_key(login, password)
    assert key is not None


@pytest.mark.create_project_positive_tests
@pytest.mark.parametrize("title", [fake.company(), fake_ru.company()])
def test_create_project(title):
    api = YouGileApi(base_url)
    length_before = len(api.get_list_projects(login, password)['content'])
    id_project = api.create_project(login, password, title)['id']
    try:
        assert id_project is not None, "Проект не создан "
        projects = api.get_list_projects(login, password)
        length_after = len(projects['content'])
        assert projects['content'][-1]['title'] == title, \
            "Заголовок нового проекта не соответствует"
        assert length_before + 1 == length_after, \
            "Количество проектов не увеличилось после создания нового"
    finally:
        api.delete_project_by_id(login, password, id_project)
        projects = api.get_list_projects(login, password)['content']
        project_ids = []
        for project in projects:
            project_ids.append(project['id'])
        assert id_project not in project_ids, \
            "Созданный проект не удален после проверки"


@pytest.mark.create_project_negative_tests
def test_create_project_empty_title():
    api = YouGileApi(base_url)
    length_before = len(api.get_list_projects(login, password)['content'])
    resp = api.create_project(login, password, "")
    assert resp['message'][0] == "title should not be empty", \
        "Нет сообщения, что заголовок не может быть пустым"
    projects = api.get_list_projects(login, password)
    length_after = len(projects['content'])
    assert length_before == length_after, \
        "Количество проектов изменилось"


@pytest.mark.get_project_by_id_positive_tests
@pytest.mark.parametrize("index", [-1, 0, random_index])
def test_get_project_by_id(index):
    api = YouGileApi(base_url)
    id_project = api.get_list_projects(login, password)['content'][index]['id']
    title_project = api.get_list_projects(
        login, password)['content'][index]['title']
    resp = api.get_project_by_id(login, password, id_project)
    assert resp['id'] == id_project, "id найденного проекта не соответствует"
    assert resp['title'] == title_project, \
        "Заголовок найденного проекта не соответствует"


@pytest.mark.get_project_by_id_negative_tests
def test_get_project_with_invalid_id():
    api = YouGileApi(base_url)
    fake_id = fake.uuid4()
    resp = api.get_project_by_id(login, password, fake_id)
    assert resp['message'] == "Проект не найден"


@pytest.mark.edit_project_by_id_positive_tests
def test_edit_title_project():
    api = YouGileApi(base_url)
    id_new_project = api.create_project(
        login, password, fake_ru.company())['id']
    new_title = "Новый заголовок"
    resp = api.edit_title_project_by_id(
        login, password, id_new_project, new_title)
    try:
        assert resp['id'] == id_new_project, \
            "id измененного проекта не соответствует"
        projects = api.get_list_projects(login, password)
        assert projects['content'][-1]['title'] == new_title, \
            "заголовок измененного проекта не соответствует"
    finally:
        api.delete_project_by_id(login, password, id_new_project)
        projects = api.get_list_projects(login, password)['content']
        project_ids = []
        for project in projects:
            project_ids.append(project['id'])
        assert id_new_project not in project_ids, \
            "Созданный проект не удален после проверки"


@pytest.mark.edit_project_by_id_positive_tests
def test_edit_deleted_project():
    api = YouGileApi(base_url)
    id_new_project = api.create_project(
        login, password, fake_ru.company())['id']
    projects_before = api.get_list_projects(login, password)['content']
    project_ids_before = []
    for project in projects_before:
        project_ids_before.append(project['id'])
    assert id_new_project in project_ids_before, \
        "id созданного проекта нет в списке всех проектов"

    api.delete_project_by_id(login, password, id_new_project)
    projects_after = api.get_list_projects(login, password)['content']
    project_ids_after = []
    for project in projects_after:
        project_ids_after.append(project['id'])
    assert id_new_project not in project_ids_after, \
        "id удаленного проекта все еще есть в списке всех проектов"


@pytest.mark.edit_project_by_id_negative_tests
def test_edit_title_project_with_invalid_id():
    api = YouGileApi(base_url)
    fake_id = fake.uuid4()
    resp = api.edit_title_project_by_id(login, password, fake_id, "Заголовок")
    assert resp['message'] == "Проект не найден"
