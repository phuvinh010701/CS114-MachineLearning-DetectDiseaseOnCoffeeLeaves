# Cách cài đặt:
* ### Tải model yolov4 : [link](https://drive.google.com/drive/folders/1sJYP4Y0kVbMeCnVLhfRxDV6ooQc3zeCM?usp=sharing)
* ### Copy thư mục model vừa tải về  để vào thư mục chứa code demo có cấu trúc như sau:
```bash
├── model
│   ├── yolov4.cfg
│   └── yolov4.weights
├── static
├── templates
├── README.md
├── README.pdf
├── requirements.txt
├── server.py
```
* ### Linux:
<pre>pip3 install -r requirements.txt</pre>

* ### Window:
<pre>pip install -r requirements.txt</pre>

# Cách chạy ứng dụng:

* ### Linux:
<pre>python3 server.py</pre>
* ### Window:
<pre>python server.py</pre>
