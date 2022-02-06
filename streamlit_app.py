import streamlit as st
import unidecode

st.session_state.toc = list()


def make_anchor():
    title_id = len(st.session_state.toc)
    st.write(
        f"""<span style="visibility:hidden;" id="title-{title_id}">""",
        unsafe_allow_html=True,
    )


def h1(text):
    st.write(f"# {text}")
    st.session_state.toc.append(("h1", text))


def h2(text):
    st.write(f"## {text}")
    st.session_state.toc.append(("h2", text))


def h3(text):
    st.write(f"### {text}")
    st.session_state.toc.append(("h3", text))


def toc():
    st.sidebar.title("Table of contents")
    markdown_toc = ""
    for title_size, title in st.session_state.toc:
        h = int(title_size.replace("h", ""))
        markdown_toc += " " * 2 * h + "- " + f"[{title}](#{normalize(title)})  \n"
    st.sidebar.write(markdown_toc)


def normalize(s):
    """
    Normalize titles as valid HTML ids for anchors
    >>> normalize("it's a test to spot how Things happ3n héhé")
    "it-s-a-test-to-spot-how-things-happ3n-h-h"
    """

    # Replace accents with "-"
    s_wo_accents = unidecode.unidecode(s)
    accents = [s for s in s if s not in s_wo_accents]
    for accent in accents:
        s = s.replace(accent, "-")

    # Lowercase
    s = s.lower()

    # Keep only alphanum and remove "-" suffix if existing
    normalized = (
        "".join([char if char.isalnum() else "-" for char in s]).strip("-").lower()
    )

    return normalized


h1("This is my crazy app")

h1("This is my crazy app")

h2("it's a test to spot how Things happ3n héhé")

# x = st.slider("Choose", 1, 10, key="widget_0")


# st.write(st.session_state)

st.write(
    """And that's how things happen my dear you know -- 
Lorem ipsum dolor mented ipsum dolor mented ipsum dolor mented 
ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum
ipsum dolor mented ipsum dolor mented ipsum dolor mented 
ipsum dolor mented ipsum dolor mented ipsum dolor mented 
 """
)

h3("Smaller again")

"""Just a detail"""

h2("Another subtitle")

"""And that's how things happen my dear you know -- Lorem ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented
"""

"""And that's how things happen my dear you know -- Lorem ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented
"""

"""And that's how things happen my dear you know -- Lorem ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented ipsum dolor mented
"""

h1("Conclusion")

"""What a great ride!"""

toc()

st.experimental_set_query_params(
    **{k: v for k, v in st.session_state.items() if k != "toc"}
)
