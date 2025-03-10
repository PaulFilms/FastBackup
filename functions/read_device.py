'''
Prompt:
`usando python, cual es el mejor metodo para listar todos los archivos de un pendrive, e identificarlo independientemente de la letra que asigne window`

Respuesta ChatGPT:

Para listar todos los archivos de un pendrive en Windows usando Python e identificarlo independientemente de la letra asignada, puedes seguir estos pasos:

Detectar el pendrive: Se puede buscar en win32api.GetLogicalDriveStrings() o usando psutil.disk_partitions().
Listar archivos recursivamente: Usar os.walk() o pathlib.Path.rglob("*").
Aquí tienes un código que detecta el pendrive y lista sus archivos:

```
import os
import psutil
from pathlib import Path

def get_usb_drive():
    """Detecta la letra de la unidad USB en Windows."""
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'removable' in partition.opts:  # Identifica unidades extraíbles
            return partition.mountpoint  # Devuelve la letra de la unidad
    return None

def list_files_in_usb():
    """Lista todos los archivos en el pendrive."""
    usb_drive = get_usb_drive()
    if not usb_drive:
        print("No se detectó ninguna unidad USB.")
        return

    print(f"Unidad USB detectada: {usb_drive}")
    usb_path = Path(usb_drive)

    # Listar archivos de manera recursiva
    for file in usb_path.rglob("*"):  # Recorrer archivos y carpetas
        print(file)

list_files_in_usb()
```

Explicación:
psutil.disk_partitions() obtiene todas las unidades montadas y filtra las que son removibles (pendrives).
Se obtiene la letra de la unidad USB automáticamente.
Path(usb_drive).rglob("*") lista todos los archivos y carpetas recursivamente.
Si tienes varios pendrives conectados, el código detectará el primero que encuentre. Si necesitas manejar múltiples dispositivos, podemos modificarlo para listar todos. 🚀


import os, subprocess
from psutil import disk_partitions
from pathlib import Path

def get_usb_drive():
    """Detecta la letra de la unidad USB en Windows."""
    partitions = disk_partitions()
    for partition in partitions:
        if 'removable' in partition.opts:  # Identifica unidades extraíbles
            # print(partition.opts)
            # print(partition.mountpoint)
            # serial = get_drive_serial(partition.mountpoint)
            # print(serial)
            return partition.mountpoint  # Devuelve la letra de la unidad
    return None

def list_files_in_usb():
    """Lista todos los archivos en el pendrive."""
    usb_drive = get_usb_drive()
    if not usb_drive:
        print("No se detectó ninguna unidad USB.")
        return

    print(f"Unidad USB detectada: {usb_drive}")
    usb_path = Path(usb_drive)

    # Listar archivos de manera recursiva
    for file in usb_path.rglob("*"):  # Recorrer archivos y carpetas
        print(file)

def get_drive_serial(drive_letter):
    """Obtiene el número de serie del volumen usando WMIC."""
    try:
        cmd = f'wmic logicaldisk where "DeviceID=\'{drive_letter}\'" get VolumeSerialNumber /value'
        result = subprocess.check_output(cmd, shell=True, text=True).strip()
        serial = result.split('=')[-1].strip() if '=' in result else None
        return serial
    except Exception as e:
        print(f"Error obteniendo serial de {drive_letter}: {e}")
        return None

def get_drive_label(drive_letter):
    """Obtiene el nombre del volumen de la unidad."""
    try:
        cmd = f'wmic logicaldisk where "DeviceID=\'{drive_letter}\'" get VolumeName /value'
        result = subprocess.check_output(cmd, shell=True, text=True).strip()
        label = result.split('=')[-1].strip() if '=' in result else None
        return label
    except Exception as e:
        print(f"Error obteniendo nombre de {drive_letter}: {e}")
        return None

# list_files_in_usb()

# usb = get_usb_drive()
# print(usb)

# serial = get_drive_serial("D:")
# print(serial)

# serial = get_drive_label("D:")
# print(serial)'

'''

from win32api import GetVolumeInformation
from dataclasses import dataclass

from psutil import disk_partitions

@dataclass
class HDD:
    label: str
    fstype: str
    removable: bool
    re_writable: bool
    letter: str = None


def get_mounted_drives() -> list[HDD]:
    # system = os.name
    # if system == "nt": # Windows
    #     drives = [os.path.splitdrive(p.mountpoint)[0] for p in disk_partitions(all=True)]
    # else: # macOS/Linux
    #     drives = [p.mountpoint for p in disk_partitions(all=True)]
    hdd_list = list()
    for partition in disk_partitions(all=True):
        # print(partition)
        # cmd = f'wmic logicaldisk where "DeviceID=\'{drive}\'" get VolumeName /value'
        # result = subprocess.check_output(cmd, shell=True, text=True).strip()
        # label = result.split('=')[-1].strip() if '=' in result else None
        # print(label)
        # cmd = f'wmic logicaldisk where "DeviceID=\'{drive}\'" get VolumeSerialNumber /value'
        # result = subprocess.check_output(cmd, shell=True, text=True).strip()
        # serial = result.split('=')[-1].strip() if '=' in result else None
        # print(serial)
        fromwin32 = GetVolumeInformation(partition.mountpoint) # (label: str, int, int, int, format: str = 'NTFS')
        hdd_list.append(
            HDD(
                label=fromwin32[0],
                fstype=partition.fstype,
                removable='removable' in partition.opts,
                re_writable='rw' in partition.opts,
                letter=partition.mountpoint
            )
        )
    return hdd_list