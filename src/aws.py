# import boto3


# class AWS():
#     def __init__(self, bucketname):
#         self.polly = boto3.client("polly")
#         self.s3 = boto3.client("s3")
#         self.bucketname = bucketname
#         self.provision()
#         pass

#     def provision(self):
#         # create the s3 bucket for the data
#         self.s3.create_bucket(Bucket=self.bucketname, ACL="public-read")
#         pass

#     def upload(self, key, body):
#         # upload the image to s3
#         return self.s3.put_object(
#             Bucket=self.bucketname,
#             Body=body,
#             Key=key,
#             ACL="public-read"
#         )
    
#     def transcribe(self, text):
#         # transcribe the text and upload to and s3 bucket
#         response = self.polly.synthesize_speech(
#             Engine='neural',
#             LanguageCode='es-ES',
#             LexiconNames=[
#                 'string',
#             ],
#             OutputFormat='mp3',
#             SampleRate='string',
#             SpeechMarkTypes=['sentence','ssml','viseme','word'],
#             Text=text,
#             TextType='text',
#             VoiceId='Camila'
#         )
#         stream = response["AudioStream"]
#         # upload audio stream to s3
#         upload = self.upload(key=text, body=stream.read())
#         return upload
