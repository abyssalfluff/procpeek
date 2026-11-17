# procpeek

**A small Linux process inspector written in Python.**

`procpeek` is a command-line learning project that explores how Linux exposes information about running processes through the `/proc` virtual filesystem. It combines practical Python programming with Linux process inspection and is being developed incrementally.

> **Status:** Early development. The current version reads and displays the full `/proc/<PID>/status` file for a process selected interactively.

## Current features

- Prompts for a process ID (PID).
- Rejects non-integer, zero, and negative PID inputs.
- Checks whether the corresponding `/proc/<PID>` directory exists.
- Asks for another PID when the input is invalid or the process is not found.
- Reads and prints the raw contents of `/proc/<PID>/status`.
- Uses only the Python standard library.

## Requirements

- **Linux** with the `/proc` filesystem available
- **Python 3**

No third-party Python packages are required.

## Getting started

Clone the repository and run the script:

```bash
git clone https://github.com/abyssalfluff/procpeek.git
cd procpeek
python3 procpeek.py
```

Enter the PID of an existing process when prompted.

### Example output

```text
Enter PID: 24
Process exists here: /proc/24
Name:   cpuhp/1
...
State:  S (sleeping)
...
Pid:    24
PPid:   2
...
```

*This is an abridged example from a Linux kernel thread; the current program prints the entire status file. PIDs, names, and other values depend on the running system.*

## How it works

Linux exposes process information through `/proc`, a virtual filesystem populated by the kernel rather than ordinary files stored on disk.

For a process with PID `1424`, the path `/proc/1424/status` contains human-readable information about that process, such as its name, state, and parent PID.

Currently, `procpeek`:

1. Validates the PID entered by the user.
2. Checks for the corresponding `/proc/<PID>` path using `os.path.exists()`.
3. Opens `/proc/<PID>/status` and prints its contents.

Processes can exit at any time, including between the existence check and the file read. Handling that situation gracefully is a planned improvement.

## Development roadmap

- [x] Validate interactive PID input
- [x] Check whether a process exists under `/proc`
- [x] Read and display `/proc/<PID>/status`
- [ ] Extract selected fields: `Name`, `Pid`, `PPid`, and `State`
- [ ] Parse fields into structured Python data and format the output
- [ ] Organize the program into focused functions
- [ ] Inspect additional process details, including executable paths
- [ ] Handle process termination and file-access errors
- [ ] Support command-line PID arguments
- [ ] Add automated tests and continuous integration

## Project goals

This project is an opportunity to practice:

- Python input validation, control flow, exceptions, and file I/O
- Linux PIDs, parent-child process relationships, and the `/proc` filesystem
- Building and documenting a command-line utility
- Incremental development, debugging, and maintainable code

The focus is on understanding how each part works and extending the tool as those skills develop.
