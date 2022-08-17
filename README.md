[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/arnaudmiribel/stoc/main)

# 📂 stoc: Table of contents in Streamlit

Learn how to generate table of contents in your Streamlit app! It's as easy as:

```python
from stoc import stoc
toc = stoc()

toc.h1("Demo")
st.write("...")

toc.h2("I want to talk about this")
st.write("...")

toc.h3("Smaller again")
st.write("...")

toc.h2("Another subtitle")
st.write("...")

toc.h3("I also should address that")
st.write("...")

toc.h2("Conclusion")
st.write("...")

toc.toc()
```

Or, if you have a large block of markdown, and want to add in a table of contents, you
can do:

```python
md = """
# Demo
...

## I want to talk about this
...

### Smaller again
...

## Another subtitle
...

### I also should address that
...

## Conclusion
...
"""

stoc.from_markdown(md)
```

And you'll see the table of contents being generated in your sidebar:

![stoc-demo](https://user-images.githubusercontent.com/7164864/153219373-efc78512-b53d-406e-9560-7c25a09b878f.gif)
