from music21 import converter
import os

def convert_midi_xml():
    path_curfile = os.path.dirname(os.path.abspath(__file__))
    path_to_og_midi = os.path.join(path_curfile, "files", "midi_with_lyrics.mid")

    # parse the midi file to xml
    abc_score = converter.parse(path_to_og_midi, forceSource=True)

    # write the xml file

    abc_score.write('xml', fp='files/og_file_converter.musicxml')

def convert_xml_to_midi():
    path_curfile = os.path.dirname(os.path.abspath(__file__))
    path_to_xml = os.path.join(path_curfile, "files", "og_file_converter.musicxml")

    abc_score = converter.parse(path_to_xml, forceSource=True)

    abc_score.write('midi', fp='files/og_file_xml_midi_version.mid')



if __name__ == "__main__":
    convert_midi_xml()
    convert_xml_to_midi()
