# numba_pokemon_prngs
Package for numba @jitclass implementations (optionally uncompiled but with integers and arrays handled by numpy) of the Pseudo-Random Number Generators used in the Pokemon series

## Installation
numba-pokemon-prngs can be installed via pip with the following command

```pip install "numba-pokemon-prngs[numba] @ git+https://github.com/Lincoln-LM/numba_pokemon_prngs"```

or without numba support

```pip install "numba-pokemon-prngs @ git+https://github.com/Lincoln-LM/numba_pokemon_prngs"```

if numba is not detected, either by not being installed or for some other reason, numba-pokemon-prngs will default to relying only on numpy (as specified in [compilation.py](https://github.com/Lincoln-LM/numba_pokemon_prngs/blob/master/numba_pokemon_prngs/compilation.py), and will log a warning unless the environment variable ``NPP_USE_NUMBA`` is set to "FALSE" (or any value other than "TRUE").

This environment variable can additionally be used to trigger numba-less mode even when numba is installed.

additionally wheels for the latest commit are provided for direct installation at https://github.com/Lincoln-LM/numba_pokemon_prngs/releases/tag/latest

and can be installed to micropip for [pyodide](https://github.com/Lincoln-LM/numba_pokemon_prngs/blob/master/numba_pokemon_prngs/compilation.py) via

```micropip.install("numba_pokemon_prngs-0.1.0-py3-none-any.whl")```

after pulling the latest build from https://github.com/Lincoln-LM/numba_pokemon_prngs/releases/download/latest/numba_pokemon_prngs-0.1.0-py3-none-any.whl

## Currently Supported PRNGs
| Name                                | Description                                        | Parameters                                                                                                                                                                                                    | Additional Info                                             |
|-------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **LCRNG32**                         |                                                    |                                                                                                                                                                                                               |                                                             |
| PokeRNG                             | Standard PRNG for Gen 3/4 Pokemon games            | Add: 0x6073, Mult: 0x41C64E6D                                                                                                                                                                                 | Supports modulo and reciprocal division random distribution |
| ARNG                                | Alternate Standard PRNG for Pokemon games          | Add: 0x1, Mult: 0x6C078965                                                                                                                                                                                    | Supports modulo random distribution                         |
| XDRNG                               | Standard PRNG for Gamecube Pokemon games           | Add: 0x269EC3, Mult: 0x343FD                                                                                                                                                                                  | Supports modulo random distribution                         |
| **LCRNG64**                         |                                                    |                                                                                                                                                                                                               |                                                             |
| BWRNG                               | Standard PRNG for Gen 5 Pokemon games              | Add: 0x269EC3, Mult: 0x5D588B656C078965                                                                                                                                                                       | Supports multiplication-shift random distribution           |
| **MT**                              |                                                    |                                                                                                                                                                                                               |                                                             |
| Mersenne Twister                    | Secondary PRNG for Gen 4/5 games, primary in Gen 6 | MT19937: <br> init_mult = 0x6C078965 <br> (w,n,m,r) = (32,624,397,31) <br> a = 0x9908B0DF <br> (u, d) = (11,0xFFFFFFFF) <br> (s,b) = (7,0x9D2C5680) <br> (t,c) = (15, 0xEFC60000) <br> l = 18                 |                                                             |
| SIMD-oriented Fast Mersenne Twister | Primary PRNG for Gen 7                              | SFMT19937: <br> init_mult = 0x6C078965 <br> POS1 = 488 <br> SL1 = 18 <br> SL2 = 8 <br> SR1 = 11 <br> SR2 = 8 <br> MASK = (0xDFFFFFEF,0xDDFECB7F,0xBFFAFFFF,0xBFFFFFF6) <br> PARITY = (0x1,0x0,0x0,0x13C9E684) | Impl is not fully SIMD optimized (yet:tm:)                  |
| TinyMT                              | Secondary PRNG for Gen 6/7                         | mat1 = 0x8F7011EE <br> mat2 = 0xFC78FF1F <br> tmat = 0x3793FDFF <br> init_mult = 0x6C078965                                                                                                                   |                                                             |

## Additionally Supported Features
| Name    | Description                                               |
|---------|-----------------------------------------------------------|
| RNGList | Cache for PRNG values to avoid expensive reinitialization |
| SHA-1   | Hash function used for Gen 5 initial seed generation      |
