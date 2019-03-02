import svgutils.transform as st


class ArticleOfClothing:
    def __init__(self, style=None, color='black'):
        self.style = style
        self.color = color
        self.base_file = '../data/articles/' + self.style + '.svg'

    def get_article(self):
        """
        get_article returns a list of tuples, each tuple
        consisting of a (start_x, start_y, end_x, end_y) set
        """
        if self.style == None:
            return None
        else:
            return st.fromfile(self.base_file).getroot()
