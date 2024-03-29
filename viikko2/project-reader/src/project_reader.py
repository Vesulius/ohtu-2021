from os import name
from urllib import request
from project import Project

import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        dictionary = toml.loads(content)
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = dictionary["tool"]["poetry"]["name"]
        description = dictionary["tool"]["poetry"]["description"]
        dependencies = dictionary["tool"]["poetry"]["dependencies"]
        dev_dependencies = dictionary["tool"]["poetry"]["dev-dependencies"]
        return Project(name, description, dependencies, dev_dependencies)
