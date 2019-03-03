import svgutils.transform as st
import os
import random


class FacialFeature:
    def __init__(self, left_pos, top_pos, scaling=1, style="eye",version=None, number=None, file_name_override=None):
        self.left_pos = left_pos
        self.top_pos = top_pos
        self.scaling = scaling
        self.style = style

        file_names = os.listdir("../data/face/" + style + '/')
        file_names_final = []
        if version is not None:
            # file_names = [file_name (if version in file_name) for file_name  in file_names]
            for file_name in file_names:
                if version in file_name:
                    file_names_final.append(file_name)

        if len(file_names_final) == 0:
            for file_name in file_names:
                if not '_' in file_name:
                    file_names_final.append(file_name)

        print(version)
        print(file_names_final)
        file_name = random.choice(file_names_final)
        print(file_name)
        self.file_name = file_name
        if file_name_override:
            self.file_name = file_name_override
        self.file_path = "../data/face/" + style + '/' + self.file_name

        # if not os.path.isfile(self.file_path):
        #     self.file_path = "../data/face/" + style + '/' + '1.svg'

        self.version = version

    def get_file_name(self):
        return self.file_name

    def get_template(self):

        template = st.fromfile(self.file_path).getroot()
        template.moveto(self.left_pos, self.top_pos, scale=self.scaling)
        return template

