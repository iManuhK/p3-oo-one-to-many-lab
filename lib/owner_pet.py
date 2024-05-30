class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,pet_type):
        self.pet_type = pet_type
        self._owner = None
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"{self.pet_type} is not a valid pet type")
       
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,owner):
        if not isinstance(owner, Owner):
            raise TypeError("owner must be an instance of Owner class")
        self._owner = owner

class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner = self
            self.pets.append(pet)
        else:
            raise Exception(f"{pet} is not a Pet")
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)