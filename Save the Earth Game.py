import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save the Earth")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_GREEN = (0, 100, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)
DARK_BLUE = (0, 0, 150)
EARTH_BLUE = (30, 144, 255)

# Fonts
try:
    title_font = pygame.font.SysFont("Arial", 24, bold=True)
    subtitle_font = pygame.font.SysFont("Arial", 20, bold=True)
    text_font = pygame.font.SysFont("Segoe UI Emoji", 18)
    button_font = pygame.font.SysFont("Segoe UI Emoji", 16)
    large_title_font = pygame.font.SysFont("Arial", 48, bold=True)
    medium_font = pygame.font.SysFont("Arial", 28, bold=True)
    small_font = pygame.font.SysFont("Arial", 14)  # Added small_font
except:
    title_font = pygame.font.SysFont("Arial", 24, bold=True)
    subtitle_font = pygame.font.SysFont("Arial", 20, bold=True)
    text_font = pygame.font.SysFont("Arial", 18)
    button_font = pygame.font.SysFont("Arial", 16)
    large_title_font = pygame.font.SysFont("Arial", 48, bold=True)
    medium_font = pygame.font.SysFont("Arial", 28, bold=True)
    small_font = pygame.font.SysFont("Arial", 14)  # Added small_font

# Image dimensions - ALL THE SAME SIZE
IMAGE_WIDTH = 400
IMAGE_HEIGHT = 250  # 400x250 = 1.6 ratio (close to 3:2)

# Create placeholder images as fallback
def create_placeholder(width, height, color=GRAY):
    """Create a simple gray placeholder image"""
    surface = pygame.Surface((width, height))
    surface.fill(color)
    pygame.draw.rect(surface, BLACK, (0, 0, width, height), 2)
    return surface

# Load or create images - ALL SAME SIZE
def load_image(filename, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, fallback_color=GRAY):
    """Load an image and scale to standard size"""
    try:
        image = pygame.image.load(filename)
        # Scale to standard size
        return pygame.transform.smoothscale(image, (width, height))
    except:
        print(f"Image not found: {filename}, using placeholder")
        return create_placeholder(width, height, fallback_color)

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')
    print("Created 'images' directory - please add your image files here")

# Load question images - ALL 400x250 (12 total)
question_images = {
    "ocean_trash": load_image("images/ocean_trash.png"),
    "factory_pollution": load_image("images/factory_pollution.png"),
    "overfishing": load_image("images/overfishing.png"),
    "coal_plant": load_image("images/coal_plant.png"),
    "traffic": load_image("images/traffic.png"),
    "energy_debate": load_image("images/energy_debate.png"),
    "plastic_bags": load_image("images/plastic_bags.png"),
    "community_project": load_image("images/community_project.png"),
    "deforestation": load_image("images/deforestation.png"),
    "climate_summit": load_image("images/climate_summit.png"),
    "funding_debate": load_image("images/funding_debate.png"),
    "global_warming": load_image("images/global_warming.png"),
}

