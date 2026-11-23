import config
import random
from faker import Faker
import pytest

from lesson_09.TeacherTable import TeacherTable

connection_string = config.DB_CONNECTION_STRING
db = TeacherTable(connection_string)

@pytest.mark.positive_test
def test_add_teacher():
    random_group_id = random.choice(db.get_list_group_id())
    random_email = Faker().email()
    db.add_teacher(email=random_email, group_id=random_group_id)
    rows = db.get_all_teachers()
    new_teacher = {}
    for row in rows:
        if row['email'] == random_email:
            new_teacher = row
            break

    db.delete_teacher_by_id(new_teacher['teacher_id'])

    assert new_teacher['email'] == random_email
    assert new_teacher['group_id'] == random_group_id

@pytest.mark.positive_test
def test_update_teacher_email():
    random_group_id = random.choice(db.get_list_group_id())
    random_email = Faker().email()
    db.add_teacher(email=random_email, group_id=random_group_id)
    rows = db.get_all_teachers()
    new_teacher = {}
    for row in rows:
        if row['email'] == random_email:
            new_teacher = row
            break
    db.update_teacher_email(new_teacher['teacher_id'], 'updated@mail.ru')
    updated_teacher = db.get_one_teacher_by_id(new_teacher['teacher_id'])[0]

    db.delete_teacher_by_id(new_teacher['teacher_id'])

    assert updated_teacher['email'] == 'updated@mail.ru'

@pytest.mark.positive_test
def test_delete_teacher_by_id():
    random_group_id = random.choice(db.get_list_group_id())
    random_email = Faker().email()
    db.add_teacher(email=random_email, group_id=random_group_id)
    rows = db.get_all_teachers()
    new_teacher = {}
    for row in rows:
        if row['email'] == random_email:
            new_teacher = row
            break

    db.delete_teacher_by_id(new_teacher['teacher_id'])
    rows = db.get_one_teacher_by_id(new_teacher['teacher_id'])
    assert len(rows) == 0
