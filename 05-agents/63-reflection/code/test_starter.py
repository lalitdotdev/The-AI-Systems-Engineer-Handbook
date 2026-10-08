"""Tests for the lesson starter. Replace or extend freely."""
import pytest

from starter import hello


def test_hello_not_todo():
    assert "TODO" not in hello()


def test_hello_returns_string():
    assert isinstance(hello(), str)
