import core.event as event

class Publisher(object):
    # Set event object in class declaration.
    evt_foo = event.Event('here comes foo')

    def foo(self):
        # Do some actions and fire event.
        self.evt_foo()


# Event handler may be a function or a instance method etc.
# Every handler must accept two arguments; a sender and an event-specific
# parameter.
def handle_foo(sender, earg):
    print('foo!')


def handle_foo_again(sender, earg):
    print('foo again!')

if __name__ == '__main__':

    pub = Publisher()
    # Add event handler
    pub.evt_foo += handle_foo
    pub.evt_foo += handle_foo_again
    # This will cause Publiser.evt_foo event.
    pub.foo()
