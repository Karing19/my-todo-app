import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo page.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"checkbox_{index}"]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
