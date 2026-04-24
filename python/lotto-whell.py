from manim import *
class BouncingBall(Scene):
    def construct(self):
        width = 12
        height = 6
        box = Rectangle(width=width, height=height)
        box.set_stroke(width=8)

        ball = Dot(radius=0.15)
        ball.vx, ball.vy = 0.05, 0.05

        def update_circle(c):
            right_point = c.get_right()[0]
            left_point = c.get_left()[0]
            top_point = c.get_top()[1]
            bottom_point = c.get_bottom()[1]

            if right_point >= width/2 or left_point <= -width/2:
                c.vx *= -1
            if top_point >= height/2 or bottom_point <= -height/2:
                c.vy *= -1

            c.shift(c.vx * RIGHT + c.vy * UP)

        self.play(Create(ball), Create(box))
        ball.add_updater(update_circle)
        self.wait(5)