<h1 align="center">TextboxHighlight</h1>

<h3 align="center">Add highlighted text to a TextBox.</h3>

```Python
textbox_highlight = TextboxHighlight()

textbox_highlight.add(text_widget=tb, the_text='Comments:', tag_name='0')
textbox_highlight.add(text_widget=tb, the_text='Units:', tag_name='0')
textbox_highlight.add(text_widget=tb, the_text='Equations/Assignments:', tag_name='0')
textbox_highlight.add(text_widget=tb, the_text='Variables:', tag_name='0')
textbox_highlight.add(text_widget=tb, tag_name='0', fg_color='blue', bg_color='lightyellow',
                      underline=True, underlinefg='red')
textbox_highlight.add(text_widget=tb, tag_name='and', the_text='and', new_text='as well as',
                      qty=1, fg_color='yellow',bg_color='green', bold=True, relief=RAISED)
textbox_highlight.add(text_widget=tb, tag_name='number', the_text='number', fg_color='blue',
                      bg_color='lightblue', underline=False, relief=GROOVE)
textbox_highlight.add(text_widget=tb, tag_name='are', the_text='are',
                      fg_color='blue', bg_color='lightblue', underline=False, relief=SUNKEN, qty=2)
```
![Screenshot](https://github.com/Crystalline-Entity/TextboxHIghlight/blob/main/textboxhighlight_messagebox.png)

  | **Parameter** | **Description** | **Default** |
  | --- | --- | --- |
  | underline | Underline the text | True |
  | underlinefg | underline colour | 'blue' |
  | fg_color | Highlighted text foreground colour | 'blue' |
  | bg_color | Highlighted txt, background colour | 'yellow' |
  | borderwidth | Apply a border to the highlighted text. If relief is specified, borderwidth is set to 3 | '' |
  | relief | Relief can be flat, raised. sunken, groove or ridge | '' |
  | bold | Make the text bold | False |
 
