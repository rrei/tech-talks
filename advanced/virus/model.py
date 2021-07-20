from des import Resource, Simulation, Process


def model(*args, **kwargs):
    sim = Simulation(*args, **kwargs)
    clubs = {
        "Hacienda": Resource(capacity=5000),
        "Studio 54": Resource(capacity=4000),
        "Paradise Garage": Resource(capacity=3000),
    }
    sim.launch(customers(clubs))
    return sim



def customers(clubs):
    pass


# mandatory mask
# distancing <=> capacity
