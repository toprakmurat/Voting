
def create_table(candidates):
    table = []
    for i in range(len(candidates)):
        tmp = []
        for j in range(len(candidates)):
            tmp.append(0)
        table.append(tmp)
    return table


class Tideman:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = []
        self.preferences = create_table(candidates)
        # preferences[i][j] shows how many people chose candidate i over candidate j

    # return true if vote is valid, false otherwise
    def vote(self, preference):
        # check if vote is valid
        if sorted(preference) != sorted(self.candidates):
            return False
        self.votes.append(preference)
        self.prefer(preference)
        return True

    # update preferences list
    def prefer(self, vote):
        for ind, cand in enumerate(vote[:-1]):
            index_winner = self.candidates.index(cand)
            for i in vote[ind+1:]:
                index_loser = self.candidates.index(i)
                self.preferences[index_winner][index_loser] += 1

    def calculate(self):
        pass

    def lock(self):
        pass

    def check(self):
        pass

    def result(self):
        pass


d = ['Erdogan', 'Kilicdaroglu', 'Ogan']
turkey2023 = Tideman(d)
turkey2023.vote(d)
print(turkey2023.preferences)
