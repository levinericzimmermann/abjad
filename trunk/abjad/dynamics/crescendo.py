from hairpin import _Hairpin

class Crescendo(_Hairpin):

   def __init__(self, music, start = None, stop = None, trim = None):
      _Hairpin.__init__(self, music, start = start, stop = stop, trim = trim)
      self._shape = '<'

   @property
   def _body(self):
      return '<'
