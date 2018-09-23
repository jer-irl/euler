import functools


@functools.total_ordering
class Value:
    ordering = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    face_types = ['T', 'J', 'Q', 'K', 'A']

    def __init__(self, char):
        self.type = char

    def __eq__(self, other):
        return self.type == other.type

    def __lt__(self, other):
        return self.ordering.index(self.type) < self.ordering.index(other.type)


@functools.total_ordering
class Card:
    suits = ['H', 'S', 'C', 'D']

    def __init__(self, the_string):
        self.suit = the_string[1]
        self.value = Value(the_string[0])

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


@functools.total_ordering
class Hand:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

    def __init__(self, cards):
        self.cards: List[Card] = cards
        self.rank = self.calc_rank()

    def calc_rank(self):
        card_values = [card.value for card in self.cards]
        all_same_suit = self._all_same_suit()
        cards_consecutive = self._cards_consecutive()

        if all_same_suit and all(face in card_values for face in Value.faces):
            return self.ROYAL_FLUSH
        elif all_same_suit and cards_consecutive:
            return self.STRAIGHT_FLUSH
        elif self._have_n_of_same_type(4):
            return self.FOUR_OF_KIND
        elif self._have_n_of_same_type(3) and self._have_n_of_same_type(2):
            return self.FULL_HOUSE
        elif all_same_suit:
            return self.FLUSH
        elif cards_consecutive:
            return self.STRAIGHT
        elif self._have_n_of_same_type(3):
            return self.THREE_OF_KIND
        elif self._have_two_pairs():
            return self.TWO_PAIRS
        elif self._have_n_of_same_type(2):
            return self.ONE_PAIR
        else:
            return self.HIGH_CARD

    def group_by_type(self):
        res = {}
        for card in self.cards:
            t = card.value.type
            if t not in res:
                res[t] = []
            res[t].append(card)
        return res

    def __eq__(self, other):
        return False

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif self.rank < other.rank:
            return false

        my_grouped = self.group_by_type()
        other_grouped = other.group_by_type()

        if self.rank == self.ROYAL_FLUSH:
            raise Exception("Shouldn't have a tie")
        elif self.rank == self.STRAIGHT_FLUSH:
            return max(self.cards) > max(other.cards)
        elif self.rank == self.FOUR_OF_KIND:
            my_four = [my_grouped[t] for t in Value.ordering if len(my_grouped[t]) == 4][0]
            their_four = [other_grouped[t] for t in Value.ordering if len(other_grouped[t]) == 4][0]
            return my_four[0] > their_four[0]
        elif self.rank == self.FULL_HOUSE:
            my_three = [my_grouped[t] for t in Value.ordering if len(my_grouped[t]) == 3][0]
            their_three = [other_grouped[t] for t in Value.ordering if len(other_grouped[t]) == 3][0]
            if my_three[0] > their_three[0]:
                return True
            elif my_three[0] < their_three[0]:
                return False

            my_two = [my_grouped[t] for t in Value.ordering if len(my_grouped[t]) == 2][0]
            their_two = [other_grouped[t] for t in Value.ordering if len(other_grouped[t]) == 2][0]
            return my_two[0] > their_two[0]
        elif self.rank == self.FLUSH:
            my_sorted = reversed(sorted(self.cards))
            their_sorted = reversed(sorted(self.cards))
            for mine, theirs in zip(my_sorted, their_sorted):
                if mine > theirs:
                    return True
                elif mine < theirs:
                    return False
            raise Exception("Shouldn't get here")
        elif self.rank == self.STRAIGHT:
            my_sorted = reversed(sorted(self.cards))
            their_sorted = reversed(sorted(self.cards))
            return my_sorted[0] > their_sorted[0]
        elif self.rank == self.THREE_OF_KIND:
            raise NotImplementedError()
        elif self.rank == self.TWO_PAIRS:
            raise NotImplementedError()
        elif self.rank == self.ONE_PAIR:
            raise NotImplementedError()
        elif self.rank == self.HIGH_CARD:
            raise NotImplementedError()

        raise Exception("Shouldn't get here")

    def _all_same_suit(self):
        return any(all(card.suit == suit for card in self.cards) for suit in Card.suits)

    def _cards_consecutive(self):
        card_types = [card.value.type for card in sorted(self.cards)]
        for i in range(1, len(self.cards)):
            if Value.ordering.index(card_types[i - 1]) + 1 != Value.ordering.index(card_types[i]):
                return False
        return True

    def _have_n_of_same_type(self, n):
        card_values = [card.value for card in self.cards]
        card_types = [val.type for val in card_values]
        return any(card_types.count(t) == n for t in Value.ordering)

    def _have_two_pairs(self):
        grouped = self.group_by_type()
        num_pairs = 0
        for t in grouped:
            if len(grouped[t]) == 2:
                num_pairs += 1
        return num_pairs == 2


player_1_wins = 0
with open('054_poker.txt', 'r') as f:
    for line in f:
        cards = [Card(s) for s in line.split()]
        p1_hand = Hand(cards[:6])
        p2_hand = Hand(cards[6:])
        if p1_hand > p2_hand:
            player_1_wins += 1

print(player_1_wins)
