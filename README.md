# simple-tts

A simple Python function that uses `os.system` to run Festival's `text2wave` command for text-to-speech (TTS) conversion.

# Prerequisites

* Only works on Linux systems. Developed and tested using Ubuntu 14.04.
* Requires `festival` installed on host Linux system.

# Installation

1. Install festival

        sudo apt-get install festival

2. Install voice pack (optional)

  Download the voice pack

        wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2

  Extract the voice pack

        tar xjf cmu_us_clb_arctic-0.95-release.tar.bz2 -C /tmp/

  Copy it to the festival shared voices directory

        sudo mkdir -p /usr/share/festival/voices/us/
        sudo cp -r /tmp/cmu_us_clb_arctic-0.95-release /usr/share/festival/voices/us/cmu_us_clb_arctic_clunits

  Make the voice pack the new default by adding/editing the `.festivalrc` file in your home directory and add the following line.

        (set! voice_default 'voice_cmu_us_clb_arctic_clunits)

3. Install simple-tts

        python setup.py install
