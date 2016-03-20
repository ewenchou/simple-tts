"""Simple function that uses Festival's text2wave command to convert
text to speech.
"""
import os
import uuid

TEMP_DIR = '/tmp/simple-tts'

def tts(text, save_to=None):
    """Converts text to speech (WAV) file.

    Args:
        text (str): Text to convert
        save_to (str): File path for saving the WAV file. If not
                       provided will save to a `/tmp/simple-tts/`

    Returns:
        Path (str) where the WAV file is saved.
    """
    os.system('mkdir -p {}'.format(TEMP_DIR))
    temp_file = TEMP_DIR + '/{}.txt'.format(uuid.uuid4())
    if not save_to:
        save_to = TEMP_DIR + '/{}.wav'.format(uuid.uuid4())
    with open(temp_file, 'w') as f:
        f.write(text)
    os.system('text2wave -o {out_fn} {in_fn}'.format(
        out_fn=save_to, in_fn=temp_file))
    return save_to
