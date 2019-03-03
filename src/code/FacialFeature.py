import svgutils.transform as st
import os

class FacialFeature:
    def __init__(self, left_pos, top_pos, scaling=1, style="eye",version=None):
        self.left_pos = left_pos
        self.top_pos = top_pos
        self.scaling = scaling
        self.style = style
        self.file_path = "../data/face/" + style + '/' + str(version) + '.svg'

        if not os.path.isfile(self.file_path):
            self.file_path = "../data/face/" + style + '/' + '1.svg'

        self.version = version

    def get_template(self):

        template = st.fromfile(self.file_path).getroot()
        template.moveto(self.left_pos, self.top_pos, scale=self.scaling)
        return template

