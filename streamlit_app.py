from textwrap import dedent

import streamlit as st

from stoc import stoc

st.set_page_config(
    page_icon="📂", page_title="stoc: Table of contents in Streamlit", layout="centered"
)
st.write("## 📂 stoc: Table of contents in Streamlit")
st.write(
    "This is a demo of stoc, a tool to help you create table of contents in Streamlit!"
)
st.write("Learn more in the [repository](https://github.com/arnaudmiribel/stoc).")

toc = stoc()

toc.h1("Show me code!")

"""This is how a table of contents gets generated using `stoc`:"""

method1, method2 = st.tabs(["Interspersed with other code", "Block of markdown"])

with method1:
    st.code(
        dedent(
            """
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
        """
        ),
        "python",
    )

with method2:
    st.code(
        dedent(
            """
            from stoc import stoc

            md = \"\"\"
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
            \"\"\"
            stoc.from_markdown(md)
            """
        ),
        "python",
    )

"""See that you can click on the different titles!"""

toc.h1("Demo")

toc.h2("I want to talk about this")

"""
Aliquam in mauris nulla. In convallis augue auctor, tincidunt lectus at, gravida lectus. Aliquam pellentesque porttitor nibh eget dapibus. Maecenas tincidunt mollis augue, non tincidunt elit fringilla eu. Ut ut arcu nec nibh bibendum pulvinar sed vitae massa. Vivamus condimentum eros ex, eu lobortis ante malesuada eu. Nulla consequat tortor eget rutrum luctus. Etiam sit amet sapien tincidunt, aliquam orci pellentesque, porta nulla. Nunc convallis imperdiet nulla, sed rutrum eros fermentum a. Pellentesque et rutrum nisi. Quisque placerat nisl quis ex feugiat pharetra. Vestibulum magna risus, elementum sed est non, pellentesque iaculis mauris. Nulla facilisi. Phasellus id mattis lorem.

Vestibulum sed purus porttitor, mattis mauris et, consectetur ligula. Praesent molestie sollicitudin imperdiet. In euismod mollis congue. Donec consectetur maximus arcu, id tempus nulla. Duis eget nunc sollicitudin sapien dictum vestibulum. Nunc efficitur pulvinar ullamcorper. Duis id condimentum sapien. Nullam sit amet pellentesque est, at lacinia arcu. Pellentesque varius eleifend odio non lacinia. Praesent fermentum urna id risus luctus, eget ultricies sapien porttitor. Etiam eget sollicitudin augue, non imperdiet augue.
"""

toc.h3("Smaller again")

"""Aliquam erat volutpat. Duis pulvinar lacus tortor, sed vestibulum metus vestibulum ut. Vivamus convallis blandit placerat. Aenean gravida magna lorem, ac interdum turpis aliquam vitae. Nullam hendrerit sed eros a pulvinar. Donec auctor tincidunt lacus quis porta. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras aliquam nunc dolor. Vivamus sed cursus ante, ut sodales nulla."""

toc.h2("Another subtitle")

"""Praesent et nisl at nisi fermentum molestie et eu nisi. Nulla condimentum purus ut neque mattis euismod. Donec tincidunt elit turpis, ut maximus diam rutrum non. Vestibulum consectetur ligula sem. Vestibulum auctor efficitur metus ac fermentum. Vivamus id venenatis ligula, eget ornare massa. In pretium accumsan dui, eget pellentesque erat pharetra at. Nulla lectus est, ullamcorper at lacinia in, gravida id leo. Praesent fringilla, lacus id euismod cursus, erat libero maximus nunc, in porta erat risus quis enim.

Morbi varius mattis odio et malesuada. Maecenas ac iaculis odio. Morbi felis lorem, imperdiet non dolor et, imperdiet finibus ligula. Ut a velit sit amet nisl varius mollis. Aliquam ac congue mauris, non lobortis tortor. Vivamus sollicitudin purus in posuere tincidunt. Nulla facilisi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
"""

toc.h3("I also should address that")

toc.h2("Conclusion")

"""Nunc feugiat rutrum finibus. Etiam eget lacinia sem, a mollis mauris. Maecenas ut egestas libero. Nam sed ipsum vel lorem ultrices molestie at at mi. Nullam vitae venenatis leo. Suspendisse lacinia urna dolor, vel malesuada metus ornare sed. Proin ut auctor eros, at sagittis erat. Maecenas sed nulla leo. Fusce sed enim ac lorem viverra elementum. Vivamus iaculis dignissim tortor non congue. In ac nisi faucibus tortor accumsan mollis. Curabitur vestibulum placerat elit, quis fermentum purus faucibus ut. Duis eleifend erat molestie, hendrerit purus vitae, volutpat neque. Mauris bibendum ornare orci ac mattis. Sed tincidunt diam magna, at pretium ligula ultrices at.
"""

toc.toc()
