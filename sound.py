import wave
import numpy as np
from wave_audio import gen_sound_arr
from checkers import is_valid_morse



channels = 1
sample_width = 2
bitrate = 44100
seconds = 1
params = (channels, sample_width, bitrate, bitrate*seconds, "NONE", "Not Compressed")


starting_offset = 1
ending_offset = .5

dot_audio_len =  .3# unit seconds(s)
dash_audio_len = dot_audio_len*1.6
space_audio_len = .15

# sound frequency
dot_frequency = 120
dash_frequency = 120

# sound amplitude(loudness)
dot_amp = 100
dash_amp = 100

dot_audio = gen_sound_arr(seconds=dot_audio_len, frequency=dot_frequency, amplitude=dot_amp)
dash_audio = gen_sound_arr(seconds=dash_audio_len, frequency=dash_frequency, amplitude=dash_amp)
space_audio = gen_sound_arr(seconds=space_audio_len, silent=True)


def write_audio_for_morse_code(file_name, morse_code_string):
    # making sure the morse code is valid
    assert is_valid_morse(morse_code_string)

    #blank sound a the start
    code_arr = np.concatenate((gen_sound_arr(seconds=starting_offset, silent=True),))

    #making sound for the morse code
    for ch in morse_code_string:
        if ch==".":
            code_arr = np.concatenate((code_arr, dot_audio, space_audio))
        elif ch=="-":
            code_arr = np.concatenate((code_arr, dash_audio, space_audio))
        else:
            code_arr = np.concatenate((code_arr, space_audio, space_audio))
    #blank sound at the end
    code_arr = np.concatenate((code_arr, gen_sound_arr(seconds=ending_offset, silent=True)))
    
    # openning an audio file
    audio_file = wave.open(file_name,"w")

    # setting headers for the audio file
    audio_file.setparams(params)

    # writing sound
    audio_file.writeframesraw(code_arr)

    #closing the file
    audio_file.close()



file_name = "hello_world_2.wav"
morse_code = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
write_audio_for_morse_code(file_name, morse_code)