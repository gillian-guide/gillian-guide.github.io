import os
import sys
import json
import logging
import requests
import subprocess
import tarfile
import configparser
import pyperclip
import webbrowser
from PySide6 import QtCore, QtWidgets
from win32api import GetFileVersionInfo, LOWORD, HIWORD, GetSystemMetrics, EnumDisplaySettings, EnumDisplayDevices

def convert_apiversion(apiversion):
    major = apiversion >> 22
    minor = (apiversion >> 12) & 0x3ff
    return f"{major}.{minor}"

def get_version_number (filename):
    try:
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return 0,0,0,0


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

def vulkancheck():
    i = 0
    vk_dgpu_dxvk_support=0
    vk_igpu_dxvk_support=0
    igpuonly=True
    dgpuonly=True
    inteligpu=False
    try:
        while True:
            if i==0:
                logging.debug(f"Running vulkaninfo on GPU0...")
            else:  
                logging.debug(f"Attempting to run vulkaninfo on GPU{i} if it exists...")
            subprocess.run(["vulkaninfo", f"--json={i}", "--output", f"data{i}.json"], check = True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            i += 1
    except: pass

    for x in range(i):
        try:
            f = open(f"data{x}.json")
        except: break
        dxvk_support=0
        data = json.load(f)['capabilities']['device']
        vulkanver = convert_apiversion(data['properties']['VkPhysicalDeviceProperties']['apiVersion']) 
        logging.debug(data['properties']['VkPhysicalDeviceProperties']['deviceName'] + "'s supported Vulkan version is: " + vulkanver)
        try:
            if data['extensions']['VK_EXT_robustness2'] >= 1 and data['extensions']['VK_EXT_transform_feedback'] >= 1 and data['features']['VkPhysicalDeviceRobustness2FeaturesEXT']['robustBufferAccess2'] == True and data['features']['VkPhysicalDeviceRobustness2FeaturesEXT']['nullDescriptor'] == True:
                logging.info("This GPU supports Latest DXVK.")
                dxvk_support=2
        except:
            if vulkanver < "1.1":
                logging.error("This GPU is not supported by DXVK.")
            elif vulkanver >= "1.1" and vulkanver < "1.3":
                logging.warning("This GPU only supports Legacy DXVK.")
                dxvk_support=1
        if data['properties']['VkPhysicalDeviceProperties']['deviceType'] == "VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU" and dxvk_support>vk_dgpu_dxvk_support:
            vk_dgpu_dxvk_support=dxvk_support
            igpuonly=False
        elif dxvk_support>vk_igpu_dxvk_support:
            vk_igpu_dxvk_support=dxvk_support
            dgpuonly=False
            if data['properties']['VkPhysicalDeviceProperties']['deviceName'].startswith("Intel"):
                inteligpu=True
        f.close()
        os.remove(f"data{x}.json")
    
    return vk_dgpu_dxvk_support, vk_igpu_dxvk_support, igpuonly, dgpuonly, inteligpu

def installdxvkfun(dl, dir, dxvkconf):    
    logging.debug("Saving the archive...")
    archive=open('./dxvk.tar.gz', 'wb')
    archive.write(dl.content)
    archive.close()

    logging.debug("Extracting d3d9.dll from the archive...")
    tar=tarfile.open("dxvk.tar.gz", mode='r')
    dll=open(dir + "/d3d9.dll", "wb")
    dll.write(tar.extractfile(os.path.commonprefix(tar.getnames()) + "/x32/d3d9.dll").read())
    dll.close()
    tar.close()
    os.remove('dxvk.tar.gz')

    logging.debug("Writing dxvk.conf to the game directory...")
    conf=open(dir + "/dxvk.conf", "w")
    for option in dxvkconf:
        conf.write(option + '\n')
    conf.close()

class DXVKInstaller(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        logTextBox = QTextEditLogger(self)
        # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)
        self.setWindowTitle("Gillian's GTA IV Setup Utility")
        self.button = QtWidgets.QPushButton("Start")
        self.text = QtWidgets.QLabel("Welcome to Gillian's GTA IV Setup Utility", alignment=QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(logTextBox.widget)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        logging.info("Asking user to choose the directory with GTAIV.exe...")
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Open GTA 4 directory")
        if not os.path.isfile(dir + "\GTAIV.exe"):
            QtWidgets.QMessageBox.critical(None,'Error',"Selected directory isn't the game directory", QtWidgets.QMessageBox.Abort)
            logging.error("User chose a directory with no GTAIV.exe in it.")
            return
        gtaVersion = ".".join ([str (i) for i in get_version_number (dir + "\GTAIV.exe")])

        installdxvk=0
        dxvk_support=vulkancheck()
        dgpu_dxvk_support = dxvk_support[0]
        igpu_dxvk_support = dxvk_support[1]
        igpuonly = dxvk_support[2]
        dgpuonly = dxvk_support[3]
        inteligpu = dxvk_support[4]

        match igpuonly, dgpuonly:
            case True, False:
                logging.info("User's PC only has an iGPU.")
                match igpu_dxvk_support:
                    case 0:
                        logging.error("User's PC only has an iGPU and it does not support DXVK.")
                    case 1:
                        logging.warning("User's PC only has an iGPU but it supports Legacy DXVK. Installing...")
                        installdxvk=1
                    case 2:
                        logging.info("User's PC only has an iGPU but it supports Latest DXVK. Installing...")
                        installdxvk=2
            case False, True:
                logging.info("User's PC only has a GPU.")
                match dgpu_dxvk_support:
                    case 0:
                        logging.error("User's GPU does not support DXVK.")
                    case 1:
                        logging.warning("User's GPU only supports Legacy DXVK. Installing...")
                        installdxvk=1
                    case 2:
                        logging.info("User's GPU supports Latest DXVK. Installing...")
                        installdxvk=2
            case False, False:
                logging.info("User's PC has both a GPU and an iGPU. Doing further checks...")
                match dgpu_dxvk_support, igpu_dxvk_support:
                    case (0,0):
                        logging.error("None of user's GPU's support DXVK.")
                    case (0,1) | (0,2):
                        logging.info("Only user's iGPU supports DXVK. Asking what do they want to do...")
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Your iGPU supports DXVK but your GPU doesn't - do you still wish to install?")
                        installaskYes = msgBox.addButton("Yes", QtWidgets.QMessageBox.YesRole)
                        installaskNo = msgBox.addButton("No", QtWidgets.QMessageBox.NoRole)
                        msgBox.exec()
                        if msgBox.clickedButton() == installaskYes:
                            match igpu_dxvk_support:
                                case 1:
                                    logging.info("User chose to install the version matching their iGPU - Legacy. Installing...")
                                    installdxvk=1
                                case 2:
                                    logging.info("User chose to install the version matching their iGPU - Latest. Installing...")
                                    installdxvk=2
                    case (1,2):
                        logging.info("User's iGPU supports a greater version of DXVK than their GPU. Asking what do they want to do...")
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Your iGPU supports a greater version of DXVK than your GPU - which version do you wish to install? Press 'Version 1' to install the version matching your GPU or 'Version 2' to install the version matching your iGPU instead.")
                        installaskver1 = msgBox.addButton("Version 1", QtWidgets.QMessageBox.YesRole)
                        installaskver2 = msgBox.addButton("Version 2", QtWidgets.QMessageBox.YesRole)
                        msgBox.exec()
                        if msgBox.clickedButton() == installaskver1:
                                logging.info("User chose to install the version matching their GPU - Legacy. Installing...")
                                installdxvk=1
                        elif msgBox.clickedButton() == installaskver2:
                                logging.info("User chose to install the version matching their iGPU - Latest. Installing...")
                                installdxvk=2
                    case (2,2) | (1,1) | (2,1) | (2,0):
                        logging.info("User's GPU supports same or better version of DXVK as iGPU.")
                        match dgpu_dxvk_support:
                            case 1:
                                logging.info("Installing Legacy version...")
                                installdxvk=1
                            case 2:
                                logging.info("Installing Latest version...")
                                installdxvk=2

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Do you want to use an async fork? It will provide better performance for most, but under some conditions it may provide worse performance instead. Without async, you might stutter the first time you see different areas. It won't stutter the next time in the same area.")
        installasync = msgBox.addButton("Yes", QtWidgets.QMessageBox.YesRole)
        noButton = msgBox.addButton("No", QtWidgets.QMessageBox.NoRole)
        msgBox.exec()
        dxvkconf=['d3d9.maxFrameLatency = 1', 'd3d9.presentInterval = 1', 'd3d9.numBackBuffers = 3']
        if inteligpu==True and igpuonly==True and installdxvk!=0:
            logging.info("User only has an intel iGPU in the system, asking them what to do... (upgrade your PC it's not fit for gaming at all - DXVK won't save you)")
            msgBox2 = QtWidgets.QMessageBox()
            msgBox2.setText("Your PC only has an Intel iGPU on it. While it does support more modern versions on paper, it's reported that DXVK 1.10.1 might be your only supported version. Do you wish to install it? If 'No' is selected, DXVK will be installed following the normal procedure.")
            yesButton = msgBox2.addButton("Yes", QtWidgets.QMessageBox.YesRole)
            noButton = msgBox2.addButton("No", QtWidgets.QMessageBox.NoRole)
            msgBox2.exec()
            if msgBox2.clickedButton() == yesButton:
                installdxvk=3
        match installdxvk:
            case 0:
                logging.info("DXVK won't be installed.")
                QtWidgets.QMessageBox.critical(None,'Error',"Your card doesn't support DXVK or you chose not to install it.", QtWidgets.QMessageBox.Abort)
            case 1:
                if msgBox.clickedButton() == installasync:
                    logging.info("DXVK-async 1.10.3 will be installed.")
                    logging.debug('Appending options to dxvk.conf...')
                    dxvkconf.append('dxvk.enableAsync = true')
                    logging.debug("Downloading DXVK-async 1.10.3...")
                    dl = requests.get(requests.get("https://api.github.com/repos/Sporif/dxvk-async/releases/assets/73567231", allow_redirects=True).json()['browser_download_url'], allow_redirects=True)
                    installdxvkfun(dl, dir, dxvkconf)
                    logging.info("Installed DXVK-async 1.10.3.")
                else:
                    logging.info("DXVK 1.10.3 will be installed.")
                    logging.debug("Downloading DXVK 1.10.3...")
                    dl = requests.get(requests.get("https://api.github.com/repos/doitsujin/dxvk/releases/assets/73461736", allow_redirects=True).json()['browser_download_url'], allow_redirects=True)
                    installdxvkfun(dl, dir, dxvkconf)
                    logging.info("Installed DXVK 1.10.3.")
            case 2:
                if msgBox.clickedButton() == installasync:
                    logging.info("Latest DXVK-gplasync will be installed.")
                    logging.debug('Appending options to dxvk.conf...')
                    logging.debug("Downloading latest DXVK-gplasync...")
                    dxvkconf.append('dxvk.enableAsync = true')
                    dxvkconf.append('dxvk.gplAsyncCache = true')
                    dl = requests.get(requests.get("https://gitlab.com/api/v4/projects/43488626/releases/", allow_redirects=True).json()[0]['assets']['links'][0]['url'], allow_redirects=True)
                    installdxvkfun(dl, dir, dxvkconf)
                    logging.info("Installed latest DXVK-gplasync.")
                else:
                    logging.info("Latest DXVK will be installed.")
                    logging.debug("Downloading latest DXVK...")
                    dl = requests.get(requests.get("https://api.github.com/repos/doitsujin/dxvk/releases/latest", allow_redirects=True).json()['assets'][0]['browser_download_url'], allow_redirects=True)
                    installdxvkfun(dl, dir, dxvkconf)
                    logging.info("Installed latest DXVK.")
            case 3:
                if msgBox.clickedButton() == installasync:
                    logging.info("DXVK-async 1.10.1 will be installed.")
                    logging.debug('Appending options to dxvk.conf...')
                    dxvkconf.append('dxvk.enableAsync = true')
                    logging.debug("Downloading DXVK-async 1.10.1...")
                    dl = requests.get(requests.get("https://api.github.com/repos/Sporif/dxvk-async/releases/assets/60677007", allow_redirects=True).json()['browser_download_url'], allow_redirects=True)
                    installdxvkfun(dl, dir, dxvkconf)
                    logging.info("Installed DXVK-async 1.10.1.")
                else:
                    logging.info("DXVK 1.10.1 will be installed.")
                    logging.debug("Downloading DXVK 1.10.1...")
                    dl = requests.get(requests.get("https://api.github.com/repos/doitsujin/dxvk/releases/assets/60669426", allow_redirects=True).json()['browser_download_url'], allow_redirects=True)
                    installdxvkfun(dl, dir, dxvkconf)
                    logging.info("Installed DXVK 1.10.1.")


        logging.info("DXVK installed - proceeding with launch options.")
        commandline=['-norestrictions']

        ## -nomemrestrict or -managed
        if installdxvk != 0:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Do you wish to use -managed or -nomemrestrict? -managed is not compatible with -nomemrestrict, and it may increase your load times. If using DXVK however, it may provide better performance in some cases.\n\n-nomemrestrict, in it's turn, allows to avoid issues when the game runs out of it's own VRAM limits.\n\nYou can always switch them yourself later.")
            yesbtn = msgBox.addButton("-managed", QtWidgets.QMessageBox.YesRole)
            nobtn = msgBox.addButton("-nomemrestrict", QtWidgets.QMessageBox.NoRole)
            msgBox.exec()
            if msgBox.clickedButton() == yesbtn:
                commandline.append('-managed')
            else:
                commandline.append('-nomemrestrict')
        else:
            logging.info("User didn't install DXVK - -managed is not needed.")
            commandline.append('-nomemrestrict')

        ## Borderless Windowed enabler
        if os.path.isfile(dir + '/ZolikaPatch.asi') == True and os.path.isfile(dir + '/ZolikaPatch.ini') == True:
            logging.info("ZolikaPatch detected - enabling Borderless Windowed.")
            zpatchconfig = configparser.ConfigParser()
            zpatchconfig.read(dir + '/ZolikaPatch.ini')
            if zpatchconfig['Options']['BorderlessWindowed'] != "1":
                zpatchconfig['Options']['BorderlessWindowed']="1"
                with open(dir + '/ZolikaPatch.ini', 'w') as config:
                    zpatchconfig.write(config)
                    config.close()
            commandline.append('-windowed')
        elif (os.path.isfile(dir + '/GTAIV.EFLC.FusionFix.asi') == True and os.path.isfile(dir + '/GTAIV.EFLC.FusionFix.ini') == True) or (os.path.isfile(dir + '/plugins/GTAIV.EFLC.FusionFix.asi') == True and os.path.isfile(dir + '/plugins/GTAIV.EFLC.FusionFix.ini') == True):
            logging.info("FusionFix detected - enabling Borderless Windowed.")
            ffconfig = configparser.ConfigParser()
            try:   
                ffconfig.read(dir + '/GTAIV.EFLC.FusionFix.ini')
                if ffconfig['MAIN']['BorderlessWindowed'] != "1":
                    ffconfig['MAIN']['BorderlessWindowed']="1"
                    with open(dir + '/GTAIV.EFLC.FusionFix.ini', 'w') as config:
                        ffconfig.write(config)
                        config.close()
            except:
                ffconfig.read(dir + '/plugins/GTAIV.EFLC.FusionFix.ini')
                if ffconfig['MAIN']['BorderlessWindowed'] != "1":
                    ffconfig['MAIN']['BorderlessWindowed']="1"
                    with open(dir + '/plugins/GTAIV.EFLC.FusionFix.ini', 'w') as config:
                        ffconfig.write(config)
                        config.close()
            commandline.append('-windowed')
        logging.info("Borderless Windowed is set up.")
        
        ## VRAM Check
        if installdxvk != 0:
            try:
                vram = subprocess.run(["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader", "--id=0"], universal_newlines = True, capture_output=True, check = True).stdout.strip("\n").strip(" MiB")
                logging.info("NVIDIA GPU detected - checking the VRAM amount.")
                commandline.append('-availablevidmem ' + vram)
                logging.debug("User has " + vram + " MB of VRAM.")
            except:
                logging.info("No NVIDIA GPU detected - asking the user to input VRAM on their own.")
                while True:
                    inputbox, ok = QtWidgets.QInputDialog().getInt(self, "VRAM Setup", "We can't query your VRAM amount automatically - check it yourself by typing dxdiag in start menu, press Enter, go through 'Display' tabs and type the biggest 'Approx. Total Memory' value you find. Type it in this box:")
                    if inputbox < 128:
                        QtWidgets.QMessageBox.critical(None,'Error',"Please enter a valid amount.", QtWidgets.QMessageBox.Retry)
                    else:
                        commandline.append('-availablevidmem ' + vram)
                        break
        else:
            logging.info("User didn't install DXVK - specifying VRAM is not needed.")

        ## Monitor info
        if installdxvk != 0:
            logging.info("Adding primary display info to the launch options.")
            commandline.append('-width ' + str(GetSystemMetrics(0)))
            commandline.append('-height ' + str(GetSystemMetrics(1)))
            commandline.append('-refreshrate ' + str(EnumDisplaySettings(EnumDisplayDevices().DeviceName, -1).DisplayFrequency))
        else:
            logging.info("User didn't install DXVK - specifying screen details is not needed.")

        cmdltext=' '.join([str(elem) for elem in commandline])
        logging.debug("Final launch options: " + cmdltext)

        ## Save launch options
        match gtaVersion:
            case e if gtaVersion.startswith("1.0"):
                logging.debug("Writing commandline.txt to the game directory...")
                cmdl=open(dir + "/commandline.txt", "w")
                for option in commandline:
                    cmdl.write(option + '\n')
                cmdl.close()
            case other:
                logging.info("User plays on 1.2 (probably), can't input settings automatically.")
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Since you didn't downgrade, there is no way to apply those settings automatically. Please input these options in your Launch Options on Steam manually:\n\n" + cmdltext + '\n\nThese options will be saved to your clipboard when you press OK.')
                msgBox.addButton("OK", QtWidgets.QMessageBox.AcceptRole)
                msgBox.exec()
                pyperclip.copy(cmdltext)
        
        logging.info("User's done with setting up. Linkng them to the guide...")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Automatic stage is complete. After pressing 'OK', you'll be redirected to my web guide to setting up GTA IV - set up the optimal game settings following that page.")
        yesbtn = msgBox.addButton("OK", QtWidgets.QMessageBox.AcceptRole)
        msgBox.exec()
        if msgBox.clickedButton() == yesbtn:
            webbrowser.open('https://gillian-guide.github.io/additional-setup/#optimal-game-settings')
            sys.exit()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = DXVKInstaller()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())