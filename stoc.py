import streamlit as st
import unidecode

DISABLE_LINK_CSS = """
<style>
a.toc {
    color: inherit;
    text-decoration: none; /* no underline */
}
</style>"""


class stoc:
    def __init__(self):
        self.toc_items = list()

    def h1(self, text: str, write: bool = True):
        if write:
            st.write(f"# {text}")
        self.toc_items.append(("h1", text))

    def h2(self, text: str, write: bool = True):
        if write:
            st.write(f"## {text}")
        self.toc_items.append(("h2", text))

    def h3(self, text: str, write: bool = True):
        if write:
            st.write(f"### {text}")
        self.toc_items.append(("h3", text))

    def toc(self):
        st.write(DISABLE_LINK_CSS, unsafe_allow_html=True)
        st.sidebar.caption("Table of contents")
        markdown_toc = ""
        for title_size, title in self.toc_items:
            h = int(title_size.replace("h", ""))
            markdown_toc += (
                " " * 2 * h
                + "- "
                + f'<a href="#{normalize(title)}" class="toc"> {title}</a> \n'
            )
        st.sidebar.write(markdown_toc, unsafe_allow_html=True)

    @classmethod
    def from_markdown(cls, text: str):
        self = cls()
        for line in text.splitlines():
            if line.startswith("###"):
                self.h3(line[3:], write=False)
            elif line.startswith("##"):
                self.h2(line[2:], write=False)
            elif line.startswith("#"):
                self.h1(line[1:], write=False)
        st.write(text)
        self.toc()



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
