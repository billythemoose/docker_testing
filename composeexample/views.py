from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import generics
from rest_framework import status
from composeexample.models import Users
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
                yield text
                # close open handles
                converter.close()
                fake_file_handle.close()

    def extract_json(self, pdf_path, name):
        data = {'Filename': name}
        data['Pages'] = []

        counter = 1
        for page in self.extract_text_by_page(pdf_path):
            text = page[0:100]
            page = {'Page_{}'.format(counter): text}
            data['Pages'].append(page)
            counter += 1
        return data
        #with open(os.path.join(settings.MEDIA_ROOT, name + "_json"), w) as fh:
            #json.dump(data, fh)

    def convert_to_json(self, text):
        split_text = str(text).split()
        for index, obj in enumerate(split_text):
            # regex expressions
            # {3,5} 3 to 5 characters
            # [A-Z] capital letters
            # | or 
            # (&amp;|&) ampersand
            skipping = False
            if re.search("^[A-Z]{2,5}$|^[A-Z]{2,4}\&$", obj):
                #if not skipping:
                if index < (len(split_text)-1) and re.search('^[0-9]{3}$', split_text[index + 1]):
                    #skipping = True
                    index_offset = index
                    build_string = ""
                    curernt_string = split_text[index]
                    print("Start string " + curernt_string)
                    print (re.search("[0-9].[0,9]", curernt_string))
                    while not re.search("[0-9].[0,9]", curernt_string): 
                        print("current string " + curernt_string)
                        curernt_string = split_text[index_offset] + " "
                        build_string += curernt_string
                        index_offset += 1
                    print(build_string)
                #if skip_count == 0:
                    #skip_count = 4
                    #skipping = False

    def extract_text(self, pdf_path):
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        with open(pdf_path, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()
        if text:
            self.convert_to_json(text)
            return text

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

    