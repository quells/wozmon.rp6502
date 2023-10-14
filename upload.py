from rp6502_sdk import rp6502
import subprocess

# Device path of the Picocomputer serial connection
tty = '/dev/ttyACM0'
# Name of the vasm output file
exe_6502 = 'wozmon'
# Name of the RP6502 ROM on host
exe_rp6502 = 'wozmon.rp6502'
# Name of the RP6502 ROM on Picocomputer
rom_name = 'wozmon'
# Start address of the executable - must match .org in src/wozmon.s
address = 0xFD00

def compile() -> subprocess.CompletedProcess:
    compile_cmd = [
        'vasm6502_oldstyle',
        '-Fbin',
        '-dotdir',
        '-c02',
        '-o', exe_6502,
        'src/wozmon.s'
    ]
    cp = subprocess.run(compile_cmd)
    if cp.returncode != 0:
        sys.exit(cp.returncode)

def build_rp6502():
    rom = rp6502.ROM()
    rom.comment('WOZ Monitor')
    rom.binary_file(exe_6502, address)
    rom.reset_vector()

    with open(exe_rp6502, 'wb') as o:
        rom.seek(0)
        while True:
            chunk = rom.read(1024)
            if len(chunk) == 0:
                break
            o.write(chunk)

def upload():
    mon = rp6502.Monitor(tty)
    mon.send_break()
    with open(exe_rp6502, 'rb') as f:
        rom = rp6502.ROM()
        mon.upload(rom_name, f)

if __name__ == '__main__':
    compile()
    build_rp6502()
    upload()
