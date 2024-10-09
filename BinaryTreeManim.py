from manim import *

class BinaryTreeScene(Scene):
    def construct(self):
        # root node
        root = self.create_node("1", position=UP*2)

        # 2nd level
        left_child = self.create_node("2", position=LEFT + UP)
        right_child = self.create_node("3", position=RIGHT + UP)

        # 3rd level
        left_left = self.create_node("4", position=LEFT * 2)
        left_right = self.create_node("5", position=ORIGIN)
        right_left = self.create_node("6", position=RIGHT)
        right_right = self.create_node("7", position=RIGHT * 2)

        # create edges
        edges = [
            self.connect_nodes(root, left_child),
            self.connect_nodes(root, right_child),
            self.connect_nodes(left_child, left_left),
            self.connect_nodes(left_child, left_right),
            self.connect_nodes(right_child, right_left),
            self.connect_nodes(right_child, right_right),
        ]
        
        #animate edges
        self.play(
            Create(root),
            Create(left_child),
            Create(right_child),
            Create(left_left),
            Create(left_right),
            Create(right_left),
            Create(right_right),
        )
        self.play(*[Create(edge) for edge in edges])
        self.wait(2)

    #node with label
    def create_node(self, label, position):
        circle = Circle(radius=0.5, color=WHITE)
        text = Text(label)
        node = VGroup(circle, text).move_to(position)
        return node

    # Creates line between nodes
    def connect_nodes(self, node1, node2):
        return Line(node1.get_center(), node2.get_center(), color=WHITE)


if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    scene = BinaryTreeScene()
    scene.render()
