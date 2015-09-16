# event.py (improved)
# ref http://emptypage.jp/notes/pyevent.en.html ,
# https://gist.github.com/emptypage/a2a37eb76a565ac1cee4/raw/4385f90069badd10e004f46f8146c114c5cd4e2f/event.py ,
# https://gist.github.com/emptypage/289e2adacee94703b1c7/raw/d3e60560020aab64ff12007d78a6b5ee77d8dc1e/event_sample_2.py


class Event(object):
    def __init__(self, doc=None):
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return EventHandler(self, obj)

    def __set__(self, obj, value):
        pass


class EventHandler(object):
    def __init__(self, event, obj):

        self.event = event
        self.obj = obj

    def _getfunctionlist(self):

        """(internal use) """

        try:
            eventhandler = self.obj.__eventhandler__
        except AttributeError:
            eventhandler = self.obj.__eventhandler__ = {}
        return eventhandler.setdefault(self.event, [])

    def add(self, func):

        """Add new event handler function.
        
        Event handler function must be defined like func(sender, earg).
        You can add handler also by using '+=' operator.
        """

        self._getfunctionlist().append(func)
        return self

    def remove(self, func):

        """Remove existing event handler function.
        
        You can remove handler also by using '-=' operator.
        """

        self._getfunctionlist().remove(func)
        return self

    def fire(self, earg=None):

        """Fire event and call all handler functions
        
        You can call EventHandler object itself like e(earg) instead of 
        e.fire(earg).
        """

        for func in self._getfunctionlist():
            func(self.obj, earg)

    __iadd__ = add
    __isub__ = remove
    __call__ = fire
