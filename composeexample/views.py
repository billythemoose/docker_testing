from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import generics
from rest_framework import status
from composeexample.models import *
from composeexample.serializers import UserSerializer, FilesSerializer
from composeexample.models import Files

import io
import os.path
import json
import re
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from django.conf import settings

class UserListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class HelloWorld(APIView):
    def get(self, request):
        return Response('Hello World! from Django.')

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def extract_text_by_page(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as fh:
                for page in PDFPage.get_pages(fh, 
                                            caching=True,
                                            check_extractable=True):
                    resource_manager = PDFResourceManager()
                    fake_file_handle = io.StringIO()
                    converter = TextConverter(resource_manager, fake_file_handle)
                    page_interpreter = PDFPageInterpreter(resource_manager, converter)
                    page_interpreter.process_page(page)
                    text = fake_file_handle.getvalue()
        except Exception as err:
            print(err)
            converter.close()
            fake_file_handle.close()
        else:
            yield text
                    # close open handles
            converter.close()
            fake_file_handle.close()
    serializer_class = UserSerializer

    def convert_to_list(self,text):
        reg = "\s[A-Z]{2,4}&?\s+[0-9][0-9][0-9]\s"
        clist = re.findall(reg,text)
        #print(re.findall(reg,text))
        for index,element in enumerate(clist):
            element = element.replace(" ","")
            clist[index] = element
        #print(element);
        #print(clist);
        return clist

    def convert_to_json(self,list):
            jsFormated = json.dumps(list)
            return jsFormated


    def save_to_db(self,list,sid):
            from composeexample.models import Student;
            try:
                transcript = Student(id=sid,cid=list)
                transcript.save()
            except Exception as err:
                print(err)
                return False
            else:
                return True

    def post(self, request, *args, **kwargs):
        file_serializer = FilesSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            print(str(request.FILES['file']))
            print(settings.MEDIA_ROOT)
            filepath = os.path.join(settings.MEDIA_ROOT, str(request.FILES['file']))
            converted = self.extract_text(filepath)
            #converted = self.extract_json(filepath, str(request.FILES['file'])) 
            return Response(converted, status=status.HTTP_201_CREATED)
            # return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    