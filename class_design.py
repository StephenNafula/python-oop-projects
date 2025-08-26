# Example: Class Design in Python (with Inheritance & Encapsulation)

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self):
        print(f"{self.brand} {self.model} is charging... Battery: {self.battery}mAh")

    def phone_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB, Battery: {self.battery}mAh")


# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu  # Graphics Processing Unit for gaming

    def play_game(self, game):
        print(f"{self.brand} {self.model} with {self.gpu} GPU is playing {game}!")

    # Overriding method (polymorphism)
    def phone_info(self):
        print(f"Gaming Phone: {self.brand} {self.model}, Storage: {self.storage}GB, Battery: {self.battery}mAh, GPU: {self.gpu}")


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S22", 128, 4000)
    phone1.phone_info()
    phone1.make_call("+254700000000")

    print("----")

    gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, 6000, "Adreno 730")
    gaming_phone.phone_info()
    gaming_phone.play_game("Call of Duty Mobile")
