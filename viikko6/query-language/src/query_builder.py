from matchers import *


class QueryBuilder:
    def __init__(self, matcher=All()):
        self.matcher = matcher

    def build(self):
        return self.matcher

    def playsIn(self, team_name):
        return QueryBuilder(And(self.matcher, PlaysIn(team_name)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))
