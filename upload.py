from google_cred import * 
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def docxDriveUpload(service):

    file_metadata = {'name': 'demo.docx'}
    media = MediaFileUpload('demo.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

    file = service.files().create(body = file_metadata, media_body = media, fields = 'id').execute()

    print('File upload successful! File ID: {}'.format(file.get('id')))
    
service = get_service()
docxDriveUpload(service)
