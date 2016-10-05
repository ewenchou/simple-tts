"""
Simple library that uses Festival's text2wave command to convert text to speech.
"""
import os
import uuid

TEMP_DIR = '/tmp/simple-tts'


class SimpleTTS(object):
    def __init__(self, temp_dir=None):
        if temp_dir is None:
            temp_dir = TEMP_DIR
        self.temp_dir = TEMP_DIR
    
    def tts(self, text, save_to=None):
        """Converts text to audio WAV file.

        @param: text: Text to convert.
        @type: text: str

        @param: save_to: File path including filename to save audio WAV file.
                         If not provided, will save to a randomly named file in
                         the temporary directory (by default: /tmp/simple-tts).
        @type: str

        @return: Full file path including filename to the saved audio WAV file.
        @rtype: str
        """
        os.system('mkdir -p {}'.format(self.temp_dir))
        temp_file = self.temp_dir + '/{}.txt'.format(uuid.uuid4())
        if not save_to:
            save_to = self.temp_dir + '/{}.wav'.format(uuid.uuid4())
        with open(temp_file, 'w') as f:
            f.write(text)
        os.system('text2wave -o {out_fn} {in_fn}'.format(
            out_fn=save_to, in_fn=temp_file))
        return save_to
    
    def clean(self):
        """Deletes files in the temporary directory."""
        os.system('rm {}/*'.format(self.temp_dir))


def tts(text, save_to=None):
    """Converts text to audio WAV file. 
    Note: This function is provided for backward compatibility.

    @param: text: Text to convert.
    @type: text: str

    @param: save_to: File path including filename to save audio WAV file.
                        If not provided, will save to a randomly named file in
                        the temporary directory (by default: /tmp/simple-tts).
    @type: str

    @return: Full file path including filename to the saved audio WAV file.
    @rtype: str
    """
    obj = SimpleTTS()
    return obj.tts(text=text, save_to=save_to)
