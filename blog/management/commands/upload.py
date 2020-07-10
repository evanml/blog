from os import path, listdir
from django.core.management.base import BaseCommand, CommandError
from blog.models import Photo, Gallery
from django.contrib.auth.models import User
from django.utils import timezone
import shutil

img_list = listdir('/Users/elarrimore/Desktop/Photos/upload_test')
gal_name = path.basename('/Users/elarrimore/Desktop/Photos/upload_test')
src_dir = '/Users/elarrimore/Desktop/Photos/upload_test'
media_dir = '/Users/elarrimore/Desktop/PG/media/images'

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
            if not photo.startswith('.'):
                img_title = path.splitext(photo)[0]
                img = path.basename(media_dir) + '/' + photo
                usr = User.objects.get(username='elarrimore')




                upload = Photo(
                    author = usr,
                    title = img_title,
                    image = img,
                    created_date = timezone.now(),
                    published_date = timezone.now(),
                    active = False,
                    gallery = Gallery.objects.get(title='upload_test')
                    )
                upload.save()
        #copy files to media dir
        for photo in img_list:
            if not photo.startswith('.'):
                shutil.copy(path.join(src_dir, photo), media_dir)
