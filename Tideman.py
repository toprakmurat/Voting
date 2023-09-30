from typing import List, Any


def create_table(add, candidates):
    table = []
    for i in range(len(candidates)):
        tmp = []
        for j in range(len(candidates)):
            tmp.append(add)
        table.append(tmp)
    return table


class Tideman:
    def __init__(self, candidates):
        self.candidates = candidates
        self.preferences = create_table(0, candidates)
        # preferences[i][j] shows how many people chose candidate i over candidate j
        self.locked = create_table(False, candidates)
        self.votes = []
        self.pairs = []
        self.pair_count = 0

    # return true if vote is valid, false otherwise
    def vote(self, preference):
        # check if vote is valid
        if sorted(preference) != sorted(self.candidates):
            return False
        self.votes.append(preference)
        self.record_preferences(preference)
        return True

    # update preferences list
    def record_preferences(self, vote):
        for ind, cand in enumerate(vote[:-1]):
            index_winner = self.candidates.index(cand)
            for i in vote[ind+1:]:
                index_loser = self.candidates.index(i)
                self.preferences[index_winner][index_loser] += 1

    def add_pairs(self):
        for i in range(len(self.candidates)):
            for j in range(len(self.candidates)):
                if self.preferences[i][j] > self.preferences[j][i]:
                    winner, loser = i, j
                    margin = self.preferences[i][j] - self.preferences[j][i]
                    self.pairs.append([winner, loser, margin])
                    self.pair_count += 1

    def sort_pairs(self):
        margin_list = []
        for pair in self.pairs:
            margin_list.append(pair[2])

        pairs_sorted = []
        for i in range(self.pair_count):
            # Get current max value of margins and append it to pairs_sorted list
            index = margin_list.index(max(margin_list))
            pairs_sorted.append(self.pairs[index])
            # Cannot remove maximum because it will change indexes. Instead, give it a value of 0.
            margin_list[index] = 0  # Minimum margin is 1 because if it's 0, it is not included to self.pairs

        self.pairs = pairs_sorted.copy()

    def has_cycle(self, winner, loser):
        # if locked[loser][winner] is True, locked[winner][loser] will create a cycle
        if self.locked[loser][winner]:
            return True

        for i in range(len(self.candidates)):
            if self.locked[loser][i] is True and self.has_cycle(winner, i):
                return True

        return False

    def lock(self):
        # Make sure self.pairs is sorted
        self.sort_pairs()

        # Lock the graph one by one in decreasing margin order
        for pair in self.pairs:
            winner, loser = pair[0], pair[1]
            if self.has_cycle(winner, loser) is False:
                self.locked[winner][loser] = True

    def result(self):
        found_source = True
        for row in range(len(self.candidates)):
            for col in range(len(self.candidates)):
                if self.locked[col][row] is True:
                    found_source = False
                    break

                found_source = True

            if found_source:
                return self.candidates[row]

        return 'There is no winner for this election using Tideman'
