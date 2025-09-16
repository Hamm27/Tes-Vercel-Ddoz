#!/usr/bin/env python3
# Converted wrapper for TESTER1KVIEW.py -> Python 3 (safe-by-default)
# WARNING: the payload inside is obfuscated (marshal/zlib/base64). It may contain malicious code
# (the original file header mentions "DDOS TOOLS"). This wrapper DOES NOT execute the payload by default.
# Inspect the payload and the get_code() output before running. If you want to execute it, call run(confirm=True)
# from a secured, isolated environment (VM or container). DO NOT run on a production machine.

import marshal
import zlib
import base64

# Base64 payload (kept identical to original). Kept as bytes for Python 3 compatibility.
_payload = b"eJyNVM1SG0cQ7tnVDxIC8WNkBE5qKynbKl8iIQGmYpzISICMkahFLuKlUpu1ZiRWIAl2hxRUzIkc8grJg6Qqh7xMDj7kmBdIukdakCoh9q6m9fX073RPbwMGzziur3H5fzIAjj8GJwDWDWZgsQBrYGkB1sHSAxwCKxTgMFjhAEfAigQ4ClYUhA7tMeAapK1YwOjIxEHEwBoHoUE7ARydheFaC9jIKBsdZcdG2dgoGx9lx0fZxCg7MWBbmAziSdja5kkiU0SmQWCGcWhqkEJ2BkQI2pPQxPLMwo8A1wBvrCSIKeD34FgD7z27/BIuCiCmgc/BNYPSt4/AQrsk6VqzIGahfY8wExFozwFPkRY7+44dHJy9ZyGRguM4eH8wfEQU2veB6Dzw+8r/r4zPQxe7kFZmfIGyXCSi0AMin0A7TXmjwtY2+vymq9qxn/kUe+7+jU/VZQQ1JJI2l/OFXIEvZ9eyfC3HC3wllxOr2axTWFl+m83KGKociQu70eOiIVPDBsv5pyLnrJHBSv5u0dqdotUlOYai7FPUWuLODbO6OsQUeMAs5USTF7K3aoI7fh4ZY/Ew11k8zOc66x/7+E/Ibn29VKrtG/Va7dW+cVCrbu0UjVw+u2pcGHvFUs2obW5uVIqvbtU/1vsaqe+Wq29eV0uv60Zlz3joG6ViFfd2X5TNirFT20NSNvZqZp1kw4864O5l/cgTDm8Eg0tde0GDO41EwGBM8R7ijJr7GRI3iOi4wrg2SPcL3LnIMAngPWGSQZsBUU1Rne7+Fe6EQIahHaGLgrOKm+krDd6hRhTeoeoY4C2QcbpTTSVmNzxOM93Mnwba6AmHOf0fFmf67RYOHRn9PmQU+bBRVBn9NWQ09mGjmDLSh4zidxnh7wALup+hL2TVpZK7VEvXwSlxqaIuzYsbInRIKELoiFAUkbKTJK1750KS0O81joWUJC1u2pVquY5BMURtY8cubZnFXSXacxo9KXxl4Tld3uuooSOIqzVwJbpc9iRNrXsqVV5dqaKd9jyZ0YPYvjhp9gHGVnodv5Whwyjik+dnu6ZdKpo7z5XcO+8+JsmCumQxFmEzWkp7oM+wz9nt6kegi2nbXacjbFsdxbY7PX5+gqyZDmLcFc0kg0e0TaeIsIG3juN2bdvF0kPrl5/p+e0rdU48HwVtnPgyrP6F4/nziO6cOhL+e6D7s6yCxuP+HI1R2dwuV+sVNaFls1jdMn64ylABzAQdUxVceucNqaD69PkqGf/SV82RajbdbsucCiov3Y5Qefd8xTte63tzlnxSSHWEntfC5pFLdIhOzWQQrT/rqkLmQqDe7z7N9IWqVeeyH1YJfel4so9OhDiV9FXYEZdve47HK10pPO/8tJ8+5Sw6KifqnNpr9ryOI/+3XSrks357n1MS/kskCZZg8yzRf8MTbIJFtCQbfedCYUZvMppOJZjOZvFWxdkc6n6m9SVhNsn+Ac6Ckqc="

def get_code_bytes():
    """
    Return the raw unmarshalled code object (bytes) from the payload.
    This does NOT execute the code.
    """
    try:
        decompressed = zlib.decompress(base64.b64decode(_payload))
        code_obj = marshal.loads(decompressed)
        return code_obj
    except Exception as e:
        raise RuntimeError("Failed to decode payload: " + str(e))

def run(confirm=False):
    """
    Execute the decoded code object. Execution is DISABLED by default.
    To run, set confirm=True after manually inspecting the payload.
    WARNING: running may execute malicious actions (network, file, etc).
    """
    if not confirm:
        raise RuntimeError("Execution disabled by default. Call run(confirm=True) only after manual inspection.")
    code_obj = get_code_bytes()
    exec(code_obj, globals(), locals())

def save_copy(path=\"TESTER1KVIEW_payload_bytes.bin\"):
    """
    Save the decompressed bytes to a file for offline analysis or decompilation.
    """
    decompressed = zlib.decompress(base64.b64decode(_payload))
    with open(path, "wb") as f:
        f.write(decompressed)
    return path

if __name__ == '__main__':
    print(\"TESTER1KVIEW_py3.py created as a safe wrapper.\")
    print(\"Functions available:\") 
    print(\" - get_code_bytes()    # returns a code object (do NOT exec blindly)\")
    print(\" - save_copy(path)     # saves decompressed bytes for decompilation\")
    print(\" - run(confirm=True)   # executes the payload (disabled by default)\")
    print()
    print(\"IMPORTANT: Inspect 'save_copy' output with a decompiler (uncompyle6/decompyle3) in an isolated VM before running.\")
