---
title: "Lộ trình học tập & Cấu trúc môn học: Cấu trúc dữ liệu và Giải thuật"
course: "Data Structures and Algorithms"
language: "vi"
version: "1.0"
---

# Lộ trình học tập & Cấu trúc môn học: Cấu trúc dữ liệu và Giải thuật

Chào mừng bạn đến với tài liệu hướng dẫn và lộ trình học tập môn **Cấu trúc dữ liệu và Giải thuật (DSA)**. Lộ trình này được xây dựng dựa trên khung chương trình chuẩn của **GeeksforGeeks DSA Tutorial**, được dịch nghĩa, Việt hóa và bổ sung chi tiết để phục vụ việc tự học và giảng dạy bằng tiếng Việt.

---

## 📂 Cấu trúc Thư mục Dự án

Toàn bộ tài liệu, mã nguồn và bài tập sẽ được lưu trữ theo cấu trúc thư mục logic dưới đây:

```text
DSAL/
├── curriculum_roadmap.md                       # Tài liệu lộ trình & mục lục (File này)
├── introduction-to-algorithm/                  # Chương 1: Nhập môn & Phân tích Thuật toán
│   ├── introduction-to-algorithm-1.md          # Bài 1: Thuật toán là gì? Nhập môn Phân tích Thuật toán (Đã có)
│   └── complexity-analysis-2.md                # Bài 2: Độ phức tạp thuật toán & Ký hiệu tiệm cận (Sắp tạo)
├── basic-data-structures/                      # Chương 2: Cấu trúc dữ liệu cơ bản
│   ├── array-string-3.md                       # Bài 3: Mảng (Arrays) & Chuỗi (Strings)
│   ├── linked-list-4.md                        # Bài 4: Danh sách liên kết (Linked Lists)
│   ├── stack-queue-5.md                        # Bài 5: Ngăn xếp (Stack) & Hàng đợi (Queue)
│   └── hashing-6.md                            # Bài 6: Bảng băm (Hashing & Hash Tables)
├── advanced-data-structures/                   # Chương 3: Cấu trúc dữ liệu nâng cao
│   ├── trees-7.md                              # Bài 7: Cây (Trees) & Cây tìm kiếm nhị phân (BST)
│   ├── heaps-8.md                              # Bài 8: Heap & Hàng đợi ưu tiên (Priority Queue)
│   ├── graphs-9.md                             # Bài 9: Đồ thị (Graphs) & Các phép duyệt BFS/DFS
│   └── trie-dsu-10.md                          # Bài 10: Cây Trie & Disjoint Set Union (DSU)
├── basic-algorithms/                           # Chương 4: Các giải thuật cơ bản
│   ├── searching-11.md                         # Bài 11: Giải thuật Tìm kiếm (Linear/Binary Search)
│   ├── sorting-12.md                           # Bài 12: Giải thuật Sắp xếp (Bubble, Merge, Quick, Heap...)
│   ├── greedy-algorithms-13.md                 # Bài 13: Giải thuật Tham lam (Greedy Algorithms)
│   ├── divide-and-conquer-14.md                # Bài 14: Chia để trị (Divide and Conquer)
│   ├── backtracking-15.md                      # Bài 15: Thuật toán Quay lui (Backtracking)
│   └── dynamic-programming-16.md               # Bài 16: Quy hoạch động (Dynamic Programming)
└── advanced-algorithms/                        # Chương 5: Giải thuật nâng cao
    ├── advanced-graphs-17.md                   # Bài 17: Giải thuật đồ thị nâng cao (Dijkstra, Bellman-Ford...)
    └── string-algorithms-18.md                 # Bài 18: Giải thuật xử lý chuỗi nâng cao (KMP, Rabin-Karp)
```

---

## 🗺️ Lộ trình Chi tiết các Bài học

Dưới đây là tiến độ học tập và chi tiết nội dung của từng bài giảng:

### 🎓 Chương 1: Nhập môn và Phân tích Thuật toán
*Mục tiêu: Nắm vững tư duy giải thuật và công cụ toán học để đánh giá hiệu năng thuật toán.*

