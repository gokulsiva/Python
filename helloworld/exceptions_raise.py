class ShortException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = raw_input('Enter something : ')
    if len(text) < 3:
        raise ShortException(len(text), 3)
except ShortException as ex:
    print 'Input is {} in length it should be at least {} in length'.format(ex.length, ex.atleast)
except [EOFError, KeyboardInterrupt]:
    print 'Operation cancelled'
else:
    print 'Entered input is valid'

