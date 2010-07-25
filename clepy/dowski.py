from multiprocessing import Pipe, Process

class SubProcessIterator(object):
    """Instances of this class process iterators in separate processes."""
    def __init__(self, itertask, eoi='__eoi__'):
        """Create a new subprocess iterator.

        itertask : some iterable task to execute in a subprocess
        eoi : an end-of-iteration marker - returned from the subprocess
              to signal that iteration is complete.
        """
        self.client, self.master = Pipe()
        self.end_of_input = eoi
        pargs = [itertask, self.master, eoi]
        self.process = Process(target=self.work, args=pargs)
        self.started = False

    def _start(self):
        self.started = True
        self.process.start()

    @staticmethod
    def work(iterator, master, eoi):
        """The actual callable that is executed in the subprocess."""
        for chunk in iterator:
            master.send(chunk)
        master.send(eoi)

    def __iter__(self):
        if not self.started:
            self._start()
        return self

    def next(self):
        item = self.client.recv()
        if item != self.end_of_input:
            return item
        else:
            self.next = self._empty
            raise StopIteration

    def _empty(self, *args, **params):
        raise StopIteration

def piter(iterable, eoi=None):
    """Create a new subprocess iterator.

    iterable : some iterable task to execute in a subprocess
    eoi : an end-of-iteration marker - returned from the subprocess
          to signal that iteration is complete.
    """
    return SubProcessIterator(iterable, eoi=eoi)

