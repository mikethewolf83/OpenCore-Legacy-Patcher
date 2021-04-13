# Lists all models and required patches
# Copyright (C) 2020-2021, Dhinak G, Mykola Grymalyuk
SupportedSMBIOS = [
    # To be overwritten on program start
]

SupportedSMBIOS11 = [
    # MacBook
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    # MacBook Air
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookAir5,1",
    "MacBookAir5,2",
    # MacBook Pro
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    # Mac Mini
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "Macmini6,1",
    "Macmini6,2",
    # iMac
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    # Mac Pro
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    # Xserve
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1"
]

SupportedSMBIOS12 = [

]

# CPU patches

MissingSSE42 = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "Macmini4,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "MacPro3,1",
    "Xserve2,1",
    "Dortania1,1"
]

SSEEmulator = [
    "MacPro3,1",
    "Xserve2,1",
    "Dortania1,1"
]

DualSocket = [
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1"
]

pciSSDT = [
    "MacBookPro6,1",
    "MacBookPro6,2",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "Dortania1,1"
]

# Ethernet patches

EthernetNvidia = [
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "Macmini3,1",
    "iMac9,1",
    "iMac10,1",
    "Dortania1,1"
]
EthernetMarvell = [
    "MacBook4,1",
    "MacBookPro4,1",
    "iMac7,1",
    "iMac8,1",
    "Dortania1,1"
]
EthernetBroadcom = [
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "Dortania1,1"
]

# Wifi patches

WifiAtheros = [
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "MacPro3,1",
    "MacPro4,1",
    "Dortania1,1"
]

WifiBCM94328 = [
    "MacBook4,1",
    "MacBookAir2,1",
    "MacBookPro4,1",
    "iMac7,1",
    "iMac8,1",
    "Dortania1,1"
]

WifiBCM94322 = [
    "MacBook5,1",
    "MacBook5,2",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "iMac9,1",
    "MacPro5,1",
    "Dortania1,1"
]

WifiBCM94331 = [
    "MacBook6,1",    # PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)
    "MacBook7,1",    # PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)
    "MacBookAir4,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookAir4,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookAir5,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookAir5,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro6,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro6,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro8,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro8,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro8,3",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro9,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro9,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro10,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro10,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini4,1",    # PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)
    "Macmini5,1",    # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini5,2",    # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini5,3",    # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini6,1",    # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini6,2",    # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "iMac13,1",      # PciRoot(0x0)/Pci(0x1C,0x3)/Pci(0x0,0x0)
    "iMac13,2",      # PciRoot(0x0)/Pci(0x1C,0x3)/Pci(0x0,0x0)
    "iMac13,3",      # PciRoot(0x0)/Pci(0x1C,0x3)/Pci(0x0,0x0)
    "Dortania1,1"
]

# Audio

LegacyAudio = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "MacPro3,1",
    "Dortania1,1"
]

nvidiaHDEF = [
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "Macmini4,1",
    "iMac9,1",
    "iMac10,1"
]

# GPU

LegacyGPU = [
    "MacBook4,1",  # GMA X3100
    "MacBook5,1",  # Nvidia 9000
    "MacBook5,2",  # Nvidia 9000
    "MacBook6,1",  # Nvidia 9000
    "MacBook7,1",  # Nvidia 300
    "MacBookAir2,1",  # Nvidia 9000
    "MacBookAir3,1",  # Nvidia 300
    "MacBookAir3,2",  # Nvidia 300
    "MacBookAir4,1",  # Intel 3000
    "MacBookAir4,2",  # Intel 3000
    "MacBookPro4,1",  # Nvidia 8000
    "MacBookPro5,1",  # Nvidia 9000
    "MacBookPro5,2",  # Nvidia 9000
    "MacBookPro5,3",  # Nvidia 9000
    "MacBookPro5,4",  # Nvidia 9000
    "MacBookPro5,5",  # Nvidia 9000
    "MacBookPro6,1",  # Intel 100 + Nvidia 300
    "MacBookPro6,2",  # Intel 100 + Nvidia 300
    "MacBookPro7,1",  # Nvidia 300
    "MacBookPro8,1",  # Intel 3000
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini3,1",  # Nvidia 9000
    "Macmini4,1",  # Nvidia 300
    "Macmini5,1",  # Intel 3000
    "Macmini5,2",  # AMD 6000
    "Macmini5,3",  # Intel 3000
    "iMac7,1",  # AMD 2000
    "iMac8,1", # Nvidia and AMD 2400
    "iMac9,1",  # Nvidia 9000
    "iMac10,1", # Nvidia 9000 and AMD 4000
    "iMac11,1",  # AMD 4000
    "iMac11,2",  # AMD 4000 and 5000
    "iMac11,3",  # AMD 5000
    "iMac12,1",  # AMD 6000
    "iMac12,2",  # AMD 6000
    "Dortania1,1"  # RTX 3080
]

