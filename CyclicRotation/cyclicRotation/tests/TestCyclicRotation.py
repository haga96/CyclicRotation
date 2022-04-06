from cyclicRotation import CyclicRotation


class TestCyclicRotation:
    def test_cyclic_rotation(self):
        c = CyclicRotation
        assert c.cyclic_rotation([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

    def test_empty_array_cyclic_rotation(self, capfd):
        c = CyclicRotation
        c.cyclic_rotation([], 3)
        out, err = capfd.readouterr()
        assert out == "the A is not an array or the length of the array is less than zero\n"
