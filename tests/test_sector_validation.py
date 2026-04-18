"""Tests for the sector validation gate."""

import pytest
from lynx_mining.core.analyzer import _validate_sector, SectorMismatchError
from lynx_mining.models import CompanyProfile


class TestSectorValidation:
    """Sector validation blocks non-basic-materials companies."""

    def _profile(self, ticker="T", sector=None, industry=None, desc=None):
        return CompanyProfile(ticker=ticker, name=f"{ticker} Corp",
                              sector=sector, industry=industry, description=desc)

    # --- Should ALLOW ---
    def test_basic_materials_sector(self):
        _validate_sector(self._profile(sector="Basic Materials", industry="Gold"))

    def test_energy_sector(self):
        _validate_sector(self._profile(sector="Energy", industry="Uranium"))

    def test_gold_industry(self):
        _validate_sector(self._profile(sector="Basic Materials", industry="Gold"))

    def test_uranium_industry(self):
        _validate_sector(self._profile(sector="Energy", industry="Uranium"))

    def test_copper_industry(self):
        _validate_sector(self._profile(sector="Basic Materials", industry="Other Industrial Metals & Mining"))

    def test_oil_gas_industry(self):
        _validate_sector(self._profile(sector="Energy", industry="Oil & Gas E&P"))

    def test_mining_in_description(self):
        _validate_sector(self._profile(sector="Technology", industry="Software",
                                       desc="A gold mining exploration company"))

    def test_ni43101_in_description(self):
        _validate_sector(self._profile(sector="Other", industry="Other",
                                       desc="Company with NI 43-101 resource estimate"))

    def test_drilling_in_description(self):
        _validate_sector(self._profile(sector="Other", industry="Other",
                                       desc="Active drilling program on property"))

    # --- Should BLOCK ---
    def test_technology_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Technology", industry="Consumer Electronics"))

    def test_financial_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Financial Services", industry="Banks"))

    def test_healthcare_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Healthcare", industry="Drug Manufacturers"))

    def test_consumer_cyclical_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Consumer Cyclical", industry="Auto Manufacturers"))

    def test_real_estate_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Real Estate", industry="REIT"))

    def test_all_none_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile())

    def test_empty_strings_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="", industry="", desc=""))

    def test_lithium_ion_battery_blocked(self):
        """TSLA mentions 'lithium-ion battery' but is not a mining company."""
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(
                sector="Consumer Cyclical", industry="Auto Manufacturers",
                desc="Electric vehicles with lithium-ion battery energy storage"))

    def test_app_store_ore_blocked(self):
        """AAPL's 'App Store' contains 'ore' but is not mining."""
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(
                sector="Technology", industry="Consumer Electronics",
                desc="App Store that allows customers to discover apps"))

    def test_error_message_content(self):
        with pytest.raises(SectorMismatchError, match="outside the scope"):
            _validate_sector(self._profile(sector="Technology", industry="Software"))
