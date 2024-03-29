from os import path, listdir
from django.core.management.base import BaseCommand, CommandError
from blog.models import Photo, Gallery
from django.contrib.auth.models import User
from django.utils import timezone
import shutil
import cloudinary
import cloudinary.uploader
import cloudinary.api

img_list = listdir('/Users/elarrimore/Desktop/Photos/Cambodia/Cambodia Best/Cambodia Website')
gal_name = path.basename('/Users/elarrimore/Desktop/Photos/Cambodia/Cambodia Best/Cambodia Website')
src_dir = '/Users/elarrimore/Desktop/Photos/Cambodia/Cambodia Best/Cambodia Website'
#media_dir = '/Users/elarrimore/Desktop/PG/media/images'

class Command(BaseCommand):
    help = 'Uploads photos as objects'




    def handle(self, *args, **kwargs):
        # attempt 1 to auto_create gallery instance

        #    if gal_name not in Gallery.objects.all().values_list('title'):
        #        new_gal = Gallery(title = gal_name)
        #        final_gal = new_gal.save()
        #    else:
        #        final_gal = gal_name
        for photo in img_list:
            #removes hidden files
            if not photo.startswith('.'):
                # extracts filename without .jpg
                img_title = path.splitext(photo)[0]
                # creates usable file for display
                #img = path.basename(media_dir) + '/' + photo
                # gets userid
                usr = User.objects.get(username='elarrimore')




                upload = Photo(
                    author = usr,
                    title = img_title,
                    image = cloudinary.uploader.upload(photo),
                    created_date = timezone.now(),
                    published_date = timezone.now(),
                    active = False,
                    gallery = Gallery.objects.get(title='Cambodia')
                    )
                upload.save()



        #copy files to media dir
"""
        for photo in img_list:
            if not photo.startswith('.'):
                #copies image from folder to blog media file
                shutil.copy(path.join(src_dir, photo), media_dir)
"""
