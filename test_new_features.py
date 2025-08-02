import streamlit as st
from src.streamlit_achievements import streamlit_achievements

# Set page configuration
st.set_page_config(
    page_title="Achievement Features Test",
    page_icon="🏆",
    layout="wide"
)

st.title("🎮 Achievement New Features Test")
st.markdown("---")

# Test Auto-Width Feature
st.header("🔄 Auto-Width Feature")
st.markdown("Test how achievements adapt to different container widths")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Narrow Column")
    if st.button("🎯 Narrow Achievement", key="narrow"):
        streamlit_achievements(
            title="Narrow Column",
            description="Auto-Width Test",
            points=25,
            icon_text="📏",
            auto_width=True
        )

with col2:
    st.subheader("Wide Column")
    if st.button("🎯 Wide Achievement", key="wide"):
        streamlit_achievements(
            title="Wide Column Achievement",
            description="This achievement spans the wider column",
            points=50,
            icon_text="📐",
            auto_width=True
        )

st.markdown("---")

# Test Fixed Width vs Auto Width
st.header("📐 Fixed Width vs Auto Width Comparison")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Fixed Width (400px)")
    if st.button("🔒 Fixed Width", key="fixed"):
        streamlit_achievements(
            title="Fixed Width",
            description="Always 400px wide",
            points=10,
            icon_text="🔒",
            auto_width=False
        )

with col_b:
    st.subheader("Auto Width")
    if st.button("🔄 Auto Width", key="auto"):
        streamlit_achievements(
            title="Auto Width",
            description="Adapts to container",
            points=10,
            icon_text="🔄",
            auto_width=True
        )

st.markdown("---")

# Test Floating Feature
st.header("🎈 Floating Achievements")
st.markdown("Test floating achievements that appear above page content")

col_top, col_mid, col_bot = st.columns(3)

with col_top:
    st.subheader("Top Position")
    if st.button("⬆️ Float Top", key="float_top"):
        streamlit_achievements(
            title="Top Achievement",
            description="Floating at top",
            points=100,
            icon_text="⬆️",
            floating=True,
            position="top",
            auto_width=True,
            duration=6000
        )

with col_mid:
    st.subheader("Middle Position")
    if st.button("➡️ Float Middle", key="float_middle"):
        streamlit_achievements(
            title="Middle Achievement",
            description="Floating in middle",
            points=200,
            icon_text="🎯",
            floating=True,
            position="middle",
            auto_width=True,
            duration=6000
        )

with col_bot:
    st.subheader("Bottom Position")
    if st.button("⬇️ Float Bottom", key="float_bottom"):
        streamlit_achievements(
            title="Bottom Achievement",
            description="Floating at bottom",
            points=300,
            icon_text="⬇️",
            floating=True,
            position="bottom",
            auto_width=True,
            duration=6000
        )

st.markdown("---")

# Test Different Floating Widths
st.header("📏 Floating Width Options")

col_fix, col_auto = st.columns(2)

with col_fix:
    st.subheader("Fixed Width Floating")
    if st.button("🔒 Fixed Float", key="fixed_float"):
        streamlit_achievements(
            title="Fixed Width Float",
            description="400px floating achievement",
            points=75,
            icon_text="🔒",
            floating=True,
            position="top",
            auto_width=False,
            duration=6000
        )

with col_auto:
    st.subheader("Auto Width Floating") 
    if st.button("🔄 Auto Float", key="auto_float"):
        streamlit_achievements(
            title="Auto Width Floating Achievement",
            description="Responsive floating achievement that adapts to screen",
            points=150,
            icon_text="🌟",
            floating=True,
            position="top",
            auto_width=True,
            duration=6000
        )

st.markdown("---")

# Demonstration content to show floating works above content
st.header("📄 Page Content")
st.markdown("""
This content demonstrates that floating achievements appear **above** the page content.
When you trigger floating achievements, they should appear as overlays on top of this text.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

**Try the floating achievements above to see them overlay this content!**
""")

# Show parameter examples
st.header("💻 Code Examples")

st.subheader("Auto-Width Achievement")
st.code("""
streamlit_achievements(
    title="Auto Width Achievement",
    description="Adapts to container width",
    points=25,
    icon_text="🔄",
    auto_width=True  # Default: True
)
""", language="python")

st.subheader("Floating Achievement")
st.code("""
streamlit_achievements(
    title="Floating Achievement", 
    description="Appears above page content",
    points=100,
    icon_text="🎈",
    floating=True,       # Default: False
    position="top",      # Options: "top", "middle", "bottom"
    auto_width=True,     # Works with floating too
    duration=6000        # Show longer for floating
)
""", language="python")

st.subheader("Fixed Width Achievement")
st.code("""
streamlit_achievements(
    title="Fixed Width Achievement",
    description="Always 400px wide",
    points=10,
    icon_text="🔒",
    auto_width=False     # Fixed 400px width
)
""", language="python")