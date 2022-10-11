""" Este es el Docstring del modulo documentar"""

class User:
    """Permite representar un usuario."""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo user.

        Args:
            username (str): El username del usuario.
            password (str): El password del usuario.
        """
        self.username = username
        self.password = password