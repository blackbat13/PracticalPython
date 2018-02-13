import cocos


class HelloWorld(cocos.layer.Layer):

    def __init__(self):
        # Always call super
        super(HelloWorld, self).__init__()

        # Create new label and add it to the layer
        self.create_label()

    def create_label(self):
        # Create new label
        label = cocos.text.Label(
            # Text of the label
            'Hello, world',
            # Label font name
            font_name='Times New Roman',
            # Label font size
            font_size=32,
            anchor_x='center', anchor_y='center'
        )

        # Define position of the new label
        label.position = 320, 240

        # Add new label to the layer
        self.add(label)


# Initialize the Director
# This creates game window
cocos.director.director.init()

# Create new layer
hello_layer = HelloWorld()

# Add new action to the layer
hello_layer.do(cocos.actions.Jump(y=50, x=200, jumps=5, duration=6))
# hello_layer.do(cocos.actions.Blink(times=10,duration=2))
hello_layer.do(cocos.actions.RotateBy(angle=360, duration=6))

# Add layer to the scene
main_scene = cocos.scene.Scene(hello_layer)

# Run the scene
cocos.director.director.run(main_scene)
