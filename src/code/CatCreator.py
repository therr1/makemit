import cognitive_face as CF
from FacialFeature import FacialFeature
from Cat import Cat
import svgutils.transform as st


KEY = '4711ef57700b4631b05c282d2b7ffa35'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

class CatCreator:
    def __init__(self, image_path):
        self.image_path = image_path
        attributes = "age,gender,headPose,smile,facialHair,glasses,emotion,makeup,accessories"
        self.faces = CF.face.detect(image_path, landmarks=True, attributes=attributes)
        print(self.faces)

    def construct_image(self):
        self.get_scalings()
        final_image = st.SVGFigure("20in", "20in")

        print(len(self.faces))
        for ix, face in enumerate(self.faces):
            scaling = self.scalings[ix]
            features = self.build_face(face,scaling=scaling)
            cat = Cat(features=features)
            image = cat.get_template()
            image.save('../data/merged_' + str(ix) + '.svg')
            final_image.append(image)

        final_image.save('../data/merged.svg')

    def get_scalings(self):
        scalings = []
        widths = [face['faceRectangle']['width'] for face in self.faces]
        scalings = [width/max(widths) for width in widths]
        self.scalings = scalings


    def get_emotion(self, face):
        emotions = face['faceAttributes']['emotion']
        anger = float(emotions['anger'])
        surprise = float(emotions['surprise'])
        neutral = float(emotions['neutral'])
        happiness = float(emotions['happiness'])

        if anger > 0.05:
            return 'anger'
        if neutral > 0.8:
            return 'neutral'
        if surprise > 0.6:
            return 'surprise'
        else:
            return None


    def build_face(self, face, scaling=1):
        features = []
        landmarks = face['faceLandmarks']
        version = 1
        left_eyebrow_details = (landmarks['eyebrowLeftInner'],landmarks['eyebrowLeftOuter'])
        rectangle = face['faceRectangle']
        left_pos, top_pos =  rectangle['left'], rectangle['top']
        emotion = self.get_emotion(face)



        feature_names = ['left_eyebrow', 'right_eyebrow', 'head', 'left_eye', 'right_eye', 'body', 'left_ear', 'right_ear', 'nose', 'mouth']
        # super hacky, put all lefts before rights in above list otherwise it breaks lmao

        file_name = None
        for feature_name in feature_names:
            ff = None
            if 'left' in feature_name:
                ff =  FacialFeature(left_pos, top_pos, scaling, style=feature_name, version=emotion, number=None)
                file_name = ff.get_file_name()
            elif 'right' in feature_name:
                ff =  FacialFeature(left_pos, top_pos, scaling, style=feature_name, version=emotion, file_name_override=file_name)
                file_name = None
            else:
                ff =  FacialFeature(left_pos, top_pos, scaling, style=feature_name, version=emotion, number=None)

            features.append(ff)


        return features

if __name__ == '__main__':
    cc = CatCreator('../data/us_final.jpg')
    cc.construct_image()




