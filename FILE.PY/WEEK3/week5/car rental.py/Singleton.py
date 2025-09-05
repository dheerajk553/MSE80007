class RentManager:
    _instance = None  # Variable in class to hold the one instance of RentalManager.
    def __new__(cls):
        # This method control object creation. It ensures only one instance of RentalManager is created.
        if cls._instance is None:
            # If no instance exists, create a new one using the superclass's __new__ method
            cls._instance = super(RentManager, cls).__new__(cls)
            cls._instance.rentals = []  # Initialize the rentals list to store all rental records
        return cls._instance  # Return the existing instance every time, enforcing Singleton behavior

    def add_rental(self, rental):
        # Adds a new rental record to the centralized rentals list
        self.rentals.append(rental)