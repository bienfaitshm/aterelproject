from db.models import Clients, session
from typing import Any, Dict, List


class ClientDataParser:
    @classmethod
    def parser_for_treeview(cls, clients: list[Clients], fields: list | dict, *args, **kwargs):
        _data = []
        for client in clients:
            dataclient = [
                getattr(client, field)
                for field in fields
                if hasattr(client, field)
            ]
            _data.append(dataclient)
        return _data

    @classmethod
    def array_todict(cls, data: list[Any], fields: list[str] | dict[str, Any]) -> dict[str, Any]:
        _dict = {}
        if isinstance(fields, dict):
            fields = list(fields.keys())

        if len(fields) < len(data):
            return _dict

        for i, value in enumerate(fields):
            _dict[value] = data[i]
        return _dict

    @classmethod
    def get_content_fields(cls, data: List[List[Any]], idx: List[str | int], position: int = 0) -> List[Any]:
        return [data[int(i)][position] for i in idx]


class ClientDBService:
    def __init__(self, clientmodel: Clients = Clients, session=session):
        self.session = session
        self.clientmodel = clientmodel

    def getclients(self):
        return self.session.query(self.clientmodel).all()

    def searchclients(self, text: str) -> list[Clients]:
        return self.session.query(self.clientmodel).filter(self.clientmodel.name.like(f"%{text}%")).all()

    def createclient(self, client: Dict[str, Any]):
        clobj = self.clientmodel(**client)
        self.session.add(clobj)
        self.session.commit()

    def deleteclient(self, iid: str | int) -> int:
        deleted = self.session.query(self.clientmodel).filter(
            self.clientmodel.id == iid).delete()
        self.session.commit()
        return deleted

    def deleteclients(self, iids: List[str | int]) -> int:
        deleted = self.session.query(self.clientmodel).filter(
            self.clientmodel.id.in_(iids)).delete()
        self.session.commit()
        return deleted

    def updateclient(self, *args, **kwargs):
        pass
