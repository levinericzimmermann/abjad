from abjad.tools.marktools.get_annotations_attached_to_component import get_annotations_attached_to_component


def is_component_with_annotation_attached(expr, annotation_name=None, annotation_value=None):
    '''.. versionadded:: 2.3

    True when `expr` is component with annotation attached::

        >>> note = Note("c'4")
        >>> marktools.Annotation('foo', 'bar')(note)
        Annotation('foo', 'bar')(c'4)

    ::

        >>> marktools.is_component_with_annotation_attached(note)
        True

    False otherwise::

        >>> note = Note("c'4")

    ::

        >>> marktools.is_component_with_annotation_attached(note)
        False

    Return boolean.
    '''
    from abjad.tools.componenttools.Component import Component

    if isinstance(expr, Component):
        for annotation in get_annotations_attached_to_component(expr):
            if annotation.name == annotation_name or annotation_name is None:
                if annotation.value == annotation_value or annotation_value is None:
                    return True

    return False
