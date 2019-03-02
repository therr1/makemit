import svgutils.transform as st


class FacialFeature:
    def __init__(self, features, style="eye"):
        self.features = features
        self.style = style
        self.file_path = "../data/face/" + style + '.svg'

    def get_template(self):
        left = self.features[0]
        right = self.features[1]

        template = st.fromfile(self.file_path).getroot()
        template.moveto(left['x'], left['y'], scale=0.5)
        return template