LegacyGPUNvidia = [
    "MacBook5,1",  # Nvidia 9000
    "MacBook5,2",  # Nvidia 9000
    "MacBook6,1",  # Nvidia 9000
    "MacBook7,1",  # Nvidia 300
    "MacBookAir2,1",  # Nvidia 9000
    "MacBookAir3,1",  # Nvidia 300
    "MacBookAir3,2",  # Nvidia 300
    "MacBookPro4,1",  # Nvidia 8000
    "MacBookPro5,1",  # Nvidia 9000
    "MacBookPro5,2",  # Nvidia 9000
    "MacBookPro5,3",  # Nvidia 9000
    "MacBookPro5,4",  # Nvidia 9000
    "MacBookPro5,5",  # Nvidia 9000
    "MacBookPro6,1",  # Intel 100 + Nvidia 300
    "MacBookPro6,2",  # Intel 100 + Nvidia 300
    "MacBookPro7,1",  # Nvidia 300
    "Macmini3,1",  # Nvidia 9000
    "Macmini4,1",  # Nvidia 300
    "iMac9,1",  # Nvidia 9000
    # "iMac10,1", # Nvidia 9000 and AMD 4000
]

LegacyGPUAMD = [
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini5,2",  # AMD 6000
    "iMac7,1",  # AMD 2000
    # "iMac8,1", # Nvidia and AMD 2000
    # "iMac10,1", # Nvidia 9000 and AMD 4000
    "iMac11,1",  # AMD 4000
    "iMac11,2",  # AMD 4000 and 5000
    "iMac11,3",  # AMD 5000
    "iMac12,1",  # AMD 6000
    "iMac12,2",  # AMD 6000
]

LegacyGPUAMDIntelGen2 = [
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini5,2",  # AMD 6000
    "iMac12,1",  # AMD 6000
    "iMac12,2",  # AMD 6000
]

LegacyGPUIntelGen1 = [
    "MacBookPro6,1",  # Intel 100 + Nvidia 300
    "MacBookPro6,2",  # Intel 100 + Nvidia 300
]

LegacyGPUIntelGen2 = [
    "MacBookAir4,1",  # Intel 3000
    "MacBookAir4,2",  # Intel 3000
    "MacBookPro8,1",  # Intel 3000
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini5,1",  # Intel 3000
    "Macmini5,3",  # Intel 3000
]

LegacyBrightness = [
    "MacBook5,2",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
]

LegacyHID = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "Macmini4,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "MacPro3,1",
    "Dortania1,1"
]

NVMePatch = [
    "MacPro3,1",
    "MacPro4,1",
    "Xserve3,1",
    "Dortania1,1"
]

SidecarPatch = [
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "Macmini6,1",
    "Macmini6,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    "Dortania1,1"
]

DualGPUPatch = [
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini5,2",
    "iMac12,1",
    "iMac12,2",
    "iMac13,2",
    "iMac14,2",
    "iMac14,3",
    "Dortania1,1"
]

DualGPUPatchRetina = [
    "MacBookPro10,1",
]

HiDPIpicker = [
    "MacBookPro10,1",
    "MacBookPro10,2",
    "Dortania1,1"
]

IDEPatch = [
    "MacPro3,1",
    "Dortania1,1"
]

# 11" Air
MacBookAir61 = [
    "MacBookAir3,1",
    "MacBookAir4,1",
    "MacBookAir5,1",
]

# MacBook and 13" Air
MacBookAir62 = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,2",
    "MacBookAir4,2",
    "MacBookAir5,2"
]

# MacBook Pro 13"

MacBookPro111 = [
    "MacBookPro5,5",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro9,2",
    "MacBookPro10,2",
]

