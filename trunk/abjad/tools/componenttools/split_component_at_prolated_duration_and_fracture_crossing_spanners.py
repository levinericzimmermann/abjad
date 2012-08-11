from abjad.tools.componenttools._split_component_at_duration import _split_component_at_duration


def split_component_at_prolated_duration_and_fracture_crossing_spanners(
    component, prolated_duration, tie_after=False):
    r'''.. versionadded:: 1.1

    Split `component` at `prolated_duration` and fracture crossing spanners.

    Return split parts::

        >>> t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
        >>> pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
        >>> beamtools.BeamSpanner(t[0])
        BeamSpanner(|2/8(2)|)
        >>> beamtools.BeamSpanner(t[1])
        BeamSpanner(|2/8(2)|)
        >>> spannertools.SlurSpanner(t.leaves)
        SlurSpanner(c'8, d'8, e'8, f'8)

    ::

        >>> f(t)
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }

    ::

        halves = componenttools.split_component_at_prolated_duration_and_fracture_crossing_spanners(t.leaves[0], Duration(1, 32))
        \new Staff {
            {
                \time 2/8
                c'32 () [
                c'16. (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }

    Function works on both leaves and containers.

    .. versionchanged:: 2.0
        renamed ``split.fractured_at_duration()`` to
        ``componenttools.split_component_at_prolated_duration_and_fracture_crossing_spanners()``.
    '''

    return _split_component_at_duration(component, prolated_duration,
        fracture_spanners=True, tie_after=tie_after)
