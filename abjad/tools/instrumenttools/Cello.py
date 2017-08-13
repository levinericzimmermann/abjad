# -*- coding: utf-8 -*-
from abjad.tools.instrumenttools.Instrument import Instrument


class Cello(Instrument):
    r'''Cello.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> clef = abjad.Clef('bass')
            >>> abjad.attach(clef, staff[0])
            >>> cello = abjad.instrumenttools.Cello()
            >>> abjad.attach(cello, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { Cello }
                \set Staff.shortInstrumentName = \markup { Vc. }
                \clef "bass"
                c'4
                d'4
                e'4
                fs'4
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_default_tuning',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        name='cello',
        short_name='vc.',
        name_markup=None,
        short_name_markup=None,
        allowable_clefs=('bass', 'tenor', 'treble'),
        default_tuning=('C2', 'G2', 'D3', 'A3'),
        middle_c_sounding_pitch=None,
        pitch_range='[C2, G5]',
        ):
        import abjad
        Instrument.__init__(
            self,
            name=name,
            short_name=short_name,
            name_markup=name_markup,
            short_name_markup=short_name_markup,
            allowable_clefs=allowable_clefs,
            middle_c_sounding_pitch=middle_c_sounding_pitch,
            pitch_range=pitch_range,
            )
        self._performer_names.extend([
            'string player',
            'cellist',
            ])
        self._starting_clefs = type(self.allowable_clefs)(['bass'])
        self._is_primary_instrument = True
        self._default_tuning = abjad.Tuning(default_tuning)

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets cello's allowable clefs.

        ..  container:: example

            ::

                >>> cello.allowable_clefs
                ClefList([Clef(name='bass'), Clef(name='tenor'), Clef(name='treble')])

            ::

                >>> show(cello.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def default_tuning(self):
        r'''Gets cello's default tuning.

        ..  container:: example

            >>> cello.default_tuning
            Tuning(pitches=PitchSegment(['c,', 'g,', 'd', 'a']))

        Returns tuning.
        '''
        return self._default_tuning

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of cello's written middle C.

        ..  container:: example

            ::

                >>> cello.middle_c_sounding_pitch
                NamedPitch("c'")

            ::

                >>> show(cello.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        r'''Gets cello's name.

        ..  container:: example

            ::

                >>> cello.name
                'cello'

        Returns string.
        '''
        return Instrument.name.fget(self)

    @property
    def name_markup(self):
        r'''Gets cello's instrument name markup.

        ..  container:: example

            ::

                >>> cello.name_markup
                Markup(contents=['Cello'])

            ::

                >>> show(cello.name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets cello's range.

        ..  container:: example

            ::

                >>> cello.pitch_range
                PitchRange('[C2, G5]')

            ::

                >>> show(cello.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_name(self):
        r'''Gets cello's short instrument name.

        ..  container:: example

            ::

                >>> cello.short_name
                'vc.'

        Returns string.
        '''
        return Instrument.short_name.fget(self)

    @property
    def short_name_markup(self):
        r'''Gets cello's short instrument name markup.

        ..  container:: example

            ::

                >>> cello.short_name_markup
                Markup(contents=['Vc.'])

            ::

                >>> show(cello.short_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_name_markup.fget(self)
