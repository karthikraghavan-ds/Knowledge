
import streamlit as st
st.title("Cheatsheet")


# Sidebar for topic selection
topic = st.sidebar.selectbox(
	"Choose a topic:",
	["SQL", "Python", "Mathematics","Machine Learning", "Deep Learning", "GCP", "Gen AI","Git"]
)

# Show SQL content only if SQL is selected
if topic == "SQL":
	st.header("SQL :sunglasses:")
	st.subheader("1. Definitions", divider="blue")
	st.write("""**Data** - Raw pieces of Information.""")
	st.write("""**Database** - An organized collection of data stored so it’s easy to find, update, and manage.""")
	st.write("""**Data and its Types** - Text, Audio, Video, Images, etc.""")
	st.write("""**Structured** - Easy to store and retrieve data - Tabular data.""")
	st.write("""**Unstuctured** - Not easy to store and not easy to retrieve.""")
	st.write("""**Database Management System(DBMS)** - """)
	st.write("""**Keys**""")
	st.write("""**Entity Relationship Diagram(ERD)** - """)
	st.image("assets/sql_commands.png")
	

	st.subheader("2. Basic", divider="blue")
	st.write("""The query selects all columns from the table""")
	st.code("""SELECT * FROM `table`""")
	st.write("""NOTE - Using * means all columns but it is a good habit to always use column names""")
	st.write("""The query selects only required columns from the table""")
	st.code("""SELECT col1, col2 FROM `table`""")
	st.write("""The query selects all columns when using * but also adds the columns from the table if added after star""")
	st.code("""SELECT *,col1, col2 FROM `table`""")
	st.write("""The query selects all columns when using * but also adds the columns from the table if added after star""")
	st.code("""SELECT *,col1, col2 FROM `table`""")

# You can add content for other topics below