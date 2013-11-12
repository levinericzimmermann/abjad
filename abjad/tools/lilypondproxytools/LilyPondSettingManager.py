# -*- encoding: utf-8 -*-
from abjad.tools import stringtools
from abjad.tools.abctools.AbjadObject import AbjadObject


class LilyPondSettingManager(AbjadObject):
    '''LilyPond setting namespace.
    '''

    ### INITIALIZER ###

    def __init__(self, **kwargs):
        # note_head__color = 'red' or staff__tuplet_full_length = True
        for key, value in kwargs.iteritems():
            proxy_name, attr_name = key.split('__')
            proxy = getattr(self, proxy_name)
            setattr(proxy, attr_name, value)

    ### SPECIAL METHODS ###

    def __eq__(self, arg):
        if isinstance(arg, type(self)):
            return self._get_attribute_tuples() == arg._get_attribute_tuples()
        return False

    def __getattr__(self, name):
        from abjad import ly
        from abjad.tools import lilypondproxytools
        if name.startswith('_'):
            try:
                return vars(self)[name]
            except KeyError:
                message = '{!r} object has no attribute: {!r}.'
                message = message.format(type(self).__name__, name)
                raise AttributeError(message)
        elif stringtools.snake_case_to_upper_camel_case(name) in ly.contexts:
            try:
                return vars(self)['_' + name]
            except KeyError:
                context = lilypondproxytools.LilyPondObjectProxy()
                vars(self)['_' + name] = context
                return context
        else:
            try:
                return vars(self)[name]
            except KeyError:
                message = '{!r} object has no attribute: {!r}.'
                message = message.format(type(self).__name__, name)
                raise AttributeError(message)

    def __repr__(self):
        body_string = ' '
        skeleton_strings = self._get_skeleton_strings()
        if skeleton_strings:
            # remove 'set__'
            skeleton_strings = [x[5:] for x in skeleton_strings]
            body_string = ', '.join(skeleton_strings)
        return '{}({})'.format(type(self).__name__, body_string)

    ### PRIVATE METHODS ###

    def _get_attribute_tuples(self):
        from abjad.tools import lilypondproxytools
        result = []
        for name, value in vars(self).iteritems():
            if isinstance(value, lilypondproxytools.LilyPondObjectProxy):
                prefixed_context_name = name
                context_name = prefixed_context_name.strip('_')
                context_proxy = value
                for attribute_name, attribute_value in \
                    context_proxy._get_attribute_pairs():
                    result.append(
                        (context_name, attribute_name, attribute_value))
            else:
                attribute_name, attribute_value = name, value
                result.append((attribute_name, attribute_value))
        return result

    def _get_skeleton_strings(self):
        result = []
        for attribute_tuple in self._get_attribute_tuples():
            if len(attribute_tuple) == 2:
                attribute_name, attribute_value = attribute_tuple
                result.append('%s=%s' % (
                    attribute_name, repr(attribute_value)))
            elif len(attribute_tuple) == 3:
                context_name, attribute_name, attribute_value = \
                    attribute_tuple
                key = '__'.join((context_name, attribute_name))
                string = '{}={}'.format(key, repr(attribute_value))
                result.append(string)
            else:
                raise ValueError
        result = ['set__' + x for x in result]
        return result
