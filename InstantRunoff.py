
def create_table(number):
    lists = []
    for i in range(number):
        new = []
        lists.append(new)

    return lists


def create_dict(values):
    new_dict = {}
    for index in range(len(values)):
        new_dict[index] = 0

    return new_dict


class InstantRunoff:
    def __init__(self, candidates):
        self.candidates = candidates
        self.choices = create_table(len(candidates))
        self.candidate_dict = create_dict(candidates)
        self.votes = []
        self.winner = None

    def vote(self, preference):
        # Check if voter's vote is valid
        if sorted(preference) == sorted(self.candidates):
            self.votes.append(preference)
            for choice_index, candidate in enumerate(preference):
                candidate_index = self.candidates.index(candidate)
                self.choices[choice_index].append(candidate_index)

        else:
            raise Exception('Invalid Vote')

    def check_winning(self):
        self.record_votes()
        num_votes = len(self.votes)
        max_vote = max(self.candidate_dict.values())

        if max_vote > num_votes // 2:
            for key, value in self.candidate_dict.items():
                if value == max_vote:
                    self.winner = self.candidates[key]
            return True
        # Reset candidate_dict for later use
        self.candidate_dict = create_dict(self.candidates)
        return False

    def record_votes(self):
        for cand in self.choices[0]:
            self.candidate_dict[cand] += 1

    # If it is not over, return the eliminating candidate
    def find_eliminating(self):
        # Save votes to the dictionary
        self.record_votes()

        values = list(self.candidate_dict.values())
        while 0 in values:
            values.remove(0)
        min_value = min(values)
        eliminating_cands = [key for key in self.candidate_dict.keys()
                             if self.candidate_dict[key] == min_value]

        # Reset candidate_dict for later use
        self.candidate_dict = create_dict(self.candidates)

        return eliminating_cands[0]  # First cand in the list in case of multiple cands

    def update(self):
        # Save index and name of eliminating candidate
        candidate_index = self.find_eliminating()
        candidate_name = self.candidates[candidate_index]

        # TODO: FIND A BETTER WAY TO SOLVE THIS YOU CLUMSY
        # Find votes to change
        for vote in self.votes:
            # Remove first and then append to the list again
            # Example: [Murat, Enes, Yusuf] --> [Enes, Yusuf, Murat]
            if vote[0] == candidate_name:
                self.votes.remove(vote)
                vote.remove(candidate_name)
                vote.append(candidate_name)
                self.votes.append(vote)

        self.choices = create_table(len(self.candidates))
        for prefer in self.votes:
            candidate_index = self.candidates.index(prefer[0])
            self.choices[0].append(candidate_index)

    def result(self):
        res = self.check_winning()
        while res is False:
            self.update()
            res = self.check_winning()

        return self.winner

# Test
# colors = ['Yellow', 'Purple', 'Blue', 'Red']
# test = InstantRunoff(colors)
# votes = [['Yellow', 'Purple', 'Red', 'Blue'],
#          ['Yellow', 'Red', 'Purple', 'Blue'],
#          ['Yellow', 'Red', 'Purple', 'Blue'],
#          ['Blue', 'Purple', 'Yellow', 'Red'],
#          ['Blue', 'Purple', 'Yellow', 'Red'],
#          ['Blue', 'Purple', 'Yellow', 'Red'],
#          ['Blue', 'Red', 'Yellow', 'Purple'],
#          ['Purple', 'Blue', 'Red', 'Yellow'],
#          ['Purple', 'Blue', 'Red', 'Yellow'],
#          ['Purple', 'Blue', 'Red', 'Yellow'],
#          ['Purple', 'Blue', 'Red', 'Yellow'],
#          ['Purple', 'Blue', 'Red', 'Yellow'],
#          ['Purple', 'Blue', 'Red', 'Yellow'],
#          ['Purple', 'Blue', 'Red', 'Yellow'],
#          ['Red', 'Blue', 'Yellow', 'Purple'],
#          ['Red', 'Blue', 'Yellow', 'Purple'],
#          ['Red', 'Blue', 'Yellow', 'Purple'],
#          ['Red', 'Blue', 'Yellow', 'Purple'],
#          ['Red', 'Blue', 'Yellow', 'Purple']]
#
# for pref in votes:
#     test.vote(pref)
# print(test.result())
