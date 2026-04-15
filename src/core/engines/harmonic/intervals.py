# Intervals module for harmonic engine

class JustInterval:
    def __init__(self, ratio):
        self.ratio = ratio

    def __str__(self):
        return f"JustInterval with ratio {self.ratio}"

class TET12Interval:
    def __init__(self, midi_note):
        self.midi_note = midi_note

    def __str__(self):
        return f"TET12Interval for MIDI note {self.midi_note}"

class IntervalAlgebra:
    @staticmethod
    def add(interval1, interval2):
        # Simplified representation of interval addition
        return interval1 + interval2

    @staticmethod
    def subtract(interval1, interval2):
        return interval1 - interval2

    @staticmethod
    def multiply(interval1, factor):
        return interval1 * factor
