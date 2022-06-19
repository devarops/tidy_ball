from tidyball import (
    read_json,
    get_appearences_on_season_for_player,
    get_goals_on_season_for_player,
    get_passes_on_season_for_player,
)

data_to_test = "tests/data/data_file_16482_2021.json"
aguirre = read_json(data_to_test)
data_to_test = "tests/data/data_file_6485_2021.json"
berterame = read_json(data_to_test)


def test_get_appearences_on_season_for_player():
    aguirre_appearences = {
        "appearences": 32,
        "lineups": 26,
        "minutes": 2257,
        "number": None,
        "position": "Attacker",
        "rating": "7.165625",
        "captain": False,
    }
    _assert_appearences_on_season_for(aguirre, aguirre_appearences)
    berterame_appearences = {
        "appearences": 37,
        "lineups": 37,
        "minutes": 3219,
        "number": None,
        "position": "Attacker",
        "rating": "7.029729",
        "captain": False,
    }
    _assert_appearences_on_season_for(berterame, berterame_appearences)


def _assert_appearences_on_season_for(player, expected_appearences):
    obtained_appearences = get_appearences_on_season_for_player(player)
    assert expected_appearences == obtained_appearences


def test_get_passes_on_season_for_player():
    berterame_passes = {"total": 722, "key": 41, "accuracy": 13}
    _assert_passes_on_season_for(berterame, berterame_passes)
    aguirre_passes = {"total": 446, "key": 25, "accuracy": 9}
    _assert_passes_on_season_for(aguirre, aguirre_passes)


def _assert_passes_on_season_for(player, expected_passes):
    aguirre_passes = get_passes_on_season_for_player(player)
    assert expected_passes == aguirre_passes


def test_get_goals_on_season_for_player():
    aguirre_goals = {
        "total": 12,
        "conceded": 0,
        "assists": 4,
        "saves": None,
    }
    _assert_goals_on_season_for(aguirre, aguirre_goals)
    berterame_goals = {
        "total": 17,
        "conceded": 0,
        "assists": 5,
        "saves": None,
    }
    _assert_goals_on_season_for(berterame, berterame_goals)


def _assert_goals_on_season_for(player, expected_goals):
    obtained_goals = get_goals_on_season_for_player(player)
    assert expected_goals == obtained_goals
