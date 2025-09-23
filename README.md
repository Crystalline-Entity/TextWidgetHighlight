<h1 align="center">TextWidgetHighlight</h1>

<h3 align="center">Add highlighted text to a Text Widget.</h3>

```Python
text_widget_highlight = TextWidgetHighlight()
tb = Textwidget(...) with some text.
text_widget_highlight.add(text_widget=tb, the_text='Comments:', tag_name='0')
text_widget_highlight.add(text_widget=tb, the_text='Units:', tag_name='0')
text_widget_highlight.add(text_widget=tb, the_text='Equations/Assignments:', tag_name='0')
text_widget_highlight.add(text_widget=tb, the_text='Variables:', tag_name='0')
text_widget_highlight.add(text_widget=tb, tag_name='0', fg_color='blue', bg_color='lightyellow',
                          underline=True, underlinefg='red', italic=True)
text_widget_highlight.add(text_widget=tb, tag_name='and', the_text='and', new_text='as well as',
                          qty=1, fg_color='yellow',bg_color='green', bold=True, relief=RAISED)
text_widget_highlight.add(text_widget=tb, tag_name='number', the_text='number', fg_color='blue',
                          bg_color='lightblue', underline=False, relief=GROOVE)
text_widget_highlight.add(text_widget=tb, tag_name='are', the_text='are',
                          fg_color='blue', bg_color='lightblue', underline=False, relief=SUNKEN, qty=2)
text_widget_highlight.add(text_widget=tb, tag_name='enter', the_text='eNTer', superscript=True,
                          ignore_case=True, fg_color='orange')
text_widget_highlight.add(text_widget=tb, tag_name='is', the_text='is', ignore_case=True,
                          subscript=True, fg_color='blue', bg_color='yellow', alpha_adjacent=True)
```
![Screenshot](https://github.com/Crystalline-Entity/TextWidgetHighlight/blob/main/textwidgethighlight_messagebox.png)

<h2 align='center'> OPTIONS </h2>
<div align='left'>

Parameters for the initial call to TextWidgetHighlight. These are the defaults for all future calls.

  | **Parameter** | **Description** | **Default** |
  | --- | --- | --- |
  | fg_color | Highlighted text foreground colour | 'blue' |
  | bg_color | Highlighted txt, background colour | 'yellow' |
  | ignore_case | ignore the case of the text widget text| False |
  | alpha_adjacent | specifies if alphabetic characters are OK adjacent to the search string.<br>if True, search for 'went', will match twenty<br>if False, search for went will not match twenty. | True |
  | borderwidth | Apply a border to the highlighted text. If relief is specified, borderwidth is set to 3 | '' |
  | relief | Relief can be flat, raised. sunken, groove or ridge | '' |
  | underline | Underline the text | True |
  | underlinefg | underline colour | 'blue' |
  | bold | Make the text bold | False |
  | italic | Make the text italic | False |
  | superscript | Make the text superscript | False |
  | subscript | Make the text subscript | False |
  

 
Parameters for calls to .add to create highlighted text.
These options are used to over-ride the options from the initial call above. These options apply only to this
highlight and are not saved.

  | **Parameter** | **Description** |
  | --- | --- |
  | text_widget |  The name of the text widget to apply highlights to |
  | tag_name | The name of the tag to use for this highlight|
  | the_text | The text in the widget to highlight |
  | new_text | Replacement text for the_text. Used if the_text has options |
  | ignore_case | ignore the case of the text widget text| False |
  | alpha_adjacent | specifies if alphabetic characters are OK adjacent to the search string.<br>if True, search for 'went', will match twenty<br>if False, search for went will not match twenty. | True |
  | qty |  Number of occurrences to highlight default is 0,  highlight all|
  | underline | Underline the text |
  | underlinefg | underline colour |
  | borderwidth | Apply a border to the highlighted text. If relief is specified, borderwidth is set to 3 |
  | relief | Relief can be flat, raised, sunken, groove or ridge |
  | bold | Make the text bold |
  | italic | Make the text italic |
  | superscript | Make the text superscript |
  | subscript | Make the text subscript |

To change the default values for future calls, use .config and set the values.

Parameters for call to .modify, which changes an existing highlight.

  | **Parameter** | **Description** |
  | --- | --- |
  | text_widget |  The name of the text widget |
  | tag_name | The name of an existing tag to use for this change |
  | underline | Underline the text |
  | underlinefg | underline colour |
  | fg_color | Highlighted text foreground colour |
  | bg_color | Highlighted txt, background colour |
  | relief | Relief can be flat, raised. sunken, groove or ridge |
  | bold | Make the text bold |
  | italic | Make the text italic |
  | superscript | Make the text superscript |
  | subscript | Make the text subscript |

