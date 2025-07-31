import streamlit as st
from src.streamlit_achievements import streamlit_achievements

# Set page configuration
st.set_page_config(
    page_title="Achievement Demo",
    page_icon="🏆",
    layout="centered"
)

st.title("🎮 Achievement Component Demo")
st.markdown("---")

# Custom achievement section
st.header("🛠️ Create Custom Achievement")

with st.form("custom_achievement"):
    st.subheader("Design Your Own Achievement")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        custom_title = st.text_input(
            "Achievement Title", 
            value="Achievement Unlocked!",
            help="The main title that appears on the achievement"
        )
        custom_description = st.text_input(
            "Achievement Description", 
            value="Custom Achievement",
            help="The description of what was accomplished"
        )
        custom_points = st.number_input(
            "Points", 
            min_value=0, 
            max_value=1000, 
            value=10,
            help="Achievement point value"
        )
        custom_icon = st.text_input(
            "Icon Text/Emoji", 
            value="🎮",
            help="Text or emoji to display in the achievement icon"
        )
    
    with col_b:
        st.subheader("Color Customization")
        icon_background_color = st.color_picker(
            "Icon Background Color", 
            value="#8BC34A",
            help="Color for the circular icon background"
        )
        background_color = st.color_picker(
            "Achievement Background", 
            value="#2E7D32",
            help="Color for the expanding background"
        )
        text_color = st.color_picker(
            "Text Color", 
            value="#FFFFFF",
            help="Color for text and icon content"
        )
        shadow_opacity = st.slider(
            "Shadow Opacity", 
            min_value=0.0, 
            max_value=1.0, 
            value=0.3,
            help="Opacity for shadows and depth effects"
        )
    
    submitted = st.form_submit_button("🚀 Trigger Custom Achievement", type="primary")
    
    if submitted:
        streamlit_achievements(
            title=custom_title,
            description=custom_description,
            points=int(custom_points),
            icon_text=custom_icon,
            icon_background_color=icon_background_color,
            background_color=background_color,
            text_color=text_color,
            shadow_color=f"rgba(0,0,0,{shadow_opacity})"
        )

st.markdown("---")

# Code example section
st.header("💻 Code Example")

st.markdown("Here's how to use the achievement component in your code:")

code_example = '''import streamlit as st
from streamlit_achievements import streamlit_achievements

# Basic usage
if st.button("Trigger Achievement"):
    streamlit_achievements(
        title="Achievement Unlocked!",
        description="You Win",
        points=10,
        icon_text="🏆"
    )

# Custom achievement with different parameters
streamlit_achievements(
    title="Master Player",
    description="Completed All Levels",
    points=100,
    icon_text="⭐"
)
'''

st.code(code_example, language="python")

# Parameter documentation
st.header("📚 Parameters")

param_data = {
    "Parameter": ["title", "description", "points", "icon_text", "duration", "icon_background_color", "background_color", "text_color", "shadow_color", "auto_width", "floating", "position"],
    "Type": ["str", "str", "int", "str", "int", "str", "str", "str", "str", "bool", "bool", "str"],
    "Default": ['""', '""', "0", '""', "5000", "#8BC34A", "#2E7D32", "#FFFFFF", "rgba(0,0,0,0.3)", "True", "False", '"top"'],
    "Description": [
        "The main title displayed on the achievement",
        "The achievement description/name", 
        "Point value for the achievement",
        "Text or emoji displayed in the circular icon",
        "Duration in milliseconds for the animation",
        "Color for the circular icon background",
        "Color for the expanding background",
        "Color for text and icon content",
        "Color for shadows and depth effects",
        "Whether to auto-fit width to container",
        "Whether to display as floating overlay above content", 
        "Vertical position when floating: 'top', 'middle', 'bottom'"
    ]
}

st.table(param_data)

st.markdown("---")

# New Features Demo
st.header("🆕 New Features Demo")

col_new1, col_new2 = st.columns(2)

with col_new1:
    st.subheader("🔄 Auto-Width Achievement")
    if st.button("🌟 Responsive Achievement", key="responsive"):
        streamlit_achievements(
            title="Responsive Width!",
            description="Adapts to container",
            points=50,
            icon_text="🌟",
            auto_width=True  # Default behavior
        )

with col_new2:
    st.subheader("🎈 Floating Achievement")
    if st.button("🚀 Floating Achievement", key="floating"):
        streamlit_achievements(
            title="Floating Achievement!",
            description="Appears above content",
            points=100,
            icon_text="🚀",
            floating=True,
            position="top",
            auto_width=True,
            duration=7000
        )

st.markdown("---")