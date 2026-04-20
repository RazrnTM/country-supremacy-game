class Resources:
    def __init__(self):
        self.resources = {
            'gold': 0,
            'food': 0,
            'military_units': 0,
            'production_capacity': 0
        }

    def add_resource(self, resource_type, amount):
        if resource_type in self.resources:
            self.resources[resource_type] += amount
        else:
            raise ValueError(f"Resource type '{resource_type}' does not exist.")

    def remove_resource(self, resource_type, amount):
        if resource_type in self.resources:
            if self.resources[resource_type] >= amount:
                self.resources[resource_type] -= amount
            else:
                raise ValueError(f"Not enough {resource_type} to remove.")
        else:
            raise ValueError(f"Resource type '{resource_type}' does not exist.")

    def get_resource(self, resource_type):
        if resource_type in self.resources:
            return self.resources[resource_type]
        else:
            raise ValueError(f"Resource type '{resource_type}' does not exist.")

    def display_resources(self):
        for resource, amount in self.resources.items():
            print(f"{resource}: {amount}")
