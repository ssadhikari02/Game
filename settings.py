class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 230)
        
        # Ship Setting
        self.ship_speed = 1.5