import pycrack
import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python pycrack_script.py <archivo_hccapx> <archivo_wordlist>")
        sys.exit(1)

    hccapx_file = sys.argv[1]
    wordlist_file = sys.argv[2]

    cracker = pycrack.WPACrack(hccapx_file, wordlist_file, verbose=True)
    cracker.run()

if __name__ == "__main__":
    main()

