from manim import *
import numpy as np


class NavierStokesMegaScene(Scene):
    def construct(self):

        # =========================================================
        # PART 1: BOUNDARY LAYER FLOW
        # =========================================================

        ground = VMobject()
        points = [
            LEFT*7 + DOWN*2,
            LEFT*5 + DOWN*2.2,
            LEFT*3 + DOWN*1.8,
            LEFT*1 + DOWN*2.3,
            RIGHT*1 + DOWN*1.9,
            RIGHT*3 + DOWN*2.2,
            RIGHT*5 + DOWN*1.8,
            RIGHT*7 + DOWN*2,
        ]
        ground.set_points_smoothly(points)
        ground.set_color("#8B4513")

        self.play(Create(ground))

        def boundary_func(x):
            return -2 + 1.2*(1 - np.exp(-(x+6)/3))

        boundary_curve = ParametricFunction(
            lambda t: np.array([t, boundary_func(t), 0]),
            t_range=[-6, 6],
            color=BLUE
        )

        self.play(Create(boundary_curve))

        particles = VGroup()
        arrows = VGroup()

        for y in np.linspace(-1.9, 2, 7):
            for x in np.linspace(-6, 6, 10):

                dot = Dot([x, y, 0], radius=0.04)

                if y <= boundary_func(x):
                    velocity = max(0, (y + 2)) * 0.8
                else:
                    velocity = 2.0

                arrow = Arrow(
                    start=dot.get_center(),
                    end=dot.get_center() + RIGHT * velocity,
                    buff=0,
                    stroke_width=2
                )

                particles.add(dot)
                arrows.add(arrow)

        flow = VGroup(particles, arrows)
        self.add(flow)

        def update_flow(mob, dt):
            for dot, arrow in zip(particles, arrows):

                x = dot.get_x()
                y = dot.get_y()

                boundary_y = boundary_func(x)

                if y <= boundary_y:
                    velocity = max(0, (y + 2)) * 0.8
                else:
                    velocity = 2.0

                dot.shift(RIGHT * velocity * dt)

                if dot.get_x() > 6:
                    dot.set_x(-6)

                arrow.put_start_and_end_on(
                    dot.get_center(),
                    dot.get_center() + RIGHT * velocity
                )

        flow.add_updater(update_flow)

        self.wait(6)

        no_slip = Text("v = 0", font_size=24).next_to(ground, DOWN)
        uniform = Text("Uniform Flow", font_size=28).to_edge(UP)

        self.play(Write(no_slip), Write(uniform))
        self.wait(3)

        flow.remove_updater(update_flow)

        self.play(*[FadeOut(m) for m in self.mobjects])


        # =========================================================
        # PART 2: CONTINUITY + MOMENTUM EQUATION
        # =========================================================

        continuity_title = Text(
            "Continuity Equation",
            gradient=(BLUE, PURPLE),
            font_size=34
        )

        continuity_eq = MathTex(r"\nabla \cdot \vec{V} = 0").scale(1.3)
        continuity_eq.set_color(YELLOW)

        continuity_group = VGroup(continuity_title, continuity_eq).arrange(DOWN)

        self.play(Write(continuity_title))
        self.play(Write(continuity_eq))
        self.wait(1)

        self.play(continuity_group.animate.to_edge(UP))

        momentum_title = Text(
            "Momentum Equation",
            gradient=(TEAL, GREEN),
            font_size=34
        )

        momentum_eq = MathTex(
            r"\rho \frac{D\vec{V}}{Dt}",
            "=",
            r"-\nabla p",
            "+",
            r"\rho \vec{g}",
            "+",
            r"\mu \nabla^2 \vec{V}"
        ).scale(1.1)

        momentum_eq[0].set_color(ORANGE)
        momentum_eq[2].set_color(RED)
        momentum_eq[4].set_color(BLUE)
        momentum_eq[6].set_color(GREEN)

        momentum_group = VGroup(momentum_title, momentum_eq).arrange(DOWN)
        momentum_group.move_to(ORIGIN)

        self.play(FadeIn(momentum_group, shift=UP))

        labels = VGroup(
            Text("Inertia", color=ORANGE, font_size=22),
            Text("Pressure", color=RED, font_size=22),
            Text("Body Force", color=BLUE, font_size=22),
            Text("Viscosity", color=GREEN, font_size=22),
        ).arrange(RIGHT, buff=0.6)

        labels.scale(0.8)
        labels.next_to(momentum_eq, DOWN, buff=0.6)

        self.play(FadeIn(labels, shift=UP))
        self.wait(1)

        conclusion_text = Text(
            "Conclusion: Solutions in 3D may not always exist or be smooth.\n"
            "Navier–Stokes remains one of the greatest unsolved problems.",
            font_size=26
        )

        conclusion_text.set_color_by_gradient(GRAY_B, WHITE)

        conclusion_box = SurroundingRectangle(
            conclusion_text,
            color=BLUE,
            buff=0.4
        )

        conclusion_group = VGroup(conclusion_box, conclusion_text)
        conclusion_group.to_edge(DOWN)

        self.play(FadeIn(conclusion_group, shift=UP))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])


        # =========================================================
        # PART 3: FINAL END SCREEN / IMPACT
        # =========================================================

        end_title = Text(
            "Navier–Stokes Equation",
            gradient=(BLUE, PURPLE)
        ).scale(1.2)

        subtitle = Text(
            "One of the Greatest Challenges in Physics & Mathematics",
            font_size=28
        ).next_to(end_title, DOWN)

        self.play(Write(end_title))
        self.play(FadeIn(subtitle))

        self.wait(3)