# Load fact images - ALL 400x250 (36 total - 3 per question)
fact_images = {
    # Ocean trash facts (3 images)
    "ocean_trash_fact1": load_image("images/ocean_trash_fact1.png"),
    "ocean_trash_fact2": load_image("images/ocean_trash_fact2.png"),
    "ocean_trash_fact3": load_image("images/ocean_trash_fact3.png"),
    
    # Factory pollution facts (3 images)
    "factory_pollution_fact1": load_image("images/factory_pollution_fact1.png"),
    "factory_pollution_fact2": load_image("images/factory_pollution_fact2.png"),
    "factory_pollution_fact3": load_image("images/factory_pollution_fact3.png"),
    
    # Overfishing facts (3 images)
    "overfishing_fact1": load_image("images/overfishing_fact1.png"),
    "overfishing_fact2": load_image("images/overfishing_fact2.png"),
    "overfishing_fact3": load_image("images/overfishing_fact3.png"),
    
    # Coal plant facts (3 images)
    "coal_plant_fact1": load_image("images/coal_plant_fact1.png"),
    "coal_plant_fact2": load_image("images/coal_plant_fact2.png"),
    "coal_plant_fact3": load_image("images/coal_plant_fact3.png"),
    
    # Traffic facts (3 images)
    "traffic_fact1": load_image("images/traffic_fact1.png"),
    "traffic_fact2": load_image("images/traffic_fact2.png"),
    "traffic_fact3": load_image("images/traffic_fact3.png"),
    
    # Energy debate facts (3 images)
    "energy_debate_fact1": load_image("images/energy_debate_fact1.png"),
    "energy_debate_fact2": load_image("images/energy_debate_fact2.png"),
    "energy_debate_fact3": load_image("images/energy_debate_fact3.png"),
    
    # Plastic bags facts (3 images)
    "plastic_bags_fact1": load_image("images/plastic_bags_fact1.png"),
    "plastic_bags_fact2": load_image("images/plastic_bags_fact2.png"),
    "plastic_bags_fact3": load_image("images/plastic_bags_fact3.png"),
    
    # Community project facts (3 images)
    "community_project_fact1": load_image("images/community_project_fact1.png"),
    "community_project_fact2": load_image("images/community_project_fact2.png"),
    "community_project_fact3": load_image("images/community_project_fact3.png"),
    
    # Deforestation facts (3 images)
    "deforestation_fact1": load_image("images/deforestation_fact1.png"),
    "deforestation_fact2": load_image("images/deforestation_fact2.png"),
    "deforestation_fact3": load_image("images/deforestation_fact3.png"),
    
    # Climate summit facts (3 images)
    "climate_summit_fact1": load_image("images/climate_summit_fact1.png"),
    "climate_summit_fact2": load_image("images/climate_summit_fact2.png"),
    "climate_summit_fact3": load_image("images/climate_summit_fact3.png"),
    
    # Funding debate facts (3 images)
    "funding_debate_fact1": load_image("images/funding_debate_fact1.png"),
    "funding_debate_fact2": load_image("images/funding_debate_fact2.png"),
    "funding_debate_fact3": load_image("images/funding_debate_fact3.png"),
    
    # Global warming facts (3 images)
    "global_warming_fact1": load_image("images/global_warming_fact1.png"),
    "global_warming_fact2": load_image("images/global_warming_fact2.png"),
    "global_warming_fact3": load_image("images/global_warming_fact3.png"),
}

