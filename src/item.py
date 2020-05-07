class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def item_name(self):
        return f"{self.name}"
