# JBInvalidPathClearTool
这个工具旨在解决JetBrains工具集无法完全清理干净早些项目遗留的 [invalid] 状态的运行环境问题，以Pycharm举例，当某个项目使用了venv配置，在项目文件夹下创建了venv文件夹和python环境，当移动了这个项目目录，就会在pycharm中产生一个[invalid] 状态的环境配置，而通过File-Settings-Project-Python Interpreter-Show All弹出的对话框删除掉无效的运行环境后，重启pycharm，该环境依然会在调试配置的Run/Debug Configurations的下拉列表中出现，我无法在软件界面中找到清理它们的办法，当项目很多时，看着很不美观，此时就可以通过运行本项目清理所有无效配置项。
***
This tool is designed to address the issue of leftover [invalid] runtime environments from earlier projects that JetBrains' suite of tools cannot completely clean up. Taking PyCharm as an example, when a project uses venv configuration and creates a venv folder along with a Python environment within the project directory, moving this project directory can result in an [invalid] environment configuration within PyCharm. Even after deleting the invalid runtime environment through "File" > "Settings" > "Project" > "Python Interpreter" > "Show All", and then restarting PyCharm, the environment still appears in the dropdown list under "Run/Debug Configurations" Dialog. There is no clear way to clean these up through the software interface, which can be unappealing when working with many projects. In such cases, you can use this tool to clear all invalid configuration items.

![image](https://github.com/user-attachments/assets/ac8b4a40-3c7f-459c-872a-e6739e353dec)
![image](https://github.com/user-attachments/assets/af429c65-d7b9-4eba-b442-1e03d54c5954)
