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

st.markdown("---")

# Add floating achievements to the custom form
st.markdown("---")
st.header("🎮 Try Floating Mode in Custom Form")

with st.form("floating_achievement"):
    st.subheader("Create a Floating Achievement")
    
    floating_col_a, floating_col_b = st.columns(2)
    
    with floating_col_a:
        floating_title = st.text_input(
            "Achievement Title", 
            value="Floating Success!",
            help="The main title for your floating achievement"
        )
        floating_description = st.text_input(
            "Achievement Description", 
            value="You mastered floating mode!",
            help="The description for your floating achievement"
        )
        floating_points = st.number_input(
            "Points", 
            min_value=0, 
            max_value=1000, 
            value=75,
            help="Achievement point value"
        )
        floating_icon = st.text_input(
            "Icon Text/Emoji", 
            value="🚀",
            help="Text or emoji to display in the achievement icon"
        )
    
    with floating_col_b:
        position_type = st.radio(
            "Position Type",
            options=["Preset", "Custom"],
            index=0,
            help="Choose between preset positions or custom pixel position"
        )
        
        if position_type == "Preset":
            floating_position = st.selectbox(
                "Floating Position",
                options=["top", "middle", "bottom"],
                index=0,
                help="Preset position where the floating achievement should appear"
            )
        else:
            custom_position = st.slider(
                "Custom Position (px from top)",
                min_value=20,
                max_value=500,
                value=100,
                help="Custom position in pixels from the top of the screen"
            )
            floating_position = f"{custom_position}px"
        floating_bg_color = st.color_picker(
            "Background Color", 
            value="#9C27B0",
            help="Color for the floating achievement background"
        )
        floating_icon_color = st.color_picker(
            "Icon Color", 
            value="#E1BEE7",
            help="Color for the floating achievement icon"
        )
        floating_duration = st.slider(
            "Display Duration (ms)", 
            min_value=3000, 
            max_value=10000, 
            value=6000,
            help="How long the floating achievement stays visible"
        )
        floating_dissolve = st.slider(
            "Dissolve Time (ms)", 
            min_value=0, 
            max_value=8000, 
            value=3000,
            help="Time after which achievement starts to fade (0 = no dissolve)"
        )
    
    floating_submitted = st.form_submit_button("🌟 Launch Floating Achievement", type="primary")
    
    if floating_submitted:
        streamlit_achievements(
            title=floating_title,
            description=floating_description,
            points=int(floating_points),
            icon_text=floating_icon,
            floating=True,
            position=floating_position,
            duration=floating_duration,
            dissolve=floating_dissolve,
            icon_background_color=floating_icon_color,
            background_color=floating_bg_color,
            text_color="#FFFFFF"
        )

st.markdown("---")

# Parameter documentation
st.header("📚 Parameters")

param_data = {
    "Parameter": ["title", "description", "points", "icon_text", "duration", "icon_background_color", "background_color", "text_color", "shadow_color", "auto_width", "floating", "position", "dissolve"],
    "Type": ["str", "str", "int", "str", "int", "str", "str", "str", "str", "bool", "bool", "str", "int"],
    "Default": ['""', '""', "0", '""', "5000", "#8BC34A", "#2E7D32", "#FFFFFF", "rgba(0,0,0,0.3)", "True", "False", '"top"', "0"],
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
        "Vertical position when floating: 'top', 'middle', 'bottom', or pixel value like '100px'",
        "Time in milliseconds to start dissolving/fading effect (0 = no dissolve)"
    ]
}

st.table(param_data)

