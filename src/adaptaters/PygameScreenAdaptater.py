from dataclasses import dataclass

@dataclass
class PygameScreenAdaptater:
    width_screen : int = 800
    height_screen : int = 800
    
    @property
    def get_width_screen(self):
        return self.width_screen
    
    @property
    def get_height_screen(self):
        return self.height_screen