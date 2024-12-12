from name import Name

class Builder(Name):
    def __init__(self,name,address,contact_info):
        super().__init__(name,address,contact_info)

    def __str__(self):
        return super().__str__()