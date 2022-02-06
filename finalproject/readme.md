<p align="center">
  <img src="https://www.uit.edu.vn/sites/vi/files/banner_uit_0.png" title="avatar_UIT">
</p>

<h1 align="center">
    
  **BÁO CÁO ĐỒ ÁN CUỐI KỲ**
  
  **PHÁT HIỆN MỘT SỐ BỆNH TRÊN LÁ CÂY CÀ PHÊ**

</h1>

* **Giáo viên hướng Dẫn** :

| STT | Họ tên | Email |
| :---: | --- | --- |
| 1 | **PGS.TS. Lê Đình Duy** | *duyld@uit.edu.vn* |
| 2 | **Ths. Phạm Nguyễn Trường An** | *truonganpn@uit.edu.vn* |

* **Giới thiệu thành viên nhóm**
<!-- ### Thông tin liên hệ -->
| STT | MSSV | Họ tên | Gmail |
|:--- | :-------|:----------|:------------|
|1|19521322|Huỳnh Ngọc Công Danh|19521322@gm.uit.edu.vn|
|2|19522524|Nguyễn Phú Vinh| 19522524@gm.uit.edu.vn|
|3|19521858|Võ Tuấn Minh|19521858@gm.uit.edu.vn|

[0]:https://github.com/danhhuynh25029
[2]:https://github.com/minh1304
[1]:https://github.com/phuvinh010701
[3]:https://www.facebook.com/danh250/
[4]:https://www.facebook.com/phuvinh0107
[5]:https://www.facebook.com/tuanminh.vo.73

