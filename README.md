# numba_pokemon_prngs
Package for numba @jitclass implementations of the Pseudo-Random Number Generators used in the Pokemon series

## Currently Supported PRNGs
| Name        | Description                               | Parameters                              | Additional Info                                             |
|-------------|-------------------------------------------|-----------------------------------------|-------------------------------------------------------------|
| **LCRNG32** |                                           |                                         |                                                             |
| PokeRNG     | Standard PRNG for Gen 3/4 Pokemon games   | Add: 0x6073, Mult: 0x41C64E6D           | Supports modulo and reciprocal division random distribution |
| ARNG        | Alternate Standard PRNG for Pokemon games | Add: 0x1, Mult: 0x6C078965              |                                                             |
| XDRNG       | Standard PRNG for Gamecube Pokemon games  | Add: 0x269EC3, Mult: 0x343FD            | Supports modulo random distribution                         |
| **LCRNG64** |                                           |                                         |                                                             |
| BWRNG       | Standard PRNG for Gen 5 Pokemon games     | Add: 0x269EC3, Mult: 0x5D588B656C078965 | Supports multiplication-shift random distribution           |