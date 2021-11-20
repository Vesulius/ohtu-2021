from player import Player

class PlayerStats:
    
    def __init__(self, reader):
        self.reader = reader
        

    def top_scorers_by_nationality(self, nat):
        players = self.reader.get_players()
        filtered_list = filter(lambda p: p.nationality == nat, players)
        sorted_list = sorted(filtered_list, key=lambda p: p.goals + p.assists, reverse=True)
        return sorted_list

