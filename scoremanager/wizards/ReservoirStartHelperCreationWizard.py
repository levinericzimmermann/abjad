# -*- encoding: utf-8 -*-
from scoremanager.wizards.Wizard import Wizard
from scoremanager import iotools


class ReservoirStartHelperCreationWizard(Wizard):
    r'''Reservoir start helper creation wizard.
    '''

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        return 'reservoir start helpers creation wizard'

    ### PRIVATE METHODS ###

    def _get_function_arguments(self, function_name):
        arguments = []
        if function_name in ('start at index n'):
            getter = self._io_manager.make_getter(where=self._where)
            getter.append_integer('index')
            result = getter._run()
            if self._session._backtrack():
                return
            arguments.append(result)
        return tuple(arguments)

    def _run(
        self,
        cache=False,
        clear=True,
        pending_user_input=None,
        is_test=False,
        ):
        if is_test:
            self._session._is_test = True
        self._io_manager._assign_user_input(pending_user_input)
        self._session._cache_breadcrumbs(cache=cache)
        while True:
            function_application_pairs = []
            self._session._push_breadcrumb(self._breadcrumb)
            selector = iotools.Selector(session=self._session)
            items = []
            items.append('start at index 0')
            items.append('start at index n')
            items.append('start at next unused index')
            selector.items = items
            with self._backtracking:
                function_name = selector._run(clear=clear)
            if self._session._backtrack():
                break
            elif not function_name:
                self._session._pop_breadcrumb()
                continue
            function_arguments = self._get_function_arguments(function_name)
            if self._session._backtrack():
                break
            elif function_arguments is None:
                self._session._pop_breadcrumb()
                continue
            function_application_pairs.append(
                (function_name, function_arguments))
            break
        self._session._pop_breadcrumb()
        self._session._restore_breadcrumbs(cache=cache)
        self.target = function_application_pairs
        return self.target
