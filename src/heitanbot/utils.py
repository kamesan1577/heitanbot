from Quote2Image import Convert, GenerateColors


class QuoteGenerator:
    def __init__(
        self,
        quote: str,
        author: str,
        fg: str,
        bg: str,
        font_size: int,
        font_type: str,
        width: int,
        height: int,
        watermark_text: str = None,
    ):
        self.quote = quote
        self.author = author
        self.fg = fg
        self.bg = bg
        self.font_size = font_size
        self.font_type = font_type
        self.width = width
        self.height = height
        self.watermark_text = watermark_text

    def generate(self):
        img = Convert(
            quote=self.quote,
            author=self.author,
            fg=self.fg,
            bg=self.bg,
            font_size=self.font_size,
            font_type=self.font_type,
            width=self.width,
            height=self.height,
            watermark_text=self.watermark_text,
        )

        return img
