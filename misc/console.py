import os

class console():
    """
    Class for some console commands, such as clearing the console output, etc
    """
    def clear(self):
        """
        Clears the console both on windows and on linux.
        
        Takes no input
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)