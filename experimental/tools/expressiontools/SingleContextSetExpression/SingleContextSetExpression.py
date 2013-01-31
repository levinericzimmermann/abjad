import abc
import copy
from experimental.tools.expressiontools.InputSetExpression import InputSetExpression


class SingleContextSetExpression(InputSetExpression):
    r'''Single-context set expression.

    Set `attribute` to `source` for single-context `target_timespan`::

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecificationInterface(score_template)
        >>> red_segment = score_specification.append_segment(name='red')

    ::

        >>> multiple_context_set_expression = red_segment.set_time_signatures([(4, 8), (3, 8)])

    ::

        >>> contexts = ['Voice 1', 'Voice 3']
        >>> multiple_context_set_expression = red_segment.set_divisions([(3, 16)], contexts=contexts)

    ::

        >>> score = score_specification.interpret()

    ::

        >>> single_context_set_expression = \
        ...     score_specification.specification.single_context_set_expressions[1]

    ::

        >>> z(single_context_set_expression)
        expressiontools.SingleContextDivisionSetExpression(
            source=expressiontools.PayloadExpression(
                ((3, 16),)
                ),
            target_timespan='red',
            target_context_name='Voice 1',
            fresh=True,
            persist=True
            )

    Composers create multiple-context set expressions with set methods.

    Multiple-context set expressions produce single-context set expressions.

    Single-context set expressions produce region expressions.
    '''

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self, attribute=None, source=None, target_timespan=None, target_context_name=None, 
        fresh=True, persist=True, truncate=None):
        InputSetExpression.__init__(self, attribute=attribute, source=source, 
            target_timespan=target_timespan, fresh=fresh, persist=persist, truncate=truncate)
        assert isinstance(target_context_name, (str, type(None)))
        self._target_context_name = target_context_name

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def storage_format(self):
        '''Single-context set expression storage format::

            >>> z(single_context_set_expression)
            expressiontools.SingleContextDivisionSetExpression(
                source=expressiontools.PayloadExpression(
                    ((3, 16),)
                    ),
                target_timespan='red',
                target_context_name='Voice 1',
                fresh=True,
                persist=True
                )

        Return string.
        '''
        return InputSetExpression.storage_format.fget(self)

    @property
    def target_context_name(self):
        '''Single-context set expression context name.

        Return string or none.
        '''
        return self._target_context_name

    ### PUBLIC METHODS ###

    def copy_set_expression_to_segment_name(self, segment_name):
        '''Create new single-context set expression. 

        Set new single-context set expression start segment identifier to `segment_name`.

        Set new single-context set expression `fresh` to false.

        Return new single-context set expression.
        '''
        assert isinstance(segment_name, str)
        if self.is_score_rooted:
            return 'score-anchored expression'
        new_set_expression = copy.deepcopy(self)
        new_set_expression._set_start_segment_identifier(segment_name)
        new_set_expression._fresh = False
        return new_set_expression

    @abc.abstractmethod
    def evaluate(self):
        '''Evaluate single-context set expression.

        Return timespan-scoped single-context set expression.
        '''
        pass
