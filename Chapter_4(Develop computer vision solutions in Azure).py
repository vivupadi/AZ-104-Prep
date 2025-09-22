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
###########

###########
'''Detect, analyze and recognize faces'''
###########


###########
'''Classify images'''
###########


###########
'''Detect objects in images'''
###########


###########
'''Analyze video'''
###########


###########
'''Develop a vision-enabled generative AI application'''
###########


###########
'''Generate images with AI'''
###########
