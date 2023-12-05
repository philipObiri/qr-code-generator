## Dynamic QR Code Generator 

This is a desktop application that allows users to generate functional qrcode images  with ease.

<img src="./demo.png" width="900px">

### Packages Utilized :
- Pillow : Rendering the QR code in a sannable image (format = ".png")
- tkinter : For constructing the entire Graphical User Interface
- Segno :  Translating links to QR code 


### How to run this on your local machine : 
- Clone the project :
```
git clone https//github.com/philipObiri/qr-code-generator.git
```

- Switch directory into the project :
```
cd qr-code-generator
```

- Create a virtual environment :<br>
(Windows)
```
python -m venv venv 
```
(Linux)
```
python3 -m venv venv 
```


- Activate virtual environment :<br>
(Windows)
```
cd venv/Scripts/activate
```

(Mac/Linux)
```
source venv/bin/activate
```

- Install required python  packages :<br>
(Windows)
```
pip install -r requirements.txt
```
(Linux/Mac)
```
pip install -r requirements.txt
```
- Once the packages are installed :<br>
(Windows)
```
python ./qrcode_generator.py
```
(Mac/Linux)
```
python3 ./qrcode_generator.py
```