# Game state
class GameState:
    def __init__(self):
        self.score = 0
        self.category_points = {"Law":0, "Tech":0, "Personal":0, "Global":0}
        self.stage = 0
        self.question = 0
        self.questions = [
            # Stage 1: Oceans
            [
                {
                    "text": "🌊 You see trash polluting the ocean.",
                    "options": [
                        "🧹 Clean the trash yourself",
                        "📝 Work to pass a law banning dumping", 
                        "📢 Start a recycling awareness campaign"
                    ],
                    "responses": [
                        "😐 Good job, but it's a short-term fix.\n\n📚 Fact: Personal clean-ups help locally but don't stop future pollution.",
                        "🌟 Long-term impact, oceans stay cleaner.\n\n📚 Fact: Laws banning dumping can significantly reduce pollution over years.",
                        "✅ People learn better habits.\n\n📚 Fact: Awareness campaigns increase recycling rates and reduce waste."
                    ],
                    "scores": [1, 3, 2],
                    "categories": ["Personal", "Law", "Tech"],
                    "image_type": "ocean_trash",
                    "fact_types": ["ocean_trash_fact1", "ocean_trash_fact2", "ocean_trash_fact3"]
                },
                {
                    "text": "🏭 A factory is dumping waste into rivers.",
                    "options": [
                        "📢 Protest and report them",
                        "🔧 Install water filters yourself",
                        "🙈 Ignore it"
                    ],
                    "responses": [
                        "🌟 They get fined and change behavior.\n\n📚 Fact: Legal action can deter harmful industrial practices.",
                        "✅ You help a little, but problem continues.\n\n📚 Fact: Local filtration only partially mitigates pollution.",
                        "❌ River ecosystem collapses.\n\n📚 Fact: Ignoring industrial waste can decimate aquatic life."
                    ],
                    "scores": [3, 2, -2],
                    "categories": ["Law", "Tech", "Global"],
                    "image_type": "factory_pollution",
                    "fact_types": ["factory_pollution_fact1", "factory_pollution_fact2", "factory_pollution_fact3"]
                },
                {
                    "text": "🐟 Fishing companies are overfishing tuna.",
                    "options": [
                        "💰 Join them to earn money",
                        "📋 Support sustainable fishing rules",
                        "🙈 Ignore it"
                    ],
                    "responses": [
                        "❌ Overfishing hurts ecosystems.\n\n📚 Fact: Overfishing can collapse fish populations and affect food chains.",
                        "🌟 Sustainable fishing keeps oceans balanced.\n\n📚 Fact: Regulations can preserve fish stocks for the long term.",
                        "😐 Fish stocks keep shrinking.\n\n📚 Fact: Inaction causes gradual ecosystem decline."
                    ],
                    "scores": [-2, 3, -1],
                    "categories": ["Personal", "Law", "Global"],
                    "image_type": "overfishing",
                    "fact_types": ["overfishing_fact1", "overfishing_fact2", "overfishing_fact3"]
                }
            ],
            # Stage 2: Energy
            [
                {
                    "text": "🏭 Your city depends on coal plants.",
                    "options": [
                        "🌳 Plant trees",
                        "📜 Push for renewable energy policies",
                        "😴 Do nothing"
                    ],
                    "responses": [
                        "✅ Trees help but coal keeps polluting.\n\n📚 Fact: Reforestation aids air quality but doesn't replace clean energy.",
                        "🌟 Renewable energy is a long-term solution.\n\n📚 Fact: Policy change can shift energy systems sustainably.",
                        "❌ Air quality worsens.\n\n📚 Fact: Continued reliance on coal increases CO2 emissions."
                    ],
                    "scores": [2, 3, -2],
                    "categories": ["Personal", "Law", "Global"],
                    "image_type": "coal_plant",
                    "fact_types": ["coal_plant_fact1", "coal_plant_fact2", "coal_plant_fact3"]
                },
                {
                    "text": "🚗 Cars dominate the city streets.",
                    "options": [
                        "🛣️ Build more highways",
                        "🚆 Improve public transport", 
                        "🚲 Promote cycling lanes"
                    ],
                    "responses": [
                        "❌ More traffic = more pollution.\n\n📚 Fact: Expanding roads often increases car usage and emissions.",
                        "🌟 Public transport reduces emissions massively.\n\n📚 Fact: Efficient mass transit lowers urban CO2 output.",
                        "✅ Cycling helps, but only a small effect.\n\n📚 Fact: Active transport reduces emissions but uptake varies."
                    ],
                    "scores": [-2, 3, 2],
                    "categories": ["Personal", "Tech", "Personal"],
                    "image_type": "traffic",
                    "fact_types": ["traffic_fact1", "traffic_fact2", "traffic_fact3"]
                },
                {
                    "text": "🏛️ Energy policy debate in parliament.",
                    "options": [
                        "⚛️ Invest in nuclear power",
                        "🛢️ Invest in oil exploration",
                        "🌞 Fund solar/wind projects"
                    ],
                    "responses": [
                        "⚖️ Nuclear is risky but low-carbon.\n\n📚 Fact: Nuclear reduces CO2 but has safety concerns.",
                        "❌ More oil = climate disaster.\n\n📚 Fact: Fossil fuel expansion accelerates global warming.",
                        "🌟 Solar/wind leads to a greener future.\n\n📚 Fact: Renewable energy mitigates climate change."
                    ],
                    "scores": [0, -3, 3],
                    "categories": ["Tech", "Law", "Tech"],
                    "image_type": "energy_debate",
                    "fact_types": ["energy_debate_fact1", "energy_debate_fact2", "energy_debate_fact3"]
                }
            ],
            # Stage 3: Lifestyle
            [
                {
                    "text": "🛍️ Shops rely heavily on plastic bags.",
                    "options": [
                        "✅ Accept cheap plastic deals",
                        "📝 Ban plastic bags",
                        "👜 Promote reusable bags"
                    ],
                    "responses": [
                        "❌ Oceans fill with plastic waste.\n\n📚 Fact: Single-use plastics contribute to marine pollution.",
                        "🌟 Plastic waste reduced a lot.\n\n📚 Fact: Legislation reduces plastic consumption significantly.",
                        "✅ Some reduction, but slower change.\n\n📚 Fact: Reusable alternatives cut waste gradually."
                    ],
                    "scores": [-2, 3, 2],
                    "categories": ["Personal", "Law", "Personal"],
                    "image_type": "plastic_bags",
                    "fact_types": ["plastic_bags_fact1", "plastic_bags_fact2", "plastic_bags_fact3"]
                },
                {
                    "text": "👨‍👩‍👧‍👦 Community project time!",
                    "options": [
                        "🏖️ Organize a one-time beach clean-up",
                        "🎓 Educate schools on recycling",
                        "💼 Create an eco-startup for green tech"
                    ],
                    "responses": [
                        "😐 Nice event, but short-term.\n\n📚 Fact: Short clean-ups help locally but impact is temporary.",
                        "🌟 Kids learn lifelong eco-habits.\n\n📚 Fact: Education drives long-term sustainable behaviors.",
                        "✅ Tech can change the future of waste, but takes some time.\n\n📚 Fact: Green startups innovate solutions for sustainability."
                    ],
                    "scores": [1, 3, 2],
                    "categories": ["Personal", "Law", "Tech"],
                    "image_type": "community_project",
                    "fact_types": ["community_project_fact1", "community_project_fact2", "community_project_fact3"]
                },
                {
                    "text": "🌳 Food production causes deforestation.",
                    "options": [
                        "🥦 Promote plant-based diets",
                        "😴 Do nothing", 
                        "👨‍🌾 Encourage sustainable farming"
                    ],
                    "responses": [
                        "✅ Reduced meat demand lowers deforestation, but not all people may do it.\n\n📚 Fact: Plant-based diets reduce land use.",
                        "❌ Forests keep shrinking.\n\n📚 Fact: Ignoring deforestation causes biodiversity loss.",
                        "🌟 Farming improves, but slower progress.\n\n📚 Fact: Sustainable farming preserves ecosystems."
                    ],
                    "scores": [2, -2, 3],
                    "categories": ["Personal", "Global", "Law"],
                    "image_type": "deforestation",
                    "fact_types": ["deforestation_fact1", "deforestation_fact2", "deforestation_fact3"]
                }
            ],
            # Stage 4: Global
            [
                {
                    "text": "🌍 A global climate summit is happening.",
                    "options": [
                        "❌ Refuse to attend",
                        "🤝 Join but make weak promises",
                        "📝 Sign strong treaties for climate action"
                    ],
                    "responses": [
                        "❌ The world ignores the crisis.\n\n📚 Fact: Absence in global talks limits cooperation.",
                        "😐 Some action, but not enough.\n\n📚 Fact: Weak commitments delay meaningful change.",
                        "🌟 You commit to saving Earth, but you have to do it.\n\n📚 Fact: Strong treaties accelerate global climate action."
                    ],
                    "scores": [-3, 0, 3],
                    "categories": ["Global", "Law", "Global"],
                    "image_type": "climate_summit",
                    "fact_types": ["climate_summit_fact1", "climate_summit_fact2", "climate_summit_fact3"]
                },
                {
                    "text": "💰 Countries debate funding.",
                    "options": [
                        "🪖 Fund military expansion",
                        "🔬 Invest in green tech research",
                        "🛢️ Give subsidies to oil companies"
                    ],
                    "responses": [
                        "❌ Resources wasted on weapons.\n\n📚 Fact: Misallocated funding slows sustainability progress.",
                        "🌟 New tech accelerates solutions.\n\n📚 Fact: Research investments drive sustainable innovations.",
                        "💀 Oil expands, Earth suffers.\n\n📚 Fact: Fossil fuel subsidies increase emissions."
                    ],
                    "scores": [-2, 3, -3],
                    "categories": ["Global", "Tech", "Law"],
                    "image_type": "funding_debate",
                    "fact_types": ["funding_debate_fact1", "funding_debate_fact2", "funding_debate_fact3"]
                },
                {
                    "text": "🔥 Global warming is accelerating.",
                    "options": [
                        "😴 Do nothing",
                        "📢 Launch global awareness campaigns",
                        "🛡️ Invest in climate adaptation"
                    ],
                    "responses": [
                        "💀 Earth spirals into crisis.\n\n📚 Fact: Inaction worsens climate impacts.",
                        "🌟 People know more, global warming will slow down.\n\n📚 Fact: Awareness campaigns encourage global behavioral change.",
                        "✅ Humanity adapts, but the Earth keeps going worse.\n\n📚 Fact: Adaptation reduces harm but doesn't stop warming."
                    ],
                    "scores": [-3, 3, 2],
                    "categories": ["Global", "Law", "Tech"],
                    "image_type": "global_warming",
                    "fact_types": ["global_warming_fact1", "global_warming_fact2", "global_warming_fact3"]
                }
            ]
        ]
        self.stage_names = ["Oceans", "Energy", "Lifestyle", "Global Cooperation"]
        self.showing_result = False
        self.result_text = ""
        self.game_complete = False
        self.current_image_type = ""
        self.current_fact_types = []
        self.current_choice = -1
        self.show_title_screen = True

    def get_current_question(self):
        if self.stage < len(self.questions) and self.question < len(self.questions[self.stage]):
            return self.questions[self.stage][self.question]
        return None

    def make_choice(self, choice):
        question = self.get_current_question()
        if question:
            self.score += question["scores"][choice]
            self.category_points[question["categories"][choice]] += question["scores"][choice]
            self.result_text = question["responses"][choice]
            self.showing_result = True
            self.current_image_type = question["image_type"]
            self.current_fact_types = question["fact_types"]
            self.current_choice = choice

    def next_question(self):
        self.question += 1
        if self.question >= len(self.questions[self.stage]):
            self.question = 0
            self.stage += 1
            if self.stage >= len(self.questions):
                self.game_complete = True
        self.showing_result = False
        self.current_choice = -1

    def start_game(self):
        self.show_title_screen = False
        self.score = 0
        self.category_points = {"Law":0, "Tech":0, "Personal":0, "Global":0}
        self.stage = 0
        self.question = 0
        self.showing_result = False
        self.game_complete = False

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color=BLUE, hover_color=LIGHT_BLUE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)
        
        text_surf = button_font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

