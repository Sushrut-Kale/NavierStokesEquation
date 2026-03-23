from manim import *
import numpy as np


class NavierStokesFullCombined(ThreeDScene):
    def construct(self):

        # ================== PART 1: INTRO ==================

        title = Text(
            "Topic : Navier-Stokes Equation",
            font="Times New Roman",
            weight=BOLD
        ).scale(1.2)
        title.set_color_by_gradient(BLUE, PURPLE)

        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        question = Text(
            "What is actually Navier-Stokes Equation?",
            font="Times New Roman",
            weight=BOLD
        ).scale(0.9)
        question.set_color_by_gradient(ORANGE, YELLOW)

        self.play(Write(question))
        self.wait(1)

        answer = Text(
            "The Navier-Stokes equation describes how\nfluids (liquids and gases) move.",
            font="Times New Roman"
        ).scale(0.8)
        answer.set_color_by_gradient(GREEN, TEAL)
        answer.next_to(question, DOWN, buff=0.7)

        self.play(FadeIn(answer, shift=UP))
        self.wait(1)

        self.play(FadeOut(question), FadeOut(answer))

        basic = Text(
            "Basic Idea :  F = m × a",
            font="Times New Roman",
            weight=BOLD
        ).scale(1.4)
        basic.set_color_by_gradient(RED, GOLD)

        self.play(Write(basic))
        self.wait(1)
        self.play(FadeOut(basic))


        # ================== PART 2: EQUATION ==================

        equation = MathTex(
            r"\rho",
            r"\left(",
            r"\frac{\partial \mathbf{v}}{\partial t}",
            "+",
            r"(\mathbf{v}\cdot\nabla)\mathbf{v}",
            r"\right)",
            "=",
            r"-\nabla p",
            "+",
            r"\mu \nabla^2 \mathbf{v}",
            "+",
            r"\mathbf{f}"
        ).scale(1.2)

        equation.set_color_by_tex(r"\rho", BLUE)
        equation.set_color_by_tex(r"\nabla p", RED)
        equation.set_color_by_tex(r"\mu", GREEN)
        equation.set_color_by_tex(r"\mathbf{f}", PURPLE)

        self.play(Write(equation))
        self.wait(2)


        # ================== EXPLANATIONS ==================

        density_box = SurroundingRectangle(equation[0], color=BLUE, buff=0.2)
        density_text = Text(
            "Density (ρ)\nMass per unit volume of the fluid",
            font_size=28,
            color=BLUE
        ).next_to(equation, DOWN)

        self.play(Create(density_box), FadeIn(density_text))
        self.wait(2)
        self.play(FadeOut(density_box), FadeOut(density_text))


        accel_box = SurroundingRectangle(
            VGroup(equation[2], equation[3], equation[4]),
            color=YELLOW
        )

        accel_text = Text(
            "Fluid Acceleration\nVelocity changing in time and space",
            font_size=28,
            color=YELLOW
        ).next_to(equation, DOWN)

        arrows = VGroup(*[
            Arrow(LEFT, RIGHT, color=YELLOW)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.4).shift(DOWN*2)

        self.play(Create(accel_box), FadeIn(accel_text))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(arrows), FadeOut(accel_box), FadeOut(accel_text))


        pressure_box = SurroundingRectangle(equation[7], color=RED)
        pressure_text = Text(
            "Pressure Gradient\nFluid moves from high pressure to low pressure",
            font_size=28,
            color=RED
        ).next_to(equation, DOWN)

        pressure_arrows = VGroup(*[
            Arrow(LEFT, RIGHT, color=RED)
            for _ in range(3)
        ]).arrange(DOWN, buff=0.4).shift(DOWN*2)

        self.play(Create(pressure_box), FadeIn(pressure_text))
        self.play(LaggedStart(*[GrowArrow(a) for a in pressure_arrows], lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(pressure_arrows), FadeOut(pressure_box), FadeOut(pressure_text))


        visc_box = SurroundingRectangle(equation[9], color=GREEN)
        visc_text = Text(
            "Viscosity (μ)\nInternal friction of the fluid",
            font_size=28,
            color=GREEN
        ).next_to(equation, DOWN)

        particles = VGroup(*[
            Dot(color=BLUE).shift(DOWN*2 + LEFT*2 + RIGHT*i)
            for i in range(5)
        ])

        self.play(Create(visc_box), FadeIn(visc_text))
        self.play(LaggedStart(*[p.animate.shift(RIGHT*0.5) for p in particles], lag_ratio=0.2))
        self.play(LaggedStart(*[p.animate.shift(LEFT*0.3) for p in particles], lag_ratio=0.2))
        self.wait(2)
        self.play(FadeOut(particles), FadeOut(visc_box), FadeOut(visc_text))


        force_box = SurroundingRectangle(equation[11], color=PURPLE)
        force_text = Text(
            "External Forces\nExamples: gravity or magnetic forces",
            font_size=28,
            color=PURPLE
        ).next_to(equation, DOWN)

        force_arrow = Arrow(UP, DOWN, color=PURPLE).shift(DOWN*2)

        self.play(Create(force_box), FadeIn(force_text))
        self.play(GrowArrow(force_arrow))
        self.wait(2)

        self.play(FadeOut(force_arrow), FadeOut(force_box), FadeOut(force_text))
        self.play(FadeOut(equation))


        # ================== PART 3: FBD ==================

        title = Text(
            "Fluid Element Free Body Diagram",
            gradient=(BLUE, PURPLE)
        ).scale(0.9)

        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        fluid = Square(side_length=2, color=WHITE)
        fluid.set_fill(BLUE, opacity=0.2)

        label = Text("Fluid Element", font_size=28).next_to(fluid, DOWN)

        self.play(Create(fluid), FadeIn(label))

        self.play(
            GrowArrow(Arrow(LEFT*3, LEFT, color=RED)),
            GrowArrow(Arrow(RIGHT*3, RIGHT, color=RED))
        )

        self.play(
            GrowArrow(Arrow(UP*3, UP, color=GREEN)),
            GrowArrow(Arrow(DOWN*3, DOWN, color=GREEN))
        )

        self.play(GrowArrow(Arrow(UP, DOWN*2, color=PURPLE).shift(RIGHT*2)))

        self.wait(2)

        # CLEAR BEFORE 3D
        self.play(*[FadeOut(m) for m in self.mobjects])


        # ================== PART 4: 3D FLUID ==================

        self.set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES)

        ground = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-6, 6],
            v_range=[-4, 4],
            resolution=(20, 20)
        ).set_fill(GREY_B, opacity=1)

        ground.set_stroke(width=0)

        rough_points = VGroup()
        for i in np.linspace(-5, 5, 20):
            for j in np.linspace(-3, 3, 10):
                dot = Sphere(radius=0.05).move_to([i, j, 0.05])
                rough_points.add(dot.set_color(GREY))

        t = ValueTracker(0)

        def flow_surface(u, v):
            time = t.get_value()
            z = 0.6 + 0.2*np.sin(2*u + time)
            return np.array([u, v, z])

        water = always_redraw(
            lambda: Surface(
                flow_surface,
                u_range=[-6, 6],
                v_range=[-4, 4],
                resolution=(30, 30)
            ).set_fill(color=BLUE_D, opacity=0.6)
        )

        boundary = Surface(
            lambda u, v: np.array([
                u,
                v,
                1.0 * (1 - np.exp(-(u + 6)/2))
            ]),
            u_range=[-6, 6],
            v_range=[-4, 4],
            resolution=(20, 20),
        ).set_fill(TEAL, opacity=0.25)

        self.play(Create(ground), FadeIn(rough_points))
        self.play(FadeIn(water), FadeIn(boundary))

        self.play(t.animate.set_value(8), run_time=6, rate_func=linear)

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        self.move_camera(
            phi=80*DEGREES,
            theta=10*DEGREES,
            zoom=2.2,
            run_time=3
        )

        self.play(t.animate.set_value(14), run_time=5, rate_func=linear)

        self.wait(2)
        