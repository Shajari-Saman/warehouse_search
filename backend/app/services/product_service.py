# Third Library
import polars as pl

from app.services.text_normalizer import normalize_text


class ProductService:
    def __init__(self):
        df = pl.read_excel("app/data/warehouse.xlsx", sheet_name="products", engine="openpyxl")

        self.df = df.with_columns(
            pl.col("نام کالا").cast(pl.Utf8).map_elements(normalize_text).alias("normalized_name")
        )

    def search(self, query: str):
        query = normalize_text(query)
        words = query.split()

        expr = pl.lit(True)
        for w in words:
            expr &= pl.col("normalized_name").str.contains(w)

        return self.df.filter(expr)


class CostCenterService:
    def __init__(self):
        self.df = pl.read_excel("app/data/warehouse.xlsx", sheet_name="cost_centers", engine="openpyxl")

    def search(self, query: str):
        words = query.strip().split()

        expr = pl.lit(True)
        for w in words:
            expr &= pl.col("نام مرکز").cast(pl.Utf8).str.contains(w)

        return self.df.filter(expr)
