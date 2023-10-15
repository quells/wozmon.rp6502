# WOZ Monitor for the RP6502 Picocomputer

Original by Steve Wozniak in 1976.

Ported to ACIA serial by Ben Eater in 2023.

Ported to the RP6502 (v0.2) by Kai Wells in 2023.

Compiles to just 248 bytes of machine code, but requires an additional 128 bytes of input buffer and 8 zero page spaces.

Occupies `0x24..0x2B` and `0xFD00..0xFE7F` when loaded. Works best with `set caps 2` to force capslock - hexadecimal and `R` must be capitalized.

## Install

Copy `wozmon.rp6502` from [the latest release](https://github.com/quells/wozmon.rp6502/releases) to a USB drive and attach to the Picocomputer.

## Build

`vasm6502_oldstyle` should be compiled from source like so:

```
$ make CPU=6502 SYNTAX=oldstyle
```

Then move the executable into your `$PATH`.

Clone this repo and initialize the rp6502-sdk submodule:

```
$ git clone https://github.com/quells/wozmon.rp6502.git
$ cd wozmon.rp6502
$ git submodule update --init
```

Finally, run `upload.py`:

```
$ python3 upload.py
```

This will compile using [vasm](http://sun.hasenbraten.de/vasm/), write that out to a RP6502 ROM file, then attempt to upload to a Picocomputer attached via USB.
