from webbrowser import open_new as open_link
from tkinter import Tk, Toplevel, Label, font
class TextboxHighlight():
    """
    Author: Kevin Glentworth
    Date: August-2025
    Extends textbox widget to allow for text highlighting.
    __init__ sets the initial values for each configurable item.
    add allows the options to be changed for that item only.
    """
    def __init__(self,
                 underline: bool=True,
                 underlinefg: str='blue',
                 hover_ul: str='green',
                 hover_bg: str='orange',
                 fg_color: str='blue',
                 bg_color: str='yellow',
                 borderwidth: str='',
                 relief: str='',
                 bold: bool = False):
        self._underline = underline
        self._underlinefg = underlinefg
        self._hover_ul = hover_ul
        self._hover_bg = hover_bg
        self._fg_color = fg_color
        self._bg_color = bg_color
        self._borderwidth = borderwidth
        self._relief = relief
        self._bold = bold
        

    def add(self,
            text_widget,
            tag_name: str,
            the_text: str='',
            new_text: str = None,
            qty: int=-1,
            underline: bool=None,
            underlinefg: str=None,
            hover_ul: str=None,
            hover_bg: str=None,
            fg_color: str=None,
            bg_color: str=None,
            borderwidth: str=None,
            relief: str=None,
            bold: bool=None):
        """
        Highlight one or more words in a textbox.
        New text, if specified, replaces the existing text. 
        """
        try:
            str0: str = text_widget.get('1.0', 'end')
        except AttributeError:
            return
        num_found: int = 0
        if len(the_text) > 0:
            if str0.find(the_text) == -1:
                return
            text_length: int = len(the_text)
            find_location: int = 0
            while True:
                find_location = str0.find(the_text, find_location)
                text_length = len(the_text)
                if find_location == -1:
                    break
                begin_pos = '1.0 linestart+' + str(find_location) + 'c'
                if new_text is not None and len(new_text) > 0:
                    end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                    text_widget.configure(state='normal')
                    text_widget.delete(begin_pos, end_pos)
                    text_widget.insert(begin_pos, new_text)
                    text_widget.configure(state='disabled')
                    text_length = len(new_text)
                    str0: str = text_widget.get('1.0', 'end')
                end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
                text_widget.tag_add(tag_name, begin_pos, end_pos)
                find_location += text_length
                num_found += 1
                if num_found==qty:
                    break
        if text_widget.tag_nextrange(tag_name, '1.0') == 0:
            return
        self._text_widget = text_widget
        fc = self._fg_color if fg_color is None else fg_color
        bc = self._bg_color if bg_color is None else bg_color
        ul = self._underline if underline is None else underline
        uf = self._underlinefg if underlinefg is None else underlinefg
        bw = self._borderwidth if borderwidth is None else borderwidth
        r = self._relief if relief is None else relief
        b = self._bold if bold is None else bold
        text_widget.tag_config(tag_name, foreground=fc, background=bc)
        if ul:
            text_widget.tag_config(tag_name, underline=True, underlinefg=uf)
        if bw:
            text_widget.tag_config(tag_name, borderwidth=bw)
        if r: # Ensure borderwidth is at least 3 to permit relief to be actioned.
            if bw:
                i = int(bw)
                if i < 3:
                    bw1 = '3'
                else:
                    bw1 = str(i)
            else:
                bw1 = '3'
            text_widget.tag_config(tag_name, borderwidth=bw1, relief=r)
        if b: # If we pass just bold to tag_config, font=('bold',), it seems to use a different font than the textbox was created with.
            font_string = text_widget.cget('font') # returned font is str '{family} size'. Split on the } and then the { to separate family.
            b1 = font_string.split('}')
            b2 = b1[0].split('{')
            f = tuple((b2[1], b1[1])) + ('bold',)
            text_widget.tag_config(tag_name, font=(f))

        
    def configure(self, **kwargs):
        self.config(**kwargs)
        
        
    def config(self, **kwargs):
        if 'underline' in kwargs:
            self._underline = kwargs.pop('underline')
        if 'underlinefg' in kwargs:
            self._underlinefg = kwargs.pop('underlinefg')
        if 'hover_ul' in kwargs:
            self._hover_ul = kwargs.pop('hover_ul')
        if 'hover_bg' in kwargs:
            self._hover_bg = kwargs.pop('hover_bg')
        if 'fg_color' in kwargs:
            self._fg_color = kwargs.pop('fg_color')
        if 'bg_color' in kwargs:
            self._bg_color = kwargs.pop('bg_color')
        if 'borderwidth' in kwargs:
            self._borderwidth = kwargs.pop('borderwidth')
        if 'relief' in kwargs:
            self._relief = kwargs.pop('relief')
        if 'bold' in kwargs:
            self._bold = kwargs.pop('bold')
        if kwargs:
            raise ValueError(f'{list(kwargs.keys())} not supported.')
        
        
    def get_config(self) -> dict:
        return vars(TextboxHighlight())
                
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
