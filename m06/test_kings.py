import pytest

from cards import C, D, H, JOKER, S, shuffle
from kings import Hand, count_points, drop_3, select_card


def make_hand(cards):
    player = Hand("Test")
    for card in cards:
        player.append(card)
    return player


@pytest.mark.parametrize(
    "cards, matching_cards, remaining_cards",
    [
        (
            [f"2{C}", f"2{D}", f"2{H}", f"5{C}", f"9{C}"],
            [f"2{C}", f"2{D}", f"2{H}"],
            [f"5{C}", f"9{C}"],
        ),
        (
            [f"9{C}", f"5{D}", f"2{S}", f"5{H}", f"5{C}"],
            [f"5{C}", f"5{D}", f"5{H}"],
            [f"2{S}", f"9{C}"],
        ),
        (
            [f"9{C}", f"5{C}", f"2{S}", f"9{D}", f"9{H}"],
            [f"9{C}", f"9{D}", f"9{H}"],
            [f"2{S}", f"5{C}"],
        ),
        (
            [f"10{C}", f"2{H}", f"10{D}", f"3{S}", f"10{H}"],
            [f"10{C}", f"10{D}", f"10{H}"],
            [f"2{H}", f"3{S}"],
        ),
    ],
)
def test_drop_3_discards_three_matching_cards(cards, matching_cards, remaining_cards):
    player = make_hand(cards)

    discarded = drop_3(player)

    assert discarded in matching_cards
    assert sorted(player.hand) == sorted(remaining_cards)


def test_drop_3_with_four_of_a_kind_removes_three_matching_cards():
    cards = [f"7{suit}" for suit in (C, D, H, S)] + [f"A{C}"]
    player = make_hand(cards)

    discarded = drop_3(player)

    assert discarded.startswith("7")
    assert len(player) == 2
    assert sum(card.startswith("7") for card in player) == 1
    assert f"A{C}" in player.hand


@pytest.mark.parametrize(
    "cards",
    [
        [f"2{C}", f"2{D}", f"5{H}", f"8{S}", f"9{C}"],
        [f"2{C}", f"4{D}", f"6{H}", f"8{S}", f"9{C}"],
    ],
    ids=["pair-only", "all-distinct"],
)
def test_drop_3_without_three_matching_cards_raises(cards):
    player = make_hand(cards)

    with pytest.raises(AssertionError, match="Called `drop_3` without 3 matching cards"):
        drop_3(player)


@pytest.mark.parametrize(
    "cards",
    [
        [f"2{C}", f"2{D}", f"2{H}", f"5{C}"],
        [f"2{C}", f"2{D}", f"2{H}", f"5{C}", f"9{C}", f"K{S}"],
    ],
    ids=["fewer-than-five", "more-than-five"],
)
def test_drop_3_requires_exactly_five_cards(cards):
    player = make_hand(cards)

    with pytest.raises(AssertionError):
        drop_3(player)


@pytest.mark.parametrize("mixup", [False, True])
def test_deck_contains_exactly_one_joker(mixup):
    deck = shuffle(mixup)

    assert deck.count(JOKER) == 1
    assert len(deck) == 53


def test_joker_is_worth_ten_points():
    assert count_points([JOKER]) == 10
    assert count_points([JOKER, f"A{S}", f"K{C}"]) == 11


@pytest.mark.parametrize("rank", ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
def test_joker_completes_a_pair_of_any_rank(rank):
    other_ranks = [candidate for candidate in ["2", "3", "4", "5"] if candidate != rank][:2]
    player = make_hand(
        [JOKER, f"{rank}{C}", f"{rank}{D}", f"{other_ranks[0]}{H}", f"{other_ranks[1]}{S}"]
    )

    discarded = drop_3(player)

    assert discarded in {JOKER, f"{rank}{C}", f"{rank}{D}"}
    assert sorted(player.hand) == sorted([f"{other_ranks[0]}{H}", f"{other_ranks[1]}{S}"])


def test_natural_three_of_a_kind_is_used_before_joker():
    player = make_hand([JOKER, f"7{C}", f"7{D}", f"7{H}", f"A{S}"])

    discarded = drop_3(player)

    assert discarded in {f"7{C}", f"7{D}", f"7{H}"}
    assert sorted(player.hand) == sorted([JOKER, f"A{S}"])


def test_drop_3_with_joker_and_four_distinct_ranks_raises():
    player = make_hand([JOKER, f"2{C}", f"4{D}", f"6{H}", f"8{S}"])

    with pytest.raises(AssertionError, match="Called `drop_3` without 3 matching cards"):
        drop_3(player)


def test_select_card_can_select_joker(monkeypatch):
    player = make_hand([JOKER, f"J{C}", f"5{D}"])
    monkeypatch.setattr("builtins.input", lambda _: "joker")

    assert select_card(player) == 0


def test_select_card_selects_jack_when_joker_is_also_present(monkeypatch):
    player = make_hand([JOKER, f"J{C}", f"5{D}"])
    monkeypatch.setattr("builtins.input", lambda _: "J")

    assert select_card(player) == 1