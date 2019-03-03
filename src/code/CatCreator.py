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
        emotions = face['emotion']
        anger = float(emotions['anger'])
        sadness = float(emotions['sadness'])
        neutral = float(emotions['neutral'])
        happiness = float(emotions['happiness'])

        if anger > 0:
            return 'anger'
        if neutral > 0.8:
            return 'neutral':
        if sadness > 0.6:
            return 'sadness':
        else:
            return 'happiness'


    def build_face(self, face, scaling=1):
        features = []
        landmarks = face['faceLandmarks']
        version = 1
        left_eyebrow_details = (landmarks['eyebrowLeftInner'],landmarks['eyebrowLeftOuter'])
        rectangle = face['faceRectangle']
        left_pos, top_pos =  rectangle['left'], rectangle['top']
        emotion = self.get_emotion



        feature_names = ['left_eyebrow', 'right_eyebrow', 'head', 'left_eye', 'right_eye', 'body', 'left_ear', 'right_ear', 'nose', 'mouth']
        for feature_name in feature_names:
            ff =  FacialFeature(left_pos, top_pos, scaling, style=feature_name, version=emotion)
            features.append(ff)
        # left_eyebrow_details = (landmarks['eyebrowLeftInner'],landmarks['eyebrowLeftOuter'])
        # features.append(FacialFeature(left_eyebrow_details, style='left_eyebrow',version=version))

        # right_eyebrow_details = (landmarks['eyebrowRightInner'],landmarks['eyebrowRightOuter'])
        # features.append(FacialFeature(right_eyebrow_details, style='right_eyebrow',version=version))

        # left_eye_details = (landmarks['eyeLeftInner'],landmarks['eyeLeftOuter'])
        # features.append(FacialFeature(left_eye_details, style='left_eye',version=version))

        # right_eye_details = (landmarks['eyeRightInner'],landmarks['eyeRightOuter'])
        # features.append(FacialFeature(right_eye_details, style='right_eye',version=version))

        # nose_details = (landmarks['noseRootLeft'],landmarks['noseRootRight'])
        # features.append(FacialFeature(nose_details, style='nose', version=version))

        # mouth_details = (landmarks['mouthLeft'], landmarks['mouthRight'])
        # features.append(FacialFeature(mouth_details, style='mouth', version=version))

        return features

if __name__ == '__main__':
    cc = CatCreator('../data/us_final.jpg')
    cc.construct_image()




