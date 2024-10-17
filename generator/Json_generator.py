import json

class JsonGenerator:
    @staticmethod
    def figure_to_json(figures):
        if isinstance(figures, list):
            return json.dumps([figure.to_dict() for figure in figures])
        else:
            return json.dumps(figures.to_dict()) #json.dumps() function will convert a subset of Python objects into a json string
