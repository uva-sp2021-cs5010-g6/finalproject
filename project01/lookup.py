
import pandas as pd


class NutrientLookup():
    def __init__(self, csv_file):
        self._df = pd.read_csv(csv_file, header=0)

    def _lookup(self, col, val):
        return self._df[self._df[col] == val].tolist()

    def lookup_id(idx):
        return self._lookup("id", idx)

    def lookup_name(name):
        return self._lookup("name", name)

    def lookup_unit(unit):
        return self._lookup("unit_name", unit)

    def lookup_nutrient_nbr(nbr):
        return self._lookup("nutrient_nbr", nbr)

    def lookup_rank(rnk):
        return self._lookup("rank", rnk)

    @staticmethod
    def _unit_translator(unit_code):
        return {
            "G": "grams",
            "MG": "miligrams",
            "KCAL": "calories",
            "IU": "international unit"
            "UG": "micrograms"
        }[unit_code]

    def _normalize(unit_code, value):
        conversion_ratio = {
            "G": 1,
            "MG": 0.001,
            "UG": 0.000001}[unit_code]
        return value*conversion_ratio

