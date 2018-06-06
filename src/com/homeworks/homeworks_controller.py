from src.models.base import DB
from src.com.homeworks.models.homeworks import Homeworks


class HomeworksController(object):
    def __init__(self):
        pass

    def get_all(self):
        try:
            all = DB.query(Homeworks).order_by(Homeworks.id.desc()).limit(10).all()
            DB.commit()
            return all
        except:
            DB.rollback()
        return None

    def new(self, fields: list):
        try:
            DB.add(Homeworks(
                lesson_id=fields[0],
                title=fields[1],
                description=fields[2],
                file_path=fields[3],
                deadline=fields[4],
                created=fields[5]))

            DB.commit()
            DB.close()
        except:
            DB.rollback()

    def edit(self, fields: list, id: int):
        try:
            DB.query(Homeworks).filter(Homeworks.id == id).update(dict(
                lesson_id=fields[0],
                title=fields[1],
                description=fields[2],
                file_path=fields[3],
                deadline=fields[4],
                modified=fields[5]))

            DB.commit()
            DB.close()
        except:
            DB.rollback()

    def delete(self, id: int):
        try:
            DB.delete(self.find_by_id(id))
        except:
            DB.rollback()

    def find_by_id(self, id):
        return DB.query(Homeworks).filter(Homeworks.id == id).first()
