@echo off
rem set dest=E:\Downloads\Evellum\peterborough_images\
set dest=E:\Downloads\Evellum\peterborough\resources\facsimiles\MS_Auct_F_2_13
magick convert "E:\Downloads\Evellum\peterborough_images\peterborough_originals\xiiv.jpg" -resize x120 "%dest%\terence_thumb\xiiv.gif"
magick convert "E:\Downloads\Evellum\peterborough_images\peterborough_originals\xiiv.jpg" -resize x360 "%dest%\terence_360\xiiv.png"
magick convert "E:\Downloads\Evellum\peterborough_images\peterborough_originals\xiiv.jpg" -resize x600 "%dest%\terence_600\xiiv.png"
magick convert "E:\Downloads\Evellum\peterborough_images\peterborough_originals\xiiv.jpg" -resize x600 "%dest%\terence_600_gif\xiiv.gif"
magick convert "E:\Downloads\Evellum\peterborough_images\peterborough_originals\xiiv.jpg" -resize x1200 "%dest%\terence_1200\xiiv.jpg"
magick convert "E:\Downloads\Evellum\peterborough_images\peterborough_originals\xiiv.jpg" -resize x2400 "%dest%\terence_2400\xiiv.jpg"
magick convert "E:\Downloads\Evellum\peterborough_images\peterborough_originals\xiiv.jpg" -resize x3600 "%dest%\terence_3600\xiiv.jpg"
