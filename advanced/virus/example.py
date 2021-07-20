from des import Process, Resource, Simulation


@Process
def player(name, ball, miss_prob=0.05):
    simulation = yield Process.GetSimulation()
    log = lambda msg: print(f"{simulation.time}: {name} {msg}")
    yield 0
    while True:
        with (yield ball.acquire()):
            yield 1
            if simulation.rng.random() < miss_prob:
                log(f"missed ball")
                raise Process.Fail()
        log(f"hit ball")


def ping_pong(*args, **kwargs):
    ball = Resource()
    sim = Simulation(*args, **kwargs)
    sim.launch(player("ping", ball) & player("PONG", ball) & player("f00b4r", ball))
    return sim


ping_pong().run()
