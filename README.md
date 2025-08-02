# streamlit-achievements

🎮 A Streamlit custom component that creates achievement notifications with smooth animations.

## Features

- **Design**: Authentic achievement look and feel
- **Smooth Animations**: Slide-in, background expansion, text fade-in, and slide-out effects
- **Customizable Colors**: Full control over icon, background, text, and shadow colors
- **Flexible Content**: Optional title, description, points, and icon text
- **Auto-Hide**: Configurable duration with automatic slide-out
- **Floating Mode**: Display achievements as overlays that float over content like `st.balloons()`
- **Dissolve Effect**: Gradual fade-out effect for smooth visual transitions
- **Flexible Positioning**: Preset positions (top, middle, bottom) or custom pixel positioning
- **Responsive**: Works on desktop and mobile devices

## Installation

```sh
pip install streamlit-achievements
```

## Basic Usage

```python
import streamlit as st
from streamlit_achievements import streamlit_achievements

# Simple achievement
if st.button("Unlock Achievement"):
    streamlit_achievements(
        title="Achievement Unlocked!",
        description="You Win",
        points=10,
        icon_text="🏆"
    )
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | str | `""` | The main title displayed on the achievement |
| `description` | str | `""` | The achievement description/name |
| `points` | int | `0` | Point value for the achievement (shows "P" suffix when > 0) |
| `icon_text` | str | `""` | Text or emoji displayed in the circular icon |
| `duration` | int | `5000` | Duration in milliseconds before auto-hide |
| `icon_background_color` | str | `"#8BC34A"` | Color for the circular icon background |
| `background_color` | str | `"#2E7D32"` | Color for the expanding background |
| `text_color` | str | `"#FFFFFF"` | Color for text and icon content |
| `shadow_color` | str | `"rgba(0,0,0,0.3)"` | Color for shadows and depth effects |
| `auto_width` | bool | `True` | Whether to auto-fit width to container |
| `floating` | bool | `False` | Whether to display as floating overlay above content |
| `position` | str | `"top"` | Vertical position when floating: "top", "middle", "bottom", or pixel value like "100px" |
| `dissolve` | int | `0` | Time in milliseconds to start dissolving/fading effect (0 = no dissolve) |
| `key` | str | `None` | Optional key for the component |

## Examples

### Gaming Achievements

```python
# Victory achievement
streamlit_achievements(
    title="Victory!",
    description="First Place",
    points=25,
    icon_text="🏆"
)

# Level up achievement
streamlit_achievements(
    title="Level Up!",
    description="Reached Level 10",
    points=15,
    icon_text="📈"
)

# Perfect score achievement
streamlit_achievements(
    title="Perfect!",
    description="100% Complete",
    points=100,
    icon_text="⭐"
)
```

### Custom Colors

```python
# Ocean theme
streamlit_achievements(
    title="Ocean Explorer",
    description="Deep Sea Discovery",
    points=25,
    icon_text="🌊",
    icon_background_color="#42A5F5",
    background_color="#1976D2"
)

# Sunset theme
streamlit_achievements(
    title="Sunset Warrior",
    description="Epic Journey",
    points=50,
    icon_text="🌅",
    icon_background_color="#FF9800",
    background_color="#F57C00"
)
```

### Empty Values

```python
# Minimal achievement (only description)
streamlit_achievements(
    description="Just Description",
    icon_text="✨"
)

# Empty achievement (shows with default styling)
streamlit_achievements()
```

### Custom Duration

```python
# Long duration achievement
streamlit_achievements(
    title="Epic Achievement!",
    description="Legendary Status",
    points=500,
    icon_text="👑",
    duration=7000  # Show for 7 seconds
)
```

### Floating Achievements

```python
# Floating at top
streamlit_achievements(
    title="Floating Achievement!",
    description="At the top of the screen",
    points=25,
    icon_text="🎈",
    floating=True,
    position="top"
)

# Floating in middle
streamlit_achievements(
    title="Centered Achievement!",
    description="In the middle of the screen",
    points=50,
    icon_text="⭐",
    floating=True,
    position="middle",
    background_color="#6200EA"
)

# Custom position (120px from top)
streamlit_achievements(
    title="Custom Position",
    description="120px from top",
    points=30,
    icon_text="📍",
    floating=True,
    position="120px"
)
```

### Dissolve Effect

```python
# Standard dissolve
streamlit_achievements(
    title="Dissolving Achievement",
    description="Fades after 3 seconds",
    points=20,
    icon_text="✨",
    duration=6000,
    dissolve=3000  # Start fading after 3 seconds
)

# Floating with dissolve
streamlit_achievements(
    title="Float + Dissolve",
    description="Best of both worlds!",
    points=40,
    icon_text="🌟",
    floating=True,
    position="middle",
    duration=8000,
    dissolve=4000
)
```

## Interactive Demo

To see all features in action, run the included example:

```python
import streamlit as st
from streamlit_achievements import streamlit_achievements

st.title("🎮 Achievement Demo")

# Custom achievement builder
with st.form("custom_achievement"):
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input("Title", "Achievement Unlocked!")
        description = st.text_input("Description", "You Win")
        points = st.number_input("Points", 0, 1000, 10)
        icon = st.text_input("Icon", "🎮")
    
    with col2:
        icon_background_color = st.color_picker("Icon Color", "#8BC34A")
        background_color = st.color_picker("Background", "#2E7D32")
        text_color = st.color_picker("Text Color", "#FFFFFF")
        shadow_opacity = st.slider("Shadow", 0.0, 1.0, 0.3)
    
    if st.form_submit_button("🚀 Show Achievement"):
        streamlit_achievements(
            title=title,
            description=description,
            points=points,
            icon_text=icon,
            icon_background_color=icon_background_color,
            background_color=background_color,
            text_color=text_color,
            shadow_color=f"rgba(0,0,0,{shadow_opacity})"
        )
```

## Styling Notes

- The component uses-inspired green colors by default
- All colors accept standard CSS color formats (hex, rgb, rgba, named colors)
- Points display includes "P" suffix when value > 0
- Empty fields are automatically hidden
- Text includes subtle shadows for better readability
- Responsive design adapts to different screen sizes

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
