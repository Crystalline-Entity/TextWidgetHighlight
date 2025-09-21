from webbrowser import open_new as open_link
from tkinter import Tk, Toplevel, Label, font
class TextWidgetHighlight():
    """
    Author: Kevin Glentworth
    Date: September-2025
    Version: 2.0
    Adds text highlighting to text in a text_widget.
    __init__ sets the initial values for each configurable item, colours, bold, superscript etc.
    .config changes those values, they will be applied to future highlights.
    .add creates a new highlight. Any values specified here, over-ride the __init__ settings, but only for this highlight.
        using .add with no the_text values, will modify the existing tag_name highlight, same function as .modify.
        qty defines how many occurrences to highlight, default of 0 highlights all.
    .modify allows an existing highlight to be changed.
    The text_widget is passed in the .add function, rather than the __init__ function. A single instance can
        then be used for all text_widgets.
    """
    def __init__(self,
                 fg_color: str='blue',
                 bg_color: str='yellow',
                 ignore_case: bool=False,
                 alpha_boundary: bool=True,
                 borderwidth: str='',
                 relief: str='',
                 underline: bool=False,
                 underlinefg: str='blue',
                 bold: bool=False,
                 italic: bool=False,
                 superscript: bool=False,
                 subscript: bool=False):
        self._fg_color = fg_color
        self._bg_color = bg_color
        self._ignore_case = ignore_case
        self._alpha_boundary = alpha_boundary
        self._borderwidth = borderwidth
        self._relief = relief
        self._underline = underline
        self._underlinefg = underlinefg
        self._bold = bold
        self._italic = italic
        self._superscript = superscript
        self._subscript = subscript
        

    def add(self,
            text_widget,
            tag_name: str,
            the_text: str='',
            new_text: str=None,
            ignore_case: bool=None,
            alpha_boundary: bool=None,
            qty: int=0,
            underline: bool=None,
            underlinefg: str=None,
            fg_color: str=None,
            bg_color: str=None,
            borderwidth: str=None,
            relief: str=None,
            bold: bool=None, 
            italic: bool=None,
            superscript: bool=None,
            subscript: bool=None):
        """
        Highlight one or more words in a text_widget.
        New text, if specified, replaces the existing text. 
        """
        try:
            str0: str = text_widget.get('1.0', 'end')
        except AttributeError:
            return
        self._text_widget = text_widget
        # Temporary variables are named as the actual variable with an _ appended.
        fg_color_ = self._fg_color if fg_color is None else fg_color
        bg_color_ = self._bg_color if bg_color is None else bg_color
        ignore_case_ = self._ignore_case if ignore_case is None else ignore_case
        alpha_boundary_ = self._alpha_boundary if alpha_boundary is None else alpha_boundary
        underline_ = self._underline if underline is None else underline
        underlinefg_ = self._underlinefg if underlinefg is None else underlinefg
        borderwidth_ = self._borderwidth if borderwidth is None else borderwidth
        relief_ = self._relief if relief is None else relief
        bold_ = self._bold if bold is None else bold
        italic_ = self._italic if italic is None else italic
        superscript_ = self._superscript if superscript is None else superscript
        subscript_ = self._subscript if subscript is None else subscript
        if ignore_case_:
            str0 = str0.lower()
            the_text = the_text.lower()
        num_found: int = 0
        if len(the_text) > 0:
            if str0.find(the_text) == -1:
                return
            text_length: int = len(the_text)
            find_location: int = 0
            while True:
                find_location = str0.find(the_text, find_location)
                if find_location == -1:
                    break
                text_length = len(the_text)
                found_whole_text = True
                if not alpha_boundary_: # check character before and after. If either is alpha, don't process this highlight.
                    first_char: int = find_location
                    last_char: int = find_location + text_length
                    if first_char > 0 and str0[first_char-1:first_char].isalpha():
                        found_whole_text = False
                    if last_char < len(str0) and str0[last_char:last_char+1].isalpha():
                        found_whole_text = False
                if not alpha_boundary_ and not found_whole_text:
                    find_location += text_length
                    continue
                begin_pos = '1.0 linestart+' + str(find_location) + 'c'
                if new_text is not None and len(new_text) > 0:
                    end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                    text_widget.configure(state='normal')
                    text_widget.delete(begin_pos, end_pos)
                    text_widget.insert(begin_pos, new_text)
                    text_widget.configure(state='disabled')
                    text_length = len(new_text)
                    str0: str = text_widget.get('1.0', 'end')
                    if ignore_case_:
                        str0 = str0.lower()
                end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                text_widget.tag_add(tag_name, begin_pos, end_pos)
                find_location += text_length
                num_found += 1
                if num_found==qty:
                    break
        if text_widget.tag_nextrange(tag_name, '1.0') == 0:
            return
        text_widget.tag_config(tag_name, foreground=fg_color_, background=bg_color)
        if underline_:
            text_widget.tag_config(tag_name, underline=True, underlinefg=underlinefg_)
        if borderwidth_:
            text_widget.tag_config(tag_name, borderwidth=borderwidth_)
        if relief_: # Ensure borderwidth is at least 3 to permit relief to be actioned.
            if borderwidth_:
                i = int(borderwidth_)
                if i < 3:
                    bw1 = '3'
                else:
                    bw1 = str(i)
            else:
                bw1 = '3'
            text_widget.tag_config(tag_name, borderwidth=bw1, relief=relief_)
        if superscript_:
            text_widget.tag_config(tag_name, offset=+1)
        if subscript_:
            text_widget.tag_config(tag_name, offset=-1)
        if bold_ or italic_: # If we just specify bold and/or italic, it seems to use a different font than the text widget was created with.
            font_string = text_widget.cget('font') # returned font is str '{family} size'. Split on the } and then the { to separate family.
            b1 = font_string.split('}')
            b2 = b1[0].split('{')
            f = tuple((b2[1], b1[1]))
            if bold_:
                f += ('bold',)
            if italic_:
                f += ('italic',)
            text_widget.tag_config(tag_name, font=(f))

        
    def modify(self,
               text_widget,
               tag_name: str,
               underline: bool=None,
               underlinefg: str=None,
               fg_color: str=None,
               bg_color: str=None,
               relief: str=None,
               bold: bool=None, 
               italic: bool=None,
               superscript: bool=None,
               subscript: bool=None):
        """
        Change the highlight for an existing tag. 
        """
        if underline is not None:
            if underline is False:
                text_widget.tag_config(tag_name, underline=False)
            else:
                if underlinefg is not None:
                    text_widget.tag_config(tag_name, underlinefg=underlinefg)
                text_widget.tag_config(tag_name, underline=True)
        if fg_color is not None:
            text_widget.tag_config(tag_name, foreground=fg_color)
        if bg_color is not None:
            text_widget.tag_config(tag_name, background=bg_color)
        if superscript is not None:
            text_widget.tag_config(tag_name, offset=+1)
        if subscript is not None:
            text_widget.tag_config(tag_name, offset=-1)
        # If we pass just bold or italic to tag_config, it seems to use a different font than the text widget was created with.
        if not (bold is None and italic is None):
            font_string = text_widget.cget('font') # returned font is str '{family} size'. Split on the } and then the { to separate family.
            b1 = font_string.split('}')
            b2 = b1[0].split('{')
            f = tuple((b2[1], b1[1]))
            if bold is True:
                f += ('bold',)
            else:
                f += ('normal',)
            if italic is True:
                f += ('italic',)
            else:
                f += ('roman',)
            text_widget.tag_config(tag_name, font=(f))
        
            
    def configure(self, **kwargs):
        self.config(**kwargs)
        
        
    def config(self, **kwargs):
        if 'underline' in kwargs:
            self._underline = kwargs.pop('underline')
        if 'underlinefg' in kwargs:
            self._underlinefg = kwargs.pop('underlinefg')
        if 'fg_color' in kwargs:
            self._fg_color = kwargs.pop('fg_color')
        if 'bg_color' in kwargs:
            self._bg_color = kwargs.pop('bg_color')
        if 'alpha_boundary' in kwargs:
            self._alpha_boundary = kwargs.pop('alpha_boundary')
        if 'ignore_case' in kwargs:
            self._ignore_case = kwargs.pop('ignore_case')
        if 'borderwidth' in kwargs:
            self._borderwidth = kwargs.pop('borderwidth')
        if 'relief' in kwargs:
            self._relief = kwargs.pop('relief')
        if 'bold' in kwargs:
            self._bold = kwargs.pop('bold')
        if 'italic' in kwargs:
            self._italic = kwargs.pop('italic')
        if 'superscript' in kwargs:
            self._italic = kwargs.pop('superscript')
        if 'subscript' in kwargs:
            self._italic = kwargs.pop('subscript')
        if kwargs:
            raise ValueError(f'{list(kwargs.keys())} not supported.')
        
        
    def get_config(self) -> dict:
        return vars(TextWidgetHighlight())
                
 
    def clear_all_tags(self, text_widget):
        self.clear_tag(text_widget, '@')


    def clear_tag(self, text_widget, tag_name: str|tuple|list|set = None):
        """
        pass one tagname to delete that tag, a list, tuple or set of tagnames to delete multiple tags, '@' or 'all' to delete all tags.
        """
        if tag_name is None:
            return
        if type(tag_name)is str:
            if tag_name == '@' or tag_name.lower() == 'all' :
                for tagname in text_widget.tag_names():
                    if tag_name != 'SEL':
                        text_widget.tag_delete(tagname)
            else:
                if tag_name != 'SEL':
                    text_widget.tag_delete(tag_name)
        else:
            if type(tag_name) in [tuple, list, set]:
                for tagname in tag_name:
                    text_widget.tag_delete(tagname)
            else:
                raise TypeError(f'{tag_name} is neither a list, tuple nor set. It is {str(type(tag_name))}.')
