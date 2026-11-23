from sqlalchemy import create_engine
from sqlalchemy.sql import text


class TeacherTable:
    def __init__(self, connection_street):
        self.db = create_engine(connection_street)

    def get_list_group_id(self):
        rows = self.db.execute("select distinct group_id from group_student "
                               "order by group_id").fetchall()
        group_id_list = []
        for row in rows:
            group_id_list.append(row[0])  # Добавляем число в новый список

        return group_id_list

    def add_teacher(self, email, group_id):
        self.db.execute(text(
            "insert into teacher (email, group_id)"
            " values (:email, :group_id)"), email=email, group_id=group_id)

    def get_all_teachers(self):
        rows = self.db.execute("select * from teacher").fetchall()
        return rows

    def get_one_teacher_by_id(self, teacher_id):
        rows = self.db.execute(
            text("select * from teacher where teacher_id = :teacher_id"),
            teacher_id=teacher_id).fetchall()
        return rows

    def delete_teacher_by_id(self, teacher_id):
        self.db.execute(text("delete from teacher where teacher_id "
                             "= :teacher_id"), teacher_id=teacher_id)

    def update_teacher_email(self, teacher_id, new_email):
        self.db.execute(text("update teacher set email = :email "
                             "where teacher_id = :teacher_id"),
                        teacher_id=teacher_id, email=new_email, )
