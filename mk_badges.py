import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from textwrap import wrap


def wrap_text(text, font_name, font_size, max_width):
    """
    Calculate wrapped text lines to fit within a maximum width.
    Returns list of lines and total height needed.
    """
    if not text:
        return [], 0

    # Create temporary canvas to measure text
    c = canvas.Canvas("temp.pdf")
    c.setFont(font_name, font_size)

    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        width = c.stringWidth(test_line, font_name, font_size)

        if width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
                current_line = []

    if current_line:
        lines.append(" ".join(current_line))

    line_height = font_size * 1.2
    total_height = len(lines) * line_height

    return lines, total_height


def create_badges(input_file, logo_path, output_file="badges.pdf"):
    """
    Create printable badges in landscape orientation.
    Generates a PDF with 8 badges per page (2 columns × 4 rows).
    Each badge is exactly 4×2 inches (width × height).
    """
    # Read the data
    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)

    # Set up landscape page
    page_width, page_height = landscape(letter)  # 11 × 8.5 inches

    # Create canvas in landscape orientation
    c = canvas.Canvas(output_file, pagesize=landscape(letter))

    # Badge dimensions (exactly 4×2 inches)
    badge_width = 3.3 * inch
    badge_height = 2 * inch

    # Calculate margins to center the badges on the page
    # Available space: 11 inches wide (page_width) and 8.5 inches high (page_height)
    # Need space for 2 badges across (8 inches total) and 4 badges down (8 inches total)
    margin_x = (
        page_width - (2 * badge_width)
    ) / 3  # Space for 2 badges with margins between
    margin_y = (
        page_height - (4 * badge_height)
    ) / 5  # Space for 4 badges with margins between

    # Load logo
    logo = ImageReader(logo_path)
    logo_width = 0.6 * inch
    logo_height = 0.6 * inch

    # Font configurations
    name_font = "Times-Bold"
    name_size = 20  # Slightly smaller to fit in narrower space
    affiliation_font = "Times-Roman"
    affiliation_size = 14
    conference_font = "Times-Bold"
    conference_size = 10

    for i, row in enumerate(df.itertuples()):
        # Calculate page position
        page_num = i // 8  # 8 badges per page (2×4)
        position = i % 8
        row_num = position // 2  # 4 rows
        col_num = position % 2  # 2 columns

        # Start new page if needed
        if position == 0 and i > 0:
            c.showPage()

        # Calculate badge position
        x = margin_x + col_num * (badge_width + margin_x)
        y = (
            page_height
            - (margin_y + badge_height)
            - row_num * (badge_height + margin_y)
        )

        # Draw badge border
        c.rect(x, y, badge_width, badge_height)

        # Add logo
        logo_x = x + 0.2 * inch
        logo_y = y + badge_height - 0.2 * inch - logo_height
        c.drawImage(
            logo,
            logo_x,
            logo_y,
            width=logo_width,
            height=logo_height,
            preserveAspectRatio=True,
        )

        # Add name next to logo
        c.setFont(name_font, name_size)
        name_x = logo_x + logo_width + 0.2 * inch
        name_y = logo_y + (logo_height - name_size) / 2  # Vertically center with logo

        # Check if name fits, scale if necessary
        available_width = badge_width - (logo_width + 0.6 * inch)
        name_width = c.stringWidth(row.name, name_font, name_size)
        if name_width > available_width:
            scaled_size = int(name_size * available_width / name_width)
            c.setFont(name_font, scaled_size)
            name_y = logo_y + (logo_height - scaled_size) / 2  # Recenter with new size

        c.drawString(name_x, name_y, row.name)

        # Add wrapped affiliation
        c.setFont(affiliation_font, affiliation_size)
        max_width = badge_width - 0.4 * inch
        affiliation_lines, _ = wrap_text(
            row.affiliation, affiliation_font, affiliation_size, max_width
        )

        # Position affiliation in middle section
        line_height = affiliation_size * 1.2
        total_affiliation_height = len(affiliation_lines) * line_height
        affiliation_start_y = y + badge_height * 0.45  # Adjusted for new dimensions

        for idx, line in enumerate(affiliation_lines):
            line_width = c.stringWidth(line, affiliation_font, affiliation_size)
            line_x = x + (badge_width - line_width) / 2
            line_y = affiliation_start_y - (idx * line_height)
            c.drawString(line_x, line_y, line)

        # Add conference name at bottom
        c.setFont(conference_font, conference_size)
        conf_text = "Proof Scaling Meeting 2024"
        conf_width = c.stringWidth(conf_text, conference_font, conference_size)
        conf_x = x + (badge_width - conf_width) / 2
        conf_y = y + 0.15 * inch  # Slightly higher from bottom
        c.drawString(conf_x, conf_y, conf_text)

    c.save()


def main():
    create_badges("badges.csv", "static/img/logo.jpg")


if __name__ == "__main__":
    main()
