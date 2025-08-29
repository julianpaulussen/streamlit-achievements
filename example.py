import streamlit as st
from src.streamlit_achievements import streamlit_achievements

# Set page configuration
st.set_page_config(
    page_title="Achievement Demo",
    page_icon="🏆",
    layout="centered"
)

st.title("🏆 Streamlit Achievements Demo")

st.markdown("""
This component allows you to easily add achievement notifications to your Streamlit app. Users can unlock achievements and see beautiful animated notifications with customizable styling!

## How to use:
1. **Install the component**: `pip install streamlit-achievements`
2. **Import it**: `from streamlit_achievements import streamlit_achievements`
3. **Use it**: Add achievement notifications to your app with customizable parameters

""")

st.markdown("---")

# Create Custom Achievement section
st.header("🛠️ Create Custom Achievement")

st.markdown("Design your own achievement with custom styling and behavior!")

with st.form("custom_achievement"):
    
    col_a, col_b, col_c  = st.columns(3)
    
    with col_a:
        st.subheader("📝 Achievement Content")
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
        st.subheader("🎨 Color Customization")
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
    
    with col_c:
        st.subheader("⚡ Behavior Settings")
        floating_duration = st.slider(
            "Display Duration (ms)", 
            min_value=3000, 
            max_value=10000, 
            value=6500,
            help="How long the achievement stays visible"
        )
        floating_dissolve = st.slider(
            "Dissolve Time (ms)", 
            min_value=0, 
            max_value=8000, 
            value=5300,
            help="Time to start disappearing. Default is ~2s after background fill if left 0."
        )
        st.subheader("🎯 Position Settings")
        floating_mode = st.checkbox(
            "Floating Mode", 
            value=True,
            help="Display as floating overlay above content"
        )
        floating_position = st.text_input(
            "Position",
            value="100px",
            help="Position: 'top', 'middle', 'bottom', or custom like '100px'"
        )

    
    submitted = st.form_submit_button("🚀 Trigger Custom Achievement", type="primary")
    
    if submitted:
        achievement_params = {
            "title": custom_title,
            "description": custom_description,
            "points": int(custom_points),
            "icon_text": custom_icon,
            "icon_background_color": icon_background_color,
            "background_color": background_color,
            "text_color": text_color,
            "shadow_color": f"rgba(0,0,0,{shadow_opacity})"
        }
        
        if floating_mode:
            achievement_params.update({
                "floating": True,
                "position": floating_position,
                "duration": floating_duration,
                "dissolve": floating_dissolve
            })
        
        streamlit_achievements(**achievement_params)

st.markdown("---")

# Code example section
st.header("💻 Code Example")

st.markdown("Here's how to use the achievement component in your code:")

code_example = '''import streamlit as st
from streamlit_achievements import streamlit_achievements

# Basic usage - Simple achievement notification
if st.button("Trigger Achievement"):
    streamlit_achievements(
        title="Achievement Unlocked!",
        description="You Win",
        points=10,
        icon_text="🏆"
    )

# Custom styled achievement
streamlit_achievements(
    title="Master Player",
    description="Completed All Levels",
    points=100,
    icon_text="⭐",
    icon_background_color="#FFD700",
    background_color="#FF8C00",
    text_color="#FFFFFF"
)

# Floating achievement with custom position and timing
streamlit_achievements(
    title="Floating Success!",
    description="You mastered floating mode!",
    points=75,
    icon_text="🚀",
    floating=True,
    position="middle",  # or "top", "bottom", or "100px"
    duration=6500,      # Display duration in milliseconds
    dissolve=5300,      # Disappear ~2s after background finish
    background_color="#9C27B0",
    icon_background_color="#E1BEE7"
)
'''

st.code(code_example, language="python")

st.markdown("---")



# Parameter documentation
st.header("⚙️ Parameters")

st.markdown("### `streamlit_achievements()`")

param_data = {
    "Parameter": [
        "title", 
        "description", 
        "points", 
        "icon_text", 
        "duration", 
        "icon_background_color", 
        "background_color", 
        "text_color", 
        "shadow_color", 
        "auto_width", 
        "floating", 
        "position", 
        "dissolve"
    ],
    "Type": [
        "str", 
        "str", 
        "int", 
        "str", 
        "int", 
        "str", 
        "str", 
        "str", 
        "str", 
        "bool", 
        "bool", 
        "str", 
        "int"
    ],
    "Description": [
        "The main title displayed on the achievement",
        "The achievement description/name", 
        "Point value for the achievement",
        "Text or emoji displayed in the circular icon",
        "Duration in milliseconds for the animation (default: 6500)",
        "Color for the circular icon background (default: '#8BC34A')",
        "Color for the expanding background (default: '#2E7D32')",
        "Color for text and icon content (default: '#FFFFFF')",
        "Color for shadows and depth effects (default: 'rgba(0,0,0,0.3)')",
        "Whether to auto-fit width to container (default: True)",
        "Whether to display as floating overlay above content (default: False)", 
        "Vertical position when floating: 'top', 'middle', 'bottom', or pixel value like '100px' (default: 'top')",
        "Time in milliseconds to start disappearing; if 0/omitted, it disappears ~2s after the background fully fills (default: 0)"
    ],
    "Required": [
        "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No"
    ]
}

st.dataframe(param_data, use_container_width=True, hide_index=True)
