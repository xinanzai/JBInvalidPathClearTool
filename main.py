import os
import xml.etree.ElementTree as ET

def traverseJetBrainsFolders():
    appDataPath = os.getenv('APPDATA')
    jetBrainsPath = os.path.join(appDataPath, 'JetBrains')

    if not os.path.exists(jetBrainsPath):
        print("JetBrains directory does not exist.")
        return

    for folderName in os.listdir(jetBrainsPath):
        folderPath = os.path.join(jetBrainsPath, folderName)
        if os.path.isdir(folderPath):
            jdkTablePath = os.path.join(folderPath, 'options', 'jdk.table.xml')
            if os.path.exists(jdkTablePath):
                processJdkTable(jdkTablePath)

def processJdkTable(jdkTablePath):
    tree = ET.parse(jdkTablePath)
    root = tree.getroot()
    applicationComponent = root.find('./component')

    if applicationComponent is not None:
        jdkNodes = applicationComponent.findall('jdk')
        for jdk in jdkNodes:
            homePathElement = jdk.find('homePath')
            if homePathElement is not None:
                homePath = homePathElement.get('value')
                if homePath.startswith(r"$USER_HOME$"):
                    nhomePath = homePath.replace(r"$USER_HOME$", os.path.expanduser("~"))
                else:
                    nhomePath = homePath
                if nhomePath and not os.path.exists(nhomePath):
                    applicationComponent.remove(jdk)
                    print(f"Removed JDK with missing path: {homePath} in {jdkTablePath}")
        tree.write(jdkTablePath)
    else:
        pass

if __name__ == "__main__":
    traverseJetBrainsFolders()
    anything = input("请输入任意字符退出程序.......\n")
