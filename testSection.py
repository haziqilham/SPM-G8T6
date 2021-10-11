import unittest
from Section import Section;

class testSection(unittest.TestCase):
    def test_addMaterial(self):
        s = Section(1, "Intro", "Slides 1")
        mat = s.material()
        self.assertEqual(mat, "Slides 1")
        self.assertEqual(s.id(), 1)
        self.assertEqual(s.addMaterial("Slides 2"), "Slides 1Slides 2")

class testSection(unittest.TestCase):
    def test_deleteMaterial(self):
        s = Section(1, "Intro", "Slides 1")
        mat = s.material()
        self.assertEqual(mat, "Slides 1")
        self.assertEqual(s.id(), 1)
        self.assertEqual(s.deleteMaterial(mat), None)