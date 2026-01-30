# Standard Library
import re

PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
EN_DIGITS = "0123456789"


def normalize_text(text: str) -> str:
    if not text:
        return ""

    # تبدیل اعداد فارسی به انگلیسی
    for p, e in zip(PERSIAN_DIGITS, EN_DIGITS):
        text = text.replace(p, e)

    # حذف نیم‌فاصله
    text = text.replace("‌", " ")

    # فاصله بین حروف و عدد (شیلنگ6 → شیلنگ 6)
    text = re.sub(r"([آ-یA-Za-z])(\d)", r"\1 \2", text)
    text = re.sub(r"(\d)([آ-یA-Za-z])", r"\1 \2", text)

    # حذف فاصله‌های اضافی
    text = re.sub(r"\s+", " ", text).strip()

    return text
