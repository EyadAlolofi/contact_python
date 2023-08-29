
class Contact:
    def __init__(self, name, phone, email) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"