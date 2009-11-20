def transpose_by_diatonic_interval(expr, diatonic_interval):
   '''.. versionadded:: 1.1.2

   Transpose all pitch carriers in `expr` by `diatonic_interval`. ::

      abjad>

   '''

   if not isinstance(diatonic_interval, DiatonicInterval):
      raise TypeError('must be diatonic interval.')

   

def _transpose_pitch_carrier_by_diatonic_interval(
   pitch_carrier, diatonic_interval):

   if isinstance(pitch_carrier, Pitch):
      pass
