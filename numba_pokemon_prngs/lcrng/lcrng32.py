"""32-bit Linear Congruential Pseudo Random Number Generator"""

from __future__ import annotations
from typing import Type, Callable
import enum
import numba
import numpy as np


class LCRNG32RandomDistribution(enum.IntEnum):
    """
    Various LCRNG32 random distribution types

    MODULO -> next_u16() % maximum

    RECIPROCAL_DIVISION -> next_u16() // ((0xFFFF // maximum) + 1)
    """

    NONE = 0
    MODULO = 1
    RECIPROCAL_DIVISION = 2


class LCRNG32:
    """32-bit LCRNG parent class"""

    seed: numba.uint32

    def __init__(self, seed: np.uint32) -> None:
        self.seed: np.uint32 = seed

    def next(self) -> np.uint32:
        """
        Generate and return the next full 32-bit random uint

        () -> seed = seed * mult + add
        """
        raise NotImplementedError()

    def jump(self, adv: np.uint32) -> np.uint32:
        """Jump ahead the LCRNG sequence by adv"""
        raise NotImplementedError()

    def advance(self, adv: np.uint32) -> np.uint32:
        """Advance the LCRNG sequence by adv"""
        for _ in range(adv):
            self.next()
        return self.seed

    def next_u16(self) -> np.uint16:
        """Generate and return the next 16-bit random uint"""
        return self.next() >> 16

    def next_rand(self, maximum: np.uint16) -> np.uint16:
        """
        Generate and return the next [0, maximum) random uint

        () -> distribution(self.next_u16(), maximum)
        """
        raise NotImplementedError()


def lcrng32_init(
    *,
    add: np.uint32,
    mult: np.uint32,
    distribution: LCRNG32RandomDistribution = LCRNG32RandomDistribution.NONE,
    reverse: bool = False,
) -> Callable[[Type[LCRNG32]], Type[LCRNG32]]:
    """Initialize a LCRNG32 class with constants and random distribution"""
    if reverse:
        mult = pow(mult, -1, 0x100000000)
        add = (-add * mult) & 0xFFFFFFFF

    jump_table = [(np.uint32(add), np.uint32(mult))]
    for i in range(31):
        jump_table.append(
            (
                np.uint32(jump_table[i][0] * (jump_table[i][1] + 1)),
                np.uint32(jump_table[i][1] * jump_table[i][1]),
            )
        )
    jump_table = tuple(jump_table)

    def wrap(lcrng_class: Type[LCRNG32]) -> Type[LCRNG32]:
        def next_(self: LCRNG32) -> np.uint32:
            self.seed = self.seed * mult + add
            return self.seed

        def jump(self: LCRNG32, adv: np.uint32):
            i = 0
            while adv:
                if adv & 1:
                    add, mult = jump_table[i]
                    self.seed = self.seed * mult + add
                adv >>= 1
                i += 1
            return self.seed

        if distribution == LCRNG32RandomDistribution.MODULO:

            def next_rand(self: LCRNG32, maximum: np.uint16) -> np.uint16:
                return self.next_u16() % maximum

        elif distribution == LCRNG32RandomDistribution.RECIPROCAL_DIVISION:

            def next_rand(self: LCRNG32, maximum: np.uint16) -> np.uint16:
                return self.next_u16() // ((0xFFFF // maximum) + 1)

        else:

            def next_rand(self: LCRNG32, maximum: np.uint16) -> np.uint16:
                raise NotImplementedError()

        lcrng_class.next = next_
        lcrng_class.jump = jump
        lcrng_class.next_rand = next_rand

        lcrng_class = numba.experimental.jitclass(lcrng_class)
        
        return lcrng_class

    return wrap