# Chương 0. Giải trình chỉnh sửa sau vấn đáp
## Cách để đánh giá mô hình:
* Nhóm đã tiến hành cập nhật về đánh gía mô hình và cách xác định True Positive, False Positive sau những góp ý của thầy. Lý do chọn mean average precision là metric để đánh giá. [Link](#Đánh-giá-model)
## Số lượng số lượng sai sót của mỗi class trong mỗi mô hình:
* Nhóm tiến hành thống kê True Positive, False Positive của mỗi class trong mỗi mô hình để tiến hành xác định số lượng. [Link](#Số-lượng-sai-sót-của-mỗi-class)

# Chương 1. TỔNG QUAN

## 1.1 Mô tả bài toán
* Ngữ cảnh ứng dụng : 
    * Hiện nay, cà phê là một trong những loại thức uống được sử dụng phổ biến lẫn trong và ngoài nước. Cà phê được sản xuất từ những hạt cà phê rang, lấy trên cây cà phê.

    <p align="center">
    <img src="images/caphe.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%;"/>
    <br>
    <a style="text-align: center">Hình 1. Ảnh minh họa (Nguồn: Internet).</a>
    </p>

    * Theo báo điện tử VTV, trên 90% tổng sản lượng cà phê của Việt Nam dành cho việc xuất khẩu, khoảng 10% còn lại là dành cho việc chế biến và tiêu thụ trong nước. Cà phê nằm trong nhóm hàng nông sản xuất khẩu chủ lực của Việt Nam, hiện đứng thứ 2 thế giới (chỉ sau Brazil). Tính chung cả năm 2021, xuất khẩu cà phê của Việt Nam đạt 1,52 triệu tấn.

    <p align="center">
    <img src="images/bieudoxuatkhau.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%;"/>
    <br>
    <a style="text-align: center">Hình 2. Lượng cà phê xuất khẩu qua các tháng giai đoạn từ 2019-2021.</a>
    </p>

    * Sản lượng tuy lớn nhưng cà phê vẫn chưa đáp ứng được các tiêu chuẩn về chất lượng. Nhằm nâng cao chất lượng của hạt cà phê, việc phát hiện và xử lý những căn bệnh trên lá của cây rất quan trọng. Nhận thấy được vấn đề đó nên nhóm đã quyết định áp dụng những kiến thức của mình và những công nghệ trong lĩnh vực Machine Learning để giải quyết bài toán phát hiện một số loại bệnh trên lá cây cà phê.

    * Mô hình hướng tới người sử dụng là người trồng cây cà phê, xây dựng một ứng dụng có thể giúp người trồng có thể phát hiện chính xác hơn các loại bệnh đang gặp trên lá của cây và đưa ra được giải pháp phù hợp nhằm loại bỏ bệnh và tác nhân gây bệnh. 
    
* Input và Output:
    
    * Input:
        
        * Một tấm ảnh chụp hình lá của cây cà phê đang bị bệnh.

        <p align="center">
        <img src="images/viduinput.JPG" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
        <br>
        <a style="text-align: center">Hình 3. Ví dụ về ảnh input thích hợp.</a>
        </p>

        * Các điều kiện ràng buộc :
            + Ảnh chụp tập trung vào lá đang bị bệnh
            + Chụp được từ cuốn lá đến chóp lá
            + Chụp trong điều kiện ánh sáng ban ngày
            
    * Output:

        * Bounding box bao quanh lá cây bị bệnh
        * Tên loại bệnh
    <br>
    🠊 Trong ứng dụng thực tế hoàn chỉnh, dựa vào tên loại bệnh xác định được ứng dụng sẽ đưa ra các giải pháp phù hợp cho người trồng

## 1.2 Mô tả dữ liệu
* Dữ liệu của bài toán đươc nhóm tự thu thập từ mốt số vườn chuyên trồng cà phê trên địa bàn huyện Lạc Dương và địa bàn thành phố Đà Lạt thuộc tỉnh Lâm Đồng. Trong quá trình thu thập dữ liệu, nhóm gặp nhiều khó khăn như việc di chuyển đến các vườn cà phê khá xa so với nhà riêng (khoảng hơn 20 km), dịch bệnh COVID-19 khiến cho việc đi qua các chốt phong tỏa khó khăn.
    <p align="center">
    <img src="images/vuoncaphetramhanh.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 4. Vườn cà phê thuộc xã Trạm Hành, thành phố Đà Lạt, tỉnh Lâm Đồng.</a>
    </p>
* Bộ dữ liệu về lá cây cà phê hiện nay chưa có ai thu thập nên số lượng dữ liệu mà nhóm có vẫn còn hạn chế do dữ liệu tự thu thập và xử lý. Mục đích của việc tự thu thập dữ liệu là để phù hợp với ngữ cảnh ứng dụng của bài toán.

# Chương 2. CÁC NGHIÊN CỨU TRƯỚC
* Bài toán của nhóm đặt ra là muốn hướng đến bài toán thuộc loại Object Detection (Phát hiện đối tượng), định vị đối tượng trong ảnh và xác định đối tượng thuộc loại nào. Trong lĩnh vực thị giác máy tính thì bài toàn phát hiện đối tượng đạt được nhiều kết quả khi áp dụng hướng tiếp cận Deep learning. Có thể kể đến một số hướng tiếp cận tiên tiến hiện nay bao gồm RCNN, Fast RCNN, Faster RCNN, Mask RCNN, RetinaNet, YOLO, v.v
* Faster RCNN
    * Phương pháp Faster RCNN là một trong các phương pháp phát hiện đối tƣợng sử dụng mạng Deep learning đạt độ chính xác cao trên các tập dữ liệu chuẩn như COCO . Faster RCNN được cải tiến dựa trên 2 phương pháp trướcc đó là RCNN và Fast RCNN.
* Mask RCNN
    * Phương pháp Mask RCNN là phương pháp thực hiện song song 2 bài toán là phân vùng đối tượng (Instance Segmentation) và phát hiện đối tượng. Mask RCNN là phương pháp được cải tiến từ Faster RCNN.
* Restinanet
    * RetinaNet là một phương pháp tiếp cận one-stage tức là ngay trong bản thân cấu trúc mạng của phương pháp đã bao gồm thao tác đưa ra vùng đề xuất
* YOLO
    * YOLO được xem là phương pháp đầu tiên xử lý dữ liệu theo thời gian thực và vẫn đạt được độ chính xác cao.
* Một số kết quả nghiên cứu được đánh giá trên tập COCO. COCO (Common Objects in Context) là một tập datasets phục vụ cho các bài toán Object Detection, Segmentation, Image Captioning. Tập dữ liệu tổng cộng có khoảng 1.5 triệu object thuộc về 80 class khác nhau.
    <p align="center">
    <img src="images/perfomance_of_coco.png" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 5. Perfomance trên tập COCO.</a>
    </p>
# Chương 3. XÂY DỰNG BỘ DỮ LIỆU
* ### Quá trình thu thập:
    * Dữ liệu được nhóm thu thập thủ công bằng camera của điện thoại.
    * Điện thoại sử dụng: Iphone 7 Plus, 32GB.
    * Mỗi tấm ảnh gốc có kích thước 3024 x 4032 (camera nằm ngang), 4032 x 3024 (camera nằm dọc)

        <p align="center">
        <img src="images/details_image.png" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
        <br>
        <a style="text-align: center">Hình 6. Độ phân giải và camera sử dụng.</a>
        </p>

    * File ảnh được lưu trữ trong cùng 1 folder trên máy tính dưới dạng tệp .JPG

    * Thời gian thu thập dữ liệu:

<center>

| STT | Thời gian thu thập | Địa điểm thu thập |
| :---: | --- | --- |
| 1 | 20/12/2021 | Huyện Lạc Dương |
| 2 | 25/12/2021 | Xã Trạm Hành |
| 3 | 1/2/2022 | Xã Trạm Hành |
</center>


* ### Tiêu chí khi thu thập dữ liệu :

    * Chụp rõ nét tập trung vào lá cây bị bệnh.
    * Chụp toàn bộ chiếc lá từ phần cuốn lá đến chóp lá.
    * Đảm bảo ánh sáng ban ngày.
    
* ### Giảm độ phân giải của ảnh :

    * Do mỗi ảnh có kích thước khá lớn nên dung lượng lưu trữ khá nặng. Đối với folder chứa toàn bộ dữ liệu gốc nặng khoảng 11.2 Gb gây khó khăn trong việc lưu trữ nến nhóm đã giảm độ phân giải xuống ~ 3.33 lần. Độ phân giải sau khi giảm 907 x 1209 và 1209 x 907. Dung lượng lưu trữ sau khi xử lý nặng khoảng 1.6 Gb.


* ### Gán nhãn dữ liệu :

    * Sử dụng công cụ labelImg để tiến hành gán nhãn toàn bộ dữ liệu
        <p align="center">
        <img src="images/label.png" style="display: block;margin-left: auto;margin-right: auto;width: 75%;"/>
        <br>
        <a style="text-align: center">Hình 7. Công cụ labelImg.</a>
        </p>

    * Sử dụng thao tác kéo thả chuột để tạo bouding box cho đối tượng. Label được lưu thành file text có cùng tên với ảnh dưới dạng YOLO format.
            <p align="center">
            <img src="images/yoloformat.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
            <br>
            <a style="text-align: center">Hình 8. Ảnh, label và label format của YOLO.</a>
            </p>

    * Trong một ảnh có thể có nhiều lá những chỉ label những lá bị bệnh và thấy rõ từ cuốn lá đến chóp lá.

    * Số loại label là 4. Được kí hiệu bằng 1 trong các chữ số 0, 1, 2, 3

    ***Label 0: Bệnh sâu vẽ bùa***
    
    * Những lá bị sâu vẽ bùa gây hại sẽ bị co lại, biến dạng. Sâu non chui qua lớp biểu bì của lá để ăn phần nhu mô của lá tạo thành đường hầm ngoằn ngoèo màu trắng, trắng đục dưới lớp biểu bì.
        
    <p align="center">
    <img src="images/vidusauvebua.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 9. Một số ví dụ về bệnh sâu vẽ bùa trên lá cà phê.</a>
    </p>

    ***Label 1: Bệnh phấn trắng***
    
    * Bệnh phấn trắng do một số loại nấm có họ hàng gần gây ra. Triệu chứng chung là chúng tạo ra lớp bột có màu trắng xám trên bề mặt của lá.
        
    <p align="center">
    <img src="images/viduphantrang.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 10. Một số ví dụ về bệnh phấn trắng trên lá cà phê.</a>
    </p>

    ***Label 2: Bệnh nấm rỉ sắt***
    
    * Trên lá xuất hiện các vết đốm hình tròn màu nâu cam hơi đỏ (giống rỉ sắt), xung quanh có vầng màu vàng úa.
        
    <p align="center">
    <img src="images/vidurisat.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 11. Một số ví dụ về bệnh nấm rỉ sắt trên lá cà phê.</a>
    </p>

    ***Label 3: Bệnh đốm rong***
    
    *  Đốm bệnh có hình tròn lúc đầu nhỏ khoảng 3 - 5 mm, hơi nhô lên trên mặt lá do rong phát triển thành ung mịn, màu hơi vàng.
        
    <p align="center">
    <img src="images/vidudomrong.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 12. Một số ví dụ về bệnh đốm rong trên lá cà phê.</a>
    </p>

* ### Thống số bộ dữ liệu :
    * Tổng số lượng ảnh trong bộ dữ liệu là: 3825 ảnh
    * Tổng số object là: 4092

    <p align="center">
    <img src="images/Figure_1.png" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 13. Số lượng object thuộc từng loại label.</a>
    </p>

    * Số ảnh có 1 object là: 3579
    * Số ảnh có nhiều hơn 1 object là: 246

    <p align="center">
    <img src="images/Figure_count.png" style="display: block;margin-left: auto;margin-right: auto;width: 50%; height:50%;"/>
    <br>
    <a style="text-align: center">Hình 14. Số lượng ảnh có 1 object và nhiều object.</a>
    </p>
    
    **Nhận xét :** Số lượng object thuộc bệnh phấn trắng khá ít so với các bệnh khác, nguyên nhân là bệnh này xuất hiện khá ít tại các vườn cà phê thu thập dữ liệu.

    * Tập dữ liệu được chia thành hai tập train và test với tỉ lệ là 80% cho tập train và 20% cho tập test
    <p align="center">
    <img src="images/train.png" style="display: block;margin-left: auto;margin-right: auto;"/>
    <br>
    <a style="text-align: center">Hình 15. Số lượng object thuộc từng loại label trong tập train.</a>
    </p>
    <p align="center">
    <img src="images/test.png" style="display: block;margin-left: auto;margin-right: auto;"/>
    <br>
    <a style="text-align: center">Hình 16. Số lượng object thuộc từng loại label trong tập test.</a>
    </p>

    Trong đó: <br>
        0 : Sâu vẽ bùa <br>
        1 : Phấn trắng <br>
        2 : Nấm rỉ sắt <br>
        3 : Đốm rong <br>
# Chương 4. TRAINING VÀ ĐÁNH GIÁ MODEL
## Cấu hình train và test:
Để train model nhóm sử dụng tài nguyên của Google Colab với thiết lập runtime type là GPU

<p align="center">
<img src="images/runtime.png" style="display: block;margin-left: auto;margin-right: auto; width: 30%; height:30%"/>
<br>
<a style="text-align: center">Hình 17. Bật GPU trên Google Colab.</a>
</p>

<p align="center">
<img src="images/cauhinhtrain.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%"/>
<br>
<a style="text-align: center">Hình 18. Cấu hình dùng để train và test.</a>
</p>

## YOLOv4:
<p align="center">
<img src="images/yolov4_archi.png" style="display: block;margin-left: auto;margin-right: auto; width: 75%"/>
<br>
<a style="text-align: center">Hình 19. Cấu trúc mô hình YOLOv4.</a>
</p>

### Sơ lược về YOLOv4

* YOLOv4 được giới thiệu bởi Alexey Bochoknovskiy, Chien-Yao Wang, and Hong-Yuan Mark Liao trong bài báo [YOLOv4: Optimal Speed and Accuracy of Object Detection](https://arxiv.org/abs/2004.10934v1) xuất bản ngày 23/4/2020.

* YOLOv4 là một loạt các cải tiến về tốc độ so với YOLOv3 và được cài đặt từ một bản fork của Darknet. Kiến trúc của YOLOv4 đã đưa bài toán object detection dễ tiếp cận hơn với những người không có tài nguyên tính toán mạnh.

<p align="center">
<img src="images/yolov4_compare.jpeg" style="display: block;margin-left: auto;margin-right: auto; width: 75%"/>
<br>
<a style="text-align: center">Hình 20. So sánh YOLOv4 với các mô hình khác.</a>
</p>

* Kết quả so sánh YOLOv4 với các mô hình khác ở thời điểm hiện tại. YOLOv4 chạy nhanh gấp đôi EfficientDet và tăng AP và FPS so với YOLOv3 lần lượt là 10% và 12%. Hình ảnh từ paper YOLOv4. Nhìn vào biểu đồ, ta dễ dàng thấy được sự hiệu quả của YOLOv4 so với các mạng tốt nhất hiện nay. Cụ thể hơn YOLOv4 đạt 43.5% AP trên tập dữ liệu MS COCO ở tốc độ 65 FPS, trên GPU Tesla V100. 

### Thiết lập training


* Nhóm sử dụng darknet repository của tác giả để huấn luyện cho model và thiết lập các thông số trong file Makefile như sau
<p align="center">
<img src="images/configmakefile.png" style="display: block;margin-left: auto;margin-right: auto; width: 20%; height:20%;"/>
<br>
<a style="text-align: center">Hình 21. Thiết lập các thông số Makefile để sử dụng GPU.</a>
</p>

* Chỉnh sửa các thông số của model YOLOv4 trong file yolov4-custom.cfg theo hướng dẫn của tác giả:
    * batch: 32
    * subdivisions = 32
    * max_batches = 8000 (Bằng số class * 2000)
    * steps = 6400, 7200 (Bằng 0.8 * max_batches, 0.9 * max_batches)
    * width = 416, height = 416 (Kích thước của ảnh)
    * classes = 4 (Số class)
    * filters = 27 (Tính theo công thức filters = (classes + 5) * 3) 

* Tạo file train.txt chứa đường dẫn tới các ảnh dùng để train (3138 ảnh)
<p align="center">
<img src="images/path_train.png" style="display: block;margin-left: auto;margin-right: auto; width: 20%; height:20%;"/>
<br>
<a style="text-align: center">Hình 22. File train.txt</a>
</p>


* Tạo file valid.txt chứa đường dẫn tới các ảnh dùng để đánh giá trong quá trình train (687 ảnh)
<p align="center">
<img src="images/path_valid.png" style="display: block;margin-left: auto;margin-right: auto; width: 20%; height:20%;"/>
<br>
<a style="text-align: center">Hình 23. File valid.txt</a>
</p>

* Tạo file obj.names chứa tên của các class
<p align="center">
<img src="images/obj.png" style="display: block;margin-left: auto;margin-right: auto; width: 20%; height:20%;"/>
<br>
<a style="text-align: center">Hình 24. File obj.names</a>
</p>

* Tạo file obj.data có nội dung như sau
<p align="center">
<img src="images/obj_data.png" style="display: block;margin-left: auto;margin-right: auto; width: 20%; height:20%;"/>
<br>
<a style="text-align: center">Hình 25. File obj.data</a>
</p>

    Trong đó:
    classes: là số lượng class
    train: đường dẫn tới file train.txt
    valid: đường dẫn tới file valid.txt
    names: đường dẫn tới file obj.names
    backup: đường dẫn tới folder backup chứa các trọng số được lưu lại trong quá trình train

### Train model
* Tải file trọng số yolov4.conv.137.weights và tiến hành train trên file trọng số này
* Trong quá trình train model các file trọng số được lưu lại tronng đó có 2 file quan trọng là:
    * yolov4-custom_last.weights (Trọng số của interation mới nhất)
    * yolov4-custom_best.weights (Trọng số tốt nhất)
* Quá trình training khá lâu vượt qua thời gian cho phép của Google Colab nên ở những lần train tiếp theo nhóm tiến hành train tiếp trên file trọng số mới nhất
* Thời gian train model: khoảng 28 tiếng
* Thời gian test trên 687 ảnh: 53 giây 

## YOLOv5:

### Sơ lược về YOLOv5
* Không lâu sau khi YOLOv4 được phát hành chính thức thì 1 phiên bản khác của YOLO xuất hiện là YOLOv5 sử dụng frame work Pytorch. YOLOv5 được giới thiệu bởi Glenn Jocher vào ngày 18/5/2020, YOLOv5 có mã nguồn mở ở [Github](https://github.com/ultralytics/yolov5). Với những số liệu của tác giả cung cấp thì mô hình này khá triển vọng. Tuy nhiên YOLOv4 hiện vẫn chưa có paper chính thức.

<p align="center">
<img src="images/yolov5_coco.png" style="display: block;margin-left: auto;margin-right: auto; width: 75%"/>
<br>
<a style="text-align: center">Hình 26. Perfomance của các phiên bản YOLOv5 trên tập COCO</a>
</p>

<p align="center">
<img src="images/pre_check.png" style="display: block;margin-left: auto;margin-right: auto; width: 75%"/>
<br>
<a style="text-align: center">Hình 27. Kết quả đánh giá trên tập COCO</a>
</p>

* Từ những kết quả mà tác giả đưa ra có thể thấy YOLOv5 có thể đạt tới 68.9% mAP0.5 trên tập COCO.

### Thiết lập training
* Tạo file data.yaml có nội dung như sau
<p align="center">
<img src="images/data_yaml.png" style="display: block;margin-left: auto;margin-right: auto; width: 20%; height:20%;"/>
<br>
<a style="text-align: center">Hình 28. File data.yaml</a>
</p>

    Trong đó:
    names: lần lượt là tên của các label được đặt trong dấu ngoặc kép
    nc: số lượng class
    train: đường dẫn tới các file ảnh train
    valid: đường dẫn tới các file ảnh dùng để valid trong quá trình train

* Thiết lập training
    * batch: 32
    * img size: 416
    * epoch: 500

### Train model
* Tải file trọng số của model YOLOv5s và tiến hành train trên file trọng số này.
* Trong quá trình train model các file trọng số được lưu lại tronng đó có 2 file quan trọng là:
    * last.pt (Trọng số của epoch mới nhất)
    * best.pt (Trọng số tốt nhất)
* Quá trình training khá lâu vượt qua thời gian cho phép của Google Colab nên ở những lần train tiếp theo nhóm tiến hành train tiếp trên file trọng số mới nhất
* Vào epoch 450 thì xuất hiện thông báo dừng train model như sau:
<p align="center">
<img src="images/stopping.jpg" style="display: block;margin-left: auto;margin-right: auto; width: 100%;"/>
<br>
<a style="text-align: center">Hình 29. Early stopping YOLOv5</a>
</p>

* Do trong 100 epoch gần nhất thì model không còn tốt lên được nữa (model hội tụ) nên tự động dừng train.
* Thời gian train model: khoảng 8 tiếng
* Thời gian test trên 687 ảnh: 32 giây

## Faster-RCNN:
### Sơ lược về Faster RCNN
* Faster-RCNN được giới thiệu bởi Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun.Trong bài báo [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497)
* Faster-RCNN  là một phương pháp phát hiện đối tượng sử dụng deep learning.Faster RCNN là một sự cải tiến dựa trên hai phương pháp  trước đó là RCNN và Fast RCNN. Faster RCNN là sự kết hợp giữa Fast-RCNN với  một mạng mới có tên gọi là region proposal network(rpn).
* Region Proposal Netwok là một mạng Convolutional Neural Network(CNN) có chức năng để tìm ra các vùng có khả năng chứa đối tượng thường dược gọi là region proposal
* Fast-RCNN là một mạng CNN dùng để trích xuất các features từ các region proposal và trả ra các bounding box cùng với label cho từng cái bounding box đó.
<p align="center">
  <img src="images/faster.png" />
</p>
<p align="center">Hình 30. Cấu trúc Faster RCNN</p>

### Thiếp lập training
* Nhóm sử dụn detectron2 một thư viện của Facebook AI Research để tiến hành huấn luyện cho Faster RCNN. Nhóm đã sử dụng file pretrained weights X-101-32x8d.pkl để tiếp tục train cho model của mình.

<p align="center">
  <img src="images/faster_yaml.png" style="display: block;margin-left: auto;margin-right: auto; width: 50%;"/> 
</p>
<p align="center">Hình 31. File pretrained được sử dụng </p>

* Thiết lập thông sô:
  * BATCH_SIZE_PER_IMAGE = 64
  * CLASSES : 5 (Tổng số class + 1)
  * MAX_ITER : 15000
  * STEP_SIZE : 6000,10000
* Nhóm chỉ chỉnh sửa một vài thông số để tiến hành việc training.
### Train model
* Thời gian train của Faster RCNN: 12 tiếng
* Thời gian test trên 687 ảnh: 175 giây
### Đánh giá model
* Để đánh giá model thì nhóm sử dụng mean average precision để đánh giá model. Trước tiên để hiểu được mean average là gì thì trước tiên chúng tôi sẽ giới thiệu một số khái niệm cơ bản.
* IOU là tỷ lệ giữa phần giao của bounding box dự đoán vói ground truth(vùng đối tượng thật mà chúng tôi label) và phần hợp của chúng.
<p align="center">
  <img src="images/ctiou.png" width="500" height="400">
</p>
<p align="center">Hình 32. Độ đo IOU </p>

* Giá trị IOU trong khoảng (0,1). Dựa vào đó có thể xác định được wrong detection hay correct detection. Dựa vào ngưỡng để xác định. Nếu IOU lớn hơn hoặc bằng ngưỡng thì đó là một correct detection còn lại thì là wrong detection.

* Dựa vào những khái niệm trên để định nghĩa True/false positive/negative.

  * True Positive (TP): IoU lớn hơn hoặc bằng ngưỡng, là một correct detection
  
  * False Positive (FP): IoU bé hơn ngưỡng, là một wrong detection
  
  * False Negative (FN): trường hợp mà ground truth không có predicted bounding box

* Nêu có nhiều predicted bounding box xếp chồng lên nhau trong cùng một ground truth thì ta sẽ chọn predicted bounding box nào có IOU lớn hơn ngưỡng cao nhất là True Positive, còn lại là False Positive.

<p align="center">
  <img src="images/AP.jpg" width="500" height="400">
</p>
<p align="center">Hình 33. AP </p>

* AP là diện tích màu xanh nằm dưới đường cong.
* Mỗi lớp bài toán sẽ có một giá trị AP, Mean Average Precision là trung bình AP cho tất cả các lớp.

* **Lý do chọn mean average precision là metric để đánh giá mô hình :** 
  
  * Mối quan hệ giữa precision – recall giúp mAP đánh giá được về độ chính xác của mô hình.
  
  * Precision – Recall thay đổi khi ngưỡng IoU thay đổi. Do đó, tại một giá trị IoU xác định,ta có thể do/đánh giá được mô hình một cách tốt nhất.

* Thiết lập các ngưỡng để đánh giá
    * confidence thresh: 0.25
    * iou thresh: 0.5
* YOLOv4
<p align="center">
<img src="images/res_yolov4.jpg" style="display: block;margin-left: auto;margin-right: auto; width: 50%;"/>
<br>
<a style="text-align: center">Hình 34. Kết quả đánh giá model YOLOv4</a>
</p>

| Class | AP@0.5 |
| :---: | --- | 
| 0 | 1.000 | 
| 1 | 0.984 |
| 2 | 0.988 |
| 3 | 0.986 |

* YOLOv5
<p align="center">
<img src="images/res_yolov5.png" style="display: block;margin-left: auto;margin-right: auto; width: 70%;"/>
<br>
<a style="text-align: center">Hình 35. Kết quả đánh giá model YOLOv5s</a>
</p>

| Class | AP@0.5 |
| :---: | --- | 
| 0 | 0.995 | 
| 1 | 0.99 |
| 2 | 0.992 |
| 3 | 0.994 |

* Faster RCNN
<p align="center">
<img src="images/fasterrcnn_res.jpg" style="display: block;margin-left: auto;margin-right: auto; width: 70%;"/>
<br>
<a style="text-align: center">Hình 36. Kết quả đánh giá model Faster RCNN</a>
</p>

| Class | AP@0.5 |
| :---: | --- | 
| 0 | 0.987 | 
| 1 | 0.997 |
| 2 | 0.999 |
| 3 | 0.998 |

* Tổng kết đánh giá

| Model\Class | 0 | 1 | 2 | 3|
| :---: | --- | --- | --- | --- |
| YOLOv4 | <ins>1.000 </ins> | 0.984| 0.988 | 0.986 |
| YOLOv5 | 0.995 | 0.99| 0.992 | 0.994 |
| Faster RCNN | 0.987 | <ins> 0.997 <ins>| <ins>0.999</ins> | <ins>0.998 </ins>|
    
🠊 Khi đánh giá bằng điểm AP@0.5, đối với class 0 model YOLOv4 cho kết quả cao nhất. Đối với 3 class còn lại, Faster RCNN đều cho kết quả tốt hơn

<p align="center">
<img src="images/results_pre.png" style="display: block;margin-left: auto;margin-right: auto;"/>
<br>
<a style="text-align: center">Hình 37. Detection result</a>
</p>

### Số lượng sai sót của mỗi class:
* Qua hình ta có thể thấy được số lượng sai sót mỗi thông qua việc đánh giá bằng AP@50

| Model | Class| True Positive | False Positive |
| :----: | :-----: | :------: | :-----: |
| YOLOv4 | class0 | 217 | 5 |
|        | class1 | 60 | 7 |
|        | class2 | 250 | 44 |
|        | class3 | 187 | 25 |
| YOLOv5 | class0 | 217 | 17 |
|        | class1 | 63 | 26 |
|        | class2 | 257 | 57|
|        | class3 | 188 | 25 |
| FasterRCNN | class0 | 217 | 5 |
|            | class1 | 63 | 5 |
|            | class2 | 258 | 14 |
|            | class3 | 186 | 4 |

* Qua bảng thông kê trên ta có thể thấy model FasterRCNN có số lượng False Positive thấp nhất và số lượng False Positive của model YOLOv5 cao nhất điều đó đòng nghĩa với việc model YOLOv5 có nhiều sai sót hơn 2 model còn lại.

| Model | Precision | Recall | mAP@0.5 |
| :---: | --- | --- | --- |
| YOLOv4 | 0.900 | 0.98 | 0.989 |
| YOLOv5s | 0.988 | <ins>0.99</ins> | 0.993 |
| Faster-RCNN | <ins>0.996 </ins> | 0.997 | <ins>0.996</ins> |

🠊 Khi đánh giá bằng mAP@0.5 cả 3 model đều cho kết quả rất tốt. Faster RCNN cho kết quả tốt nhất.

| Model | Thời gian test 687 ảnh (giây) | 
| :---: | --- | 
| YOLOv4 | 53 | 
| YOLOv5s | 32 | 
| Faster-RCNN | 175 |

🠊 Khi thử nghiệm trên cùng một cấu hình, mặc dù Faster RCNN cho kết quả mAP@0.5 tốt nhất nhưng cũng tốn thời gian nhiều nhất so với 2 model còn lại.
* Một số hình ảnh test
<p align="center">
<img src="images/1.png" style="display: block;margin-left: auto;margin-right: auto; width: 120%;"/>
<br>
<a style="text-align: center">Hình 38. Kết quả test</a>
</p>

    Model YOLOv4 và YOLOv5 detect sai 1 phần lá bị bệnh đốm rong ở góc trên bên trái

<p align="center">
<img src="images/2.png" style="display: block;margin-left: auto;margin-right: auto; width: 120%;"/>
<br>
<a style="text-align: center">Hình 39. Kết quả test</a>
</p>

    YOLOv5 detect sai loại bệnh (Ground truth là nấm rỉ sắt - Predict đốm rong)

<p align="center">
<img src="images/3.png" style="display: block;margin-left: auto;margin-right: auto; width: 120%;"/>
<br>
<a style="text-align: center">Hình 40. Kết quả test</a>
</p>

    YOLOv5 detect 1 lá bình thường ở góc trên thành bệnh sâu vẽ bùa

<p align="center">
<img src="images/4.png" style="display: block;margin-left: auto;margin-right: auto; width: 120%;"/>
<br>
<a style="text-align: center">Hình 41. Kết quả test</a>
</p>

    Cả ba model đều cho kết quả chính xác khi detect được 2 lá bị bệnh.

<p align="center">
<img src="images/5.png" style="display: block;margin-left: auto;margin-right: auto; width: 120%;"/>
<br>
<a style="text-align: center">Hình 42. Kết quả test</a>
</p>

    YOLOv4 cho kết quả chính xác, Faster RCNN và YOLOv5 detect sai 1 là bình thường ở bên trái thành bệnh sâu vẽ bùa

* Nhìn chung kết quả thử nghiệm đều khá tốt.
    * Một số lá bình thường bị detect nhầm thành bệnh sâu vẽ bùa và nấm rỉ sắt do 1 số ảnh trong tập train bệnh còn nhẹ và khá giống với lá bình thường
    * Một số lá bị nấm rỉ sắt nhìn khá giống với bệnh đốm rong làm cho model bị nhầm lẫn.
    * YOLOv4 và YOLOv5 đều có những trường hợp detect ra 1 phần lá bị bệnh. Trường hợp này xảy ra nhiều hơn đối với model YOLOv5 
## Chướng 5. Ứng dụng và hướng phát triển:

### Ứng dụng:
* Ứng dụng hướng tới người sử dụng chính là người trồng cà phê, giúp người trồng có thể phát hiện được các loại bệnh xuất hiện trên lá từ đó có thể xử lý đúng cách và hiệu quả.
* Như đã đề cập trước đó, việc giúp người trồng cà phê phát hiện được bệnh xuất hiện trên lá sẽ góp phần nâng cao được chất lượng sản phẩm cà phê, đáp ứng được các tiêu chuẩn về hàng xuất khẩu từ đó nguồn thu nhập của người dân sẽ được tăng lên. Việc sử các mô hình máy học sẽ thúc đẩy quá trình ứng dụng khoa học kĩ thuật vào trong nông nghiệp.

### Hướng phát triển:
* Thu thập thêm nhiều dữ liệu về các loại bệnh nhằm giúp ứng dụng phát hiện được nhiều loại bệnh và chính xác hơn.
* Có thể hướng tới việc phát hiện các loại bệnh trên nhiều loại lá cây nông nghiệp khác nhau dựa trên các đặc điểm giống nhau của các loại bệnh khi xuất hiện trên lá.

