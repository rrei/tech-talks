def person(sim):
    yield max(0, sim.rng.normal(1, 1))
    yield enter_club(sim)


def enter_club(sim):
    club = sim.get("club")
    drinks = 0
    yield club.enter()
    while sim.rng.random() < 1 - 1 / (1 + drinks):
        yield sim.rng.normal(0.5, 0.1)
        yield club.get_drink()
    yield club.leave()
