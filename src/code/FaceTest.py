import cognitive_face as CF

KEY = '4711ef57700b4631b05c282d2b7ffa35'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
faces = CF.face.detect("../data/me.jpg", landmarks=True, attributes="age,gender,headPose,smile,facialHair,glasses,emotion,makeup,accessories")
print(faces)

