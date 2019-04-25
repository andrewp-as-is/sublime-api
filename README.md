#### Benefits
+   `sublime`, `sublime_plugin` modules available
+   learn/test Sublime Text API without pain :)

#### How it works
+   python files with `.subl` extension. `Build System` -> `Automatic`
+   python files with `.py` extension. `Build System` -> `Sublime API`

#### Examples
`error_message_example.subl`
```python
import sublime

sublime.error_message("Hello world")
```

or `error_message_example.py`, `Build System` -> `Sublime API`
```python
import sublime

sublime.error_message("Hello world")
```

#### Links
+   [API Reference](https://www.sublimetext.com/docs/3/api_reference.html)