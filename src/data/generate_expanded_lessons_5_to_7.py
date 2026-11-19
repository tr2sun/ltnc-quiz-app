# -*- coding: utf-8 -*-
"""
Script to generate 90 new questions for Lessons 5, 6, and 7
- Lesson 5: L5_Q46 to L5_Q75 (Đề 5D: 15 questions, Đề 5E: 15 questions)
- Lesson 6: L6_Q31 to L6_Q60 (Đề 6C: 15 questions, Đề 6D: 15 questions)
- Lesson 7: L7_Q31 to L7_Q60 (Đề 7C: 15 questions, Đề 7D: 15 questions)
"""

import json
import os

L5_NEW = [
    # --- ĐỀ 5D (L5_Q46 - L5_Q60): equals & hashCode Contract, Complex Map/Set & Fail-Fast ---
    {
        "id": "L5_Q46",
        "lessonId": 5,
        "type": "single",
        "title": "Theo hợp đồng (Contract) giữa phương thức equals() và hashCode() trong lớp java.lang.Object, khẳng định nào sau đây là BẮT BUỘC?",
        "code": None,
        "options": [
            "Nếu hai đối tượng bằng nhau theo equals() (o1.equals(o2) == true), thì giá trị hashCode() của chúng BẮT BUỘC phải bằng nhau",
            "Nếu hai đối tượng có hashCode() bằng nhau, thì phép so sánh o1.equals(o2) bắt buộc phải trả về true",
            "Hai đối tượng khác nhau (o1.equals(o2) == false) bắt buộc phải có giá trị hashCode() khác nhau",
            "Mỗi lần gọi hashCode() trên cùng một đối tượng trong các lần chạy khác nhau của ứng dụng bắt buộc phải trả về cùng một số nguyên duy nhất"
        ],
        "correctAnswer": 0,
        "explanation": "Quy tắc cốt lõi của hợp đồng equals-hashCode: Nếu hai đối tượng equals bằng nhau thì hashCode của chúng bắt buộc phải bằng nhau. Ngược lại, hai đối tượng có cùng hashCode có thể không equals nhau (hiện tượng va chạm băm - Hash Collision). Hai đối tượng không equals nhau không bắt buộc phải có hashCode khác nhau.",
        "difficulty": "medium",
        "tags": ["equals", "hashCode", "Contract"]
    },
    {
        "id": "L5_Q47",
        "lessonId": 5,
        "type": "single",
        "title": "Xem xét lớp Person ghi đè equals() nhưng QUÊN ghi đè hashCode(). Đoạn mã sau in ra kết quả gì?",
        "code": "class Person {\n    String id;\n    Person(String id) { this.id = id; }\n    @Override\n    public boolean equals(Object o) {\n        if (this == o) return true;\n        if (!(o instanceof Person)) return false;\n        return this.id.equals(((Person) o).id);\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Map<Person, String> map = new HashMap<>();\n        map.put(new Person(\"P01\"), \"Alice\");\n        System.out.println(map.get(new Person(\"P01\")));\n    }\n}",
        "options": [
            "null",
            "Alice",
            "Lỗi biên dịch vì Person chưa cài đặt Comparable",
            "Ném ngoại lệ NullPointerException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Vì không ghi đè hashCode(), lớp Person kế thừa hashCode() mặc định từ Object (dựa trên địa chỉ bộ nhớ). Hai đối tượng 'new Person(\"P01\")' có địa chỉ khác nhau nên hầu như chắc chắn sinh ra hai giá trị hashCode khác nhau và rơi vào hai bucket khác nhau trong HashMap. Do đó map.get() không tìm thấy và trả về null, phá vỡ logic tra cứu của Map.",
        "difficulty": "hard",
        "tags": ["HashMap", "hashCode", "EqualsTrap"]
    },
    {
        "id": "L5_Q48",
        "lessonId": 5,
        "type": "single",
        "title": "Điều gì xảy ra khi bạn thay đổi thuộc tính của một đối tượng Mutable (có thể sửa đổi) sau khi đã thêm nó làm Key vào HashSet hoặc HashMap?",
        "code": "class Key {\n    int val;\n    Key(int val) { this.val = val; }\n    public boolean equals(Object o) { return o instanceof Key && this.val == ((Key)o).val; }\n    public int hashCode() { return val; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Set<Key> set = new HashSet<>();\n        Key k = new Key(10);\n        set.add(k);\n        k.val = 20; // Sua doi sau khi da them\n        System.out.println(set.contains(new Key(10)) + \" \" + set.contains(k));\n    }\n}",
        "options": [
            "false false",
            "false true",
            "true true",
            "true false"
        ],
        "correctAnswer": 0,
        "explanation": "Khi add k với val=10, nó được đặt vào bucket tương ứng hashCode 10. Khi sửa k.val = 20, hashCode của k biến thành 20. Khi gọi set.contains(new Key(10)): tìm ở bucket 10, thấy đối tượng tại đó có k.val=20 không equals với 10 -> false. Khi gọi set.contains(k): tìm ở bucket 20, nhưng bucket 20 đang rỗng (đối tượng thực tế vẫn nằm ở bucket 10) -> false! Đối tượng bị kẹt lại và gây rò rỉ bộ nhớ (Memory Leak). Vì vậy Key trong Map/Set luôn phải là Immutable.",
        "difficulty": "hard",
        "tags": ["MutableKey", "HashSet", "MemoryLeak"]
    },
    {
        "id": "L5_Q49",
        "lessonId": 5,
        "type": "multiple",
        "title": "Về cơ chế Fail-Fast của Iterator trong Java Collections (như ArrayList, HashMap), những khẳng định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Khi một luồng đang duyệt qua Collection bằng Iterator mà Collection đó bị sửa đổi cấu trúc (thêm/xóa phần tử) không thông qua chính phương thức của Iterator, Iterator sẽ ném ConcurrentModificationException ngay lập tức",
            "Cơ chế Fail-Fast hoạt động dựa trên việc so sánh biến đếm số lần sửa đổi 'modCount' của Collection với 'expectedModCount' của Iterator",
            "Để xóa phần tử an toàn trong khi duyệt vòng lặp, ta phải dùng phương thức iterator.remove() thay vì list.remove()",
            "Fail-Fast đảm bảo 100% ngăn chặn hoàn toàn mọi lỗi tương tranh trong môi trường đa luồng mà không cần dùng cơ chế đồng bộ hóa"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Fail-Fast chỉ là cơ chế 'best-effort' phát hiện lỗi sớm qua modCount, không bảo đảm tuyệt đối trong môi trường đa luồng không đồng bộ. Muốn xóa an toàn khi lặp phải dùng iterator.remove().",
        "difficulty": "medium",
        "tags": ["FailFast", "Iterator", "ConcurrentModificationException"]
    },
    {
        "id": "L5_Q50",
        "lessonId": 5,
        "type": "single",
        "title": "Xác định output của đoạn mã sau khi xóa phần tử trong vòng lặp for-each của List:",
        "code": "List<String> list = new ArrayList<>(Arrays.asList(\"A\", \"B\", \"C\"));\nfor (String s : list) {\n    if (s.equals(\"A\")) {\n        list.remove(s);\n    }\n}",
        "options": [
            "Ném ngoại lệ java.util.ConcurrentModificationException khi sang lần lặp kế tiếp",
            "Chương trình chạy bình thường và danh sách còn lại [\"B\", \"C\"]",
            "Lỗi biên dịch tại lệnh list.remove(s)",
            "Vòng lặp chạy vô hạn không dừng"
        ],
        "correctAnswer": 0,
        "explanation": "Vòng lặp for-each trong Java ngầm định sử dụng Iterator. Khi gọi list.remove(s) trực tiếp trên List, modCount tăng lên nhưng expectedModCount của Iterator không đổi. Ở lần gọi iterator.next() kế tiếp, sự bất đồng bộ giữa modCount và expectedModCount làm ném ngay java.util.ConcurrentModificationException.",
        "difficulty": "medium",
        "tags": ["ForEachTrap", "ConcurrentModificationException", "ArrayList"]
    },
    {
        "id": "L5_Q51",
        "lessonId": 5,
        "type": "single",
        "title": "Lớp LinkedHashMap có tính năng độc đáo nào so với HashMap thông thường?",
        "code": None,
        "options": [
            "Duy trì một danh sách liên kết kép (doubly-linked list) xuyên qua các entry, cho phép duyệt theo thứ tự chèn (Insertion Order) hoặc theo thứ tự truy cập (Access Order để làm LRU Cache)",
            "Luôn tự động sắp xếp các phần tử tăng dần theo giá trị của Key giống TreeMap",
            "Chỉ cho phép lưu trữ tối đa 16 phần tử và không bao giờ xảy ra va chạm băm",
            "Tự động đồng bộ hóa tất cả các phương thức get() và put() giống như Hashtable"
        ],
        "correctAnswer": 0,
        "explanation": "LinkedHashMap mở rộng từ HashMap và bổ sung danh sách liên kết kép giữa các node. Constructor của nó cho phép bật cờ accessOrder=true: mỗi khi một entry được get() hoặc put(), nó được chuyển về cuối danh sách liên kết, rất lý tưởng để xây dựng bộ nhớ đệm Least Recently Used (LRU Cache) bằng cách override removeEldestEntry().",
        "difficulty": "medium",
        "tags": ["LinkedHashMap", "LRUCache", "Collections"]
    },
    {
        "id": "L5_Q52",
        "lessonId": 5,
        "type": "single",
        "title": "Điều gì xảy ra khi đưa một đối tượng của lớp KHÔNG cài đặt Comparable vào một TreeSet không có Comparator?",
        "code": "class Item {\n    int price;\n    Item(int p) { this.price = p; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Set<Item> set = new TreeSet<>();\n        set.add(new Item(100));\n    }\n}",
        "options": [
            "Ném ngoại lệ java.lang.ClassCastException: Item cannot be cast to java.lang.Comparable khi chạy lệnh add()",
            "Biên dịch thành công và phần tử được thêm vào bình thường",
            "Lỗi biên dịch ngay tại dòng 'new TreeSet<>()'",
            "Tự động sắp xếp theo hashCode của đối tượng Item"
        ],
        "correctAnswer": 0,
        "explanation": "TreeSet hoạt động dựa trên cây đỏ-đen (Red-Black Tree) và bắt buộc các phần tử phải có khả năng so sánh được để xác định vị trí trong cây. Nếu không truyền Comparator vào constructor của TreeSet, khi add() phần tử, nó sẽ ép kiểu sang Comparable. Vì Item không implements Comparable nên ném java.lang.ClassCastException tại runtime.",
        "difficulty": "easy",
        "tags": ["TreeSet", "Comparable", "ClassCastException"]
    },
    {
        "id": "L5_Q53",
        "lessonId": 5,
        "type": "multiple",
        "title": "So sánh giữa ConcurrentHashMap và Hashtable trong Java, những khẳng định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Hashtable khóa toàn bộ bảng (khóa toàn phần trên chính đối tượng Hashtable) cho mọi thao tác đọc/ghi, gây nút thắt cổ chai về hiệu năng khi nhiều luồng truy cập",
            "ConcurrentHashMap sử dụng kỹ thuật khóa phân đoạn (Segment Locking / Lock striping) hoặc CAS (Compare-And-Swap) kết hợp synchronized trên từng bucket riêng lẻ, cho phép nhiều luồng đọc/ghi đồng thời",
            "ConcurrentHashMap không cho phép lưu trữ null cho cả Key và Value",
            "Hashtable cho phép Key là null nhưng cấm Value là null"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1 và 2 mô tả chính xác sự khác biệt về cơ chế concurrency: Hashtable khóa toàn bộ, ConcurrentHashMap khóa theo từng bucket/node. 3 đúng: ConcurrentHashMap cấm hoàn toàn null key và null value để tránh nhập nhằng trong môi trường đa luồng. 4 sai: Hashtable cấm cả null key và null value.",
        "difficulty": "hard",
        "tags": ["ConcurrentHashMap", "Hashtable", "Concurrency"]
    },
    {
        "id": "L5_Q54",
        "lessonId": 5,
        "type": "single",
        "title": "Xác định output của đoạn mã sau sử dụng IdentityHashMap:",
        "code": "Map<String, String> map = new IdentityHashMap<>();\nString s1 = new String(\"key\");\nString s2 = new String(\"key\");\nmap.put(s1, \"Value 1\");\nmap.put(s2, \"Value 2\");\nSystem.out.println(map.size());",
        "options": [
            "2",
            "1",
            "Lỗi biên dịch",
            "Ném ngoại lệ DuplicateKeyException"
        ],
        "correctAnswer": 0,
        "explanation": "Khác với HashMap thông thường so sánh key bằng phương thức equals(), IdentityHashMap so sánh key bằng TOÁN TỬ SO SÁNH THAM CHIẾU '==' (Reference Equality). Vì s1 và s2 là 2 đối tượng String độc lập trong Heap (s1 == s2 là false), chúng được coi là 2 key khác nhau hoàn toàn trong IdentityHashMap, do đó map.size() bằng 2.",
        "difficulty": "hard",
        "tags": ["IdentityHashMap", "ReferenceEquality", "Map"]
    },
    {
        "id": "L5_Q55",
        "lessonId": 5,
        "type": "multiple",
        "title": "Những Collection nào sau đây trong gói java.util là cấu trúc dữ liệu duy trì thứ tự chèn (Insertion Order) của các phần tử?",
        "code": None,
        "options": [
            "ArrayList",
            "LinkedList",
            "LinkedHashSet",
            "TreeSet"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "ArrayList, LinkedList và LinkedHashSet đều duy trì thứ tự chèn (phần tử thêm trước đứng trước, thêm sau đứng sau). TreeSet không duy trì thứ tự chèn mà sắp xếp các phần tử theo thứ tự tự nhiên (Natural Order) hoặc theo Comparator.",
        "difficulty": "easy",
        "tags": ["InsertionOrder", "Collections", "Set"]
    },
    {
        "id": "L5_Q56",
        "lessonId": 5,
        "type": "single",
        "title": "Lớp CopyOnWriteArrayList giải quyết bài toán lặp đa luồng theo cơ chế nào?",
        "code": None,
        "options": [
            "Mỗi khi có thao tác sửa đổi (add, set, remove), nó tạo ra một bản sao mới (cloned copy) của toàn bộ mảng bên dưới, các Iterator đang duyệt tiếp tục duyệt trên bản chụp (snapshot) cũ mà không bị ConcurrentModificationException",
            "Khóa toàn bộ danh sách bằng từ khóa synchronized mỗi khi đọc phần tử",
            "Chuyển đổi danh sách thành mảng nguyên thủy tại thời điểm compile-time",
            "Tự động loại bỏ các phần tử trùng lặp khi có nhiều luồng cùng ghi"
        ],
        "correctAnswer": 0,
        "explanation": "Đúng như tên gọi 'Copy-On-Write', mỗi thao tác ghi (write/modify) sẽ nhân bản một mảng mới. Iterator được tạo ra tại một thời điểm chỉ duyệt trên bản chụp (snapshot) không đổi của mảng tại thời điểm đó, nên không bao giờ ném ConcurrentModificationException và các luồng đọc không cần lock, rất thích hợp khi số lần đọc áp đảo số lần ghi.",
        "difficulty": "medium",
        "tags": ["CopyOnWriteArrayList", "Snapshot", "ThreadSafeCollections"]
    },
    {
        "id": "L5_Q57",
        "lessonId": 5,
        "type": "single",
        "title": "Cho đoạn mã sau với PriorityQueue. Output khi lấy lần lượt các phần tử ra là gì?",
        "code": "Queue<Integer> pq = new PriorityQueue<>();\npq.offer(30);\npq.offer(10);\npq.offer(20);\nwhile (!pq.isEmpty()) {\n    System.out.print(pq.poll() + \" \");\n}",
        "options": [
            "10 20 30 ",
            "30 10 20 ",
            "30 20 10 ",
            "10 30 20 "
        ],
        "correctAnswer": 0,
        "explanation": "PriorityQueue trong Java mặc định là một Min-Heap (phần tử nhỏ nhất có độ ưu tiên cao nhất). Mỗi lần gọi pq.poll(), nó luôn lấy ra phần tử nhỏ nhất hiện có. Do đó thứ tự lấy ra là 10 20 30.",
        "difficulty": "easy",
        "tags": ["PriorityQueue", "MinHeap", "Queue"]
    },
    {
        "id": "L5_Q58",
        "lessonId": 5,
        "type": "single",
        "title": "Trong HashMap của Java 8, khi số lượng phần tử trong một bucket (thùng) vượt quá ngưỡng TREEIFY_THRESHOLD (mặc định là 8) và dung lượng mảng đạt tối thiểu 64, danh sách liên kết đơn trong bucket đó được chuyển đổi thành cấu trúc gì?",
        "code": None,
        "options": [
            "Cây Đỏ-Đen (Red-Black Tree) giúp cải thiện độ phức tạp tìm kiếm trong bucket từ O(n) thành O(log n)",
            "Cây nhị phân tìm kiếm thông thường (BST) không cân bằng",
            "Mảng động ArrayList",
            "Bảng băm lồng nhau (Nested HashTable)"
        ],
        "correctAnswer": 0,
        "explanation": "Từ Java 8, nhằm chống lại các cuộc tấn công từ chối dịch vụ (Hash DoS attack) do cố tình tạo va chạm băm, khi số phần tử trong 1 bucket >= 8 và tổng capacity >= 64, LinkedList đơn sẽ biến thành Red-Black Tree (TreeNode), giảm thời gian tra cứu từ O(n) xuống O(log n).",
        "difficulty": "medium",
        "tags": ["HashMapInternals", "RedBlackTree", "Java8Optimization"]
    },
    {
        "id": "L5_Q59",
        "lessonId": 5,
        "type": "multiple",
        "title": "Để đảm bảo an toàn tuyệt đối khi sử dụng đối tượng làm Key trong HashMap, các thuộc tính cấu thành hashCode() và equals() nên được thiết kế như thế nào?",
        "code": None,
        "options": [
            "Nên thiết kế lớp của Key là Immutable (các trường là private final và không có setter)",
            "Không bao giờ thay đổi trạng thái của đối tượng Key sau khi đã đưa vào Map",
            "Chỉ nên sử dụng các kiểu dữ liệu đã được chứng minh bất biến như String, Integer, UUID làm Key",
            "Nên cho các trường của Key là public để HashMap có thể sửa đổi trực tiếp"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Nếu Key bị thay đổi sau khi put vào Map, hashCode sẽ thay đổi và entry sẽ bị thất lạc vĩnh viễn (không thể get ra được). Do đó, Key bất biến (Immutable) như String, Integer hoặc lớp tự viết có trường private final là best practice hàng đầu.",
        "difficulty": "easy",
        "tags": ["HashMapBestPractice", "ImmutableKey", "Design"]
    },
    {
        "id": "L5_Q60",
        "lessonId": 5,
        "type": "single",
        "title": "Xác định output của đoạn mã so sánh hai danh sách sau:",
        "code": "List<Integer> list1 = new ArrayList<>(Arrays.asList(1, 2, 3));\nList<Integer> list2 = new LinkedList<>(Arrays.asList(1, 2, 3));\nSystem.out.println(list1.equals(list2));",
        "options": [
            "true (theo đặc tả List.equals(), hai List bằng nhau nếu cùng kích thước và các phần tử tại từng vị trí tương ứng equals bằng nhau, không phụ thuộc vào lớp triển khai cụ thể)",
            "false (vì ArrayList và LinkedList là hai lớp triển khai khác nhau)",
            "Lỗi biên dịch tại phép so sánh",
            "Ném ClassCastException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Hợp đồng List.equals() trong Java quy định: hai danh sách được coi là bằng nhau nếu chúng chứa cùng số phần tử và các phần tử tương ứng ở từng chỉ số đều bằng nhau (e1 == null ? e2 == null : e1.equals(e2)). Việc một bên là ArrayList và bên kia là LinkedList không ảnh hưởng đến kết quả, kết quả in ra true.",
        "difficulty": "medium",
        "tags": ["ListEquals", "CollectionsContract", "ArrayListVsLinkedList"]
    },

    # --- ĐỀ 5E (L5_Q61 - L5_Q75): Advanced Exceptions, Masking & Serialization ---
    {
        "id": "L5_Q61",
        "lessonId": 5,
        "type": "single",
        "title": "Hiện tượng 'Exception Masking' (Nuốt ngoại lệ) xảy ra trong trường hợp nào sau đây?",
        "code": "public class MaskingTest {\n    static int test() {\n        try {\n            throw new RuntimeException(\"Lỗi từ try\");\n        } finally {\n            return 42; // Lệnh return trong finally\n        }\n    }\n    public static void main(String[] args) {\n        System.out.println(test());\n    }\n}",
        "options": [
            "In ra: 42 (RuntimeException bị khối finally nuốt trọn và biến mất hoàn toàn)",
            "Ném ngoại lệ RuntimeException: Lỗi từ try",
            "Lỗi biên dịch vì không thể return trong khối finally",
            "In ra 42 sau đó ném RuntimeException"
        ],
        "correctAnswer": 0,
        "explanation": "Lệnh 'return' hoặc ném ngoại lệ mới bên trong khối 'finally' sẽ ghi đè và hủy bỏ hoàn toàn bất kỳ ngoại lệ nào chưa được xử lý phát sinh từ khối 'try' hoặc 'catch'. Đây là một 'anti-pattern' rất nguy hiểm trong Java vì nó làm mất dấu vết lỗi nghiêm trọng.",
        "difficulty": "hard",
        "tags": ["ExceptionMasking", "FinallyReturn", "Trap"]
    },
    {
        "id": "L5_Q62",
        "lessonId": 5,
        "type": "single",
        "title": "Trong cấu trúc try-with-resources, thứ tự đóng các tài nguyên (AutoCloseable resources) diễn ra như thế nào?",
        "code": "class Res implements AutoCloseable {\n    String name;\n    Res(String name) { this.name = name; }\n    public void close() { System.out.print(name + \" \"); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        try (Res r1 = new Res(\"R1\"); Res r2 = new Res(\"R2\")) {\n            System.out.print(\"WORK \");\n        }\n    }\n}",
        "options": [
            "WORK R2 R1 ",
            "WORK R1 R2 ",
            "R1 R2 WORK ",
            "R2 R1 WORK "
        ],
        "correctAnswer": 0,
        "explanation": "Trong khối try-with-resources, các tài nguyên được khởi tạo theo thứ tự từ trái sang phải (R1 rồi đến R2), nhưng KHI ĐÓNG TÀI NGUYÊN (close()), CHÚNG ĐƯỢC ĐÓNG THEO THỨ TỰ NGƯỢC LẠI (Reverse Order: R2 đóng trước, sau đó mới đến R1). Điều này tương tự như cơ chế giải phóng stack và đóng luồng bọc ngoài trước luồng bên trong.",
        "difficulty": "medium",
        "tags": ["TryWithResources", "AutoCloseable", "CloseOrder"]
    },
    {
        "id": "L5_Q63",
        "lessonId": 5,
        "type": "single",
        "title": "Khi khối try ném ngoại lệ Ex1, và phương thức close() của tài nguyên trong try-with-resources cũng ném ngoại lệ Ex2, JVM xử lý hai ngoại lệ này như thế nào?",
        "code": None,
        "options": [
            "Ex1 (ngoại lệ ban đầu trong try) được ném ra ngoài làm ngoại lệ chính, còn Ex2 được gắn kèm vào Ex1 dưới dạng một Ngoại lệ bị ức chế (Suppressed Exception) và có thể lấy qua phương thức ex1.getSuppressed()",
            "Ex2 ghi đè hoàn toàn Ex1 giống như trong khối finally thông thường",
            "JVM ném ngoại lệ kép DoubleException",
            "Cả hai ngoại lệ đều bị hủy và chương trình dừng đột ngột"
        ],
        "correctAnswer": 0,
        "explanation": "Đây là cải tiến vượt trội của try-with-resources (Java 7) so với try-finally truyền thống. Thay vì để ngoại lệ ở close() nuốt mất ngoại lệ gốc trong try, JVM bảo toàn ngoại lệ gốc và gắn ngoại lệ sinh ra lúc đóng tài nguyên vào danh sách 'Suppressed Exceptions' (truy xuất qua Throwable.getSuppressed()).",
        "difficulty": "hard",
        "tags": ["SuppressedExceptions", "TryWithResources", "JVM"]
    },
    {
        "id": "L5_Q64",
        "lessonId": 5,
        "type": "single",
        "title": "Điều gì xảy ra khi sắp xếp sai thứ tự các khối catch ngoại lệ:",
        "code": "try {\n    int x = 10 / 0;\n} catch (Exception e) {\n    System.out.println(\"Exception\");\n} catch (ArithmeticException e) {\n    System.out.println(\"Arithmetic\");\n}",
        "options": [
            "Lỗi biên dịch: Unreachable catch block for ArithmeticException (khối catch con không thể với tới vì đã bị bắt bởi Exception)",
            "Biên dịch thành công và in ra: Arithmetic",
            "Biên dịch thành công và in ra: Exception",
            "Cả hai khối catch đều được thực thi lần lượt"
        ],
        "correctAnswer": 0,
        "explanation": "Trong Java, các khối catch được đánh giá tuần tự từ trên xuống dưới. Nếu một khối catch cha (Exception) đứng trước khối catch con (ArithmeticException), khối catch con sẽ trở thành 'mã chết' (unreachable code) vì mọi ngoại lệ con đều đã bị cha tóm trước. Trình biên dịch báo lỗi ngay tại thời điểm biên dịch.",
        "difficulty": "easy",
        "tags": ["CatchOrder", "CompileError", "UnreachableCode"]
    },
    {
        "id": "L5_Q65",
        "lessonId": 5,
        "type": "multiple",
        "title": "Về tính năng Multi-Catch Block (cho phép bắt nhiều loại ngoại lệ trong một khối catch duy nhất, ví dụ: catch (IOException | SQLException e)), những phát biểu nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Biến tham chiếu ngoại lệ 'e' trong khối multi-catch ngầm định là 'final', không thể gán lại giá trị mới cho 'e'",
            "Không được phép khai báo các ngoại lệ có quan hệ cha-con kế thừa trong cùng một mệnh đề multi-catch (ví dụ: catch (IOException | FileNotFoundException e) gây lỗi biên dịch)",
            "Giúp giảm bớt việc lặp mã nguồn (boilerplate code) khi nhiều ngoại lệ có cùng một logic xử lý lỗi",
            "Mỗi khối multi-catch có thể bắt tối đa đúng 2 loại ngoại lệ"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1 đúng: e là implicitly final. 2 đúng: nếu có quan hệ cha con thì dư thừa và compiler báo lỗi. 3 đúng: đây là mục đích chính của tính năng đưa vào từ Java 7. 4 sai: có thể nối bao nhiêu ngoại lệ tùy ý bằng dấu gạch đứng '|'.",
        "difficulty": "medium",
        "tags": ["MultiCatch", "Java7", "ExceptionRules"]
    },
    {
        "id": "L5_Q66",
        "lessonId": 5,
        "type": "single",
        "title": "Vai trò của thuộc tính 'private static final long serialVersionUID' trong một lớp implements Serializable là gì?",
        "code": None,
        "options": [
            "Đóng vai trò là mã định danh phiên bản của lớp trong quá trình tuần tự hóa và giải tuần tự hóa; nếu mã nguồn thay đổi làm lệch serialVersionUID, JVM sẽ ném InvalidClassException để bảo vệ tính toàn vẹn dữ liệu",
            "Xác định kích thước tối đa của file nhị phân được ghi ra đĩa",
            "Bắt buộc JVM phải mã hóa dữ liệu đối tượng bằng thuật toán AES",
            "Dùng để đánh số thứ tự số lượng đối tượng đã được tạo trong bộ nhớ"
        ],
        "correctAnswer": 0,
        "explanation": "serialVersionUID là con số định danh phiên bản của cấu trúc class khi ghi và đọc stream. Nếu bạn không khai báo tường minh, JVM tự động tính toán băm theo cấu trúc class. Khi sửa đổi class (thêm field, đổi method), giá trị tự tính thay đổi, dẫn đến khi đọc lại dữ liệu cũ sẽ bị ném java.io.InvalidClassException.",
        "difficulty": "medium",
        "tags": ["serialVersionUID", "Serialization", "Compatibility"]
    },
    {
        "id": "L5_Q67",
        "lessonId": 5,
        "type": "single",
        "title": "Khi một đối tượng được tuần tự hóa (Serialization), từ khóa 'transient' đặt trước một trường dữ liệu (field) có tác dụng gì?",
        "code": "class Account implements Serializable {\n    String username;\n    transient String password;\n}",
        "options": [
            "Yêu cầu JVM bỏ qua trường đó, không ghi giá trị của nó vào luồng tuần tự hóa; khi giải tuần tự hóa (deserialization), trường đó sẽ mang giá trị mặc định (null với đối tượng, 0 với số)",
            "Mã hóa trường đó bằng mật khẩu trước khi ghi ra file",
            "Biến trường đó thành biến tĩnh (static)",
            "Tự động chuyển đổi chuỗi thành mảng byte"
        ],
        "correctAnswer": 0,
        "explanation": "Từ khóa 'transient' dùng để đánh dấu các trường nhạy cảm (như password, credit card) hoặc dữ liệu tạm thời không cần lưu trữ trạng thái. Khi deserialization, trường transient không được khôi phục từ stream mà nhận giá trị mặc định của kiểu dữ liệu (null, 0, false).",
        "difficulty": "easy",
        "tags": ["Transient", "Serialization", "Security"]
    },
    {
        "id": "L5_Q68",
        "lessonId": 5,
        "type": "multiple",
        "title": "Những thành phần nào sau đây trong một class KHÔNG BAO GIỜ được lưu trữ vào luồng dữ liệu khi thực hiện Java Serialization tiêu chuẩn?",
        "code": None,
        "options": [
            "Các trường được khai báo với từ khóa 'static' (vì biến static thuộc về Class chứ không thuộc về trạng thái của đối tượng)",
            "Các trường được khai báo với từ khóa 'transient'",
            "Các phương thức của lớp (chỉ có dữ liệu trạng thái được tuần tự hóa, mã bytecode của phương thức không được ghi vào file stream)",
            "Tất cả các trường kiểu String"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Serialization chỉ ghi lại TRẠNG THÁI (state) của đối tượng cụ thể (các instance fields non-transient). Các trường static (thuộc về class), trường transient (bị đánh dấu bỏ qua) và code phương thức không nằm trong luồng tuần tự hóa. Trường String nếu không transient vẫn được tuần tự hóa bình thường.",
        "difficulty": "medium",
        "tags": ["SerializationRules", "Static", "Transient"]
    },
    {
        "id": "L5_Q69",
        "lessonId": 5,
        "type": "single",
        "title": "Điều gì xảy ra khi lớp con thực thi Serializable nhưng lớp cha KHÔNG thực thi Serializable?",
        "code": "class Parent {\n    int parentVal = 10;\n    Parent() { System.out.print(\"ParentCons \"); }\n}\nclass Child extends Parent implements Serializable {\n    int childVal = 20;\n    Child() { System.out.print(\"ChildCons \"); }\n}",
        "options": [
            "Lớp con vẫn tuần tự hóa bình thường, nhưng khi giải tuần tự hóa (Deserialization), constructor không tham số của lớp cha (Parent()) BẮT BUỘC phải được gọi để khởi tạo lại các trường của cha",
            "Lỗi biên dịch ngay tại dòng khai báo class Child",
            "Ném ngoại lệ NotSerializableException ngay khi chạy lệnh serialize",
            "Toàn bộ các trường của lớp cha tự động biến mất và không thể truy cập được"
        ],
        "correctAnswer": 0,
        "explanation": "Nếu lớp con Serializable kế thừa lớp cha Non-Serializable: Khi deserialization, JVM không khôi phục trường của cha từ stream mà bắt buộc phải gọi Constructor không tham số của lớp cha đầu tiên không Serializable để khởi tạo trạng thái của cha. Nếu lớp cha không có no-arg constructor, JVM sẽ ném InvalidClassException tại runtime.",
        "difficulty": "hard",
        "tags": ["SerializationInheritance", "ConstructorInDeserialization", "JVM"]
    },
    {
        "id": "L5_Q70",
        "lessonId": 5,
        "type": "single",
        "title": "Sự khác biệt căn bản giữa interface 'Serializable' và 'Externalizable' trong Java là gì?",
        "code": None,
        "options": [
            "Serializable là Marker Interface (không có phương thức nào, JVM tự động thực hiện hoàn toàn); còn Externalizable có 2 phương thức writeExternal() và readExternal() bắt buộc lập trình viên phải tự viết mã lưu/đọc từng trường thủ công",
            "Externalizable chỉ dùng cho mạng Socket, Serializable dùng cho file đĩa",
            "Serializable nhanh hơn Externalizable gấp 10 lần",
            "Externalizable không cho phép sử dụng constructor không tham số"
        ],
        "correctAnswer": 0,
        "explanation": "Serializable là marker interface rỗng, JVM dùng reflection tự động ghi đọc toàn bộ đồ thị đối tượng (chậm hơn và sinh file lớn hơn). Externalizable kế thừa từ Serializable, cung cấp writeExternal và readExternal trao toàn quyền kiểm soát cấu trúc nhị phân cho lập trình viên (nhanh hơn, nhỏ gọn hơn, nhưng đòi hỏi phải có public no-arg constructor).",
        "difficulty": "medium",
        "tags": ["Externalizable", "Serializable", "Comparison"]
    },
    {
        "id": "L5_Q71",
        "lessonId": 5,
        "type": "multiple",
        "title": "Để tùy biến sâu quá trình tuần tự hóa của một lớp implements Serializable mà không cần dùng Externalizable, lớp đó có thể khai báo những phương thức private đặc biệt nào?",
        "code": None,
        "options": [
            "private void writeObject(ObjectOutputStream out) throws IOException",
            "private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException",
            "private Object readResolve() throws ObjectStreamException (dùng để bảo toàn tính duy nhất của Singleton)",
            "public void serializeToDisk(File file)"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "JVM hỗ trợ cơ chế hook đặc biệt: nếu lớp có khai báo private writeObject() và readObject(), JVM sẽ gọi chúng qua reflection để tùy biến ghi/đọc dữ liệu. Phương thức readResolve() cực kỳ quan trọng để ngăn chặn deserialization tạo ra thể hiện mới phá vỡ mẫu thiết kế Singleton.",
        "difficulty": "hard",
        "tags": ["CustomSerialization", "ReadResolve", "SingletonSafety"]
    },
    {
        "id": "L5_Q72",
        "lessonId": 5,
        "type": "single",
        "title": "Lớp ByteArrayInputStream và ByteArrayOutputStream khác biệt căn bản với FileInputStream và FileOutputStream ở điểm nào?",
        "code": None,
        "options": [
            "ByteArrayInputStream đọc và ghi dữ liệu trực tiếp trên mảng byte trong bộ nhớ RAM, không phát sinh thao tác I/O trên đĩa cứng hệ điều hành",
            "ByteArrayInputStream chỉ đọc được các ký tự tiếng Việt Unicode",
            "FileInputStream không thể đóng bằng lệnh close()",
            "ByteArrayOutputStream tự động mã hóa dữ liệu thành chuỗi Base64"
        ],
        "correctAnswer": 0,
        "explanation": "ByteArrayInputStream / ByteArrayOutputStream hoạt động hoàn toàn trên bộ nhớ RAM (bộ đệm byte buffer), tốc độ cực nhanh vì không truy cập thiết bị I/O vật lý của hệ điều hành. Việc gọi close() trên ByteArray stream thực tế không có tác dụng và phương thức của nó vẫn có thể gọi tiếp sau khi close().",
        "difficulty": "medium",
        "tags": ["ByteStreams", "MemoryIO", "ByteArrayInputStream"]
    },
    {
        "id": "L5_Q73",
        "lessonId": 5,
        "type": "single",
        "title": "So sánh giữa Luồng Byte (Byte Streams - InputStream/OutputStream) và Luồng Ký tự (Character Streams - Reader/Writer):",
        "code": None,
        "options": [
            "Byte Stream xử lý dữ liệu thô nhị phân theo từng byte 8-bit (phù hợp cho file ảnh, video, âm thanh); Character Stream xử lý văn bản theo từng ký tự 16-bit Unicode và tự động chuyển đổi bảng mã (charset)",
            "Byte Stream chỉ đọc được số nguyên, Character Stream chỉ đọc được chuỗi rỗng",
            "Character Stream không thể đọc dữ liệu từ bàn phím",
            "Byte Stream tự động nhận diện định dạng UTF-8"
        ],
        "correctAnswer": 0,
        "explanation": "Byte Streams (InputStream, OutputStream) xử lý dữ liệu nhị phân nguyên thủy 8-bit. Character Streams (Reader, Writer) được thiết kế từ Java 1.1 chuyên xử lý văn bản 16-bit Unicode, tự động ánh xạ giữa bảng mã nhị phân của OS và ký tự Java qua các lớp cầu nối như InputStreamReader.",
        "difficulty": "easy",
        "tags": ["ByteStreams", "CharacterStreams", "IOStream"]
    },
    {
        "id": "L5_Q74",
        "lessonId": 5,
        "type": "single",
        "title": "Mục đích của việc bọc BufferedReader xung quanh một FileReader (ví dụ: new BufferedReader(new FileReader(\"data.txt\"))) là gì?",
        "code": None,
        "options": [
            "Tạo một vùng đệm bộ nhớ (Buffer) để giảm bớt số lần truy xuất I/O đĩa cứng vật lý và cung cấp phương thức tiện ích readLine() để đọc từng dòng văn bản",
            "Để mã hóa file văn bản chống xem trộm",
            "Để tự động đảo ngược thứ tự các từ trong file",
            "FileReader không thể hoạt động nếu không có BufferedReader bao quanh"
        ],
        "correctAnswer": 0,
        "explanation": "Đọc từng ký tự trực tiếp từ đĩa bằng FileReader rất tốn kém tài nguyên CPU và I/O đĩa. BufferedReader đọc một khối lớn dữ liệu vào bộ đệm RAM (mặc định 8KB), giúp tăng tốc độ đọc lên hàng chục lần và hỗ trợ phương thức readLine() đọc theo dòng.",
        "difficulty": "easy",
        "tags": ["BufferedReader", "Decorator", "Performance"]
    },
    {
        "id": "L5_Q75",
        "lessonId": 5,
        "type": "single",
        "title": "Xác định output của đoạn mã xử lý ngoại lệ phức tạp sau:",
        "code": "public class ExceptionFlow {\n    static String test() {\n        String res = \"\";\n        try {\n            res += \"T\";\n            int x = 1 / 0;\n            res += \"X\";\n        } catch (ArithmeticException e) {\n            res += \"C\";\n            return res;\n        } finally {\n            res += \"F\";\n        }\n        return res;\n    }\n    public static void main(String[] args) {\n        System.out.println(test());\n    }\n}",
        "options": [
            "TC (khối finally chạy nhưng giá trị trả về 'TC' đã được lưu vào bộ nhớ stack trước khi finally thực thi)",
            "TCF",
            "TF",
            "TCXF"
        ],
        "correctAnswer": 0,
        "explanation": "Trong catch, res đang là \"TC\". Khi gặp lệnh 'return res;', giá trị trả về của hàm (\"TC\") được sao chép và lưu trữ sẵn trong thanh ghi trả về (return register). Tiếp theo, khối 'finally' bắt buộc phải chạy và thực hiện res += \"F\" (biến res cục bộ đổi thành \"TCF\"), nhưng vì finally không có lệnh return ghi đè, giá trị đã được lưu trước đó (\"TC\") sẽ được trả về hàm main. In ra: TC.",
        "difficulty": "hard",
        "tags": ["FinallyFlow", "ReturnValueStack", "TrickyOutput"]
    }
]

L6_NEW = [
    # --- ĐỀ 6C (L6_Q31 - L6_Q45): Advanced Creational & Structural Patterns ---
    {
        "id": "L6_Q31",
        "lessonId": 6,
        "type": "single",
        "title": "Tại sao giải pháp 'Bill Pugh Singleton' (sử dụng Static Inner Helper Class) được coi là cách cài đặt Singleton tối ưu nhất trong Java truyền thống?",
        "code": "public class Singleton {\n    private Singleton() {}\n    private static class Holder {\n        private static final Singleton INSTANCE = new Singleton();\n    }\n    public static Singleton getInstance() {\n        return Holder.INSTANCE;\n    }\n}",
        "options": [
            "Đảm bảo Lazy Loading (chỉ khởi tạo khi getInstance() được gọi lần đầu) và đảm bảo Thread-safe tuyệt đối nhờ cơ chế Class Loading của JVM mà không cần dùng từ khóa 'synchronized'",
            "Tự động chống lại việc phá vỡ Singleton bằng Java Reflection API",
            "Có thể tạo ra nhiều hơn một thể hiện nếu máy chủ có nhiều nhân CPU",
            "Tự động giải phóng thể hiện khi bộ nhớ RAM đạt ngưỡng 90%"
        ],
        "correctAnswer": 0,
        "explanation": "Lớp nội tĩnh Holder không được nạp vào bộ nhớ khi class Singleton được load, mà chỉ được nạp khi getInstance() được gọi lần đầu (Lazy Loading). Quá trình nạp lớp của JVM được đồng bộ hóa sẵn bởi ClassLoader (JLS 12.4.2), đảm bảo thread-safe 100% mà không phải chịu chi phí chậm chạp của từ khóa synchronized.",
        "difficulty": "hard",
        "tags": ["Singleton", "BillPugh", "ClassLoading"]
    },
    {
        "id": "L6_Q32",
        "lessonId": 6,
        "type": "single",
        "title": "Theo Joshua Bloch (tác giả Effective Java), phương pháp cài đặt Singleton nào an toàn tuyệt đối trước cả tấn công qua Reflection và Serialization?",
        "code": "public enum EnumSingleton {\n    INSTANCE;\n    public void doSomething() {}\n}",
        "options": [
            "Enum Singleton (sử dụng kiểu enum một phần tử)",
            "Double-Checked Locking Singleton",
            "Eager Initialization Singleton",
            "Bill Pugh Static Holder Singleton"
        ],
        "correctAnswer": 0,
        "explanation": "Enum trong Java được JVM bảo vệ đặc biệt: Constructor của enum không thể bị gọi qua Reflection (Constructor.newInstance() kiểm tra và ném IllegalArgumentException: Cannot reflectively create enum objects), và cơ chế Serialization của enum chỉ ghi nhận tên hằng số nên không bao giờ tạo đối tượng mới. Do đó Enum Singleton là cách duy nhất chống phá vỡ 100%.",
        "difficulty": "medium",
        "tags": ["EnumSingleton", "EffectiveJava", "ReflectionProof"]
    },
    {
        "id": "L6_Q33",
        "lessonId": 6,
        "type": "single",
        "title": "Trong mẫu Double-Checked Locking Singleton, tại sao biến thể hiện 'instance' BẮT BUỘC phải được khai báo với từ khóa 'volatile'?",
        "code": "public class Singleton {\n    private static volatile Singleton instance;\n    public static Singleton getInstance() {\n        if (instance == null) {\n            synchronized (Singleton.class) {\n                if (instance == null) {\n                    instance = new Singleton(); // DONG NAY\n                }\n            }\n        }\n        return instance;\n    }\n}",
        "options": [
            "Để ngăn chặn hiện tượng Tái sắp xếp lệnh (Instruction Reordering) của trình biên dịch và CPU, đảm bảo đối tượng được khởi tạo đầy đủ các trường trước khi gán tham chiếu vào biến instance",
            "Để đảm bảo phương thức getInstance() chạy nhanh gấp 2 lần",
            "Nếu không có volatile thì lớp Singleton không thể biên dịch được",
            "Để cho phép các luồng có thể xóa đối tượng instance khi cần"
        ],
        "correctAnswer": 0,
        "explanation": "Lệnh 'new Singleton()' gồm 3 bước: 1. Cấp phát bộ nhớ, 2. Khởi tạo đối tượng (chạy constructor), 3. Gán địa chỉ cho biến instance. Nếu không có volatile, CPU/JIT có thể reorder bước 3 lên trước bước 2. Khi đó luồng khác gọi getInstance() thấy instance != null nhưng thực chất đối tượng bên trong chưa chạy xong constructor (Half-initialized object) dẫn đến lỗi chết người.",
        "difficulty": "hard",
        "tags": ["DoubleCheckedLocking", "Volatile", "InstructionReordering"]
    },
    {
        "id": "L6_Q34",
        "lessonId": 6,
        "type": "multiple",
        "title": "Phân biệt giữa Factory Method Pattern và Abstract Factory Pattern, những nhận định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Factory Method dựa trên cơ chế Kế thừa (Inheritance): một phương thức trừu tượng trong lớp cha được các lớp con ghi đè để quyết định kiểu đối tượng cụ thể được tạo ra",
            "Abstract Factory dựa trên cơ chế Bao hàm/Ủy quyền (Composition): một interface/abstract class cung cấp một họ các phương thức để tạo ra một họ các sản phẩm liên quan hoặc phụ thuộc nhau (family of related products)",
            "Factory Method tạo ra một sản phẩm duy nhất, trong khi Abstract Factory thường tạo ra cả một bộ/hệ thống các sản phẩm tương thích với nhau",
            "Abstract Factory là tên gọi cũ của Factory Method trước khi có cuốn sách Design Patterns của GoF"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 nêu bật bản chất phân biệt: Factory Method dùng kế thừa để sinh 1 loại sản phẩm; Abstract Factory dùng composition và chứa nhiều factory methods để sinh ra cả một họ sản phẩm tương thích (ví dụ GUIFactory tạo Button và Checkbox cho Windows/Mac).",
        "difficulty": "medium",
        "tags": ["FactoryMethod", "AbstractFactory", "CreationalPatterns"]
    },
    {
        "id": "L6_Q35",
        "lessonId": 6,
        "type": "single",
        "title": "Vấn đề 'Telescoping Constructor' (quá nhiều constructor nạp chồng với số lượng tham số tăng dần) được giải quyết thanh lịch nhất bởi mẫu thiết kế nào?",
        "code": "public class House {\n    public House(int rooms) { ... }\n    public House(int rooms, int doors) { ... }\n    public House(int rooms, int doors, boolean hasPool) { ... }\n    public House(int rooms, int doors, boolean hasPool, boolean hasGarage) { ... }\n}",
        "options": [
            "Builder Pattern (sử dụng lớp Builder với các phương thức thiết lập fluent chaining và phương thức build())",
            "Singleton Pattern",
            "Adapter Pattern",
            "Observer Pattern"
        ],
        "correctAnswer": 0,
        "explanation": "Builder Pattern là mẫu thiết kế chuyên biệt giải quyết vấn đề Telescoping Constructor khi một đối tượng có quá nhiều tham số (đặc biệt là các tham số tùy chọn - optional). Nó giúp code dễ đọc, an toàn, hỗ trợ Fluent API (chaining .withPool(true).build()) và đảm bảo đối tượng tạo ra có thể là Immutable.",
        "difficulty": "easy",
        "tags": ["BuilderPattern", "TelescopingConstructor", "Creational"]
    },
    {
        "id": "L6_Q36",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Prototype Pattern giải quyết bài toán nào sau đây?",
        "code": None,
        "options": [
            "Tạo ra các đối tượng mới bằng cách sao chép (clone) từ một đối tượng mẫu có sẵn thay vì khởi tạo mới tốn kém qua toán tử 'new'",
            "Đảm bảo chỉ có một đối tượng duy nhất tồn tại trong bộ nhớ",
            "Chuyển đổi giao diện của một lớp thành giao diện khác mà client mong đợi",
            "Đóng gói thuật toán vào các lớp riêng biệt để tráo đổi tại runtime"
        ],
        "correctAnswer": 0,
        "explanation": "Prototype Pattern cho phép tạo đối tượng mới bằng cách clone một instance hiện có (prototype). Điều này cực kỳ hữu ích khi việc khởi tạo một đối tượng từ đầu đòi hỏi các thao tác tốn kém (truy vấn DB, đọc file, tính toán nặng) hoặc cấu trúc đối tượng quá phức tạp.",
        "difficulty": "medium",
        "tags": ["PrototypePattern", "Clone", "Creational"]
    },
    {
        "id": "L6_Q37",
        "lessonId": 6,
        "type": "multiple",
        "title": "Về phương thức clone() và interface Cloneable trong Java, những khẳng định nào sau đây phản ánh ĐÚNG các vấn đề thiết kế?",
        "code": None,
        "options": [
            "Phương thức Object.clone() mặc định chỉ thực hiện sao chép nông (Shallow Copy): sao chép giá trị các trường nguyên thủy và sao chép tham chiếu của đối tượng, không nhân bản đối tượng bên trong",
            "Để thực hiện sao chép sâu (Deep Copy), lập trình viên bắt buộc phải tự ghi đè clone() và sao chép đệ quy từng đối tượng tham chiếu bên trong",
            "Interface Cloneable là một Marker Interface kỳ lạ vì nó không chứa phương thức clone() nào (phương thức clone() vốn nằm ở Object và mang quyền protected)",
            "Sử dụng Copy Constructor (hoặc Factory) được các chuyên gia Java khuyến khích thay thế cho clone() và Cloneable"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Cả 4 phát biểu đều chính xác. Cơ chế Cloneable của Java bị chỉ trích nặng nề trong sách Effective Java: Cloneable không có method clone, Object.clone chỉ shallow copy, ném CloneNotSupportedException phiền phức. Copy Constructor (như new ArrayList(existingList)) được khuyến nghị thay thế.",
        "difficulty": "hard",
        "tags": ["Cloneable", "DeepCopy", "ShallowCopy"]
    },
    {
        "id": "L6_Q38",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Adapter Pattern có mục đích cốt lõi là gì?",
        "code": None,
        "options": [
            "Chuyển đổi giao diện (interface) của một lớp hiện có thành một giao diện khác mà client mong muốn, giúp các lớp không tương thích về giao diện có thể làm việc được với nhau",
            "Bổ sung các hành vi mới cho đối tượng một cách linh hoạt tại runtime",
            "Ẩn giấu sự phức tạp của toàn bộ hệ thống đằng sau một giao diện đơn giản duy nhất",
            "Tạo một thể hiện duy nhất của một lớp trong toàn bộ ứng dụng"
        ],
        "correctAnswer": 0,
        "explanation": "Adapter Pattern (như củ sạc chuyển đổi chân cắm) đóng vai trò làm cầu nối chuyển đổi giữa hai interface không tương thích mà không cần phải chỉnh sửa mã nguồn gốc của lớp Adaptee (tuân thủ Open/Closed Principle).",
        "difficulty": "easy",
        "tags": ["AdapterPattern", "StructuralPatterns", "Compatibility"]
    },
    {
        "id": "L6_Q39",
        "lessonId": 6,
        "type": "single",
        "title": "Trong Java, ví dụ nào sau đây thể hiện việc áp dụng mẫu thiết kế Adapter Pattern trong thư viện chuẩn JDK?",
        "code": None,
        "options": [
            "Arrays.asList(T... a) (chuyển đổi mảng Java array thành giao diện List)",
            "System.out.println()",
            "Math.sqrt()",
            "Thread.sleep()"
        ],
        "correctAnswer": 0,
        "explanation": "Arrays.asList() chuyển đổi một mảng thô (Array) thành giao diện chuẩn List của Java Collections Framework mà không cần tạo mới toàn bộ dữ liệu. Tương tự, InputStreamReader là một adapter chuyển đổi Byte Stream thành Character Stream.",
        "difficulty": "medium",
        "tags": ["AdapterPattern", "ArraysAsList", "JDKExamples"]
    },
    {
        "id": "L6_Q40",
        "lessonId": 6,
        "type": "multiple",
        "title": "Phân biệt giữa Object Adapter và Class Adapter trong mẫu thiết kế Adapter:",
        "code": None,
        "options": [
            "Object Adapter sử dụng quan hệ Bao hàm (Composition): Adapter chứa một tham chiếu tới đối tượng Adaptee",
            "Class Adapter sử dụng quan hệ Kế thừa (Inheritance): Adapter kế thừa trực tiếp từ lớp Adaptee",
            "Trong Java, Object Adapter được sử dụng phổ biến hơn vì Java không hỗ trợ đa kế thừa lớp (Multiple class inheritance)",
            "Class Adapter và Object Adapter hoàn toàn giống nhau về mặt mã nguồn trong Java"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Class Adapter đòi hỏi kế thừa cả Client Interface và Adaptee Class (cần đa kế thừa). Vì Java không cho đa kế thừa lớp nên Object Adapter (dùng Composition bao bọc instance của Adaptee) là giải pháp tiêu chuẩn trong lập trình Java.",
        "difficulty": "medium",
        "tags": ["ObjectAdapter", "ClassAdapter", "DesignPatterns"]
    },
    {
        "id": "L6_Q41",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Facade Pattern khác với Adapter Pattern ở điểm cơ bản nào?",
        "code": None,
        "options": [
            "Facade tạo ra một giao diện đơn giản hóa mới để dễ sử dụng một hệ thống con phức tạp (Subsystem), còn Adapter làm cho hai giao diện sẵn có không tương thích có thể làm việc được với nhau",
            "Facade luôn dùng kế thừa, còn Adapter luôn dùng con trỏ hàm",
            "Facade chỉ dùng cho cơ sở dữ liệu, Adapter chỉ dùng cho mạng",
            "Facade làm tăng độ phức tạp của hệ thống"
        ],
        "correctAnswer": 0,
        "explanation": "Mục đích của Facade là cung cấp một cổng giao tiếp bậc cao, đơn giản hóa (Simplified Interface) che giấu cả một mớ bòng bong các lớp con bên trong. Còn Adapter giữ nguyên chức năng nhưng biến đổi giao diện từ chuẩn A sang chuẩn B để tương thích.",
        "difficulty": "easy",
        "tags": ["FacadePattern", "AdapterPattern", "Comparison"]
    },
    {
        "id": "L6_Q42",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Bridge Pattern nhằm mục đích tách biệt cái gì khỏi cái gì?",
        "code": None,
        "options": [
            "Tách biệt phần Trừu tượng (Abstraction) khỏi phần Cài đặt (Implementation) để cả hai có thể thay đổi và phát triển độc lập với nhau",
            "Tách biệt giao diện người dùng khỏi cơ sở dữ liệu",
            "Tách biệt các luồng đọc khỏi các luồng ghi",
            "Tách biệt việc biên dịch mã khỏi việc chạy máy ảo"
        ],
        "correctAnswer": 0,
        "explanation": "Bridge Pattern (Cầu nối) phân tách Abstraction (ví dụ RemoteControl) và Implementation (ví dụ Device: TV, Radio) thành hai cây phân cấp độc lập, kết nối với nhau bằng composition, tránh việc bùng nổ số lượng lớp con (Cartesian product of subclasses).",
        "difficulty": "medium",
        "tags": ["BridgePattern", "StructuralPatterns", "Abstraction"]
    },
    {
        "id": "L6_Q43",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Proxy Pattern được sử dụng trong các tình huống nào sau đây?",
        "code": None,
        "options": [
            "Cung cấp một đối tượng đại diện (Placeholder / Surrogate) để kiểm soát quyền truy cập tới đối tượng thực tế (ví dụ: Virtual Proxy tải ảnh lười, Protection Proxy kiểm tra quyền, Remote Proxy gọi RMI)",
            "Chuyển đổi giao diện không tương thích thành tương thích",
            "Nhân bản đối tượng mẫu nhanh chóng",
            "Đảm bảo duy nhất một đối tượng trong bộ nhớ"
        ],
        "correctAnswer": 0,
        "explanation": "Proxy Pattern cung cấp một đối tượng trung gian đứng trước đối tượng gốc. Client tương tác với Proxy, Proxy kiểm tra quyền (Protection), lazy load khởi tạo đối tượng nặng (Virtual Proxy), ghi log hoặc điều hướng mạng (Remote Proxy) trước khi ủy quyền cho RealSubject.",
        "difficulty": "medium",
        "tags": ["ProxyPattern", "StructuralPatterns", "VirtualProxy"]
    },
    {
        "id": "L6_Q44",
        "lessonId": 6,
        "type": "multiple",
        "title": "So sánh giữa Decorator Pattern và Proxy Pattern, những nhận định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Decorator và Proxy có cấu trúc sơ đồ lớp rất giống nhau (đều bọc đối tượng mục tiêu và cùng thực thi một interface chung)",
            "Decorator tập trung vào việc bổ sung các tính năng/trách nhiệm mới cho đối tượng một cách động",
            "Proxy tập trung vào việc kiểm soát quyền truy cập, quản lý vòng đời hoặc hoãn việc khởi tạo đối tượng mục tiêu",
            "Decorator chỉ có thể bọc đối tượng một lần duy nhất, không thể lồng nhau nhiều lớp"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Sự khác biệt giữa Decorator và Proxy nằm ở Ý ĐỊNH (Intent): Decorator mở rộng hành vi (chuỗi bọc decorator có thể lồng nhau vô hạn); Proxy kiểm soát việc truy cập tới đối tượng (thường tự quản lý hoặc gán cố định RealSubject bên trong).",
        "difficulty": "hard",
        "tags": ["DecoratorVsProxy", "DesignIntent", "Comparison"]
    },
    {
        "id": "L6_Q45",
        "lessonId": 6,
        "type": "single",
        "title": "Xác định output của đoạn mã minh họa Builder Pattern sau:",
        "code": "class Query {\n    private String table;\n    private String where;\n    public static class Builder {\n        private Query q = new Query();\n        public Builder from(String t) { q.table = t; return this; }\n        public Builder where(String w) { q.where = w; return this; }\n        public Query build() { return q; }\n    }\n    public String toString() { return \"SELECT * FROM \" + table + \" WHERE \" + where; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Query q = new Query.Builder().from(\"Users\").where(\"age > 18\").build();\n        System.out.println(q);\n    }\n}",
        "options": [
            "SELECT * FROM Users WHERE age > 18",
            "SELECT * FROM null WHERE null",
            "Lỗi biên dịch do phương thức build() không thể truy cập thuộc tính private",
            "Ném ngoại lệ NullPointerException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Đoạn mã triển khai chuẩn Builder Pattern với phương thức trả về 'this' cho phép gọi hàm liên hoàn (Method Chaining / Fluent API). Khi gọi build(), đối tượng Query hoàn chỉnh được trả về và in ra đúng chuỗi truy vấn.",
        "difficulty": "easy",
        "tags": ["BuilderPattern", "FluentAPI", "Output"]
    },

    # --- ĐỀ 6D (L6_Q46 - L6_Q60): Behavioral Patterns, MVC & SOLID ---
    {
        "id": "L6_Q46",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Observer Pattern định nghĩa mối quan hệ phụ thuộc nào giữa các đối tượng?",
        "code": None,
        "options": [
            "Mối quan hệ Một - Nhiều (One-to-Many): Khi một đối tượng (Subject) thay đổi trạng thái, tất cả các đối tượng phụ thuộc (Observers) của nó đều được thông báo và tự động cập nhật",
            "Mối quan hệ Một - Một (One-to-One) chặt chẽ giữa hai class",
            "Mối quan hệ kế thừa cha - con trong cây phả hệ",
            "Mối quan hệ độc lập hoàn toàn không liên quan đến nhau"
        ],
        "correctAnswer": 0,
        "explanation": "Observer Pattern định nghĩa mối phụ thuộc 1-Nhiều giữa Subject (chủ thể) và các Observer (người quan sát). Khi trạng thái của Subject đổi, nó gọi phương thức notifyObservers() để tự động kích hoạt hàm update() của mọi observer đã đăng ký mà không cần biết chi tiết về từng observer (Loose Coupling).",
        "difficulty": "easy",
        "tags": ["ObserverPattern", "OneToMany", "BehavioralPatterns"]
    },
    {
        "id": "L6_Q47",
        "lessonId": 6,
        "type": "multiple",
        "title": "Trong Observer Pattern, phân biệt giữa mô hình Đẩy (Push Model) và mô hình Kéo (Pull Model):",
        "code": None,
        "options": [
            "Mô hình Đẩy (Push): Subject gửi chi tiết tất cả dữ liệu thay đổi qua các tham số của phương thức update(data) cho Observer, bất kể Observer đó có cần dữ liệu đó hay không",
            "Mô hình Kéo (Pull): Subject chỉ gửi một thông báo tối thiểu (hoặc truyền chính tham chiếu của Subject: update(this)), sau đó Observer tự chủ động gọi getter để lấy đúng phần dữ liệu nó quan tâm",
            "Mô hình Kéo linh hoạt hơn khi các Observer có nhu cầu sử dụng các phần dữ liệu khác nhau",
            "Mô hình Đẩy cấm sử dụng trong các hệ thống phân tán"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 mô tả đúng hai biến thể của Observer: Push gửi thừa dữ liệu nhưng observer không phải query lại; Pull gửi ít dữ liệu hơn và tăng tính độc lập vì observer tự kéo dữ liệu nó cần thông qua getter của Subject.",
        "difficulty": "medium",
        "tags": ["ObserverPattern", "PushVsPull", "DesignDetails"]
    },
    {
        "id": "L6_Q48",
        "lessonId": 6,
        "type": "single",
        "title": "Sự khác biệt căn bản về mục đích thiết kế giữa Strategy Pattern và State Pattern là gì?",
        "code": None,
        "options": [
            "Strategy cho phép Client chủ động lựa chọn và hoán đổi thuật toán từ bên ngoài; State cho phép đối tượng Context tự động thay đổi hành vi khi trạng thái nội bộ của nó thay đổi theo thời gian",
            "Strategy chỉ dùng cho vòng lặp, State chỉ dùng cho switch-case",
            "Strategy dùng đa kế thừa, State dùng đơn kế thừa",
            "Cả hai hoàn toàn đồng nhất không có sự khác biệt nào"
        ],
        "correctAnswer": 0,
        "explanation": "Mặc dù Strategy và State có biểu đồ lớp UML gần như giống hệt nhau (Context chứa tham chiếu tới Strategy/State interface), ý định thiết kế hoàn toàn khác nhau: Trong Strategy, người dùng chủ động cấu hình thuật toán mong muốn (ví dụ thuật toán sắp xếp, thuật toán tính thuế). Trong State, các trạng thái cụ thể tự động chuyển đổi lẫn nhau bên trong Context dựa trên các sự kiện (ví dụ đơn hàng: Mới tạo -> Đã thanh toán -> Đang giao).",
        "difficulty": "hard",
        "tags": ["StrategyVsState", "BehavioralPatterns", "UMLComparison"]
    },
    {
        "id": "L6_Q49",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Decorator Pattern tuân thủ hoàn hảo nguyên lý thiết kế SOLID nào nhất?",
        "code": None,
        "options": [
            "Open/Closed Principle (Mở rộng cho việc mở rộng tính năng mới, nhưng đóng cho việc sửa đổi mã nguồn đã ổn định)",
            "Single Responsibility Principle duy nhất",
            "Liskov Substitution Principle",
            "Interface Segregation Principle"
        ],
        "correctAnswer": 0,
        "explanation": "Decorator Pattern cho phép bổ sung thêm trách nhiệm mới cho đối tượng tại thời điểm runtime bằng cách bọc nó trong các lớp Decorator mới mà không cần chạm vào hay sửa đổi mã nguồn của lớp đối tượng gốc ban đầu, hiện thực hóa hoàn hảo nguyên lý Mở/Đóng (Open/Closed Principle).",
        "difficulty": "medium",
        "tags": ["DecoratorPattern", "OpenClosedPrinciple", "SOLID"]
    },
    {
        "id": "L6_Q50",
        "lessonId": 5,
        "type": "single",
        "title": "Mẫu thiết kế Composite Pattern giải quyết tốt nhất bài toán có cấu trúc dữ liệu dạng nào?",
        "code": None,
        "options": [
            "Cấu trúc dạng Cây (Tree structure) phân cấp Một phần - Toàn thể (Part-Whole), giúp client tương tác với đối tượng đơn lẻ (Leaf) và đối tượng chứa (Composite) một cách đồng nhất",
            "Cấu trúc bảng băm một chiều",
            "Cấu trúc hàng đợi tuyến tính FIFO",
            "Cấu trúc ma trận đồ thị 3 chiều"
        ],
        "correctAnswer": 0,
        "explanation": "Composite Pattern chuyên dùng để biểu diễn các cấu trúc cây (ví dụ cây thư mục File/Directory, cây giao diện UI Component/Container, cây tổ chức công ty Employee/Manager). Cả lá (Leaf) và cành (Composite) đều thực thi chung một Component interface.",
        "difficulty": "easy",
        "tags": ["CompositePattern", "TreeHierarchy", "PartWhole"]
    },
    {
        "id": "L6_Q51",
        "lessonId": 6,
        "type": "multiple",
        "title": "Trong kiến trúc MVC (Model - View - Controller), trách nhiệm của từng thành phần được phân định như thế nào?",
        "code": None,
        "options": [
            "Model: Quản lý toàn bộ dữ liệu, trạng thái và các logic nghiệp vụ (business rules) của ứng dụng; độc lập hoàn toàn với giao diện",
            "View: Chịu trách nhiệm hiển thị giao diện người dùng và trực quan hóa dữ liệu từ Model",
            "Controller: Tiếp nhận tương tác từ người dùng (sự kiện click, gõ phím), xử lý và điều phối cập nhật trạng thái của Model hoặc chọn View thích hợp để hiển thị",
            "View được phép truy cập trực tiếp và thực hiện các câu lệnh SQL vào cơ sở dữ liệu mà không qua Model"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "MVC phân chia rõ ràng: Model quản lý dữ liệu/logic; View chỉ lo hiển thị giao diện; Controller điều phối tiếp nhận input. View tuyệt đối không được truy cập trực tiếp DB (vi phạm tách biệt trách nhiệm).",
        "difficulty": "easy",
        "tags": ["MVC", "Architecture", "SeparationOfConcerns"]
    },
    {
        "id": "L6_Q52",
        "lessonId": 6,
        "type": "single",
        "title": "Nguyên lý Đảo ngược phụ thuộc (Dependency Inversion Principle - chữ D trong SOLID) quy định điều gì?",
        "code": None,
        "options": [
            "Các module cấp cao không nên phụ thuộc vào các module cấp thấp; cả hai nên phụ thuộc vào sự trừu tượng (Abstraction / Interface)",
            "Lớp con bắt buộc phải kế thừa toàn bộ thuộc tính của lớp cha",
            "Mỗi class chỉ nên có duy nhất một lý do để thay đổi",
            "Chỉ được phép sử dụng các interface có dưới 3 phương thức"
        ],
        "correctAnswer": 0,
        "explanation": "DIP (Dependency Inversion Principle) khẳng định: Module cấp cao (logic nghiệp vụ) không được phụ thuộc trực tiếp vào module cấp thấp (như DB cụ thể, thiết bị cụ thể), mà cả hai phải phụ thuộc vào abstraction (interface). Điều này giúp code linh hoạt và dễ kiểm thử với mock.",
        "difficulty": "medium",
        "tags": ["DIP", "SOLID", "Abstraction"]
    },
    {
        "id": "L6_Q53",
        "lessonId": 6,
        "type": "single",
        "title": "Nguyên lý Thay thế Liskov (Liskov Substitution Principle - chữ L trong SOLID) bị vi phạm trong trường hợp kinh điển nào sau đây?",
        "code": None,
        "options": [
            "Lớp Hình vuông (Square) kế thừa từ lớp Hình chữ nhật (Rectangle) và phương thức setWidth(w) của Square tự động sửa cả height làm sai lệch hành vi kỳ vọng của Rectangle",
            "Lớp Chó kế thừa từ lớp Động vật",
            "Lớp ArrayList kế thừa từ AbstractList",
            "Lớp String kế thừa từ Object"
        ],
        "correctAnswer": 0,
        "explanation": "Ví dụ kinh điển về vi phạm LSP: Trong hình học, hình vuông là hình chữ nhật. Nhưng trong OOP, nếu Square kế thừa Rectangle, khi người dùng gọi rect.setWidth(5); rect.setHeight(4); với Square thì diện tích bị biến thành 16 thay vì 20, phá vỡ hợp đồng hành vi của Rectangle.",
        "difficulty": "medium",
        "tags": ["LSP", "SOLID", "SquareRectangleProblem"]
    },
    {
        "id": "L6_Q54",
        "lessonId": 6,
        "type": "multiple",
        "title": "Những mẫu thiết kế nào sau đây thuộc nhóm Mẫu hành vi (Behavioral Patterns) theo phân loại của GoF (Gang of Four)?",
        "code": None,
        "options": [
            "Observer",
            "Strategy",
            "Command",
            "Singleton"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Observer, Strategy và Command đều là Behavioral Patterns (quản lý thuật toán và sự phân công trách nhiệm giữa các đối tượng). Singleton là Creational Pattern (khởi tạo).",
        "difficulty": "easy",
        "tags": ["BehavioralPatterns", "GoF", "Classification"]
    },
    {
        "id": "L6_Q55",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Command Pattern đóng gói cái gì thành một đối tượng độc lập?",
        "code": None,
        "options": [
            "Đóng gói toàn bộ một yêu cầu hành động (Request / Action) thành một đối tượng độc lập chứa đầy đủ thông tin để thực thi, cho phép hỗ trợ tính năng Undo/Redo, hàng đợi lệnh và ghi nhật ký (logging)",
            "Đóng gói toàn bộ cơ sở dữ liệu thành một file duy nhất",
            "Đóng gói giao diện người dùng thành mã nhị phân",
            "Đóng gói thuật toán mã hóa mật khẩu"
        ],
        "correctAnswer": 0,
        "explanation": "Command Pattern đóng gói một request thành một object độc lập (với phương thức execute() và undo()). Điều này cho phép tham số hóa các client với các request khác nhau, xếp hàng đợi thực thi, hỗ trợ hoàn tác (Undo/Redo) trong các phần mềm soạn thảo.",
        "difficulty": "medium",
        "tags": ["CommandPattern", "UndoRedo", "BehavioralPatterns"]
    },
    {
        "id": "L6_Q56",
        "lessonId": 6,
        "type": "single",
        "title": "Mẫu thiết kế Template Method Pattern sử dụng cơ chế nào để định nghĩa khung sườn (skeleton) của một thuật toán?",
        "code": None,
        "options": [
            "Định nghĩa cấu trúc các bước của thuật toán trong một phương thức 'final' ở lớp cha, và trì hoãn việc cài đặt cụ thể một số bước cho các lớp con thông qua các phương thức trừu tượng (abstract methods)",
            "Dùng con trỏ hàm trong ngôn ngữ C",
            "Tự động sinh mã nguồn bằng trình thông dịch",
            "Sử dụng biến static để lưu trữ kết quả"
        ],
        "correctAnswer": 0,
        "explanation": "Template Method nằm ở lớp cha (thường là abstract class), chứa phương thức khung (thường là final để cấm con sửa thứ tự các bước). Các bước con được khai báo abstract hoặc hook method để các lớp con tự do cài đặt chi tiết mà không làm thay đổi cấu trúc thuật toán chung.",
        "difficulty": "medium",
        "tags": ["TemplateMethod", "Inheritance", "BehavioralPatterns"]
    },
    {
        "id": "L6_Q57",
        "lessonId": 6,
        "type": "multiple",
        "title": "Nguyên lý Phân tách Giao diện (Interface Segregation Principle - chữ I trong SOLID) khuyên lập trình viên điều gì?",
        "code": None,
        "options": [
            "Không nên ép buộc một client phải phụ thuộc vào các phương thức trong interface mà nó không sử dụng",
            "Nên chia nhỏ một interface 'béo' (Fat interface) có quá nhiều phương thức thành nhiều interface nhỏ hơn, tập trung vào các vai trò cụ thể (Role-based interfaces)",
            "Mỗi interface chỉ nên phục vụ một mục đích chuyên biệt cho một nhóm client cụ thể",
            "Bắt buộc tất cả các phương thức trong interface phải được viết code cài đặt sẵn"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "ISP khuyên: thà có nhiều interface nhỏ chuyên biệt còn hơn một interface khổng lồ chứa hàng chục phương thức buộc các lớp implement phải viết thân hàm rỗng cho những phương thức nó không cần dùng.",
        "difficulty": "medium",
        "tags": ["ISP", "SOLID", "InterfaceDesign"]
    },
    {
        "id": "L6_Q58",
        "lessonId": 6,
        "type": "single",
        "title": "Đoạn mã sau áp dụng mẫu thiết kế nào?",
        "code": "interface PaymentStrategy {\n    void pay(int amount);\n}\nclass CreditCardPayment implements PaymentStrategy {\n    public void pay(int amount) { System.out.println(\"Card: \" + amount); }\n}\nclass PaypalPayment implements PaymentStrategy {\n    public void pay(int amount) { System.out.println(\"Paypal: \" + amount); }\n}\nclass ShoppingCart {\n    private PaymentStrategy strategy;\n    public void setPaymentStrategy(PaymentStrategy s) { this.strategy = s; }\n    public void checkout(int amount) { strategy.pay(amount); }\n}",
        "options": [
            "Strategy Pattern",
            "State Pattern",
            "Decorator Pattern",
            "Singleton Pattern"
        ],
        "correctAnswer": 0,
        "explanation": "Đây là ví dụ kinh điển về Strategy Pattern: định nghĩa một họ các thuật toán thanh toán (CreditCard, Paypal), đóng gói từng thuật toán và cho phép hoán đổi linh hoạt bên trong ShoppingCart tại thời điểm chạy.",
        "difficulty": "easy",
        "tags": ["StrategyPattern", "PaymentExample", "BehavioralPatterns"]
    },
    {
        "id": "L6_Q59",
        "lessonId": 6,
        "type": "single",
        "title": "Xem xét đoạn mã bọc luồng Decorator sau. Kết quả in ra là gì?",
        "code": "interface Text {\n    String getContent();\n}\nclass SimpleText implements Text {\n    public String getContent() { return \"Hello\"; }\n}\nclass BoldDecorator implements Text {\n    private Text text;\n    BoldDecorator(Text t) { this.text = t; }\n    public String getContent() { return \"<b>\" + text.getContent() + \"</b>\"; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Text t = new BoldDecorator(new SimpleText());\n        System.out.println(t.getContent());\n    }\n}",
        "options": [
            "<b>Hello</b>",
            "Hello",
            "<b></b>",
            "Lỗi biên dịch"
        ],
        "correctAnswer": 0,
        "explanation": "BoldDecorator bọc lấy SimpleText. Khi gọi t.getContent(), BoldDecorator lấy nội dung từ SimpleText (\"Hello\") và bổ sung thêm thẻ <b>...</b> xung quanh, in ra kết quả '<b>Hello</b>'.",
        "difficulty": "easy",
        "tags": ["DecoratorPattern", "CodeSnippet", "Output"]
    },
    {
        "id": "L6_Q60",
        "lessonId": 6,
        "type": "single",
        "title": "Nguyên lý Đơn trách nhiệm (Single Responsibility Principle - chữ S trong SOLID) định nghĩa tiêu chuẩn gì cho một lớp?",
        "code": None,
        "options": [
            "Một lớp chỉ nên có một và chỉ một lý do duy nhất để thay đổi (A class should have only one reason to change)",
            "Một lớp chỉ được phép có duy nhất một phương thức public",
            "Một lớp chỉ được phép có duy nhất một thuộc tính",
            "Mỗi project chỉ được phép có một lập trình viên duy nhất chịu trách nhiệm"
        ],
        "correctAnswer": 0,
        "explanation": "SRP định nghĩa rằng một lớp chỉ nên đảm nhận một trách nhiệm duy nhất trong hệ thống và chỉ có một tác nhân (actor) hoặc một lý do duy nhất khiến nó phải thay đổi. Tách riêng logic tính toán, logic hiển thị và logic lưu trữ DB vào các lớp khác nhau là ví dụ chuẩn của SRP.",
        "difficulty": "easy",
        "tags": ["SRP", "SOLID", "ClassDesign"]
    }
]

L7_NEW = [
    # --- ĐỀ 7C (L7_Q31 - L7_Q45): Advanced Synchronization, Monitor Lock & Volatile ---
    {
        "id": "L7_Q31",
        "lessonId": 7,
        "type": "single",
        "title": "Trong Java, cơ chế Monitor Lock (Intrinsic Lock / Khóa nội tại) được gắn liền với đối tượng nào?",
        "code": None,
        "options": [
            "MỌI đối tượng (Object) trong Java đều sở hữu một Monitor Lock ngầm định do JVM quản lý",
            "Chỉ các lớp kế thừa từ java.lang.Thread mới có Monitor Lock",
            "Chỉ các đối tượng được khai báo với từ khóa 'volatile' mới có Monitor Lock",
            "Monitor Lock chỉ tồn tại ở hệ điều hành và gắn với thanh ghi CPU"
        ],
        "correctAnswer": 0,
        "explanation": "Trong Java, mọi đối tượng (bất kỳ instance nào của java.lang.Object) đều có một header chứa thông tin Mark Word của JVM, trong đó tích hợp sẵn một Monitor Lock ngầm định. Từ khóa 'synchronized' sử dụng chính khóa nội tại này.",
        "difficulty": "medium",
        "tags": ["MonitorLock", "IntrinsicLock", "JVMInternals"]
    },
    {
        "id": "L7_Q32",
        "lessonId": 7,
        "type": "single",
        "title": "Phân biệt đối tượng bị khóa khi sử dụng 'synchronized' trên phương thức instance vs phương thức static:",
        "code": "class Counter {\n    public synchronized void incInstance() { ... } // (1)\n    public static synchronized void incStatic() { ... } // (2)\n}",
        "options": [
            "(1) khóa trên chính thể hiện hiện tại (this); (2) khóa trên đối tượng Class (Counter.class) trong Metaspace",
            "(1) và (2) cùng khóa chung trên một đối tượng duy nhất",
            "(1) khóa trên CPU, (2) khóa trên RAM",
            "(1) khóa trên luồng cha, (2) khóa trên luồng con"
        ],
        "correctAnswer": 0,
        "explanation": "Phương thức instance synchronized lấy khóa trên chính thể hiện 'this' (đối tượng cụ thể gọi hàm). Phương thức static synchronized lấy khóa trên đối tượng Class đại diện cho lớp đó (Counter.class). Do đó một luồng gọi incInstance() và một luồng gọi incStatic() trên cùng một instance sẽ KHÔNG chặn lẫn nhau vì chúng giữ 2 lock khác nhau hoàn toàn.",
        "difficulty": "hard",
        "tags": ["Synchronized", "InstanceLockVsClassLock", "Concurrency"]
    },
    {
        "id": "L7_Q33",
        "lessonId": 7,
        "type": "single",
        "title": "Tại sao việc gọi phương thức wait(), notify(), hoặc notifyAll() BẮT BUỘC phải nằm bên trong một khối 'synchronized' đang giữ lock của đối tượng đó?",
        "code": None,
        "options": [
            "Nếu gọi bên ngoài khối synchronized, JVM sẽ ném ngay ngoại lệ java.lang.IllegalMonitorStateException tại thời điểm runtime để ngăn chặn điều kiện tương tranh (Race Condition) trong việc kiểm tra điều kiện chờ",
            "Để trình biên dịch không báo lỗi cú pháp Compile-time",
            "Để phương thức wait() có thể chạy nhanh gấp 2 lần",
            "Để luồng không bao giờ bị rơi vào trạng thái ngủ"
        ],
        "correctAnswer": 0,
        "explanation": "Gọi wait()/notify() đòi hỏi luồng phải là chủ sở hữu monitor của đối tượng (đang trong synchronized(obj)). Nếu không nắm giữ monitor, JVM sẽ ném IllegalMonitorStateException ngay lập tức. Điều này nhằm ngăn chặn lỗi Lost Wakeup: luồng A kiểm tra điều kiện, chưa kịp wait() thì luồng B notify(), sau đó luồng A mới wait() và ngủ vĩnh viễn.",
        "difficulty": "medium",
        "tags": ["IllegalMonitorStateException", "WaitNotify", "Synchronization"]
    },
    {
        "id": "L7_Q34",
        "lessonId": 7,
        "type": "single",
        "title": "Tại sao theo chuẩn Java, phương thức wait() LUÔN PHẢI được đặt trong vòng lặp 'while' (while (condition)) thay vì câu lệnh 'if' (if (condition))?",
        "code": "// Chuan Java:\nwhile (!condition) {\n    obj.wait();\n}",
        "options": [
            "Để phòng chống hiện tượng 'Thức giấc giả tạo' (Spurious Wakeup) và đảm bảo điều kiện vẫn thực sự thỏa mãn sau khi luồng thức dậy trước khi tiếp tục thực thi",
            "Vì cú pháp Java cấm sử dụng if với wait()",
            "Để tăng tốc độ giải phóng khóa cho CPU",
            "Để tự động chuyển đổi sang Thread Pool"
        ],
        "correctAnswer": 0,
        "explanation": "Hệ điều hành và JVM có thể làm một luồng thức dậy mà không có bất kỳ lời gọi notify() nào (hiện tượng Spurious Wakeup). Ngoài ra, khi notifyAll(), nhiều luồng cùng thức dậy nhưng chỉ 1 luồng xử lý dữ liệu trước, khi luồng sau được cấp lock thì điều kiện có thể đã không còn thỏa mãn nữa. Đặt trong 'while' bảo đảm luồng luôn kiểm tra lại điều kiện sau khi thức dậy.",
        "difficulty": "hard",
        "tags": ["SpuriousWakeup", "WhileWaitPattern", "BestPractice"]
    },
    {
        "id": "L7_Q35",
        "lessonId": 7,
        "type": "single",
        "title": "Sự khác biệt then chốt giữa Thread.sleep(millis) và object.wait(millis) là gì?",
        "code": None,
        "options": [
            "Thread.sleep() tạm dừng luồng nhưng KHÔNG nhả Monitor Lock (vẫn tiếp tục giữ khóa); còn object.wait() tạm dừng luồng và NHẢ Monitor Lock để các luồng khác có cơ hội nhảy vào xử lý",
            "Thread.sleep() nhả lock, object.wait() giữ lock",
            "Cả hai đều nhả lock như nhau",
            "Thread.sleep() chỉ dùng trong static method, object.wait() chỉ dùng trong constructor"
        ],
        "correctAnswer": 0,
        "explanation": "Khác biệt kinh điển: 'sleep() sleeps with its locks; wait() gives up its lock'. Thread.sleep() giữ nguyên tất cả các lock nó đang cầm. Ngược lại, object.wait() nhả monitor lock của object đó ra và đi vào hàng đợi chờ (Wait Set).",
        "difficulty": "medium",
        "tags": ["SleepVsWait", "LockHandling", "Concurrency"]
    },
    {
        "id": "L7_Q36",
        "lessonId": 7,
        "type": "single",
        "title": "Tại sao trong đoạn mã đa luồng sau, biến 'count' dù được khai báo là 'volatile' nhưng giá trị cuối cùng vẫn KHÔNG ĐẠT 2000?",
        "code": "class Counter {\n    volatile int count = 0;\n    void increment() { count++; }\n}\n// 2 luong chay song song, moi luong goi increment() 1000 lan",
        "options": [
            "Vì toán tử 'count++' không phải là một thao tác nguyên tử (Atomic); nó gồm 3 bước riêng biệt (Đọc -> Tăng -> Ghi), từ khóa volatile chỉ đảm bảo tính khả kiến (Visibility) chứ không đảm bảo tính nguyên tử (Atomicity)",
            "Vì volatile làm biến count bị khóa vĩnh viễn",
            "Vì biến count bị tràn số nguyên",
            "Do trình biên dịch Java tự động tối ưu bỏ qua từ khóa volatile"
        ],
        "correctAnswer": 0,
        "explanation": "Toán tử count++ bản chất là: 1. Đọc count từ bộ nhớ vào thanh ghi, 2. Cộng 1 vào thanh ghi, 3. Ghi giá trị mới vào bộ nhớ. Nếu 2 luồng cùng đọc giá trị 5 cùng lúc, cả 2 cùng tăng lên 6 và cùng ghi đè 6, dẫn đến mất 1 lần tăng (Lost Update). Từ khóa volatile không có cơ chế khóa (locking) nên không đảm bảo tính nguyên tử.",
        "difficulty": "hard",
        "tags": ["VolatileTrap", "Atomicity", "RaceCondition"]
    },
    {
        "id": "L7_Q37",
        "lessonId": 7,
        "type": "multiple",
        "title": "Từ khóa 'volatile' trong Java mang lại những đảm bảo kỹ thuật nào sau đây theo Mô hình bộ nhớ Java (JMM)?",
        "code": None,
        "options": [
            "Tính khả kiến trong bộ nhớ (Memory Visibility): Mọi thao tác ghi vào biến volatile được đẩy ngay lập tức về bộ nhớ chính (Main Memory), và mọi thao tác đọc luôn đọc trực tiếp từ bộ nhớ chính (bỏ qua cache riêng của CPU)",
            "Ngăn chặn việc tái sắp xếp lệnh (Instruction Reordering / Memory Barrier): Trình biên dịch và CPU không được phép đảo thứ tự các lệnh đọc/ghi xung quanh biến volatile",
            "Đảm bảo tính nguyên tử (Atomicity) cho các biểu thức phức tạp như count = count + 1",
            "Đảm bảo an toàn tuyệt đối khi nhiều luồng cùng ghi đè dữ liệu mà không cần synchronized"
        ],
        "correctAnswer": [0, 1],
        "explanation": "volatile trong Java Memory Model (JMM) cung cấp đúng 2 sự bảo đảm: 1. Visibility (đọc/ghi thông qua Main Memory), 2. Happens-Before ordering (Memory Barrier chống reordering). Nó KHÔNG đảm bảo Atomicity cho các thao tác phức tạp.",
        "difficulty": "medium",
        "tags": ["Volatile", "JMM", "MemoryVisibility"]
    },
    {
        "id": "L7_Q38",
        "lessonId": 7,
        "type": "single",
        "title": "Tại sao phương thức notifyAll() thường được khuyến nghị sử dụng thay vì notify() trong hầu hết các ứng dụng đa luồng thực tế?",
        "code": None,
        "options": [
            "notify() chỉ đánh thức ngẫu nhiên một luồng duy nhất trong hàng đợi chờ; nếu luồng đó thức dậy nhưng không thỏa mãn điều kiện tiếp tục chạy thì cả hệ thống có nguy cơ bị treo vĩnh viễn (Lost Signal)",
            "notifyAll() chạy nhanh gấp 10 lần notify()",
            "notify() đã bị đánh dấu @Deprecated từ Java 8",
            "notifyAll() cho phép các luồng chạy không cần CPU"
        ],
        "correctAnswer": 0,
        "explanation": "notify() chỉ đánh thức 1 luồng ngẫu nhiên. Nếu có nhiều luồng chờ các điều kiện khác nhau, việc đánh thức sai luồng có thể dẫn đến việc luồng đó kiểm tra lại thấy chưa đủ điều kiện và tiếp tục ngủ, trong khi luồng cần thức thực sự lại không được đánh thức, làm toàn bộ chương trình bị tắc nghẽn (Lost Notification). notifyAll() đánh thức tất cả để từng luồng tự kiểm tra điều kiện của mình.",
        "difficulty": "medium",
        "tags": ["NotifyAll", "NotifyVsNotifyAll", "LostNotification"]
    },
    {
        "id": "L7_Q39",
        "lessonId": 7,
        "type": "single",
        "title": "Khái niệm 'Khóa tái nhập' (Reentrant Synchronization) trong Java có nghĩa là gì?",
        "code": "class Test {\n    public synchronized void m1() {\n        m2(); // Goi method synchronized khac cung class\n    }\n    public synchronized void m2() {}\n}",
        "options": [
            "Nếu một luồng đã nắm giữ Monitor Lock của một đối tượng, nó có thể tự do đi vào các khối/phương thức synchronized khác của cùng đối tượng đó mà không bị tự chặn chính mình (khóa có bộ đếm hold count)",
            "Khóa tự động mở sau 5 giây nếu luồng bị treo",
            "Khóa có thể được chuyển nhượng cho một tiến trình khác của hệ điều hành",
            "Khóa chỉ có thể dùng được một lần duy nhất rồi tự hủy"
        ],
        "correctAnswer": 0,
        "explanation": "Cả synchronized và ReentrantLock trong Java đều là Reentrant (tái nhập): Khi luồng đã có lock, nó được phép đi vào các phương thức synchronized khác cùng lock đó. JVM tăng biến đếm số lần vào (hold count). Khi thoát ra khỏi mỗi khối synchronized, biến đếm giảm 1. Khi đếm về 0, lock mới thực sự được giải phóng.",
        "difficulty": "medium",
        "tags": ["ReentrantLock", "HoldCount", "Synchronization"]
    },
    {
        "id": "L7_Q40",
        "lessonId": 7,
        "type": "multiple",
        "title": "Những trường hợp nào sau đây khiến một Thread trong Java chuyển từ trạng thái RUNNABLE sang BLOCKED hoặc WAITING?",
        "code": None,
        "options": [
            "Cố gắng bước vào một khối hoặc phương thức 'synchronized' mà khóa monitor đang bị một luồng khác chiếm giữ (chuyển sang BLOCKED)",
            "Gọi phương thức object.wait() (chuyển sang WAITING hoặc TIMED_WAITING)",
            "Gọi phương thức otherThread.join() (chuyển sang WAITING hoặc TIMED_WAITING)",
            "Gọi phương thức Thread.yield()"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1 chuyển sang BLOCKED (chờ monitor lock). 2 và 3 chuyển sang WAITING/TIMED_WAITING. 4 sai: Thread.yield() chỉ gợi ý nhường CPU và luồng vẫn nằm ở trạng thái RUNNABLE.",
        "difficulty": "hard",
        "tags": ["ThreadStates", "Blocked", "Waiting"]
    },
    {
        "id": "L7_Q41",
        "lessonId": 7,
        "type": "single",
        "title": "Phương thức Thread.interrupt() có tác dụng thực tế gì đối với một luồng đang chạy?",
        "code": None,
        "options": [
            "Chỉ thiết lập cờ ngắt (Interrupt Flag = true) của luồng; nếu luồng đang trong trạng thái sleep(), wait() hoặc join(), nó sẽ thức dậy ngay lập tức và ném java.lang.InterruptedException",
            "Dừng và hủy luồng ngay lập tức tương tự như Thread.stop()",
            "Khởi động lại luồng từ đầu phương thức run()",
            "Tự động tăng độ ưu tiên priority của luồng lên tối đa"
        ],
        "correctAnswer": 0,
        "explanation": "Thread.interrupt() là cơ chế dừng luồng cộng tác (Cooperative cancellation): nó chỉ đặt cờ interrupt flag. Luồng đang chạy bình thường phải tự chủ động kiểm tra Thread.currentThread().isInterrupted() để thoát gọn gàng. Nếu luồng đang bị chặn ở sleep(), wait(), join(), JVM sẽ đánh thức luồng và ném InterruptedException.",
        "difficulty": "medium",
        "tags": ["ThreadInterrupt", "InterruptedException", "ThreadLifecycle"]
    },
    {
        "id": "L7_Q42",
        "lessonId": 7,
        "type": "single",
        "title": "Tại sao các phương thức cổ xưa như Thread.stop(), Thread.suspend(), Thread.resume() đều bị Java đánh dấu @Deprecated và cấm sử dụng?",
        "code": None,
        "options": [
            "Vì chúng dừng/đóng băng luồng một cách thô bạo mà không giải phóng các Monitor Lock đang giữ, dễ dẫn đến việc làm hỏng trạng thái dữ liệu (Inconsistent state) và gây Deadlock toàn hệ thống",
            "Vì chúng tốn quá nhiều dung lượng RAM",
            "Vì chúng chỉ chạy được trên hệ điều hành Linux 32-bit",
            "Vì Java muốn lập trình viên tự tạo luồng bằng tay"
        ],
        "correctAnswer": 0,
        "explanation": "Thread.stop() giải phóng mọi lock đột ngột làm đối tượng ở trạng thái dở dang (ví dụ tiền bị trừ ở tài khoản A nhưng chưa kịp cộng vào B). Thread.suspend() đóng băng luồng nhưng KHÔNG nhả lock, bất kỳ luồng nào chờ lock đó sẽ bị Deadlock vĩnh viễn.",
        "difficulty": "easy",
        "tags": ["DeprecatedMethods", "ThreadSafety", "DeadlockRisk"]
    },
    {
        "id": "L7_Q43",
        "lessonId": 7,
        "type": "multiple",
        "title": "Những khẳng định nào sau đây về Luồng ngầm (Daemon Thread) trong Java là ĐÚNG?",
        "code": None,
        "options": [
            "JVM sẽ tự động thoát và kết thúc toàn bộ chương trình khi tất cả các luồng người dùng (User Threads / Non-daemon threads) đều đã kết thúc thực thi, bất kể vẫn còn các Daemon Thread đang chạy",
            "Bộ dọn rác Garbage Collector của Java chạy dưới dạng một Daemon Thread trong nền",
            "Phải gọi phương thức thread.setDaemon(true) TRƯỚC KHI gọi thread.start(), nếu gọi sau khi luồng đã chạy sẽ ném IllegalThreadStateException",
            "Daemon Thread có mức độ ưu tiên CPU cao hơn User Thread"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 đều chính xác: Daemon thread là luồng phục vụ nền, JVM không đợi nó hoàn thành. Gọi setDaemon(true) sau khi start() ném IllegalThreadStateException. Daemon thread không liên quan đến độ ưu tiên CPU.",
        "difficulty": "medium",
        "tags": ["DaemonThread", "ThreadLifecycle", "JVMExit"]
    },
    {
        "id": "L7_Q44",
        "lessonId": 7,
        "type": "single",
        "title": "Xác định output của đoạn mã sau với biến ThreadLocal:",
        "code": "public class ThreadLocalTest {\n    static ThreadLocal<Integer> tl = ThreadLocal.withInitial(() -> 100);\n    public static void main(String[] args) throws Exception {\n        Thread t = new Thread(() -> {\n            tl.set(200);\n            System.out.print(\"T:\" + tl.get() + \" \");\n        });\n        t.start();\n        t.join();\n        System.out.println(\"M:\" + tl.get());\n    }\n}",
        "options": [
            "T:200 M:100",
            "T:200 M:200",
            "T:100 M:100",
            "Lỗi biên dịch"
        ],
        "correctAnswer": 0,
        "explanation": "ThreadLocal cung cấp bản sao biến riêng biệt độc lập cho MỖI luồng. Luồng phụ 't' ghi giá trị 200 vào bản sao của nó (in ra T:200). Luồng main có bản sao độc lập của riêng nó với giá trị khởi tạo là 100 (in ra M:100), hoàn toàn không bị ảnh hưởng bởi luồng phụ.",
        "difficulty": "medium",
        "tags": ["ThreadLocal", "ThreadIsolation", "Output"]
    },
    {
        "id": "L7_Q45",
        "lessonId": 7,
        "type": "single",
        "title": "Xem xét đoạn mã sau với từ khóa synchronized trên String literal. Rủi ro tiềm ẩn lớn nhất là gì?",
        "code": "void doWork() {\n    String lock = \"MY_LOCK\";\n    synchronized (lock) {\n        // Xu ly\n    }\n}",
        "options": [
            "Vì String literal được lưu trong String Constant Pool dùng chung cho toàn bộ JVM, bất kỳ đoạn mã nào khác ở bất kỳ thư viện nào khóa trên chuỗi \"MY_LOCK\" cũng sẽ vô tình chia sẻ chung một khóa, dễ dẫn đến Deadlock bất ngờ hoặc nghẽn luồng nghiêm trọng",
            "Mã bị lỗi biên dịch vì synchronized không chấp nhận đối tượng String",
            "Khối synchronized trên String tự động bị vô hiệu hóa khi chạy",
            "Ném ngoại lệ NullPointerException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "String literals được tái sử dụng trong String Pool. Khóa trên một chuỗi literal có nghĩa là bạn đang khóa trên một đối tượng toàn cục duy nhất của toàn bộ ứng dụng. Nếu hai module không liên quan cùng tình cờ synchronized(\"MY_LOCK\"), chúng sẽ khóa chặn lẫn nhau. Best practice là luôn dùng 'private final Object lock = new Object();'.",
        "difficulty": "hard",
        "tags": ["StringLockTrap", "SynchronizationBestPractice", "Deadlock"]
    },

    # --- ĐỀ 7D (L7_Q46 - L7_Q60): Deadlock, ReentrantLock, ExecutorService & Concurrency Utilities ---
    {
        "id": "L7_Q46",
        "lessonId": 7,
        "type": "multiple",
        "title": "Theo lý thuyết hệ điều hành (Coffman Conditions), Bế tắc (Deadlock) giữa các luồng chỉ có thể xảy ra khi thỏa mãn ĐỒNG THỜI cả 4 điều kiện nào sau đây?",
        "code": None,
        "options": [
            "Loại trừ lẫn nhau (Mutual Exclusion): Tài nguyên/Khóa chỉ có thể được sở hữu bởi duy nhất một luồng tại một thời điểm",
            "Nắm giữ và chờ đợi (Hold and Wait): Một luồng đang nắm giữ một tài nguyên lại tiếp tục yêu cầu thêm tài nguyên mới đang bị giữ bởi luồng khác",
            "Không thể chiếm đoạt (No Preemption): Tài nguyên không thể bị tước đoạt cưỡng bức từ luồng đang sở hữu nó",
            "Chờ đợi vòng tròn (Circular Wait): Tồn tại một chuỗi các luồng T1 -> T2 -> ... -> Tn -> T1 trong đó mỗi luồng đang chờ tài nguyên do luồng kế tiếp nắm giữ"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Đây là 4 điều kiện kinh điển của Coffman. Chỉ cần phá vỡ ĐÚNG MỘT trong bốn điều kiện này (thường là Circular Wait bằng kỹ thuật Lock Ordering) là có thể triệt tiêu hoàn toàn khả năng xảy ra Deadlock.",
        "difficulty": "medium",
        "tags": ["Deadlock", "CoffmanConditions", "OSTheory"]
    },
    {
        "id": "L7_Q47",
        "lessonId": 7,
        "type": "single",
        "title": "Kỹ thuật hiệu quả và phổ biến nhất để phòng chống Deadlock do Chờ đợi vòng tròn (Circular Wait) trong ứng dụng Java là gì?",
        "code": None,
        "options": [
            "Sắp xếp thứ tự lấy khóa cố định (Lock Ordering / Resource Hierarchy): Đảm bảo tất cả các luồng trong toàn bộ hệ thống luôn chiếm dụng các khóa theo cùng một thứ tự toàn cục duy nhất",
            "Tăng số lượng luồng trong hệ thống lên gấp 10 lần",
            "Sử dụng từ khóa volatile cho tất cả các biến",
            "Chỉ chạy chương trình trên máy tính có 1 CPU duy nhất"
        ],
        "correctAnswer": 0,
        "explanation": "Kỹ thuật Lock Ordering bảo đảm nếu cần 2 lock A và B, mọi luồng đều BẮT BUỘC phải lấy A trước rồi mới lấy B (ví dụ sắp xếp theo hash code hoặc ID). Không bao giờ có chuyện luồng 1 giữ A chờ B trong khi luồng 2 giữ B chờ A, triệt tiêu hoàn toàn điều kiện Circular Wait.",
        "difficulty": "easy",
        "tags": ["LockOrdering", "DeadlockPrevention", "BestPractice"]
    },
    {
        "id": "L7_Q48",
        "lessonId": 7,
        "type": "multiple",
        "title": "Khóa ReentrantLock (gói java.util.concurrent.locks) cung cấp những tính năng vượt trội nào so với từ khóa 'synchronized' truyền thống?",
        "code": None,
        "options": [
            "Hỗ trợ phương thức tryLock(timeout, unit): cho phép thử lấy khóa trong một khoảng thời gian nhất định, nếu không lấy được thì từ bỏ thay vì bị chặn vĩnh viễn (giúp tránh Deadlock)",
            "Hỗ trợ khóa công bằng (Fair Lock): hàng đợi cấp phát khóa theo thứ tự FIFO cho luồng chờ lâu nhất",
            "Hỗ trợ phương thức lockInterruptibly(): cho phép luồng đang chờ khóa có thể bị đánh thức bởi interrupt()",
            "Không bao giờ cần phải gọi phương thức unlock() trong khối finally"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 là các ưu điểm lớn của ReentrantLock. Ý 4 sai: Với ReentrantLock, BẮT BUỘC lập trình viên phải tự gọi lock.unlock() bên trong khối finally, nếu quên sẽ dẫn đến lock không bao giờ được giải phóng.",
        "difficulty": "medium",
        "tags": ["ReentrantLock", "TryLock", "FairLock"]
    },
    {
        "id": "L7_Q49",
        "lessonId": 7,
        "type": "multiple",
        "title": "So sánh giữa Callable<V> và Runnable trong Java Concurrency, những khẳng định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Phương thức call() của Callable có kiểu trả về generic V; phương thức run() của Runnable có kiểu trả về là void",
            "Phương thức call() của Callable có thể khai báo ném ra Checked Exception (throws Exception); phương thức run() của Runnable không được ném checked exception",
            "Cả Callable và Runnable đều là Functional Interface",
            "Callable có thể được truyền trực tiếp vào constructor của lớp java.lang.Thread(callable).start()"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 đúng: Callable có return type và ném exception. Ý 4 sai: Thread không có constructor nhận trực tiếp Callable (phải bọc qua FutureTask: new Thread(new FutureTask<>(callable)).start() hoặc submit vào ExecutorService).",
        "difficulty": "medium",
        "tags": ["CallableVsRunnable", "FunctionalInterface", "FutureTask"]
    },
    {
        "id": "L7_Q50",
        "lessonId": 7,
        "type": "single",
        "title": "Khi gọi phương thức future.get() trên đối tượng Future<V>, hành vi nào diễn ra?",
        "code": "ExecutorService pool = Executors.newSingleThreadExecutor();\nFuture<String> f = pool.submit(() -> {\n    Thread.sleep(2000);\n    return \"Done\";\n});\nString res = f.get(); // DONG NAY",
        "options": [
            "Phương thức get() là một lời gọi chặn (Blocking Call): luồng gọi get() sẽ bị tạm dừng cho đến khi tác vụ nền hoàn thành và trả về kết quả",
            "Phương thức get() ngay lập tức trả về null nếu tác vụ chưa chạy xong",
            "Chương trình ném ngoại lệ TimeoutException ngay lập tức",
            "Phương thức get() hủy bỏ tác vụ đang chạy"
        ],
        "correctAnswer": 0,
        "explanation": "future.get() là blocking call. Luồng gọi nó sẽ bị chặn (chuyển sang WAITING) cho đến khi tác vụ nền chạy xong và trả về kết quả (hoặc ném ExecutionException nếu task lỗi). Muốn tránh chờ vĩnh viễn, nên dùng future.get(timeout, unit).",
        "difficulty": "easy",
        "tags": ["FutureGet", "BlockingCall", "Concurrency"]
    },
    {
        "id": "L7_Q51",
        "lessonId": 7,
        "type": "single",
        "title": "Điều gì xảy ra nếu bạn gọi phương thức f.get() HAI LẦN liên tiếp trên cùng một đối tượng Future?",
        "code": "Future<Integer> f = pool.submit(() -> 42);\nSystem.out.println(f.get());\nSystem.out.println(f.get());",
        "options": [
            "Lần gọi thứ hai trả về ngay lập tức giá trị kết quả đã được lưu trong bộ đệm (cached result) mà không chạy lại tác vụ",
            "Lần gọi thứ hai chạy lại tác vụ từ đầu và tính toán lại",
            "Ném ngoại lệ IllegalStateException ở lần gọi thứ hai",
            "Lần gọi thứ hai trả về null"
        ],
        "correctAnswer": 0,
        "explanation": "Future lưu trữ kết quả của tác vụ sau khi hoàn thành. Lần gọi get() đầu tiên có thể phải chờ task chạy, nhưng các lần gọi get() tiếp theo sẽ lấy trực tiếp kết quả đã lưu trong bộ nhớ đệm ngay tức thì mà không cần chờ đợi hay chạy lại task.",
        "difficulty": "medium",
        "tags": ["Future", "CachedResult", "SampleExamTopic"]
    },
    {
        "id": "L7_Q52",
        "lessonId": 7,
        "type": "single",
        "title": "Sự khác biệt giữa shutdown() và shutdownNow() của ExecutorService là gì?",
        "code": None,
        "options": [
            "shutdown() từ chối nhận thêm tác vụ mới nhưng tiếp tục chạy nốt các tác vụ đang chờ trong hàng đợi; shutdownNow() cố gắng ngắt (interrupt) các tác vụ đang chạy và trả về danh sách các tác vụ chưa được thực thi",
            "shutdown() xóa toàn bộ file trên đĩa cứng",
            "shutdownNow() khóa toàn bộ CPU của máy tính",
            "Cả hai phương thức hoàn toàn giống hệt nhau"
        ],
        "correctAnswer": 0,
        "explanation": "shutdown() thực hiện đóng tuần tự (graceful shutdown): không nhận task mới, chạy hết task cũ. shutdownNow() thực hiện đóng cưỡng bức (hard shutdown): gửi interrupt() tới các worker thread đang chạy và rút danh sách task chưa kịp chạy ra trả về.",
        "difficulty": "medium",
        "tags": ["ExecutorService", "ShutdownVsShutdownNow", "ThreadPool"]
    },
    {
        "id": "L7_Q53",
        "lessonId": 7,
        "type": "single",
        "title": "Điều gì có thể xảy ra nếu chương trình kết thúc hàm main() nhưng quên gọi pool.shutdown() trên ExecutorService?",
        "code": "public static void main(String[] args) {\n    ExecutorService pool = Executors.newFixedThreadPool(2);\n    pool.submit(() -> System.out.println(\"Hello\"));\n    // Quen goi pool.shutdown()\n}",
        "options": [
            "Ứng dụng Java (JVM) sẽ không bao giờ kết thúc và tiếp tục chạy ngầm vô hạn, vì các luồng trong ThreadPool mặc định là Non-daemon threads đang chờ việc",
            "JVM tự động đóng Thread Pool sau 1 giây",
            "Chương trình bị lỗi biên dịch",
            "Hệ điều hành tự động khởi động lại máy tính"
        ],
        "correctAnswer": 0,
        "explanation": "Các luồng worker trong ThreadPool được tạo bởi ThreadFactory mặc định đều là User Threads (Non-daemon). JVM chỉ dừng khi TẤT CẢ User Threads đã kết thúc. Nếu không gọi shutdown(), các luồng worker này tiếp tục nằm chờ task mới trong hàng đợi BlockingQueue, khiến JVM không bao giờ tắt được.",
        "difficulty": "hard",
        "tags": ["ThreadPoolShutdown", "NonDaemonThreads", "JVMExitTrap"]
    },
    {
        "id": "L7_Q54",
        "lessonId": 7,
        "type": "single",
        "title": "Lớp AtomicInteger trong java.util.concurrent.atomic đảm bảo an toàn đa luồng mà KHÔNG cần dùng khóa (Lock-free) nhờ thuật toán phần cứng nào?",
        "code": None,
        "options": [
            "Thuật toán CAS (Compare-And-Swap / So sánh và Hoán đổi) được hỗ trợ trực tiếp ở cấp độ tập lệnh vi xử lý CPU",
            "Thuật toán mã hóa RSA 2048-bit",
            "Sử dụng mutex lock của hệ điều hành Linux",
            "Chuyển đổi luồng thành tiến trình độc lập"
        ],
        "correctAnswer": 0,
        "explanation": "AtomicInteger sử dụng chỉ thị phần cứng nguyên tử CAS (Compare-And-Swap) thông qua Unsafe/VarHandle: nếu giá trị hiện tại ở ô nhớ đúng bằng giá trị kỳ vọng, CPU mới cập nhật giá trị mới, nếu bị tranh chấp thì vòng lặp thử lại (Spinlock/CAS loop). Không cần tạm dừng luồng (no context switch), đem lại hiệu năng cực cao.",
        "difficulty": "medium",
        "tags": ["AtomicInteger", "CAS", "LockFree"]
    },
    {
        "id": "L7_Q55",
        "lessonId": 7,
        "type": "single",
        "title": "Tiện ích đồng bộ CountDownLatch trong Java Concurrency hoạt động như thế nào?",
        "code": None,
        "options": [
            "Khởi tạo với một số đếm N; các luồng gọi await() sẽ bị chặn cho đến khi các luồng khác gọi đủ N lần phương thức countDown() để đưa số đếm về 0",
            "Cho phép đếm số lần ném ngoại lệ trong vòng lặp",
            "Tự động đặt lại số đếm N về giá trị ban đầu sau mỗi lần đếm về 0 (tương tự CyclicBarrier)",
            "Chỉ cho phép duy nhất một luồng chạy tại một thời điểm"
        ],
        "correctAnswer": 0,
        "explanation": "CountDownLatch khởi tạo với số đếm N. Mỗi khi một tác vụ con hoàn thành, nó gọi latch.countDown(). Luồng chính gọi latch.await() sẽ bị chặn cho đến khi số đếm giảm về 0. Chú ý: CountDownLatch dùng một lần, không thể tái sử dụng (muốn tái sử dụng phải dùng CyclicBarrier).",
        "difficulty": "medium",
        "tags": ["CountDownLatch", "ConcurrencyUtilities", "Synchronization"]
    },
    {
        "id": "L7_Q56",
        "lessonId": 7,
        "type": "single",
        "title": "Sự khác biệt giữa Executors.newFixedThreadPool(n) và Executors.newCachedThreadPool() là gì?",
        "code": None,
        "options": [
            "FixedThreadPool có số lượng luồng cố định và dùng hàng đợi vô hạn (LinkedBlockingQueue); CachedThreadPool tự động tạo luồng mới khi cần (không giới hạn số luồng tối đa) và tái sử dụng các luồng rảnh sau 60 giây",
            "FixedThreadPool chỉ chạy được 1 task duy nhất",
            "CachedThreadPool lưu trữ kết quả trên đĩa cứng SSD",
            "Cả hai đều có số luồng tối đa là 10"
        ],
        "correctAnswer": 0,
        "explanation": "FixedThreadPool duy trì đúng n luồng, task thừa xếp hàng trong LinkedBlockingQueue (nguy cơ OOM nếu task đến quá nhanh). CachedThreadPool dùng SynchronousQueue, không xếp hàng mà tạo luồng mới nếu không có luồng rỗi (nguy cơ OOM do sinh quá nhiều luồng nếu tải tăng đột biến).",
        "difficulty": "medium",
        "tags": ["FixedThreadPool", "CachedThreadPool", "ExecutorTypes"]
    },
    {
        "id": "L7_Q57",
        "lessonId": 7,
        "type": "single",
        "title": "Tiện ích Semaphore trong Java Concurrency dùng để giải quyết bài toán nào?",
        "code": None,
        "options": [
            "Quản lý và giới hạn số lượng luồng tối đa được phép đồng thời truy cập vào một tài nguyên cụ thể (hỗ trợ các giấy phép - permits)",
            "Chỉ dùng để đếm số lượng luồng đang chạy",
            "Thay thế hoàn toàn cho Garbage Collector",
            "Tự động chuyển đổi mã Java sang bytecode"
        ],
        "correctAnswer": 0,
        "explanation": "Semaphore duy trì một tập hợp các giấy phép (permits). Luồng gọi acquire() để lấy giấy phép (nếu hết giấy phép thì phải chờ), sau khi dùng xong gọi release() để trả lại. Rất phổ biến khi giới hạn số lượng kết nối Database Connection Pool hoặc số luồng đồng thời gọi API bên ngoài.",
        "difficulty": "easy",
        "tags": ["Semaphore", "Permits", "RateLimiting"]
    },
    {
        "id": "L7_Q58",
        "lessonId": 7,
        "type": "multiple",
        "title": "Những nguy cơ tiềm ẩn khi sử dụng Thread Pool mà lập trình viên cần lưu ý là gì?",
        "code": None,
        "options": [
            "Thread Pool Starvation (Đói tài nguyên): Các tác vụ trong pool phụ thuộc lẫn nhau, task cha chờ kết quả task con nhưng pool đã hết luồng trống để chạy task con",
            "Tràn bộ nhớ OutOfMemoryError do hàng đợi tác vụ không giới hạn (Unbounded Queue) bị phình to khi tốc độ nạp task vượt quá tốc độ xử lý",
            "Rò rỉ dữ liệu qua ThreadLocal nếu không gọi threadLocal.remove() khi luồng được trả về pool để tái sử dụng",
            "Thread Pool làm CPU luôn luôn hoạt động ở mức 100% dù không có tác vụ nào"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 là các lỗi kinh điển khi vận hành Thread Pool trong production: Starvation Deadlock, Memory Leak do ThreadLocal không clean khi reuse thread, và OOM do LinkedBlockingQueue vô hạn.",
        "difficulty": "hard",
        "tags": ["ThreadPoolPitfalls", "Starvation", "MemoryLeak"]
    },
    {
        "id": "L7_Q59",
        "lessonId": 7,
        "type": "single",
        "title": "Xác định output của chương trình sau sử dụng AtomicInteger:",
        "code": "AtomicInteger ai = new AtomicInteger(10);\nint v1 = ai.getAndIncrement();\nint v2 = ai.incrementAndGet();\nSystem.out.println(v1 + \" \" + v2 + \" \" + ai.get());",
        "options": [
            "10 12 12",
            "11 12 12",
            "10 11 12",
            "11 11 12"
        ],
        "correctAnswer": 0,
        "explanation": "Ban đầu ai = 10. ai.getAndIncrement() trả về giá trị cũ (10) sau đó tăng lên 11 (v1 = 10, ai = 11). ai.incrementAndGet() tăng lên 12 sau đó trả về giá trị mới 12 (v2 = 12, ai = 12). ai.get() trả về 12. Kết quả là '10 12 12'.",
        "difficulty": "easy",
        "tags": ["AtomicInteger", "GetAndIncrement", "Output"]
    },
    {
        "id": "L7_Q60",
        "lessonId": 7,
        "type": "single",
        "title": "Trong Java 21, tính năng 'Virtual Threads' (Tiểu trình ảo - Project Loom) mang lại đột phá lớn nhất là gì?",
        "code": None,
        "options": [
            "Tiểu trình ảo siêu nhẹ được quản lý trực tiếp bởi JVM (thay vì ánh xạ 1-1 với Kernel Thread của hệ điều hành), cho phép tạo hàng triệu luồng đồng thời với chi phí bộ nhớ cực thấp",
            "Cho phép CPU chạy với xung nhịp 10GHz",
            "Tự động sửa chữa tất cả các lỗi Deadlock trong mã nguồn",
            "Loại bỏ hoàn toàn sự cần thiết của từ khóa synchronized"
        ],
        "correctAnswer": 0,
        "explanation": "Virtual Threads (Project Loom) là tiểu trình ảo siêu nhẹ do JVM quản lý. Trong khi Platform Thread của OS tốn ~1MB stack và tối đa chỉ tạo được vài nghìn luồng, Virtual Thread chỉ tốn vài trăm byte và có thể chạy hàng triệu luồng đồng thời, tối ưu hóa triệt để mô hình Blocking I/O theo kiểu thread-per-request.",
        "difficulty": "medium",
        "tags": ["VirtualThreads", "ProjectLoom", "ModernJava"]
    }
]

def update_file(filename, new_questions):
    path = os.path.join(r"D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\questions", filename)
    with open(path, "r", encoding="utf-8") as f:
        existing = json.load(f)
    
    existing_ids = {q["id"] for q in existing}
    added_count = 0
    for q in new_questions:
        if q["id"] not in existing_ids:
            existing.append(q)
            existing_ids.add(q["id"])
            added_count += 1
        else:
            print(f"Warning: Question {q['id']} already exists in {filename}!")
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"Updated {filename}: Added {added_count} new questions (Total now: {len(existing)})")

if __name__ == "__main__":
    update_file("lesson5.json", L5_NEW)
    update_file("lesson6.json", L6_NEW)
    update_file("lesson7.json", L7_NEW)
    print("All 90 questions for Lessons 5, 6, 7 generated and appended successfully.")
