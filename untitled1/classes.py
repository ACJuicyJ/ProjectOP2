class boats:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.x = 0
        self.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.x, self.y)

    def update(self):
        self.x = random.randrange(0,400)
        self.y = random.randrange(0,400)