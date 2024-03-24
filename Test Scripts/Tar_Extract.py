import tarfile

with tarfile.open("C:/Users/Great/Segregation AI/MobileNetV1 AI/mobilenet_v1_1.0_224_quant.tar", "r") as tar:
    tar.extractall("C:/Users/Great/Segregation AI/MobileNetV1 AI/Model/") 