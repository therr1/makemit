import svgutils.transform as st
from ArticleOfClothing import ArticleOfClothing


class Cat:
    def __init__(self, clothes=None, bodyparts=None, features=None, gender='m', glasses='n', ):
        self.gender = gender
        self.bodyparts = bodyparts
        self.clothes = clothes
        self.features = features

    def get_template(self):
        """
        """
        final_cat = st.SVGFigure("20in", "20in")
        for feature in self.features:
            feature_template = feature.get_template()
            final_cat.append(feature_template)

        return final_cat
        # for cloth in self.clothes:
        #     cloth_template = cloth.get_article()
        #     final_cat.append(cloth_template)

        # final_cat.save('../data/merged.svg')


    def get_base_cat(self):
        template = st.fromfile('../data/articles/drawsvg.svg').getroot()
        return template


if __name__ == '__main__':
    shirt = ArticleOfClothing(style="shirt")
    clothes = [shirt]
    cat = Cat(clothes=clothes)
    cat.get_cat()