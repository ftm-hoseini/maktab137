import json
from json import JSONDecodeError


class InvalidConfigError(Exception):
    pass


def load_config():
    try:
        with open('config.json', 'r') as file:
            data = json.load(file)
            key_list = list(data.keys())
            if set(data.keys()) != {"mode", "api_keys", "database_url"}:
                raise InvalidConfigError("format is not correct")
            for i in key_list:
                if i not in ["mode", "api_keys", "database_url"]:
                    raise InvalidConfigError("format is not correct")
            if data["mode"] != "debug" and data["mode"] != "production":
                raise InvalidConfigError("mode is not supported")

    except FileNotFoundError as e:
        print("file not found")
    except JSONDecodeError as e:
        print("json decode error")


load_config()