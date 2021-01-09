# joniturunen/picam

> Learning project:
> Raspberry Pi 4, NOIR Camera Module v2.

## About The Project

---

Built with Python. Different scripts to do timelapse and snapshots. Plan to implement s3 bucket integration for image uploading. 


## Getting Started

### Prerequisites

- Raspberry Pi (4 tested)
- Camera module (v.2.1)
- Raspberry Pi power brick or battery pack
- MicroSD card for the OS (of your choice)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/joniturunen/picam.git
   ```
2. Install NPM packages
   ```sh
   pip3 install -r requirements.txt
   ```

### Running camera

1. Run timelapse
   ```sh
   python3 timelapse.py # cli argument parsing not implemented, change variables via script
   ```

2. Take a single shot
   ```sh
   python3 snapshot.py
   ```

## License

Distributed under the MIT License.
