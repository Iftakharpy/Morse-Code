import numpy as np
from scipy.io.wavfile import write

BIT_RATE=44100


def max_num_for_bits(bits=4):

    return (2**(bits-1))-1

def nums(stop, bits=4):
    max_val = max_num_for_bits(bits)
    start = 0
    while start<stop+1:
        yield start % max_val
        start += 1


def gen_sound_arr(seconds, frequency=120, amplitude=1, bitrate=BIT_RATE, silent=False):
    if silent:
        return gen_sound_arr(seconds, frequency=0, amplitude=0)
    # https://en.wikipedia.org/wiki/Compact_Disc_Digital_Audio
    # samples per second
    sps = bitrate

    # frequency/pitch of sound(sine wave) : unit (Hz)
    frequency = frequency

    # duration of the audio/sound : unit s(seconds)
    duration = seconds

    # total samples
    total_samples = duration*sps
    
    # numbers
    sample_numbers = np.array(list(nums(total_samples)))

    # generating sin wave
    wave_form = np.sin( (2 * np.pi * sample_numbers * frequency)/ sps )
    
    # changing amplitude of the wave form
    changed_apm_sound = wave_form * amplitude

    # final wave form
    # wave_form_ints = np.int16(low_sound * 32767) #converting to 16 bit audio
    max_val = max_num_for_bits(16)

    wave_form_ints = np.int16(changed_apm_sound * max_val) #converting to 16 bit audio
    return wave_form_ints


if __name__ == "__main__":
    write("sound_high.wav", BIT_RATE, gen_sound_arr(10))
