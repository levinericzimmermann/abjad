# -*- coding: utf-8 -*-


def show(expr, return_timing=False, **kwargs):
    r'''Shows `expr`.

    ..  container:: example

        Shows a note:

        ::

            >>> note = Note("c'4")
            >>> show(note) # doctest: +SKIP

    Abjad writes LilyPond input files to the ``~/.abjad/output/``
    directory by default.

    You may change this by setting the ``abjad_output_directory`` variable in
    the Abjad ``config.py`` file.

    Returns none when `return_timing` is false.

    Returns pair of `abjad_formatting_time` and `lilypond_rendering_time`
    when `return_timing` is true.
    '''
    import abjad
    if not hasattr(expr, '__illustrate__'):
        message = 'must have __illustrate__ method: {!r}.'
        message = message.format(expr)
        raise Exception(message)
    result = abjad.persist(expr).as_pdf(**kwargs)
    pdf_file_path = result[0]
    abjad_formatting_time = result[1]
    lilypond_rendering_time = result[2]
    success = result[3]
    if success:
        abjad.systemtools.IOManager.open_file(pdf_file_path)
    else:
        with open(abjad.abjad_configuration.lilypond_log_file_path, 'r') as fp:
            print(fp.read())
    if return_timing:
        return abjad_formatting_time, lilypond_rendering_time
