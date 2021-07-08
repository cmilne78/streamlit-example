import streamlit as st


def show():
    st.write(
        """
        ## ✅ To-do List
        
        Use this space to create a daily list of things to do. Keep on top of things. 
        """
    )

        # Define callback when text_input changed.
    def new_todo_changed():
        if st.session_state.new_todo:
            st.session_state.todos.append(
                {
                    "description": st.session_state.new_todo,
                    "done": False,
                }
            )
    # Define initial state.
    if "todos" not in st.session_state:
        st.session_state.todos = [
            {"description": "Done!", "done": False},
        ]



    # Show widgets to add new TODO.
    st.write(
        "<style>.main * div.row-widget.stRadio > div{flex-direction:row;}</style>",
        unsafe_allow_html=True,
    )
    st.text_input("What do you want to do?", on_change=new_todo_changed, key="new_todo")

    # Show all TODOs.
    write_todo_list(st.session_state.todos)


def write_todo_list(todos):
    "Display the todo list (mostly layout stuff, no state)."
    st.write("")
    col1, col2, _ = st.beta_columns([0.05, 0.8, 0.15])
    all_done = True
    for i, todo in enumerate(todos):
        done = col1.checkbox("", todo["done"], key=str(i))
        if done:
            format_str = (
                '<span style="color: grey; text-decoration: line-through;">{}</span>'
            )
        else:
            format_str = "{}"
            all_done = False
        col2.markdown(
            format_str.format(todo["description"]),
            unsafe_allow_html=True,
        )

    if all_done:
        st.success("Nice job on finishing all TODO items! Enjoy your day! 🎈")


if __name__ == "__main__":
    show()
