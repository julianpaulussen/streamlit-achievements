// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

// Track current achievement to prevent interruptions  
let lastAchievementTime = 0;
let currentAchievementId = null;

function sendValue(value) {
  Streamlit.setComponentValue(value)
}

function createAchievement(title, description, points, iconText, duration, iconBackgroundColor, backgroundColor, textColor, shadowColor, timestamp) {
  const container = document.getElementById('root');
  
  // Use timestamp as unique achievement ID
  const achievementId = `achievement_${timestamp}`;
  
  // Don't interrupt ongoing animations (minimum 2 seconds between achievements)
  if (timestamp - lastAchievementTime < 2000 && currentAchievementId) {
    console.log('Preventing interruption of ongoing achievement');
    return;
  }
  
  // Check if same achievement is already showing using timestamp
  if (currentAchievementId === achievementId) {
    console.log('Same achievement already showing, skipping');
    return;
  }
  
  // Update tracking variables  
  lastAchievementTime = timestamp;
  currentAchievementId = achievementId;
  
  console.log('Creating achievement:', { title, description, points, iconText, achievementId });
  
  // Clear any existing achievements
  container.innerHTML = '';
  
  // Create the achievement element
  const achievementContainer = document.createElement('div');
  achievementContainer.className = 'achievement-container';
  achievementContainer.setAttribute('data-achievement-id', achievementId);
  
  // Set custom colors using CSS custom properties with fallbacks
  achievementContainer.style.setProperty('--light-green', iconBackgroundColor || '#8BC34A');
  achievementContainer.style.setProperty('--dark-green', backgroundColor || '#2E7D32');
  achievementContainer.style.setProperty('--text-color', textColor || '#FFFFFF');
  achievementContainer.style.setProperty('--shadow-color', shadowColor || 'rgba(0,0,0,0.3)');
  
  // Handle empty values - show defaults or hide elements
  const displayTitle = title || "";
  const displayDescription = description || "";
  const displayPoints = points || 0;
  const displayIcon = iconText || "";
  
  // Check if points should be displayed (not 0, not empty string, not null/undefined)
  const shouldShowPoints = displayPoints > 0 && displayPoints !== "" && displayPoints !== null;
  
  achievementContainer.innerHTML = `
    <div class="achievement-notification">
      <div class="achievement-background"></div>
      <div class="achievement-icon">${displayIcon}</div>
      <div class="achievement-content">
        <div class="achievement-title" style="display: ${displayTitle ? 'block' : 'none'}">${displayTitle}</div>
        <div class="achievement-description" style="display: ${displayDescription ? 'block' : 'none'}">${displayDescription}</div>
      </div>
      <div class="achievement-points" style="display: ${shouldShowPoints ? 'block' : 'none'}">${displayPoints}P</div>
    </div>
  `;
  
  container.appendChild(achievementContainer);
  
  // Auto-hide after specified duration
  // Make sure it stays visible for at least the animation duration
  const minDuration = Math.max(duration || 5000, 5000); // At least 5 seconds
  const hideTimeout = setTimeout(() => {
    const element = container.querySelector(`[data-achievement-id="${achievementId}"]`);
    if (element && !element.classList.contains('slide-out')) {
      console.log('Starting slide-out for achievement:', achievementId);
      element.classList.add('slide-out');
      setTimeout(() => {
        if (container.contains(element)) {
          container.removeChild(element);
          console.log('Achievement removed:', achievementId);
        }
        // Clear tracking when this specific achievement is done
        if (currentAchievementId === achievementId) {
          currentAchievementId = null;
        }
      }, 600); // Wait for slide-out animation
    }
  }, minDuration);
  
  // Store timeout ID on element for potential cleanup
  achievementContainer.setAttribute('data-timeout-id', hideTimeout);
  
  // Send completion status back to Streamlit
  sendValue({
    status: 'shown',
    title: title,
    description: description,
    points: points,
    timestamp: timestamp
  });
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
  // Get the data passed from Python
  const {
    title, 
    description, 
    points, 
    icon_text, 
    duration,
    icon_background_color,
    background_color, 
    text_color,
    shadow_color,
    timestamp
  } = event.detail.args;
  
  // Skip if no arguments are provided (initial render)
  if (!event.detail.args || timestamp === undefined) {
    return;
  }
  
  console.log('onRender called with:', { title, description, points, icon_text, timestamp });
  
  // Only create achievement if we have been called with valid parameters
  // This includes empty achievement tests
  createAchievement(
    title, 
    description, 
    points, 
    icon_text, 
    duration || 5000,
    icon_background_color || "#8BC34A",
    background_color || "#2E7D32", 
    text_color || "#FFFFFF",
    shadow_color || "rgba(0,0,0,0.3)",
    timestamp
  );
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height
Streamlit.setFrameHeight(120)
