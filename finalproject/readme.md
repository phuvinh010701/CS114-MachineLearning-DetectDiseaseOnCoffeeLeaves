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

## Bảng mục lục
1.[Giới thiệu bài toán](#giới-thiệu-bài-toán:)

2.[Bộ dữ liệu](#xây-dựng-bộ-dữ-liệu:)

3.[Mô hình sử dụng](#mô-hình-sử-dụng:)

4.[Phương pháp đánh giá](#phương-pháp-đánh-giá:)

5.[Đánh giá kết quả](#đánh-giá-kết-quả:)

6.[Hướng phát triển](#hướng-phát-triển:)

7.[Tài liệu tham khảo](#Tài-liệu-tham-khảo:)

## 1.Giới thiệu bài toán:

* Ngữ cảnh ứng dụng : 
    
    * Hiện nay, cà phê là một trong những loại thức uống được sử dụng phổ biến lẫn trong và ngoài nước. Cà phê được sản xuất từ những hạt cà phê rang, lấy trên cây cà phê.
    
    <img src="images/caphe.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%;"/>

    * Theo báo điện tử VTV, trên 90% tổng sản lượng cà phê của Việt Nam dành cho việc xuất khẩu, khoảng 10% còn lại là dành cho việc chế biến và tiêu thụ trong nước. Cà phê nằm trong nhóm hàng nông sản xuất khẩu chủ lực của Việt Nam, hiện đứng thứ 2 thế giới (chỉ sau Brazil). Tính chung cả năm 2021, xuất khẩu cà phê của Việt Nam đạt 1,52 triệu tấn.

    <img src="images/bieudoxuatkhau.jpg" style="display: block;margin-left: auto;margin-right: auto;width: 50%;"/>

    * Sản lượng tuy lớn nhưng cà phê vẫn chưa đáp ứng được các tiêu chuẩn về chất lượng. Nhằm nâng cao chất lượng của hạt cà phê, việc phát hiện và xử lý những căn bệnh trên lá của cây rất quan trọng. Nhận thấy được vấn đề đó nên nhóm đã quyết định áp dụng những kiến thức của mình và những công nghệ có sẵn hiện nay để giải quyết bài toán phát hiện một số loại bệnh trên lá cây cà phê.

    * Mô hình hướng tới người sử dụng là người trồng cây cà phê, xây dựng một ứng dụng có thể giúp người trồng có thể phát hiện chính xác hơn các loại bệnh đang gặp trên lá của cây và đưa ra được giải pháp phù hợp nhằm loại bỏ bệnh và tác nhân gây bệnh. 
    
* Input và Output:
    
    * Input:
        
        * Một tấm ảnh chụp chụp hình lá của cây cà phê đang bị bệnh.
        * Các điều kiện ràng buộc :
            + Ảnh chụp tập trung vào lá đang bị bệnh
            + Chụp mặt trên của lá
            + Chụp được từ cuốn lá đến chóp lá
            + Chụp trong điều kiện ánh sáng ban ngày
            
    * Output:

        * Bounding box bao quanh lá cây bị bệnh
        * Tên loại bệnh
    <br>
    🠊 ***Trong ứng dụng thực tế hoàn chỉnh, dựa vào tên loại bệnh xác định được ứng dụng sẽ đưa ra các giải pháp phù hợp cho người trồng***
## 2.Bộ dữ liệu:
* ### Quá trình thu thập:
    * Dữ liệu được nhóm thu thập thủ công bằng điện thoại.Thu thập thủ công tại vườn giúp bộ dữ liệu gần sát với thực tế khi người nông dân tiến hành chụp.Sau đó nhóm tiến hành gắn nhãn cho bộ dữ liệu.
* ### Tiêu chí khi thu thập dữ liệu :
    * Chụp toàn bộ chiếc lá
    * Đảm bộ độ sáng phù hợp
    * khoảng cách chụp vừa phải
    * Gốc camera từ trên xuống
* ### Nơi thu thập dữ liệu :
    * Vườn cà phê của nhà người thân xa khoảng 40km
* ### Khó khắn khi thu thập dữ liệu : 
    * Đường đi xa xôi.Hiện nay dịch bệnh vẫn còn ảnh hưởng nên có rất nhiều khó khăn trong việc đi lại và có thể gây ảnh hưởng đến sức khỏe
* ### Tổng quan về bộ dữ liệu :
    * Bộ dữ liệu gồm có 3825 tấm ảnh gồm bốn lớp là bốn loại bệnh phổ biến xuất hiện trên lá cây cà phê
    * Bốn loại bệnh : 
        * Sâu vẽ bùa
        * Phấn trắng
        * Nấm rỉ sắt
        * Đốm rong 
* ### Thống số bộ dữ liệu : 
    * Tập dữ liệu sẽ được chia thành hai tập train và test với tỉ lệ là 82% cho tập train và 18% cho tập test
    <p algin="center">
        <img src="images/data.png"/>
    </p>
    0 : Sâu vẽ bùa <br>
    1 : Phấn trắng <br>
    2 : Nấm rỉ sắt <br>
    3 : Đốm rong <br>
**Nhận xét :** Số lương dữ liệu của bệnh đốm rong khá ít so với các bệnh khác.Một phần là do vườn của người thân ít xuất hiện bệnh này.Mặc khác các bệnh thường xảy ra theo mùa.
## 3.Mô hình sử dụng:
* Yolov4:
    * Giới thiệu: Vinh
* Yolov5:
    * Giới thiệu: Danh or Vinh or Minh
* Faster-RCNN:
    * Giới thiệu: Danh
## 4.Phương pháp đánh giá:
* Các mô hình được nhóm đánh giá dựa trên độ đo mean average precision(map) được sử dụng phổ biến trong các bài toán object detection.
* Bổ sung thêm : Minh
## 5.Đánh giá kết quả:
 Danh
## 6.Hướng phát triển:
* Mô hình :
    * Thu thập thêm nhiều dữ liệu không chỉ các bệnh trên lá cây mà còn trên các bộ phận khác của cây cà phê.
* Ứng dụng : 
    * Tạo ra một ứng điện thoại có thể phát hiện các loại bệnh trên cây cà phê giúp người nông dân có thể dễ dàng sử dụng và có cách ngăn chặn kịp thời.
## 7.Tài liệu tham khảo:
Danh & Vinh
