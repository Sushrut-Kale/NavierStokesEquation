from manim import *
import numpy as np
class NavierStokeseq(Scene):
    def construct(self):
        self.add_sound("teaching.mp3")
        title = Text("Understanding Navier-Stokes Equation", font_size=40)
        title.set_color_by_gradient(BLUE, TEAL)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        equation = MathTex(
            r"\rho \left( \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} \right)"
            r"= -\nabla p + \mu \nabla^2 \mathbf{u} + \mathbf{f}",
            font_size=36
        )
        equation.set_color(YELLOW)
        explanation = Text(
            "Force = Mass × Acceleration (Applied to Fluids)",
            font_size=24
        ).next_to(equation, DOWN)
        self.play(Write(equation))
        self.wait(2)
        self.play(FadeIn(explanation))
        self.wait(3)
        self.play(FadeOut(equation), FadeOut(explanation))
        particle = Dot(color=WHITE).scale(1.5)
        particle_label = Text("Fluid Particle", font_size=24).next_to(particle, UP)
        self.play(FadeIn(particle), Write(particle_label))
        pressure_arrow = Arrow(particle.get_center(), particle.get_center() + LEFT * 2, buff=0, color=RED)
        pressure_text = Text("Pressure", font_size=20).next_to(pressure_arrow, LEFT)
        gravity_arrow = Arrow(particle.get_center(), particle.get_center() + DOWN * 2, buff=0, color=BLUE)
        gravity_text = Text("Gravity", font_size=20).next_to(gravity_arrow, DOWN)
        wind_arrow = Arrow(particle.get_center(), particle.get_center() + RIGHT * 2, buff=0, color=GREEN)
        wind_text = Text("Wind Force", font_size=20).next_to(wind_arrow, RIGHT)
        self.play(GrowArrow(pressure_arrow), FadeIn(pressure_text))
        self.wait(1)
        self.play(GrowArrow(gravity_arrow), FadeIn(gravity_text))
        self.wait(1)
        self.play(GrowArrow(wind_arrow), FadeIn(wind_text))
        self.wait(2)
        self.play(
            FadeOut(particle), FadeOut(particle_label),
            FadeOut(pressure_arrow), FadeOut(pressure_text),
            FadeOut(gravity_arrow), FadeOut(gravity_text),
            FadeOut(wind_arrow), FadeOut(wind_text)
        )
        self.wait(1)
        nx, ny = 60, 40   
        x = np.linspace(-6, 6, nx)
        y = np.linspace(-3, 3, ny)
        X, Y = np.meshgrid(x, y)
        def update_field(t):
            U_new = np.sin(X + 0.2*t) * np.cos(Y)
            V_new = np.cos(X) * np.sin(Y + 0.2*t)
            return U_new, V_newd
        num_x, num_y = 150, 100
        px = np.linspace(-6, 6, num_x)
        py = np.linspace(-3, 3, num_y)
        particles = np.array([[xx, yy] for xx in px for yy in py])
        dots = VGroup(*[Dot(point=[px, py, 0], radius=0.015, color=RED) for px, py in particles])
        self.add(dots)
        for t in range(180):  
            U, V = update_field(t)
            for i, dot in enumerate(dots):
                px, py = particles[i]
                xi = np.argmin(np.abs(x - px))
                yi = np.argmin(np.abs(y - py))
                vx, vy = U[yi, xi], V[yi, xi]
                particles[i] += 0.02 * np.array([vx, vy])  
                dot.move_to([particles[i][0], particles[i][1], 0])
            self.wait(0.05)
        final_text = Text(
            "Navier-Stokes Predicts Fluid Motion\nFrom Particle to Flowing Cloth",
            font_size=32
        )
        final_text.set_color_by_gradient(BLUE, PURPLE)
        self.play(FadeOut(dots))
        self.play(Write(final_text))
        self.wait(4)