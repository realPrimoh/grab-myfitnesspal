from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from myfitnesspal.base import MFPBase
from myfitnesspal.types import FoodItemNutritionDict

from . import types
from .fooditemserving import FoodItemServing

if TYPE_CHECKING:
    from myfitnesspal.client import Client


class FoodItem(MFPBase):
    """Stores information about a particular food item."""

    def __init__(
        self,
        mfp_id: int,
        name: str,
        brand: Optional[str],
        verified: bool,
        calories: float,
        details: Optional[FoodItemNutritionDict] = None,
        confirmations: Optional[int] = None,
        serving_sizes: Optional[List[types.ServingSizeDict]] = None,
        client: Optional["Client"] = None,
    ):
        self._mfp_id = mfp_id
        self._name = name
        self._brand = brand
        self._verified = verified
        self._calories = calories

        self._details: Optional[FoodItemNutritionDict] = None
        self._confirmations = confirmations
        self._serving_sizes = serving_sizes
        self._client = client

    def _load_nutrition_details(self):
        if self._details:
            return

        assert self._client

        details = self._client._get_food_item_details(self.mfp_id)

        self._details = details["nutrition"]
        self._confirmations = details["confirmations"]
        self._serving_sizes = details["serving_sizes"]

    @property
    def details(self) -> FoodItemNutritionDict:
        """Nutritional details."""
        self._load_nutrition_details()
        assert self._details is not None

        return self._details

    @property
    def mfp_id(self) -> int:
        """Myfitnespal ID for this item."""
        return self._mfp_id

    @property
    def name(self) -> str:
        """Name"""
        return self._name

    @property
    def brand(self) -> Optional[str]:
        """Brand"""
        return self._brand

    @property
    def verified(self) -> bool:
        """Verified?"""
        return self._verified

    @property
    def serving(self) -> Optional[str]:
        """Serving"""
        self._load_nutrition_details()

        assert self._serving_sizes is not None

        for s in self._serving_sizes:
            if s["index"] == 0:
                return s["unit"]

        return None

    @property
    def calories(self) -> float:
        """Calories"""
        return self._calories

    @property
    def calcium(self) -> float:
        """Calcium"""
        return self.details.get("calcium", 0)

    @property
    def carbohydrates(self) -> float:
        """Carbohydrates"""
        return self.details.get("carbohydrates", 0)

    @property
    def cholesterol(self) -> float:
        """Cholesterol"""
        return self.details.get("cholesterol", 0)

    @property
    def fat(self) -> float:
        """Fat"""
        return self.details.get("fat", 0)

    @property
    def fiber(self) -> float:
        """Fiber"""
        return self.details.get("fiber", 0)

    @property
    def iron(self) -> float:
        """Iron"""
        return self.details.get("iron", 0)

    @property
    def monounsaturated_fat(self) -> float:
        """Monounsaturated Fat"""
        return self.details.get("monounsaturated_fat", 0)

    @property
    def polyunsaturated_fat(self) -> float:
        """Polyunsaturated Fat"""
        return self.details.get("polyunsaturated_fat", 0)

    @property
    def potassium(self) -> float:
        """Potassium"""
        return self.details.get("potassium", 0)

    @property
    def protein(self) -> float:
        """Protein"""
        return self.details.get("protein", 0)

    @property
    def saturated_fat(self) -> float:
        """Saturated Fat"""
        return self.details.get("saturated_fat", 0)

    @property
    def sodium(self) -> float:
        """Sodium"""
        return self.details.get("sodium", 0)

    @property
    def sugar(self) -> float:
        """Sugar"""
        return self.details.get("sugar", 0)

    @property
    def trans_fat(self) -> float:
        """Trans Fat"""
        return self.details.get("trans_fat", 0)

    @property
    def vitamin_a(self) -> float:
        """Vitamin A"""
        return self.details.get("vitamin_a", 0)

    @property
    def vitamin_c(self) -> float:
        """Vitamin C"""
        return self.details.get("vitamin_c", 0)

    @property
    def confirmations(self) -> int:
        """Confirmations"""
        self._load_nutrition_details()

        assert self._confirmations is not None

        return self._confirmations

    @property
    def servings(self) -> List[FoodItemServing]:
        """Servings"""
        self._load_nutrition_details()

        assert self._serving_sizes is not None

        servings: List[FoodItemServing] = []

        for s in self._serving_sizes:
            serving = FoodItemServing(
                s["id"],
                s["nutrition_multiplier"],
                s["value"],
                s["unit"],
                s["index"],
            )
            servings.append(serving)

        return servings

    def __str__(self) -> str:
        return f"{self.name} -- {self.brand}"