# MacBook Pro 15" and 17"

MacBookPro113 = [
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro10,1",
]

# Mac Mini

Macmini71 = [
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "Macmini6,1",
    "Macmini6,2"
]
# iMacPro = dGPU only iMacs
iMacPro11 = [
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
]

# iMac = AMD and Nvidia GPU with iGPU
iMac151 = [
    "iMac12,1",
    "iMac12,2",
    "iMac13,2",
    "iMac14,2",
    "iMac14,3"
]
# iMac = Intel iGPU
iMac144 = [
    "iMac13,1",
    "iMac14,1"
]

# Mac Pro and Xserve
MacPro71 = [
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1"
]

XXerve = [
    "Xserve3,1",
]

iXac = [
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
]

XacBookNormal = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
]

XacBookAir = [
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookAir5,1",
    "MacBookAir5,2",
]

XacBookPro = [
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
]

XacPro = [
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
]

Xacmini = [
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "Macmini6,1",
    "Macmini6,2",
]

ControllerTypes = [
    "",
    "-EHCI",
    "-EHC1",
    "-EHC2",
    "-XHC1",
    "-OHC1",
    "-OHC2",
    "-InternalHub-EHC1",
    "-InternalHub-EHC1-InternalHub",
    "-InternalHub-EHC2",
    "-InternalHub",
]

upgradableMXMGPUs = [
    "iMac10,1"
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "Xserve3,1",
    "Dortania1,1"
]

# Reference: https://forums.macrumors.com/threads/2011-imac-graphics-card-upgrade.1596614/
NVIDIAMXMGPUs = [
    "0x12b9",  # Quadro K610M
    "0x0ff6",  # Quadro K1100M
    "0x11fc",  # Quadro K2100M
    "0x0ffc",  # Quadro K1000M
    "0x0ffb",  # Quadro K2000M
    "0x11b6",  # Quadro K3100M
    "0x11b7",  # Quadro K4100M
    "0x11bc",  # Quadro K5000M
    "0x11b8",  # Quadro K5100M
    "0x11e1",  # GTX 765M
    "0x11e2",  # GTX 765M
    "0x11e0",  # GTX 770M
    "0x119e",  # GTX 780M Mac Edition
    "0x119e",  # GTX 780M
    "0x119f",  # GTX 880M
    "0x119a",  # GTX 860M
    "0x1392",  # GTX 860M
    "0x1199",  # GTX 870M
    "0x11a9",  # GTX 870M
]

AMDMXMGPUs = [
    "0x67EF",  # AMD RX 460
    "0x67e8",  # AMD WX 4130/WX 4150
    "0x67e0",  # AMD WX 4170
    "0x67c0",  # AMD WX 7100
]

BCM4360Wifi = [
    "43BA",  # BCM43602
    "43A3",  # BCM4350
    "43A0",  # BCM4360
]

BCM94331Wifi = [
    "4331",  # BCM94331
    "4353",  # BCM943224
]

BCM94322Wifi = [
    "432B",  # BCM94322
]

BCM94328Wifi = [
    "4311",
    "4312",
    "4313",
    "4318",
    "4319",
    "431A",
    "4320",
    "4324",
    "4325",
    "4328",
    "432C",
    "432D",
]

AtherosWifi = [
    "0030",
    "002A",
    "001C",
    "0023",
    "0024",
]

NightShiftExclude = [
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "Macmini6,1",
    "Macmini6,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
]

UGAtoGOP = [
    "MacBook4,1",
    "MacBookPro4,1",
    "iMac7,1",
    "iMac8,1",
    "MacPro3,1",
    "Xserve2,1",
]

NoSATAPatch = [
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
]

NoAPFSsupport = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBookAir2,1",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "Macmini3,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "MacPro3,1",
    "MacPro4,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1"
]

NoRootPatch11 = [
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "Macmini6,1",
    "Macmini6,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve3,1",
]

NoExFat = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "Macmini3,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1"
]

