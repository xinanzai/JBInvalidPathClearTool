@echo off
setlocal

rem 设置路径变量
set PYTHON_EXE=.\venv\Scripts\python.exe
set NUITKA_BAT=.\venv\Scripts\nuitka.bat
set NUITKA_CMD=.\venv\Scripts\nuitka.cmd

rem 检查 nuitka.bat 或 nuitka.cmd 是否存在
if exist "%NUITKA_BAT%" (
    set NUITKA_EXEC=%NUITKA_BAT%
    echo Found nuitka.bat
) else if exist "%NUITKA_CMD%" (
    set NUITKA_EXEC=%NUITKA_CMD%
    echo Found nuitka.cmd
) else (
    echo nuitka.bat or nuitka.cmd not found, installing nuitka...
    "%PYTHON_EXE%" -m pip install nuitka

    rem 检查 nuitka 是否安装成功
    if exist "%NUITKA_BAT%" (
        set NUITKA_EXEC=%NUITKA_BAT%
        echo Successfully installed nuitka.bat.
    ) else if exist "%NUITKA_CMD%" (
        set NUITKA_EXEC=%NUITKA_CMD%
        echo Successfully installed nuitka.cmd.
    ) else (
        echo Failed to install nuitka.
        exit /b 1
    )
)

rem 注意，项目目录全路径不能含有中文
rem 执行 nuitka 编译
rem 注意替换 xxxxx 为您的源文件名和任何必要的编译选项
"%NUITKA_EXEC%" --standalone --onefile --windows-icon-from-ico=icon.ico --output-dir=dist --output-filename=JBInvalidPathClearTool.exe  main.py

endlocal