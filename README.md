<h1 align="center">TextWidgetHighlight</h1>

<h3 align="center">Add highlighted text to a Text Widget.</h3>

```Python
textwidget_highlight = TextWidgetHighlight()

textwidget_highlight.add(text_widget=tb, the_text='Comments:', tag_name='0')
textwidget_highlight.add(text_widget=tb, the_text='Units:', tag_name='0')
textwidget_highlight.add(text_widget=tb, the_text='Equations/Assignments:', tag_name='0')
textwidget_highlight.add(text_widget=tb, the_text='Variables:', tag_name='0')
textwidget_highlight.add(text_widget=tb, tag_name='0', fg_color='blue', bg_color='lightyellow',
                      underline=True, underlinefg='red')
textwidget_highlight.add(text_widget=tb, tag_name='and', the_text='and', new_text='as well as',
                      qty=1, fg_color='yellow',bg_color='green', bold=True, relief=RAISED)
textwidget_highlight.add(text_widget=tb, tag_name='number', the_text='number', fg_color='blue',
                      bg_color='lightblue', underline=False, relief=GROOVE)
textwidget_highlight.add(text_widget=tb, tag_name='are', the_text='are',
                      fg_color='blue', bg_color='lightblue', underline=False, relief=SUNKEN, qty=2)
```
![Screenshot](https://github.com/Crystalline-Entity/TextWidgetHighlight/blob/main/textwidgethighlight_messagebox.png)

<h2 align='center'> OPTIONS </h2>
<div align='left'>

Parameters for the initial call to textbox_link. These are the defaults for all future calls.

  | **Parameter** | **Description** | **Default** |
  | --- | --- | --- |
  | underline | Underline the text | True |
  | underlinefg | underline colour | 'blue' |
  | fg_color | Highlighted text foreground colour | 'blue' |
  | bg_color | Highlighted txt, background colour | 'yellow' |
  | borderwidth | Apply a border to the highlighted text. If relief is specified, borderwidth is set to 3 | '' |
  | relief | Relief can be flat, raised. sunken, groove or ridge | '' |
  | bold | Make the text bold | False |
 
Parameters for calls to .add to create highlighted text.
These options are used to over-ride the options from the initial call above. These options apply only to this
call and are not saved.

  | **Parameter** | **Description** |
  | --- | --- |
  | text_widget |  The name of the text widget to apply highlights to |
  | the_text | The text in the widget to highlight |
  | tag_name | The name of the tag to use for this highlight|
  | new_text | Replacement text for the_text. Used if the_text has id options |
  | underline | Underline text |
  | underlinefg | Underline colour |
  | fg_color | Highlighted text foreground colour |
  | bg_color | Highlighted text background colour |
  | borderwidth | Apply a border to the highlighted text. If relief is specified, borderwidth is set to 3 |
  | relief | Relief can be flat, raised. sunken, groove or ridge |
  | bold | Make the text bold |

To change the default values for future calls, use .config and set the values.