| Bài học | Tên bài giảng | Trạng thái | Nội dung chính |
| :--- | :--- | :---: | :--- |
| **Bài 1** | [Thuật toán là gì? Nhập môn Phân tích](file:///E:/MinhVD/Github/DSAL/introduction-to-algorithm/introduction-to-algorithm-1.md) | ✅ Hoàn thành | Định nghĩa thuật toán, Đặc tính thuật toán, Phân tích tiên nghiệm & hậu nghiệm, Độ phức tạp thời gian cơ bản |
| **Bài 2** | [Phân tích Độ phức tạp & Ký hiệu](file:///E:/MinhVD/Github/DSAL/introduction-to-algorithm/complexity-analysis-2.md) | ✅ Hoàn thành | Ký hiệu tiệm cận ($O, \Omega, \Theta$), phân tích vòng lặp lồng nhau, đệ quy (Master Theorem), độ phức tạp bộ nhớ |

---

### 📦 Chương 2: Cấu trúc dữ liệu cơ bản (Basic Data Structures)
*Mục tiêu: Hiểu cách tổ chức dữ liệu tuyến tính trong bộ nhớ và các thao tác cơ bản đi kèm.*

| Bài học | Tên bài giảng | Trạng thái | Nội dung chính |
| :--- | :--- | :---: | :--- |
| **Bài 3** | `array-string-3.md` | ⏳ Tiếp theo | Mảng tĩnh, mảng động, các thao tác chèn/xóa/sửa; Xử lý chuỗi ký tự, các bài toán mảng phổ biến (Two Pointers, Sliding Window) |
| **Bài 4** | `linked-list-4.md` | 📝 Chưa bắt đầu | Danh sách liên kết đơn (Singly LL), kép (Doubly LL), vòng (Circular LL); Chèn, xóa, đảo ngược danh sách |
| **Bài 5** | `stack-queue-5.md` | 📝 Chưa bắt đầu | Ngăn xếp (LIFO), Hàng đợi (FIFO); Cài đặt bằng mảng & danh sách liên kết; Ứng dụng (ngoặc hợp lệ, khử đệ quy) |
| **Bài 6** | `hashing-6.md` | 📝 Chưa bắt đầu | Bảng băm, Hàm băm (Hash Functions); Xử lý đụng độ (Chaining, Open Addressing); Ứng dụng tra cứu $O(1)$ |

---

### 🌲 Chương 3: Cấu trúc dữ liệu nâng cao (Advanced Data Structures)
*Mục tiêu: Làm quen với cấu trúc dữ liệu phi tuyến tính và phân cấp.*

| Bài học | Tên bài giảng | Trạng thái | Nội dung chính |
| :--- | :--- | :---: | :--- |
| **Bài 7** | `trees-7.md` | 📝 Chưa bắt đầu | Cây nhị phân (Binary Tree), Cây tìm kiếm nhị phân (BST); Phép duyệt cây (Pre/In/Post-order, Level-order); Cân bằng cây |
| **Bài 8** | `heaps-8.md` | 📝 Chưa bắt đầu | Min-Heap, Max-Heap; Cài đặt heap bằng mảng; Thao tác Heapify, chèn, xóa; Ứng dụng trong Priority Queue |
| **Bài 9** | `graphs-9.md` | 📝 Chưa bắt đầu | Biểu diễn đồ thị (Adjacency Matrix, Adjacency List); Thuật toán duyệt đồ thị BFS (Breadth-First) và DFS (Depth-First) |
| **Bài 10** | `trie-dsu-10.md` | 📝 Chưa bắt đầu | Cây Trie (phục vụ tìm kiếm từ gợi ý/autocomplete); Cấu trúc tập hợp rời rạc Union-Find (DSU) và tối ưu hóa đường đi |

---

### ⚙️ Chương 4: Các giải thuật cơ bản (Algorithms)
*Mục tiêu: Làm chủ các chiến lược giải quyết bài toán kinh đoán và kỹ thuật tối ưu hóa hiệu năng.*

| Bài học | Tên bài giảng | Trạng thái | Nội dung chính |
| :--- | :--- | :---: | :--- |
| **Bài 11** | `searching-11.md` | 📝 Chưa bắt đầu | Tìm kiếm tuyến tính (Linear Search); Tìm kiếm nhị phân (Binary Search) và ứng dụng mở rộng (Tìm kiếm trên không gian đáp án) |
| **Bài 12** | `sorting-12.md` | 📝 Chưa bắt đầu | Sắp xếp cơ bản ($O(n^2)$) & sắp xếp nâng cao ($O(n \log n)$: Merge Sort, Quick Sort, Heap Sort); Độ ổn định (Stability) của sắp xếp |
| **Bài 13** | `greedy-algorithms-13.md` | 📝 Chưa bắt đầu | Chiến lược tham lam; Các bài toán tối ưu hóa kinh điển (Chọn công việc, Đổi tiền, Mã hóa Huffman) |
| **Bài 14** | `divide-and-conquer-14.md` | 📝 Chưa bắt đầu | Triết lý chia để trị; Phân tích các thuật toán đệ quy chia đôi; Ứng dụng tìm kiếm nhị phân, nhân ma trận |
| **Bài 15** | `backtracking-15.md` | 📝 Chưa bắt đầu | Kỹ thuật quay lui kết hợp nhánh cận; Giải quyết bài toán N-Queens, Sudoku, sinh hoán vị/tập con |
| **Bài 16** | `dynamic-programming-16.md` | 📝 Chưa bắt đầu | Kỹ thuật Quy hoạch động; Phân biệt Memoization (Top-down) và Tabulation (Bottom-up); Knapsack, LCS, LIS |

---

### 🚀 Chương 5: Giải thuật nâng cao (Advanced Algorithms)
*Mục tiêu: Tiếp cận các giải thuật chuyên biệt và phức tạp hơn cho đồ thị và xử lý văn bản.*

| Bài học | Tên bài giảng | Trạng thái | Nội dung chính |
| :--- | :--- | :---: | :--- |
| **Bài 17** | `advanced-graphs-17.md` | 📝 Chưa bắt đầu | Tìm đường đi ngắn nhất (Dijkstra, Bellman-Ford, Floyd-Warshall); Cây khung nhỏ nhất (MST: Kruskal, Prim) |
| **Bài 18** | `string-algorithms-18.md` | 📝 Chưa bắt đầu | Thuật toán so khớp chuỗi hiệu năng cao: KMP (Knuth-Morris-Pratt), Rabin-Karp sử dụng mã băm lăn |

---

## 🛠️ Hướng dẫn Học tập

1. **Đọc bài giảng lý thuyết**: Theo thứ tự lộ trình từ Chương 1 đến Chương 5. Mỗi bài giảng đều có phần giả mã và ví dụ minh họa bằng Python.
2. **Thực hành viết code**: Hãy tự cài đặt lại các cấu trúc dữ liệu và giải thuật trong bài học bằng ngôn ngữ bạn đang học (Python/C++/Java) mà không nhìn code mẫu.
3. **Làm bài tập ôn tập**: Trả lời các câu hỏi lý thuyết và tự giải quyết các bài tập thực hành ở cuối mỗi file bài giảng.
4. **Luyện tập trên LeetCode/HackerRank**: Áp dụng các kiến thức đã học để giải các bài toán thực tế trên các nền tảng lập trình thi đấu.