DeleteNvidiaAccel11 = [
    "AMDRadeonX4000.kext",
    "AMDRadeonX4000HWServices.kext",
    "AMDRadeonX5000.kext",
    "AMDRadeonX5000HWServices.kext",
    "AMDRadeonX6000.kext",
    "AMDRadeonX6000Framebuffer.kext",
    "AMDRadeonX6000HWServices.kext",
    "AppleIntelBDWGraphics.kext",
    "AppleIntelBDWGraphicsFramebuffer.kext",
    "AppleIntelCFLGraphicsFramebuffer.kext",
    "AppleIntelHD4000Graphics.kext",
    "AppleIntelHD5000Graphics.kext",
    "AppleIntelICLGraphics.kext",
    "AppleIntelICLLPGraphicsFramebuffer.kext",
    "AppleIntelKBLGraphics.kext",
    "AppleIntelKBLGraphicsFramebuffer.kext",
    "AppleIntelSKLGraphics.kext",
    "AppleIntelSKLGraphicsFramebuffer.kext",
    "AppleIntelFramebufferAzul.kext",
    "AppleIntelFramebufferCapri.kext",
    "AppleParavirtGPU.kext",
    "GeForce.kext",
    "IOAcceleratorFamily2.kext",
    "IOGPUFamily.kext",
]

DeleteAMDAccel11 = [
    "AMDRadeonX4000.kext",
    "AMDRadeonX4000HWServices.kext",
    "AMDRadeonX5000.kext",
    "AMDRadeonX5000HWServices.kext",
    "AMDRadeonX6000.kext",
    "AMDRadeonX6000Framebuffer.kext",
    "AMDRadeonX6000HWServices.kext",
    "AMD7000Controller.kext",  # AMDSupport Dependancy
    "AMD8000Controller.kext",  # AMDSupport Dependancy
    "AMD9000Controller.kext",  # AMDSupport Dependancy
    "AMD9500Controller.kext",  # AMDSupport Dependancy
    "AMD10000Controller.kext",  # AMDSupport Dependancy
    "AppleIntelBDWGraphics.kext",
    "AppleIntelBDWGraphicsFramebuffer.kext",
    "AppleIntelCFLGraphicsFramebuffer.kext",
    "AppleIntelHD4000Graphics.kext",
    "AppleIntelHD5000Graphics.kext",
    "AppleIntelICLGraphics.kext",
    "AppleIntelICLLPGraphicsFramebuffer.kext",
    "AppleIntelKBLGraphics.kext",
    "AppleIntelKBLGraphicsFramebuffer.kext",
    "AppleIntelSKLGraphics.kext",
    "AppleIntelSKLGraphicsFramebuffer.kext",
    "AppleIntelFramebufferAzul.kext",
    "AppleIntelFramebufferCapri.kext",
    "AppleParavirtGPU.kext",
    "GeForce.kext",
    "IOAcceleratorFamily2.kext",
    "IOGPUFamily.kext",
]

AddNvidiaAccel11 = [
    "GeForceGA.bundle",
    "GeForceTesla.kext",
    "GeForceTeslaGLDriver.bundle",
    "GeForceTeslaVADriver.bundle",
    "NVDANV50HalTesla.kext",
    "NVDAResmanTesla.kext",
    "IOSurface.kext",
]

AddNvidiaBrightness11 = [
    "GeForceGA.bundle",
    "GeForceTesla.kext",
    "GeForceTeslaGLDriver.bundle",
    "GeForceTeslaVADriver.bundle",
    "NVDANV50HalTesla.kext",
    "NVDAResmanTesla.kext",
]

AddAMDAccel11 = [
    "AMD2400Controller.kext",
    "AMD2600Controller.kext",
    "AMD3800Controller.kext",
    "AMD4600Controller.kext",
    "AMD4800Controller.kext",
    "AMD5000Controller.kext",
    "AMD6000Controller.kext",
    "AMDFramebuffer.kext",
    "AMDLegacyFramebuffer.kext",
    "AMDLegacySupport.kext",
    "AMDRadeonVADriver.bundle",
    "AMDRadeonVADriver2.bundle",
    # "AMDRadeonX3000.kext", # __ZN22IOAccelDisplayMachine210gMetaClassE link issues
    # "AMDRadeonX3000GLDriver.bundle",
    "AMDShared.bundle",
    "AMDSupport.kext",
    "ATIRadeonX2000.kext",
    "ATIRadeonX2000GA.plugin",
    "ATIRadeonX2000GLDriver.bundle",
    "ATIRadeonX2000VADriver.bundle",
    "IOSurface.kext",
]

