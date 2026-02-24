"""Tests for env-diff."""

import pytest
from env_diff import diff


class TestDiff:
    """Test suite for diff."""

    def test_basic(self):
        """Test basic usage."""
        result = diff("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            diff("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = diff(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
