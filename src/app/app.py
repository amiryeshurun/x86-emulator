import argparse
import emulator

def main():
    app_parser = argparse.ArgumentParser(description="""
        A Simple x86 emulator written in Python. The emulator accepts a pure binary file.
        """)
    app_parser.add_argument('-f', '--file', type=str, required=True, help="A binary file path")
    cpu_initial_mode = app_parser.add_mutually_exclusive_group()
    cpu_initial_mode.add_argument('-rm', '--real-mode', dest='real_mode', action='store_true', default=True,
        help="When specified, the CPU is started in 16-bits real mode")
    cpu_initial_mode.add_argument('-pm', '--protected-mode', dest='protected_mode', action='store_true', default=False,
        help="When specified, the CPU is started in 32-bits protected mode with paging disabled")
    cpu_initial_mode.add_argument('-lm', '--long-mode', dest='long_mode', action='store_true', default=False,
        help="When specified, the CPU is started in 64-bits long mode")
    # Parse the arguments    
    app_parser.parse_args()

    

if __name__ == "__main__":
    main()