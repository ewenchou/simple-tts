# SimpleTTS

A simple Python class that uses Festival's `text2wave` command to perform text-to-speech (TTS) conversion.

## Prerequisites

* Only works on Linux systems. Developed and tested using Ubuntu 16.04.
* Requires `festival` installed on host Linux system.

## Installation

1. Install festival:

      ```
      sudo apt-get install festival
      ```

2. Download and install voice pack (optional):

      ```
      wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2
      tar xjf cmu_us_clb_arctic-0.95-release.tar.bz2 -C /tmp/
      sudo mkdir -p /usr/share/festival/voices/us/
      sudo cp -r /tmp/cmu_us_clb_arctic-0.95-release /usr/share/festival/voices/us/cmu_us_clb_arctic_clunits

3. Make the voice pack the new default by adding/editing the `.festivalrc` file in your home directory and add the following line:

      ```
      (set! voice_default 'voice_cmu_us_clb_arctic_clunits)
      ```

3. Clone this repository and install:

      ```
      git clone https://github.com/ewenchou/simple-tts.git
      cd simple-tts
      sudo python setup.py install
      ```

## Temporary Directory and Files

`SimpleTTS` will save text and WAV files to its temporary directory (default: `/tmp/simple-tts`). The WAV files can be large in size and take up disk space. 

Use the `clean()` method to delete them after you're done using the `SimpleTTS` object instance.