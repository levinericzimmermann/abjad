import copy
from abjad.tools import sequencetools
from experimental.tools.settingtools.RegionCommand import RegionCommand


class DivisionRegionCommand(RegionCommand):
    r'''Division region command.

    Region command indicating durated period of time 
    to which a division-maker will apply.
    '''

    ### INITIALIZER ###

    def __init__(self, request=None, context_name=None, timespan=None, fresh=None, truncate=None):
        RegionCommand.__init__(self, request, context_name, timespan, fresh=fresh)
        assert isinstance(truncate, (bool, type(None))), repr(truncate)
        self._truncate = truncate

    ### PRIVATE METHODS ###

    def _can_fuse(self, expr):
        '''True when self can fuse `expr` to the end of self. Otherwise false.

        Return boolean.
        '''
        if not isinstance(expr, type(self)):
            return False
        if self.truncate:
            return False
        if expr.fresh or expr.truncate:
            return False
        if expr.request != self.request:
            return False
        return True

    def _get_payload(self, score_specification, voice_name):
        from experimental.tools import requesttools
        from experimental.tools import selectortools
        from experimental.tools import settingtools
        region_timespan = self.timespan
        region_duration = self.timespan.duration
        # TODO: maybe compress these two branches into a single suite
        if isinstance(self.request, selectortools.DivisionSelector):
            division_region_product = self.request._get_payload(score_specification)
            if division_region_product is None:
                return
            divisions = division_region_product.payload.divisions[:]
            divisions = sequencetools.repeat_sequence_to_weight_exactly(divisions, region_duration)
            divisions = [settingtools.Division(x) for x in divisions]
            division_list = division_region_product.payload.new(divisions=divisions)
            division_region_product = division_region_product.new(payload=division_list)
            right = self.timespan.start_offset
            left = division_region_product.timespan.start_offset
            translation = right - left
            division_region_product.translate(translation)
            return [division_region_product]
        elif isinstance(self.request, (settingtools.AbsoluteExpression,
                selectortools.BeatSelector, selectortools.MeasureSelector, 
                requesttools.DivisionSettingLookupRequest)):
            # TODO: maybe call self.request._get_payload(score_specification) instead
            divisions = self.request._get_payload(score_specification, self.voice_name)
            divisions = [settingtools.Division(x) for x in divisions]
            divisions = sequencetools.repeat_sequence_to_weight_exactly(divisions, region_duration)
            result = settingtools.DivisionRegionProduct(divisions, voice_name, region_timespan.start_offset)
            return [result]
        else:
            raise TypeError(self.request)

    ## READ-ONLY PUBLIC PROPERTIES ###

    @property
    def attribute(self):
        '''Return string.
        '''
        return 'divisions'

    @property
    def truncate(self):
        '''Return boolean.
        '''
        return self._truncate

    @property
    def voice_name(self):
        '''Aliased to division region command `context_name`.

        Return string.
        '''
        return self.context_name
