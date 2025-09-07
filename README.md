<h1 align="center">TextboxHighlight</h1>

<h3 align="center">Add highlighted text to a TextBox.</h3>

```Python
textbox_highlight = TextboxHighlight()

textbox_link.add(text_widget=tb, the_text='Complex Numbers:', tag_name='Complex',
                new_text='Complex Numbers',
                popup_fg='red', popup_bg='lightgreen', popup_border='purple',
                the_link='https://en.wikipedia.org/wiki/Complex_number')
textbox_link.add(text_widget=tb, the_text='Base Numbers:', tag_name='Base',
                the_link='https://en.wikipedia.org/wiki/Radix')
textbox_link.add(text_widget=tb, the_text='Roman Numbers:', tag_name='Roman',
                the_link='https://en.wikipedia.org/wiki/Roman_numerals')
textbox_link.add(text_widget=tb, the_text='3.1415927', tag_name='pi',
                the_link='https://en.wikipedia.org/wiki/Pi')
textbox_link.add(text_widget=tb, the_text='[EMail]', new_text='EMail',
                popup_font=('Courier New', 18), show_url=False,
                tag_name='email', the_link='mailto:username@domain')
```
![Screenshot](https://github.com/Crystalline-Entity/TextboxHIghlight/blob/main/textboxhighlight_messagebox.png)
