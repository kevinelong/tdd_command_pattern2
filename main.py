class Command:
    def __init__(self, name: str, payload: dict):
        self.name = name
        self.payload = payload


class App:
    def __init__(self, commands: dict):
        self.commands = commands

    def execute(self, command):
        if command.name not in self.commands:
            return None
        return self.commands[command.name](command.payload)


def do_work(payload):
    print(payload["option1"])
    return True


def do_more_work(payload):
    print(payload["option1"])
    return payload["option1"]

app = App({
    "do_work": do_work,
    "do_more_work": do_more_work,
})

tests = [
    ["do_work", {"option1":"abc"}, True],
    ["do_more_work", {"option1": "abc"}, "abc"]
]
for t in tests:
    assert t[2] == app.execute(Command(t[0],t[1]))

