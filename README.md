# 🔐 Ứng dụng Mô phỏng Entropy & Đo độ mạnh Mật khẩu

> **Đồ án môn học:** Lý thuyết Thông tin  
> **Đề tài:** Ứng dụng Entropy trong đo độ ngẫu nhiên của mật khẩu

## 📖 Giới thiệu

Ứng dụng này là một công cụ trực quan hóa khái niệm **Entropy (Lượng tin)** trong Lý thuyết thông tin và áp dụng nó vào lĩnh vực An toàn thông tin (Cybersecurity). 

Phần mềm giúp người dùng hiểu sự khác biệt giữa **Entropy Lý thuyết** (dựa trên công thức Hartley) và **Entropy Thực tế** (dựa trên khả năng đoán định của con người và máy tính), từ đó thấy được tầm quan trọng của việc sinh mật khẩu ngẫu nhiên.

## ✨ Tính năng chính

1.  **Tính toán Entropy:**
    * **Lý thuyết (Hartley):** Tính toán dựa trên độ dài chuỗi ($L$) và không gian mẫu ($N$).
    * **Thực tế (Real-world):** Sử dụng thuật toán `zxcvbn` để phát hiện các mẫu dễ đoán (tên riêng, ngày tháng, phím lân cận, lặp lại...).
2.  **Ước lượng thời gian tấn công (Crack Time):**
    * Dựa trên kịch bản tấn công Offline với tốc độ xử lý của phần cứng hiện đại (GPU Cluster).
3.  **Trực quan hóa (Biểu đồ):**
    * Minh họa sự sụt giảm Entropy khi mật khẩu không ngẫu nhiên (hiện tượng "vón cục").
4.  **Sinh mật khẩu ngẫu nhiên:**
    * Công cụ tạo mật khẩu chuẩn an toàn.

## 🛠️ Yêu cầu cài đặt

Để chạy ứng dụng, máy tính cần cài đặt **Python 3.8+** và các thư viện sau:

1.  **Streamlit:** Framework tạo web app.
2.  **Matplotlib:** Vẽ biểu đồ.
3.  **zxcvbn:** Thư viện đánh giá độ mạnh mật khẩu thực tế (do Dropbox phát triển).

### Cài đặt thư viện
Mở Terminal (hoặc CMD/PowerShell) và chạy lệnh:

```bash
pip install streamlit matplotlib zxcvbn
```

## Hướng dẫn sử dụng

### Bước 1: Khởi chạy ứng dụng
Tại thư mục chứa file app.py, chạy lệnh:

```bash
streamlit run app.py
```

Trình duyệt sẽ tự động mở địa chỉ http://localhost:8501.

### Bước 2: Thao tác trên giao diện

Cách 1 - Nhập tay: Nhập mật khẩu bất kỳ vào ô chính giữa màn hình để xem phân tích.

Cách 2 - Sinh tự động: Mở thanh menu bên trái (Sidebar), chọn độ dài và các tùy chọn (Số, Ký tự đặc biệt), sau đó bấm "TẠO & PHÂN TÍCH NGAY".

### Bước 3: Đọc biểu đồ
Đường nét đứt: Các ngưỡng lý thuyết (ví dụ: đường màu xanh lá là mức cao nhất - Full ASCII).

Điểm màu Xanh (Blue dot): Entropy lý thuyết của mật khẩu bạn nhập.

Điểm màu Đỏ (Red dot): Độ mạnh thực sự.

Nếu Đỏ trùng Xanh: Mật khẩu tốt (ngẫu nhiên hoàn hảo).

Nếu Đỏ thấp hơn Xanh: Mật khẩu chứa quy luật dễ đoán.