AddAMDBrightness11 = [
    "AMD2400Controller.kext",
    "AMD2600Controller.kext",
    "AMD3800Controller.kext",
    "AMD4600Controller.kext",
    "AMD4800Controller.kext",
    "AMD5000Controller.kext",
    "AMD6000Controller.kext",
    "AMDLegacyFramebuffer.kext",
    "AMDLegacySupport.kext",
    "AMDRadeonX3000.kext",
    "AMDRadeonX3000GLDriver.bundle",
    "ATIRadeonX2000.kext",
    "ATIRadeonX2000GA.plugin",
    "ATIRadeonX2000GLDriver.bundle",
    "ATIRadeonX2000VADriver.bundle",
]

AddIntelGen1Accel = [
    "AppleIntelFramebufferAzul.kext",
    "AppleIntelFramebufferCapri.kext",
    "AppleIntelHDGraphics.kext",
    "AppleIntelHDGraphicsFB.kext",
    "AppleIntelHDGraphicsGA.plugin",
    "AppleIntelHDGraphicsGLDriver.bundle",
    "AppleIntelHDGraphicsVADriver.bundle",
    "IOSurface.kext",
]

AddIntelGen1Brightness = [
    "AppleIntelFramebufferAzul.kext",
    "AppleIntelFramebufferCapri.kext",
    "AppleIntelHDGraphics.kext",
    "AppleIntelHDGraphicsFB.kext",
    "AppleIntelHDGraphicsGA.plugin",
    "AppleIntelHDGraphicsGLDriver.bundle",
    "AppleIntelHDGraphicsVADriver.bundle",
]

AddIntelGen2Accel = [
    "AppleIntelHD3000Graphics.kext",
    "AppleIntelHD3000GraphicsGA.plugin",
    "AppleIntelHD3000GraphicsGLDriver.bundle",
    "AppleIntelHD3000GraphicsVADriver.bundle",
    "AppleIntelSNBGraphicsFB.kext",
    "AppleIntelSNBVA.bundle",
    "IOSurface.kext",
]

AddIntelGen2Brightness = [
    "AppleIntelHD3000Graphics.kext",
    "AppleIntelHD3000GraphicsGA.plugin",
    "AppleIntelHD3000GraphicsGLDriver.bundle",
    "AppleIntelHD3000GraphicsVADriver.bundle",
    "AppleIntelSNBGraphicsFB.kext",
    "AppleIntelSNBVA.bundle",
]

DeleteBrightness = [
    "AppleGraphicsControl.kext/Contents/PlugIns/AGDCBacklightControl.kext"
]

AddBrightness = [
    "AppleBacklight.kext",
    "AppleBacklightExpert.kext",
]

# List supported IDs

TeraScale1pciid = [
	"0x9400",
	"0x9401",
	"0x9402",
	"0x9403",
	"0x9581",
	"0x9583",
	"0x9588",
	"0x94c8",
	"0x94c9",
	"0x9500",
	"0x9501",
	"0x9505",
	"0x9507",
	"0x9504",
	"0x9506",
	"0x9598",
	"0x9488",
	"0x9599",
	"0x9591",
	"0x9593",
	"0x9440",
	"0x9442",
	"0x944A",
	"0x945A",
	"0x9490",
	"0x949E",
	"0x9480",
	"0x9540",
	"0x9541",
	"0x954E",
	"0x954F",
	"0x9552",
	"0x9553",
	"0x94a0",
]

TeraScale2pciid = [
	"0x6738",
	"0x6739",
	"0x6720",
	"0x6722",
	"0x6768",
	"0x6770",
	"0x6779",
	"0x6760",
	"0x6761",
	"0x68E0",
	"0x6898",
	"0x6899",
	"0x68B8",
	"0x68B0",
	"0x68B1",
	"0x68A0",
	"0x68A1",
	"0x6840",
	"0x6841",
	"0x68D8",
	"0x68C0",
	"0x68C1",
	"0x68D9",
	"0x6750",
	"0x6758",
	"0x6759",
	"0x6740",
	"0x6741",
	"0x6745",
]

IronLakepciid = [
	"0x0044",
	"0x0046",
]

SandyBridgepiciid = [
	"0x0106",
	"0x0601",
	"0x0116",
	"0x0102",
	"0x0126",
]