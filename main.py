class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def win(self):
        self.points += 3

    def draw(self):
        self.points += 1


class Tournament:
    def __init__(self):
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def match(self, i1, i2, result):
        if result == "1":
            self.teams[i1].win()
        elif result == "2":
            self.teams[i2].win()
        else:
            self.teams[i1].draw()
            self.teams[i2].draw()

    def table(self):
        sorted_teams = sorted(self.teams, key=lambda t: t.points, reverse=True)
        for t in sorted_teams:
            print(t.name, "-", t.points)


tour = Tournament()

while True:
    print("\n1.Jamoa 2.O‘yin 3.Jadval 0.Exit")
    c = input(">>> ")

    if c == "1":
        tour.add_team(Team(input("Nomi: ")))
    elif c == "2":
        tour.match(int(input("Jamoa1: ")), int(input("Jamoa2: ")), input("1/2/X: "))
    elif c == "3":
        tour.table()
    elif c == "0":
        break
