import sys


# CONSTANTS


WINDOWS = str(sys.platform) in ("win32", "cygwin")


# SCRIPT


if __name__ == "__main__":
    import subprocess
    import sys
    import time

    proc = list()
    here = sys.path[0]

    print("\n\nPlease enter taxa searches on any line:\n")

    while True:
        time.sleep(0.01)
        try:
            term = input().strip()
            if (term == "exit"):
                break
            proc.append(subprocess.Popen((
                f"python{'3' if not WINDOWS else str()} " +
                f"{here}/src/arboretum.py {term}"
            ).split()))
        except KeyboardInterrupt:
            break

    for p in proc:
        p.kill()

    print("\n")
