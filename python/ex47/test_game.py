# Exercise 47: test_game.py

# NOTE: this should be added to the tests directory inside a newly created project

from ex47.game import Room


def test_room():
    text = "This room has a pile of gold. There's a door to the north."
    gold = Room("GoldRoom", text)
    assert gold.name == "GoldRoom"
    assert gold.description == text
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in center")
    north = Room("North", "Test room to north")
    south = Room("South", "Test room to south")

    center.add_paths({ 'north': north, 'south': south })
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({ 'west': west, 'down': down })
    west.add_paths({ 'east': start})
    down.add_paths({ 'up': start })

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

