class SerialGenerator:
    """
    A class for generating unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(initial_value=100)
    >>> serial.generate()
    100
    >>> serial.generate()
    101
    >>> serial.reset()
    >>> serial.generate()
    100
    """
    def __init__(self, initial_value=0):
        """Initialize the generator with an initial value."""
        self.start = self.next = initial_value

    def __repr__(self):
        """Return a string representation of the generator."""
        return f"<SerialGenerator initial_value={self.start} current_value={self.next}>"

    def generate(self):
        """Generate and return the next serial number."""
        current_serial = self.next
        self.next += 1
        return current_serial

    def reset(self):
        """Reset the generator to its initial value."""
        self.next = self.start