# Text rendering with proper line breaks
def render_multiline_text(text, font, color, max_width, line_spacing=5):
    """Render text with proper line breaks for \n characters"""
    lines = text.split('\n')
    surfaces = []
    
    for line in lines:
        if line.strip() == "":  # Empty line for spacing
            surfaces.append((None, font.get_height()))
            continue
            
        words = line.split(' ')
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_surface = font.render(test_line, True, color)
            
            if test_surface.get_width() <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    surface = font.render(' '.join(current_line), True, color)
                    surfaces.append((surface, surface.get_height()))
                current_line = [word]
        
        if current_line:
            surface = font.render(' '.join(current_line), True, color)
            surfaces.append((surface, surface.get_height() + line_spacing))
    
    return surfaces

# Create game state and buttons
game_state = GameState()
option_buttons = [
    Button(100, 350, 600, 50, ""),
    Button(100, 420, 600, 50, ""),
    Button(100, 490, 600, 50, "")
]
next_button = Button(350, 520, 100, 40, "Next", GREEN, DARK_GREEN)
restart_button = Button(300, 500, 200, 50, "🔄 Play Again", GREEN, DARK_GREEN)
start_button = Button(300, 470, 200, 60, "Start Game", GREEN, DARK_GREEN)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if game_state.show_title_screen:
            if start_button.is_clicked(mouse_pos, event):
                game_state.start_game()
        elif not game_state.game_complete:
            if game_state.showing_result:
                if next_button.is_clicked(mouse_pos, event):
                    game_state.next_question()
            else:
                for i, button in enumerate(option_buttons):
                    if button.is_clicked(mouse_pos, event):
                        game_state.make_choice(i)
        else:
            if restart_button.is_clicked(mouse_pos, event):
                game_state = GameState()
    
    # Update button hover states
    for button in option_buttons:
        button.check_hover(mouse_pos)
    next_button.check_hover(mouse_pos)
    restart_button.check_hover(mouse_pos)
    start_button.check_hover(mouse_pos)
    
    # Draw everything
    screen.fill(LIGHT_GRAY)
    
    if game_state.show_title_screen:
        # Draw title screen
        # Background gradient effect
        for i in range(HEIGHT):
            color_value = 200 + int(55 * (i / HEIGHT))
            pygame.draw.line(screen, (color_value, color_value, 255), (0, i), (WIDTH, i))
        
        # Title
        title_text = large_title_font.render("Save the Earth", True, DARK_BLUE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        
        # Subtitle
        subtitle_text = medium_font.render("Make Choices That Matter", True, DARK_GREEN)
        screen.blit(subtitle_text, (WIDTH // 2 - subtitle_text.get_width() // 2, 180))
        
        # Description
        desc_lines = [
            "Your decisions shape the future of our planet.",
            "Navigate through 4 stages of environmental challenges:",
            "🌊 Oceans • ⚡ Energy • 👨‍👩‍👧‍👦 Lifestyle • 🌍 Global Cooperation",
            "",
            "Each choice affects your score and determines Earth's fate!",
            "Learn real facts about environmental impact as you play."
        ]
        
        y_pos = 250
        for line in desc_lines:
            desc_surf = text_font.render(line, True, BLACK)
            screen.blit(desc_surf, (WIDTH // 2 - desc_surf.get_width() // 2, y_pos))
            y_pos += 35
        
        # Start button
        start_button.draw(screen)
        
        # Footer
        footer_text = small_font.render("Make a difference. Play now!", True, DARK_BLUE)
        screen.blit(footer_text, (WIDTH // 2 - footer_text.get_width() // 2, 550))
        
    elif not game_state.game_complete:
        # Draw stage title
        if game_state.stage < len(game_state.stage_names):
            stage_text = title_font.render(f"Stage {game_state.stage + 1}: {game_state.stage_names[game_state.stage]}", True, DARK_BLUE)
            screen.blit(stage_text, (WIDTH // 2 - stage_text.get_width() // 2, 20))
        
        # Draw score
        score_text = text_font.render(f"Score: {game_state.score}", True, BLACK)
        screen.blit(score_text, (20, 20))
        
        if game_state.showing_result:
            # Draw result section with fact image
            result_lines = render_multiline_text(game_state.result_text, text_font, BLACK, 700)
            y_pos = 120
            
            # Draw the main result text
            for surface, height in result_lines:
                if surface is not None:
                    screen.blit(surface, (WIDTH // 2 - surface.get_width() // 2, y_pos))
                y_pos += height
            
            # Draw fact image below the text (show the fact corresponding to the choice)
            fact_y = y_pos + 20
            if game_state.current_choice >= 0 and game_state.current_choice < len(game_state.current_fact_types):
                fact_image = fact_images[game_state.current_fact_types[game_state.current_choice]]
                screen.blit(fact_image, (WIDTH // 2 - fact_image.get_width() // 2, fact_y))
            
            next_button.draw(screen)
        else:
            # Draw question section with image
            question = game_state.get_current_question()
            if question:
                # Draw question image at the top
                question_image = question_images[question["image_type"]]
                screen.blit(question_image, (WIDTH // 2 - question_image.get_width() // 2, 60))
                
                # Draw question text below the image
                question_y = 60 + question_image.get_height() + 20
                question_surf = text_font.render(question["text"], True, BLACK)
                screen.blit(question_surf, (WIDTH // 2 - question_surf.get_width() // 2, question_y))
                
                # Draw options below the question
                option_start_y = question_y + 50
                for i, (button, option) in enumerate(zip(option_buttons, question["options"])):
                    button.rect.y = option_start_y + i * 70
                    button.text = option
                    button.draw(screen)
    else:
        # Draw final outcome
        title = title_font.render("Final Outcome", True, DARK_BLUE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))
        
        # Determine ending
        outcome_icon = ""
        outcome_text = ""
        if game_state.score >= 24:
            outcome_icon = "🌟✨"
            outcome_text = "Excellent Ending: Earth is thriving! Humanity and nature live in balance."
        elif game_state.score >= 16:
            outcome_icon = "🙂"
            outcome_text = "Good Ending: Earth is much better, though challenges remain."
        elif game_state.score >= 8:
            outcome_icon = "😐"
            outcome_text = "Neutral Ending: Some progress, but big problems still hurt Earth."
        elif game_state.score >= 0:
            outcome_icon = "💀"
            outcome_text = "Bad Ending: Earth is in crisis, future generations struggle."
        else:
            outcome_icon = "☠️"
            outcome_text = "Catastrophic Ending: Humanity failed. Earth becomes unlivable."
        
        # Draw outcome
        y_pos = 80
        
        # Draw outcome with icon
        outcome_display = f"{outcome_icon} {outcome_text}"
        outcome_lines = render_multiline_text(outcome_display, text_font, BLACK, 700)
        for surface, height in outcome_lines:
            if surface is not None:
                screen.blit(surface, (WIDTH // 2 - surface.get_width() // 2, y_pos))
            y_pos += height
        
        # Draw final score
        y_pos += 20
        score_text = subtitle_font.render(f"Final Score: {game_state.score}", True, BLACK)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, y_pos))
        
        # Draw category points
        y_pos += 50
        category_title = subtitle_font.render("Category Points", True, DARK_BLUE)
        screen.blit(category_title, (WIDTH // 2 - category_title.get_width() // 2, y_pos))
        
        y_pos += 40
        for category, points in game_state.category_points.items():
            cat_text = text_font.render(f"{category}: {points}", True, BLACK)
            screen.blit(cat_text, (WIDTH // 2 - cat_text.get_width() // 2, y_pos))
            y_pos += 30
        
        # Draw final feedback
        y_pos += 20
        feedback_title = subtitle_font.render("Final Feedback", True, DARK_BLUE)
        screen.blit(feedback_title, (WIDTH // 2 - feedback_title.get_width() // 2, y_pos))
        
        y_pos += 40
        max_points = max(game_state.category_points.values())
        leaders = [cat for cat, pts in game_state.category_points.items() if pts == max_points and pts > 0]
        
        if len(leaders) == 1:
            cat = leaders[0]
            if cat == "Law":
                feedback = "📝 You focused on laws: strong policies reshaped society."
            elif cat == "Tech":
                feedback = "🔬 You focused on technology: innovation pushed sustainability forward."
            elif cat == "Personal":
                feedback = "👤 You focused on personal choices: community habits slowly changed the Earth."
            elif cat == "Global":
                feedback = "🌍 You focused on global cooperation: international efforts drove large-scale change."
        elif len(leaders) == 2:
            feedback = f"⚖️ Balanced efforts: You combined {leaders[0]} and {leaders[1]}, shaping a mixed future."
        elif len(leaders) == 3:
            feedback = f"🔺 Tri-fold approach: You spread efforts across {', '.join(leaders)}, making broad progress."
        elif len(leaders) == 4:
            feedback = "🎯 Perfectly balanced: You addressed every area, giving Earth the best chance to thrive!"
        else:
            feedback = "📈 Your efforts were scattered across different approaches."
        
        # Draw feedback
        feedback_lines = render_multiline_text(feedback, text_font, BLACK, 700)
        for surface, height in feedback_lines:
            if surface is not None:
                screen.blit(surface, (WIDTH // 2 - surface.get_width() // 2, y_pos))
            y_pos += height
        
        # Position restart button at the bottom
        restart_button.rect.y = min(y_pos + 30, 500)
        restart_button.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()