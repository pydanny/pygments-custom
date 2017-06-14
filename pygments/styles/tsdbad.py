# -*- coding: utf-8 -*-
"""
    pygments.styles.tsdbad
    ~~~~~~~~~~~~~~~~~~~~~~

    pygments Two Scoops of Django 'bad' theme

    :copyright: Copyright 2017 by Daniel Roy Greenfeld
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Token, Whitespace


class TSDBadStyle(Style):
    """
    pygments Two Scoops of Django 'bad' theme
    """

    background_color = '#666666'
    highlight_color = '#666666'

    styles = {
        Token:              '#f0f0f0',
        Whitespace:         '#666666',

        Comment:            'italic #f0f0f0',
        Comment.Preproc:    'italic bold #f0f0f0',
        Comment.Special:    'italic bold #f0f0f0 bg:#f0f0f0',

        Keyword:            'bold #f0f0f0',
        Keyword.Pseudo:     'nobold',
        Operator.Word:      'bold #f0f0f0',

        String:             '#f0f0f0',
        String.Other:       '#f0f0f0',

        Number:             '#f0f0f0',

        Name.Builtin:       '#f0f0f0',
        Name.Variable:      '#f0f0f0',
        Name.Constant:      '#f0f0f0',
        Name.Class:         'bold #f0f0f0',
        Name.Function:      'bold #f0f0f0',
        Name.Namespace:     'bold #f0f0f0',
        Name.Exception:     'bold #f0f0f0',
        Name.Tag:           'bold #f0f0f0',
        Name.Attribute:     'bold #f0f0f0',
        Name.Decorator:     'bold #f0f0f0',

        Generic.Heading:    'bold #ffffff',
        Generic.Subheading: 'underline #ffffff',
        Generic.Deleted:    '#f0f0f0',
        Generic.Inserted:   '#f0f0f0',
        Generic.Error:      '#f0f0f0',
        Generic.Emph:       'italic',
        Generic.Strong:     'bold',
        Generic.Prompt:     '#d0d0d0',
        Generic.Output:     '#d0d0d0',
        Generic.Traceback:  '#f0f0f0',

        Error:              'bg:#f0f0f0 #d0d0d0'
    }
