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

    def construct_image(self):
        final_image = st.SVGFigure("20in", "20in")

        print(len(self.faces))
        for ix, face in enumerate(self.faces):
            features = self.build_face(face)
            cat = Cat(features=features)
            image = cat.get_template()
            image.save('../data/merged_' + str(ix) + '.svg')
            final_image.append(image)

        final_image.save('../data/merged.svg')



    def build_face(self, face):
        features = []
        landmarks = face['faceLandmarks']
        left_eyebrow_details = (landmarks['eyebrowLeftInner'],landmarks['eyebrowLeftOuter'])
        features.append(FacialFeature(left_eyebrow_details, style='left_eyebrow'))

        right_eyebrow_details = (landmarks['eyebrowRightInner'],landmarks['eyebrowRightOuter'])
        features.append(FacialFeature(right_eyebrow_details, style='right_eyebrow'))

        left_eye_details = (landmarks['eyeLeftInner'],landmarks['eyeLeftOuter'])
        features.append(FacialFeature(left_eye_details, style='left_eye'))

        right_eye_details = (landmarks['eyeRightInner'],landmarks['eyeRightOuter'])
        features.append(FacialFeature(right_eye_details, style='right_eye'))

        nose_details = (landmarks['noseRootLeft'],landmarks['noseRootRight'])
        features.append(FacialFeature(nose_details, style='nose'))

        mouth_details = (landmarks['mouthLeft'], landmarks['mouthRight'])
        features.append(FacialFeature(mouth_details, style='mouth'))

        return features

if __name__ == '__main__':
    cc = CatCreator('../data/us2.jpg')
    cc.construct_image()




