from faker import Faker

class Randomizer:
    fake = Faker()

    @staticmethod
    def generate_Random_name():
        fake_name = Randomizer.fake.first_name()
        return fake_name
    
    @staticmethod
    def generate_random_lastname():
        fake_lastname = Randomizer.fake.last_name()
        return fake_lastname
    
    @staticmethod
    def generate_random_address():
        fake_address = Randomizer.fake.address()
        return fake_address