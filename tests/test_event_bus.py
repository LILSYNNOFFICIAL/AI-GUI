"""
Tests for EventBus.
"""

import pytest
from engines.events import EventBus


def test_subscribe_and_emit():
    bus = EventBus()
    results = []

    def handler(value=None):
        results.append(value)

    bus.subscribe("test", handler)
    bus.emit("test", value=123)

    assert results == [123]


def test_unsubscribe():
    bus = EventBus()
    results = []

    def handler(value=None):
        results.append(value)

    bus.subscribe("test", handler)
    bus.unsubscribe("test", handler)
    bus.emit("test", value=123)

    assert results == []
