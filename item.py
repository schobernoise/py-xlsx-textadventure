import utils

class item_manager:
    def __init__(self, item_excel) -> None:
        self.items = self.items_from_xlsx(item_excel)
        
    def items_from_xlsx(self, excel_file):
        raise NotImplementedError


class item:
    def __init__(self, name, description, value) -> None:
        self.name = name
        self.description = description
        self.value = value