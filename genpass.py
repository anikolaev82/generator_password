import json
from interface.abcgenpass import AbcGenPass


class GenPass(AbcGenPass):

    def __init__(self, length_pswd=6,  **kwargs):
        super().__init__(length_pswd=length_pswd, **kwargs)

    def to_file(self, cnt_pswd=1, file=open("new_password", "w")):
        for _ in range(cnt_pswd):
            file.write(self.make_password() + "\n")
        file.close()

    def to_json(self, cnt_pswd=1):
        data = {}
        data["complexity"] = {"classes": self.get_classes(), "count_password": cnt_pswd}
        data["passwords"] = [self.make_password() for _ in range(cnt_pswd)]
        return json.dumps(data)
