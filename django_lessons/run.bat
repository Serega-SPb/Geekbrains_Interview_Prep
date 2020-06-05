echo off
echo Activate venv

IF EXIST venv goto this_dir
IF EXIST ..\venv goto parent_dir

echo Directory venv not found
set /p other_path="Enter venv dir:"
set activate=%other_path%\Scripts\activate
echo %activate%
call %activate%
goto end

:this_dir
echo venv\Scripts\activate
call venv\Scripts\activate
goto end

:parent_dir
echo ..\venv\Scripts\activate
call ..\venv\Scripts\activate
goto end

:end
echo Start local server
python shop_storage\manage.py runserver
