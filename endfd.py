from manim import *

class CreativeEnding(Scene):
    def construct(self):

        # ---------------- THANK YOU (CREATIVE ENTRY) ----------------
        thank_you = Text(
            "Thank You",
            font_size=90,
            weight=BOLD
        )

        thank_you.set_color_by_gradient(BLUE, PURPLE, PINK)

        # Glow effect (duplicate with blur illusion)
        glow = thank_you.copy().set_opacity(0.3).scale(1.2)

        self.play(FadeIn(glow, scale=1.5))
        self.play(Write(thank_you), run_time=2)

        self.play(
            thank_you.animate.scale(0.6).to_edge(UP),
            glow.animate.scale(0.6).to_edge(UP)
        )

        # ---------------- CREATED BY ----------------
        created_by = Text(
            "Created by",
            font_size=30
        ).set_color(GRAY_B)

        name = Text(
            "VERTEX GDNA (SUSHRUT KALE)",
            font_size=40,
            weight=BOLD
        )

        name.set_color_by_gradient(TEAL, GREEN)

        creator_group = VGroup(created_by, name).arrange(DOWN, buff=0.2)
        creator_group.move_to(ORIGIN)

        self.play(FadeIn(created_by, shift=UP))
        self.play(Write(name), run_time=2)

        # Subtle scale animation
        self.play(name.animate.scale(1.05), run_time=0.5)
        self.play(name.animate.scale(1), run_time=0.5)

        # ---------------- GUIDANCE ----------------
        guidance = Text(
            "Under the guidance of",
            font_size=26
        ).set_color(GRAY_B)

        prof = Text(
            "Prof. Priti Shinde Ma'am",
            font_size=32,
            weight=BOLD
        )

        prof.set_color_by_gradient(ORANGE, GOLD)

        guidance_group = VGroup(guidance, prof).arrange(DOWN, buff=0.2)
        guidance_group.next_to(creator_group, DOWN, buff=1)

        self.play(FadeIn(guidance, shift=UP))
        self.play(Write(prof), run_time=2)

        # ---------------- FINAL EFFECT ----------------
        # Gentle floating animation
        self.play(
            creator_group.animate.shift(UP * 0.2),
            guidance_group.animate.shift(DOWN * 0.2),
            run_time=1
        )

        self.wait(2)

        # Fade out everything smoothly
        self.play(
            FadeOut(VGroup(thank_you, glow, creator_group, guidance_group)),
            run_time=2
        )