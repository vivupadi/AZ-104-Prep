###########
'''Analyze Images'''

#Azure AI vision

##Submitting an image for analysis

#To analyze an image, you can use the Analyze Image REST method or the equivalent method 
# in the SDK for your preferred programming language, specifying the visual features 
# you want to include in the analysis.

#check the features available: Tags, Caption, DenseCaption, object, persons, smart crops, read
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

client = ImageAnalysisClient(
    endpoint="<YOUR_RESOURCE_ENDPOINT>",
    credential=AzureKeyCredential("<YOUR_AUTHORIZATION_KEY>")
)

result = client.analyze(
    image_data=<IMAGE_DATA_BYTES>, # Binary data from your image file
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS],
    gender_neutral_caption=True,
)

#The response is in Json format
{
  "apim-request-id": "abcde-1234-5678-9012-f1g2h3i4j5k6",
  "modelVersion": "<version>",
  "denseCaptionsResult": {
    "values": [
      {
        "text": "a house in the woods",
        "confidence": 0.7055229544639587,
        "boundingBox": {
          "x": 0,
          "y": 0,
          "w": 640,
          "h": 640
        }
      },
      {
        "text": "a trailer with a door and windows",
        "confidence": 0.6675070524215698,
        "boundingBox": {
          "x": 214,
          "y": 434,
          "w": 154,
          "h": 108
        }
      }
    ]
  },
  "metadata": {
    "width": 640,
    "height": 640
  }
}

###########

###########
'''Read text in Images'''

'''
Options:
1. Azure AI Vision
  - Optical Character Recognition
  - Digital Asset Management (DAM)

2. Azure AI Document Intelligence
  - Form processing
  - Prebuilt models
  - Custom models

3. Azure AI Content Understanding
  - Multimodal Content Extraction
  - Custom content analysis scenarios
'''

'''
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

client = ImageAnalysisClient(
    endpoint="<YOUR_RESOURCE_ENDPOINT>",
    credential=AzureKeyCredential("<YOUR_AUTHORIZATION_KEY>")
)

result = client.analyze(
    image_data=<IMAGE_DATA_BYTES>, # Binary data from your image file
    visual_features=[VisualFeatures.READ],
    language="en",
)'''


###########

###########
'''Detect, analyze and recognize faces'''

"""
Uses:
1. Face Detection
2. Face attribute analysis
3. Facial landmark location
4. Face comparison
5. Facial recognition
6. Facial liveness"""


"""
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import *
from azure.core.credentials import AzureKeyCredential

face_client = FaceClient(
    endpoint="<YOUR_RESOURCE_ENDPOINT>",
    credential=AzureKeyCredential("<YOUR_RESOURCE_KEY>"))
    
# Specify facial features to be retrieved
features = [FaceAttributeTypeDetection01.HEAD_POSE,
            FaceAttributeTypeDetection01.OCCLUSION,
            FaceAttributeTypeDetection01.ACCESSORIES]

# Use client to detect faces in an image
with open("<IMAGE_FILE_PATH>", mode="rb") as image_data:
    detected_faces = face_client.detect(
        image_content=image_data.read(),
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_id=True,
        return_face_attributes=features,
    )
        """
###########


###########
'''Classify images'''

"""
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient


 # Authenticate a client for the prediction API
credentials = ApiKeyCredentials(in_headers={"Prediction-key": "<YOUR_PREDICTION_RESOURCE_KEY>"})
prediction_client = CustomVisionPredictionClient(endpoint="<YOUR_PREDICTION_RESOURCE_ENDPOINT>",
                                                 credentials=credentials)

# Get classification predictions for an image
image_data = open("<PATH_TO_IMAGE_FILE>"), "rb").read()
results = prediction_client.classify_image("<YOUR_PROJECT_ID>",
                                           "<YOUR_PUBLISHED_MODEL_NAME>",
                                           image_data)

# Process predictions
for prediction in results.predictions:
    if prediction.probability > 0.5:
        print(image, ': {} ({:.0%})'.format(prediction.tag_name, prediction.probability))
"""
###########


###########
'''Detect objects in images'''

"""
Needs 2 Custome vision resources:
1. Azure AI Custome Vision training
2. Azure AI Custom Vision prediction

Can be used:
azure-cognitiveservices-vision-customvision



from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient


 # Authenticate a client for the prediction API
credentials = ApiKeyCredentials(in_headers={"Prediction-key": "<YOUR_PREDICTION_RESOURCE_KEY>"})
prediction_client = CustomVisionPredictionClient(endpoint="<YOUR_PREDICTION_RESOURCE_ENDPOINT>",
                                                 credentials=credentials)

# Get classification predictions for an image
image_data = open("<PATH_TO_IMAGE_FILE>", "rb").read()
results = prediction_client.detect_image("<YOUR_PROJECT_ID>",
                                           "<YOUR_PUBLISHED_MODEL_NAME>",
                                           image_data)

# Process predictions
for prediction in results.predictions:
    if prediction.probability > 0.5:
        left = prediction.bounding_box.left
        top = prediction.bounding_box.top 
        height = prediction.bounding_box.height
        width =  prediction.bounding_box.width
        print(f"{prediction.tag_name} ({prediction.probability})")
        print(f"  Left:{left}, Top:{top}, Height:{height}, Width:{width}")
"""
###########


###########
'''Analyze video'''

"""
3 main Concepts:
1. Azure Video Indexer capabilities
2. Extract custom insights
3. Use Azure Video Indexer widgets and APi's
4. Deploy with Azure Resource Manager(ARM) template
"""
###########


###########
'''Develop a vision-enabled generative AI application'''

"""
1. Deploy a multimodal model(Available in Az AI FOundry: Microsoft Phi-4, 
OpenAI gpt 4o, OpenAI gpt-4o-mini)
"""
###########


###########
'''Generate images with AI'''

"""
Image generation based on prompts.

Image generation models(like DAll E)
Controls available with Dall E:
  - resoluion (like 1024 x 1024)
  - image style (like vivid, natural)
  - image quality (standard or hd)

  How to use image generation models:
    - RestAPI
    - OenAI Python SDK or .Net SDK.

"""
###########
