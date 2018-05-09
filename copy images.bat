@echo off
rem set dest=E:\Downloads\Evellum\peterborough_images\
set src=E:\Downloads\Evellum\exeter3.0\resources\facsimiles\Ex_Cath_Lib_MS_3501
set dest=E:\Downloads\Evellum\exeter3.0\resources\facsimiles\MS_Auct_F_2_13
copy /y "%src%\exeter_thumb\*" "%dest%\terence_thumb\"
copy /y "%src%\exeter_360\*" "%dest%\terence_360\"
copy /y "%src%\exeter_600\*" "%dest%\terence_600\"
copy /y "%src%\exeter_600_gif\*" "%dest%\terence_600_gif\"
copy /y "%src%\exeter_1200\*" "%dest%\terence_1200\"
copy /y "%src%\exeter_2400\*" "%dest%\terence_2400\"
copy /y "%src%\exeter_3600\*" "%dest%\terence_3600\"
