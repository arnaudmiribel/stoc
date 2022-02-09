[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/arnaudmiribel/stoc/main)

# 📂 stoc: Table of contents in Streamlit

Learn how to generate table of contents in your Streamlit app! It's as easy as:

```
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

And you'll see the table of contents being generated in your sidebar: