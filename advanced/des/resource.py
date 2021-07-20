import collections

from .actions import Action


class Resource:
    def __init__(self, capacity=1):
        self.queue = collections.deque()
        self.capacity = capacity
        self.available = capacity

    def acquire(self, amount=1):
        return Request(resource=self, amount=amount)

    def _acquire(self, request):
        self.queue.append(request)
        self._service()

    def _release(self, request):
        self.available += request.amount
        self._service()

    def _cancel(self, request):
        self.queue.remove(request)

    def _service(self):
        while len(self.queue) > 0:
            request = self.queue[0]
            if self.available < request.amount:
                break
            self.available -= request.amount
            self.queue.popleft()
            request.complete()


class Request(Action):
    def __init__(self, resource, amount=1, simulation=None):
        super().__init__(simulation)
        self.resource = resource
        self.amount = amount

    def _start(self):
        self.resource._acquire(self)

    def _end(self, state):
        if state is not Action.State.COMPLETED:
            self.resource._cancel(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.is_completed:
            self.resource._release(self)
