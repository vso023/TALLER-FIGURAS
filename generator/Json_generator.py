import json

class JsonGenerator:
    @staticmethod
    def figure_to_json(figure):
        return json.dumps(figure.to_dict())
