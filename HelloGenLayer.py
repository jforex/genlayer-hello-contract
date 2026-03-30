# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class HelloGenLayer(gl.Contract):
    greeting: str

    def __init__(self):
        self.greeting = "Welcome to GenLayer! AI just entered the blockchain 🔥"

    @gl.public.view
    def say_hello(self, name: str) -> str:
        return f"{self.greeting} Hey {name}!"

    @gl.public.write
    def update_greeting(self, new_greeting: str):
        print(f"🔄 Updating greeting to: {new_greeting}")  # shows in logs
        self.greeting = new_greeting
