# -*- coding: utf-8 -*-
"""
Script to generate 90 new questions for Lesson 1, 3, and 4
- Lesson 1 & 2: L1_Q31 to L1_Q60 (Đề 1C: 15 questions, Đề 1D: 15 questions)
- Lesson 3: L3_Q46 to L3_Q75 (Đề 3D: 15 questions, Đề 3E: 15 questions)
- Lesson 4: L4_Q46 to L4_Q75 (Đề 4D: 15 questions, Đề 4E: 15 questions)
"""

import json
import os

L1_NEW = [
    # --- ĐỀ 1C (L1_Q31 - L1_Q45): Memory Model, String Pool, Immutability & GC ---
    {
        "id": "L1_Q31",
        "lessonId": 1,
        "type": "single",
        "title": "Phân biệt vị trí lưu trữ giữa String literal (chuỗi ký tự trực tiếp) và đối tượng chuỗi được tạo bằng toán tử 'new String(\"abc\")' trong JVM:",
        "code": None,
        "options": [
            "String literal được lưu trong String Constant Pool (nằm trong Heap), còn 'new String()' luôn tạo một đối tượng mới hoàn toàn trong vùng nhớ Heap thông thường",
            "String literal được lưu trên Stack, còn 'new String()' được lưu trên Metaspace",
            "Cả hai đều luôn được lưu cùng một vị trí trong String Constant Pool và trỏ tới cùng một địa chỉ bộ nhớ",
            "String literal được lưu trong bộ nhớ tĩnh của CPU, còn 'new String()' được nạp vào Heap"
        ],
        "correctAnswer": 0,
        "explanation": "Trong Java (từ Java 7 trở đi), String Constant Pool nằm trong vùng nhớ Heap. Khi khai báo String literal (ví dụ String s = \"abc\"), JVM sẽ kiểm tra và tái sử dụng chuỗi trong Pool. Ngược lại, toán tử 'new String(\"abc\")' luôn tạo một đối tượng String độc lập trong Heap thông thường bên ngoài Pool.",
        "difficulty": "medium",
        "tags": ["StringPool", "Heap", "MemoryModel"]
    },
    {
        "id": "L1_Q32",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định output của đoạn mã so sánh chuỗi sau:",
        "code": "String s1 = \"Java\";\nString s2 = new String(\"Java\");\nString s3 = s2.intern();\nSystem.out.println((s1 == s2) + \" \" + (s1 == s3) + \" \" + s1.equals(s2));",
        "options": [
            "false true true",
            "true true true",
            "false false true",
            "false true false"
        ],
        "correctAnswer": 0,
        "explanation": "s1 trỏ tới đối tượng trong String Pool. s2 là đối tượng mới trong Heap nên s1 == s2 là false. Phương thức s2.intern() trả về tham chiếu từ String Pool (chính là s1), do đó s1 == s3 là true. Phương thức .equals() so sánh nội dung chuỗi nên s1.equals(s2) là true.",
        "difficulty": "medium",
        "tags": ["StringPool", "Intern", "Equality"]
    },
    {
        "id": "L1_Q33",
        "lessonId": 1,
        "type": "multiple",
        "title": "Những trường hợp nào sau đây khiến một đối tượng trong Heap đủ điều kiện để Garbage Collector (GC) thu hồi bộ nhớ?",
        "code": None,
        "options": [
            "Tất cả các biến tham chiếu đến đối tượng đó đều được gán bằng null",
            "Đối tượng nằm trong một nhóm các đối tượng chỉ tham chiếu vòng tới nhau (Island of Isolation) nhưng không có bất kỳ đường dẫn nào từ GC Roots nối tới",
            "Biến tham chiếu cục bộ trỏ tới đối tượng đó ra khỏi phạm vi (scope) khi phương thức kết thúc thực thi",
            "Đối tượng được gọi phương thức finalize() một lần bởi lập trình viên"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Trong Java, một đối tượng trở thành rác khi không còn bất kỳ đường dẫn tiếp cận nào (unreachable) từ các GC Roots (bao gồm biến cục bộ trong Stack, biến static trong Metaspace, JNI references). Đảo cô lập (Island of Isolation) dù có tham chiếu chéo nhưng không tới được từ GC Roots nên vẫn bị thu hồi. Gọi finalize() bằng tay chỉ là gọi một method bình thường, không biến đối tượng thành rác.",
        "difficulty": "hard",
        "tags": ["GarbageCollection", "GCRoots", "Heap"]
    },
    {
        "id": "L1_Q34",
        "lessonId": 1,
        "type": "single",
        "title": "Đoạn mã sau thực hiện phép nối chuỗi trong vòng lặp. Vấn đề chính về bộ nhớ và hiệu năng của đoạn mã này là gì?",
        "code": "String s = \"\";\nfor (int i = 0; i < 1000; i++) {\n    s = s + i;\n}",
        "options": [
            "Vì String là bất biến (immutable), mỗi lần nối chuỗi '+' trong vòng lặp sẽ tạo ra các đối tượng StringBuilder và String tạm thời mới, gây tốn bộ nhớ và giảm hiệu năng nghiêm trọng (độ phức tạp O(n^2))",
            "Đoạn mã sẽ ném ngoại lệ OutOfMemoryError ngay tại lần lặp thứ 10 do Stack Overflow",
            "Trình biên dịch Java sẽ tự động tối ưu hóa toàn bộ vòng lặp thành một StringBuilder duy nhất nên hiệu năng tương đương hoàn toàn",
            "Đoạn mã bị lỗi biên dịch vì không thể nối chuỗi rỗng với kiểu int"
        ],
        "correctAnswer": 0,
        "explanation": "Mặc dù javac có thể tối ưu phép cộng chuỗi đơn lẻ bằng StringBuilder, nhưng trong vòng lặp, mỗi lần lặp lại tạo ra một StringBuilder mới và chuyển thành một String mới. Điều này sinh ra hàng nghìn đối tượng trung gian trong Heap và có độ phức tạp thời gian O(n^2). Cần dùng StringBuilder trực tiếp bên ngoài vòng lặp.",
        "difficulty": "medium",
        "tags": ["Immutability", "Performance", "StringBuilder"]
    },
    {
        "id": "L1_Q35",
        "lessonId": 1,
        "type": "multiple",
        "title": "Về phương thức System.gc() và Runtime.getRuntime().gc(), những khẳng định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Lời gọi System.gc() chỉ là một lời gợi ý (hint) gửi tới JVM rằng lập trình viên mong muốn thu hồi bộ nhớ, không đảm bảo GC sẽ chạy ngay lập tức",
            "JVM có toàn quyền bỏ qua hoặc trì hoãn lời gọi System.gc() tùy thuộc vào cấu hình và trạng thái bộ nhớ hiện tại",
            "Không nên phụ thuộc vào System.gc() trong mã nguồn ứng dụng thực tế vì có thể gây gián đoạn (Stop-The-World) không cần thiết",
            "System.gc() đảm bảo thu hồi tức thì 100% tất cả các đối tượng rác trước khi câu lệnh tiếp theo được thực thi"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Đặc tả ngôn ngữ Java (JLS) khẳng định System.gc() không có bất kỳ cam kết nào rằng GC sẽ chạy ngay lập tức hay thu hồi hết rác. JVM có thể bỏ qua hoàn toàn (ví dụ khi bật cờ -XX:+DisableExplicitGC). Việc gọi thủ công có thể gây dừng toàn bộ các luồng ứng dụng (Stop-the-world), làm giảm hiệu năng.",
        "difficulty": "medium",
        "tags": ["GarbageCollection", "System.gc", "JVM"]
    },
    {
        "id": "L1_Q36",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định thứ tự in ra màn hình khi chương trình sau được thực thi:",
        "code": "class Demo {\n    static {\n        System.out.print(\"S1 \");\n    }\n    {\n        System.out.print(\"I1 \");\n    }\n    Demo() {\n        System.out.print(\"C1 \");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        System.out.print(\"M1 \");\n        new Demo();\n        new Demo();\n    }\n}",
        "options": [
            "M1 S1 I1 C1 I1 C1",
            "S1 M1 I1 C1 I1 C1",
            "M1 S1 I1 C1 S1 I1 C1",
            "S1 I1 C1 M1 I1 C1"
        ],
        "correctAnswer": 0,
        "explanation": "Khi chạy Main, hàm main chạy in 'M1 '. Khi gặp lệnh 'new Demo()' lần đầu, lớp Demo được nạp vào JVM nên khối static block chạy một lần duy nhất in 'S1 '. Tiếp theo, khối instance initializer chạy in 'I1 ', sau đó constructor chạy in 'C1 '. Ở lần 'new Demo()' thứ hai, static block không chạy lại nữa, chỉ có khối instance 'I1 ' và constructor 'C1 ' chạy. Kết quả là 'M1 S1 I1 C1 I1 C1'.",
        "difficulty": "hard",
        "tags": ["StaticBlock", "InstanceBlock", "ConstructorOrder"]
    },
    {
        "id": "L1_Q37",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định output của chương trình sau:",
        "code": "public class Main {\n    public static void main(String[] args) {\n        String s = \"UET\";\n        s.concat(\"-VNU\");\n        s.toLowerCase();\n        System.out.println(s);\n    }\n}",
        "options": [
            "UET",
            "UET-VNU",
            "uet-vnu",
            "uet"
        ],
        "correctAnswer": 0,
        "explanation": "Lớp String trong Java là bất biến (immutable). Các phương thức như concat(), toLowerCase(), replace() không bao giờ thay đổi chuỗi ban đầu mà chỉ trả về một đối tượng String mới chứa kết quả. Do giá trị trả về không được gán lại cho s (ví dụ s = s.concat(...)), biến s vẫn trỏ tới chuỗi ban đầu là \"UET\".",
        "difficulty": "easy",
        "tags": ["String", "Immutability", "Methods"]
    },
    {
        "id": "L1_Q38",
        "lessonId": 1,
        "type": "multiple",
        "title": "Những thành phần nào sau đây được JVM công nhận là các 'GC Roots' (Gốc thu gom rác) để xác định tính vươn tới (reachability) của một đối tượng?",
        "code": None,
        "options": [
            "Các biến cục bộ (Local variables) và tham số phương thức nằm trong Stack Frame của các luồng (Thread) đang hoạt động",
            "Các biến tĩnh (Static variables / fields) của các lớp đã được nạp trong bộ nhớ Metaspace",
            "Các tham chiếu đối tượng trong mã bản địa JNI (Java Native Interface global & local references)",
            "Tất cả các đối tượng đã được đánh dấu @Deprecated trong mã nguồn"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "GC Roots cơ bản trong JVM gồm: 1. Biến cục bộ trong Call Stack của luồng đang sống, 2. Biến static của class, 3. JNI native references, 4. Các luồng (Thread) đang chạy. Annotation @Deprecated chỉ là chú thích cảnh báo của trình biên dịch, không liên quan đến GC Roots.",
        "difficulty": "hard",
        "tags": ["GarbageCollection", "GCRoots", "JVM"]
    },
    {
        "id": "L1_Q39",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định số lượng đối tượng đủ điều kiện bị GC thu hồi tại dòng comment // TAI DAY:",
        "code": "class A {}\npublic class Main {\n    public static void main(String[] args) {\n        A a1 = new A();\n        A a2 = new A();\n        A a3 = a1;\n        a1 = null;\n        a2 = null;\n        // TAI DAY\n        System.out.println(\"Done\");\n    }\n}",
        "options": [
            "1 đối tượng (đối tượng ban đầu của a2)",
            "2 đối tượng (cả đối tượng a1 và a2)",
            "0 đối tượng",
            "3 đối tượng"
        ],
        "correctAnswer": 0,
        "explanation": "Có 2 đối tượng được tạo bởi 'new A()'. Đối tượng thứ nhất ban đầu được trỏ bởi a1, sau đó a3 cũng trỏ tới đối tượng này (a3 = a1). Khi a1 = null, đối tượng thứ nhất vẫn còn biến a3 trỏ tới nên chưa bị thu hồi. Đối tượng thứ hai được trỏ bởi a2, khi a2 = null thì không còn tham chiếu nào trỏ tới nữa. Do đó chỉ có 1 đối tượng đủ điều kiện bị GC thu hồi.",
        "difficulty": "medium",
        "tags": ["Reference", "GarbageCollection", "Memory"]
    },
    {
        "id": "L1_Q40",
        "lessonId": 1,
        "type": "single",
        "title": "Vùng nhớ Metaspace (được giới thiệu từ Java 8 thay thế cho Permanent Generation - PermGen) có đặc điểm nào sau đây?",
        "code": None,
        "options": [
            "Được cấp phát từ bộ nhớ hệ điều hành (Native Memory), có thể tự động co giãn kích thước theo mặc định và lưu trữ thông tin metadata của class",
            "Nằm bên trong phân vùng Heap cố định giống như Heap của đối tượng và có kích thước tối đa cố định 64MB",
            "Chỉ được dùng để lưu trữ mảng các số nguyên và số thực nguyên thủy",
            "Lưu trữ toàn bộ biến cục bộ của hàm main và bị xóa sạch mỗi khi gọi System.gc()"
        ],
        "correctAnswer": 0,
        "explanation": "Từ Java 8, PermGen bị loại bỏ và thay bằng Metaspace. Khác với PermGen nằm trong Heap, Metaspace được cấp phát từ Native Memory của hệ điều hành, giúp giảm thiểu lỗi java.lang.OutOfMemoryError: PermGen space và có khả năng tự động điều chỉnh kích thước theo tài nguyên khả dụng của hệ thống.",
        "difficulty": "medium",
        "tags": ["Metaspace", "PermGen", "JVM"]
    },
    {
        "id": "L1_Q41",
        "lessonId": 1,
        "type": "multiple",
        "title": "So sánh giữa StringBuilder và StringBuffer trong Java, những nhận định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "StringBuffer là thread-safe (an toàn đa luồng) vì hầu hết các phương thức quan trọng đều được đồng bộ hóa với từ khóa 'synchronized'",
            "StringBuilder không thread-safe nhưng có tốc độ thực thi nhanh hơn StringBuffer trong môi trường đơn luồng",
            "Cả StringBuilder và StringBuffer đều là các lớp có thể thay đổi trạng thái nội bộ (mutable), không tạo ra đối tượng mới khi gọi phương thức append()",
            "StringBuilder kế thừa từ StringBuffer và ghi đè lại các phương thức để bỏ synchronized"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "StringBuffer được thiết kế từ Java 1.0 với các phương thức synchronized để an toàn đa luồng. Java 1.5 bổ sung StringBuilder không có synchronized nhằm tối ưu tốc độ cho ứng dụng đơn luồng. Cả hai đều kế thừa từ AbstractStringBuilder, không phải StringBuilder kế thừa từ StringBuffer.",
        "difficulty": "medium",
        "tags": ["StringBuilder", "StringBuffer", "ThreadSafety"]
    },
    {
        "id": "L1_Q42",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định output của đoạn mã kiểm tra cơ chế Integer Cache sau:",
        "code": "Integer a = 127;\nInteger b = 127;\nInteger c = 128;\nInteger d = 128;\nSystem.out.println((a == b) + \" \" + (c == d));",
        "options": [
            "true false",
            "true true",
            "false false",
            "false true"
        ],
        "correctAnswer": 0,
        "explanation": "Java triển khai cơ chế Integer Cache (lưu trữ sẵn các đối tượng Integer từ -128 đến 127). Khi gán 'Integer a = 127', Java tự động Autoboxing qua Integer.valueOf(127) và trả về đối tượng có sẵn trong Cache, do đó a == b so sánh cùng địa chỉ bộ nhớ trả về true. Với giá trị 128 (vượt ngoài phạm vi [-128, 127]), JVM tạo hai đối tượng Integer mới trong Heap, nên c == d so sánh tham chiếu trả về false.",
        "difficulty": "medium",
        "tags": ["Autoboxing", "IntegerCache", "Equality"]
    },
    {
        "id": "L1_Q43",
        "lessonId": 1,
        "type": "multiple",
        "title": "Để thiết kế một lớp Immutable (Bất biến hoàn toàn) chuẩn mực trong Java, lớp đó cần thỏa mãn những điều kiện nào sau đây?",
        "code": None,
        "options": [
            "Khai báo lớp là 'final' để ngăn chặn các lớp con kế thừa và ghi đè làm thay đổi hành vi",
            "Tất cả các trường (fields) phải được khai báo là 'private' và 'final'",
            "Không cung cấp bất kỳ phương thức setter nào làm thay đổi trạng thái của các trường",
            "Nếu lớp chứa trường tham chiếu tới một đối tượng mutable (ví dụ Date, List), phải thực hiện sao chép sâu (defensive deep copy) cả trong constructor và getter"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Cả 4 điều kiện trên đều bắt buộc theo quy tắc thiết kế lớp Immutable (Effective Java). Nếu không defensive copy trong getter hoặc constructor, người dùng bên ngoài có thể lấy tham chiếu và sửa đổi dữ liệu bên trong đối tượng mutable đó, phá vỡ tính bất biến.",
        "difficulty": "hard",
        "tags": ["Immutable", "Design", "Encapsulation"]
    },
    {
        "id": "L1_Q44",
        "lessonId": 1,
        "type": "single",
        "title": "Đoạn mã sau vi phạm tính bất biến (Immutability) tại điểm nào?",
        "code": "public final class Student {\n    private final String name;\n    private final List<String> subjects;\n    public Student(String name, List<String> subjects) {\n        this.name = name;\n        this.subjects = subjects;\n    }\n    public List<String> getSubjects() {\n        return subjects;\n    }\n}",
        "options": [
            "Cả trong constructor và phương thức getSubjects() đều không thực hiện defensive copy, cho phép bên ngoài sửa đổi danh sách subjects",
            "Lớp Student không implements Cloneable",
            "Thuộc tính name kiểu String không thể khai báo là final",
            "Thiếu phương thức setSubjects() để bảo đảm an toàn dữ liệu"
        ],
        "correctAnswer": 0,
        "explanation": "Lớp Student lưu trữ trực tiếp tham chiếu danh sách 'subjects' được truyền vào và getter trả về trực tiếp tham chiếu nội bộ. Bất kỳ mã ngoài nào cũng có thể gọi student.getSubjects().add(\"Math\") để thay đổi danh sách. Để khắc phục, constructor cần new ArrayList<>(subjects) và getter cần trả về Collections.unmodifiableList(subjects) hoặc bản copy.",
        "difficulty": "hard",
        "tags": ["Immutability", "DefensiveCopy", "Security"]
    },
    {
        "id": "L1_Q45",
        "lessonId": 1,
        "type": "single",
        "title": "Xem xét hiện tượng Đảo cô lập (Island of Isolation) trong đoạn mã sau. Điều gì xảy ra với hai đối tượng Node sau khi thực hiện hai lệnh gán null?",
        "code": "class Node {\n    Node next;\n}\npublic class Main {\n    public static void main(String[] args) {\n        Node a = new Node();\n        Node b = new Node();\n        a.next = b;\n        b.next = a;\n        a = null;\n        b = null;\n        // TAI DAY\n    }\n}",
        "options": [
            "Cả hai đối tượng Node a và b đều đủ điều kiện bị GC thu hồi vì không còn bất kỳ đường dẫn nào từ GC Roots có thể vươn tới chúng",
            "Không đối tượng nào bị thu hồi vì chúng vẫn đang tham chiếu chéo lẫn nhau (a.next trỏ b và b.next trỏ a)",
            "Chỉ có đối tượng b bị thu hồi, còn đối tượng a vẫn tồn tại vĩnh viễn trong bộ nhớ",
            "Chương trình bị lỗi biên dịch vì không thể tạo tham chiếu vòng lặp giữa hai đối tượng"
        ],
        "correctAnswer": 0,
        "explanation": "Đây là ví dụ kinh điển về 'Island of Isolation'. Trình thu gom rác hiện đại của Java dùng thuật toán Mark-and-Sweep (dựa trên Root Reachability) chứ không dùng thuật toán đếm tham chiếu (Reference Counting) đơn giản. Do không có biến nào từ GC Roots nối tới a hay b, toàn bộ hòn đảo này được coi là rác và sẽ bị thu hồi.",
        "difficulty": "medium",
        "tags": ["IslandOfIsolation", "GarbageCollection", "Reachability"]
    },

    # --- ĐỀ 1D (L1_Q46 - L1_Q60): Access Modifiers, Overloading Resolution & Constructor Pitfalls ---
    {
        "id": "L1_Q46",
        "lessonId": 1,
        "type": "single",
        "title": "Theo quy tắc kiểm soát truy cập trong Java, một thành viên mang thuộc tính 'protected' trong class A (thuộc package p1) có thể được truy cập từ class B (thuộc package p2) trong điều kiện nào?",
        "code": None,
        "options": [
            "Class B phải là lớp con kế thừa từ Class A, và việc truy cập phải thông qua cơ chế kế thừa trên chính thể hiện của Class B (hoặc lớp con của B)",
            "Chỉ cần Class B import package p1 thì có thể truy cập tự do qua bất kỳ tham chiếu nào của Class A",
            "Thành viên protected không bao giờ có thể truy cập được từ bên ngoài package p1 dù có kế thừa",
            "Class B chỉ cần nằm cùng một project là tự động có quyền truy cập mà không cần kế thừa"
        ],
        "correctAnswer": 0,
        "explanation": "Thành viên protected có thể truy cập trong cùng package. Nếu ở package khác, chỉ có lớp con mới truy cập được và phải thông qua quan hệ kế thừa (trên chính đối tượng con đó hoặc dùng super). Lớp con ở package khác không thể truy cập thành viên protected thông qua một biến tham chiếu kiểu lớp cha (ví dụ: A a = new A(); a.protectedMember gây lỗi biên dịch).",
        "difficulty": "hard",
        "tags": ["Protected", "Package", "AccessModifiers"]
    },
    {
        "id": "L1_Q47",
        "lessonId": 1,
        "type": "single",
        "title": "Cho hai lớp nằm ở hai package khác nhau như sau. Đoạn mã tại SubClass có hợp lệ không?",
        "code": "// File: p1/SuperClass.java\npackage p1;\npublic class SuperClass {\n    protected int value = 42;\n}\n\n// File: p2/SubClass.java\npackage p2;\nimport p1.SuperClass;\npublic class SubClass extends SuperClass {\n    public void test() {\n        SuperClass sup = new SuperClass();\n        System.out.println(sup.value); // DONG 1\n        System.out.println(this.value); // DONG 2\n    }\n}",
        "options": [
            "Dòng 1 gây lỗi biên dịch (không thể truy cập protected qua tham chiếu của lớp cha từ package khác), Dòng 2 hợp lệ",
            "Cả Dòng 1 và Dòng 2 đều hợp lệ",
            "Cả Dòng 1 và Dòng 2 đều gây lỗi biên dịch",
            "Dòng 1 hợp lệ, Dòng 2 gây lỗi biên dịch"
        ],
        "correctAnswer": 0,
        "explanation": "Đây là bẫy rất sâu về từ khóa protected trong Java. Khi kế thừa từ package khác, lớp con chỉ có thể truy cập trường protected thông qua kế thừa (this.value hoặc super.value). Lớp con không được phép truy cập trường protected thông qua tham chiếu của đối tượng lớp cha (sup.value) nằm ngoài package. Do đó Dòng 1 gây lỗi biên dịch.",
        "difficulty": "hard",
        "tags": ["ProtectedTrap", "AccessModifiers", "Package"]
    },
    {
        "id": "L1_Q48",
        "lessonId": 1,
        "type": "multiple",
        "title": "Những phát biểu nào sau đây là ĐÚNG về cơ chế gọi Constructor Chaining với 'this()' và 'super()' trong Java?",
        "code": None,
        "options": [
            "Lời gọi 'this()' hoặc 'super()' bắt buộc phải là câu lệnh thực thi đầu tiên bên trong constructor",
            "Trong cùng một constructor, không thể gọi đồng thời cả 'this()' và 'super()'",
            "Nếu lập trình viên không viết lời gọi constructor nào, trình biên dịch sẽ tự động chèn 'super()' không tham số vào dòng đầu tiên",
            "Có thể gọi 'this()' hoặc 'super()' ở bất kỳ phương thức instance thông thường nào để tái khởi tạo đối tượng"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Trong Java, this() hoặc super() chỉ được gọi trong constructor và bắt buộc phải nằm ở dòng lệnh đầu tiên. Vì đều phải ở dòng đầu nên không thể gọi cả hai trong cùng một constructor. Không thể gọi this() hay super() trong các phương thức thông thường.",
        "difficulty": "medium",
        "tags": ["Constructor", "This", "Super"]
    },
    {
        "id": "L1_Q49",
        "lessonId": 1,
        "type": "single",
        "title": "Điều gì xảy ra khi biên dịch lớp sau:",
        "code": "public class Test {\n    Test() {\n        this(5);\n    }\n    Test(int x) {\n        this();\n    }\n}",
        "options": [
            "Lỗi biên dịch: Recursive constructor invocation (lời gọi constructor đệ quy)",
            "Biên dịch thành công, khi chạy sẽ ném lỗi StackOverflowError",
            "Lỗi biên dịch vì không thể truyền giá trị 5 vào constructor",
            "Biên dịch thành công và chương trình chạy bình thường không có lỗi"
        ],
        "correctAnswer": 0,
        "explanation": "Trình biên dịch Java phát hiện chu trình gọi đệ quy giữa các constructor (Test() gọi Test(int) và Test(int) lại gọi Test()) ngay tại thời điểm compile-time và báo lỗi biên dịch 'Recursive constructor invocation'.",
        "difficulty": "easy",
        "tags": ["Constructor", "CompileError", "Chaining"]
    },
    {
        "id": "L1_Q50",
        "lessonId": 1,
        "type": "multiple",
        "title": "Khi một phương thức nạp chồng (Overloaded method) được gọi, JVM và trình biên dịch xác định phương thức phù hợp theo thứ tự ưu tiên nào sau đây?",
        "code": None,
        "options": [
            "Ưu tiên 1: Khớp chính xác (Exact match) hoặc Mở rộng kiểu nguyên thủy (Primitive Widening conversion, ví dụ int sang long)",
            "Ưu tiên 2: Tự động đóng gói/mở gói (Autoboxing / Unboxing, ví dụ int sang Integer)",
            "Ưu tiên 3: Tham số có độ dài biến đổi (Varargs, ví dụ int... args)",
            "Ưu tiên tuyệt đối cho kiểu Object bất kể tham số truyền vào là gì"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Quy tắc phân giải Overloading của Java (JLS 15.12.2) chia làm 3 giai đoạn rõ ràng: Giai đoạn 1: Không dùng boxing/varargs (chỉ exact match hoặc widening). Giai đoạn 2: Cho phép boxing/unboxing nhưng không dùng varargs. Giai đoạn 3: Cho phép dùng varargs. Kiểu Object chỉ được chọn nếu không có kiểu cụ thể hơn khớp ở giai đoạn tương ứng.",
        "difficulty": "hard",
        "tags": ["Overloading", "Resolution", "JLS"]
    },
    {
        "id": "L1_Q51",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định output của chương trình sau khi gọi hàm nạp chồng với biến nguyên thủy:",
        "code": "public class OverloadTest {\n    static void test(long x) { System.out.print(\"long \"); }\n    static void test(Integer x) { System.out.print(\"Integer \"); }\n    static void test(int... x) { System.out.print(\"varargs \"); }\n    public static void main(String[] args) {\n        int a = 10;\n        test(a);\n    }\n}",
        "options": [
            "long ",
            "Integer ",
            "varargs ",
            "Lỗi biên dịch do nhập nhằng (ambiguous method call)"
        ],
        "correctAnswer": 0,
        "explanation": "Biến 'a' có kiểu int. Theo thứ tự ưu tiên của Java, Primitive Widening (int -> long) được ưu tiên cao hơn Autoboxing (int -> Integer) và Varargs (int...). Do đó phương thức test(long) được gọi và in ra 'long '.",
        "difficulty": "medium",
        "tags": ["Overloading", "Widening", "Autoboxing"]
    },
    {
        "id": "L1_Q52",
        "lessonId": 1,
        "type": "single",
        "title": "Điều gì xảy ra khi biên dịch và chạy đoạn mã nạp chồng sau?",
        "code": "public class AmbiguityTest {\n    static void print(String s, Object o) {\n        System.out.println(\"String, Object\");\n    }\n    static void print(Object o, String s) {\n        System.out.println(\"Object, String\");\n    }\n    public static void main(String[] args) {\n        print(null, null);\n    }\n}",
        "options": [
            "Lỗi biên dịch: Lời gọi hàm nhập nhằng (reference to print is ambiguous)",
            "In ra: String, Object",
            "In ra: Object, String",
            "Ném ngoại lệ NullPointerException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Cả hai phương thức print đều có thể nhận đối số (null, null). Trình biên dịch cố gắng tìm phương thức 'cụ thể nhất' (most specific). Tuy nhiên, phương thức thứ nhất cụ thể hơn ở tham số 1 nhưng kém cụ thể hơn ở tham số 2, và ngược lại. Không phương thức nào hoàn toàn cụ thể hơn phương thức kia, dẫn đến lỗi biên dịch Ambiguous method call.",
        "difficulty": "hard",
        "tags": ["Overloading", "Ambiguity", "CompileError"]
    },
    {
        "id": "L1_Q53",
        "lessonId": 1,
        "type": "multiple",
        "title": "Những khẳng định nào sau đây về từ khóa 'final' trong Java là ĐÚNG?",
        "code": None,
        "options": [
            "Biến khai báo với 'final' chỉ được gán giá trị một lần duy nhất, sau đó không thể thay đổi giá trị hoặc trỏ sang tham chiếu khác",
            "Một đối tượng được trỏ bởi biến 'final' vẫn có thể thay đổi trạng thái nội bộ nếu lớp của nó là mutable",
            "Phương thức khai báo là 'final' sẽ không thể bị ghi đè (overridden) bởi bất kỳ lớp con nào",
            "Lớp khai báo là 'final' thì tất cả các phương thức trong lớp đó tự động ngầm định là 'final'"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Tất cả các khẳng định trên đều chính xác theo đặc tả Java. final cho biến nghĩa là tham chiếu bất biến, nhưng đối tượng trong Heap vẫn có thể bị sửa đổi nếu mutable (ví dụ final List list; list.add(1) hoàn toàn hợp lệ). Lớp final không thể bị kế thừa, nên tất cả các phương thức của nó cũng không thể bị ghi đè, tương đương ngầm định là final.",
        "difficulty": "medium",
        "tags": ["Final", "Methods", "Variables"]
    },
    {
        "id": "L1_Q54",
        "lessonId": 1,
        "type": "single",
        "title": "Điều gì xảy ra khi biên dịch đoạn mã khai báo 'Blank final' field sau?",
        "code": "public class BlankFinalTest {\n    private final int x;\n    public BlankFinalTest() {\n        // Khong gan x\n    }\n    public BlankFinalTest(int val) {\n        this.x = val;\n    }\n}",
        "options": [
            "Lỗi biên dịch tại constructor không tham số: biến final x có thể chưa được khởi tạo",
            "Biên dịch thành công và biến x trong constructor rỗng sẽ nhận giá trị mặc định là 0",
            "Lỗi biên dịch tại dòng khai báo private final int x vì bắt buộc phải gán giá trị ngay",
            "Lỗi runtime khi khởi tạo đối tượng bằng constructor không tham số"
        ],
        "correctAnswer": 0,
        "explanation": "Một biến instance final (blank final) nếu không được khởi tạo ngay tại dòng khai báo thì BẮT BUỘC phải được khởi tạo trong MỌI constructor của lớp (trừ khi constructor đó gọi this(...) sang constructor khác đã khởi tạo x). Vì constructor rỗng không gán giá trị cho x nên trình biên dịch sẽ báo lỗi.",
        "difficulty": "medium",
        "tags": ["BlankFinal", "Constructor", "CompileError"]
    },
    {
        "id": "L1_Q55",
        "lessonId": 1,
        "type": "single",
        "title": "Xem xét bẫy nguy hiểm khi Constructor gọi phương thức ảo (overridable method):",
        "code": "class Parent {\n    Parent() {\n        init();\n    }\n    void init() {\n        System.out.print(\"P \");\n    }\n}\nclass Child extends Parent {\n    int count = 42;\n    void init() {\n        System.out.print(\"C:\" + count + \" \");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        new Child();\n    }\n}",
        "options": [
            "C:0 ",
            "C:42 ",
            "P C:42 ",
            "Lỗi biên dịch do không thể gọi phương thức ảo trong constructor"
        ],
        "correctAnswer": 0,
        "explanation": "Khi new Child(), constructor của Parent chạy trước. Constructor Parent gọi init(). Do tính đa hình động (Dynamic Binding), phương thức init() của lớp Child được gọi! Tuy nhiên, lúc này constructor của Child chưa chạy, và thuộc tính 'count = 42' chưa được khởi tạo (nó chỉ đang mang giá trị mặc định của kiểu int là 0). Vì vậy in ra 'C:0 '. Đây là lý do Java khuyến cáo KHÔNG bao giờ gọi phương thức overridable trong constructor.",
        "difficulty": "hard",
        "tags": ["ConstructorTrap", "DynamicBinding", "Polymorphism"]
    },
    {
        "id": "L1_Q56",
        "lessonId": 1,
        "type": "multiple",
        "title": "Các gói thư viện (package) nào sau đây được trình biên dịch Java tự động import ngầm định mà lập trình viên không cần viết lệnh 'import' tường minh?",
        "code": None,
        "options": [
            "Gói 'java.lang' (chứa String, Math, System, Thread, Object,...)",
            "Gói hiện tại (mọi class nằm cùng package với file đang viết)",
            "Gói 'java.util' (chứa List, Map, Scanner,...)",
            "Gói 'java.io' (chứa File, InputStream, OutputStream,...)"
        ],
        "correctAnswer": [0, 1],
        "explanation": "Java chỉ tự động import 2 thành phần: 1. Gói java.lang, 2. Tất cả các lớp trong cùng package hiện tại (hoặc default package nếu không khai báo package). Gói java.util và java.io bắt buộc phải import tường minh.",
        "difficulty": "easy",
        "tags": ["Import", "Package", "JavaLang"]
    },
    {
        "id": "L1_Q57",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định output của chương trình sau khi gặp hiện tượng Che giấu biến (Variable Shadowing):",
        "code": "public class ShadowTest {\n    int count = 100;\n    public void setCount(int count) {\n        count = count;\n    }\n    public static void main(String[] args) {\n        ShadowTest st = new ShadowTest();\n        st.setCount(500);\n        System.out.println(st.count);\n    }\n}",
        "options": [
            "100",
            "500",
            "0",
            "Lỗi biên dịch tại dòng count = count"
        ],
        "correctAnswer": 0,
        "explanation": "Trong phương thức setCount(int count), tham số cục bộ 'count' che giấu (shadows) trường instance 'count'. Câu lệnh 'count = count' chỉ gán giá trị của biến cục bộ cho chính nó, không làm thay đổi biến trường của đối tượng (đúng ra phải viết this.count = count). Do đó st.count vẫn giữ nguyên giá trị ban đầu là 100.",
        "difficulty": "easy",
        "tags": ["Shadowing", "This", "Variables"]
    },
    {
        "id": "L1_Q58",
        "lessonId": 1,
        "type": "single",
        "title": "Xác định output khi gọi nạp chồng giữa kiểu Object và kiểu String với đối số null:",
        "code": "public class NullOverload {\n    static void foo(Object o) {\n        System.out.println(\"Object\");\n    }\n    static void foo(String s) {\n        System.out.println(\"String\");\n    }\n    public static void main(String[] args) {\n        foo(null);\n    }\n}",
        "options": [
            "String",
            "Object",
            "Lỗi biên dịch do nhập nhằng",
            "Ném ngoại lệ NullPointerException"
        ],
        "correctAnswer": 0,
        "explanation": "Cả Object và String đều có thể nhận giá trị null. Tuy nhiên, String là lớp con của Object (cụ thể hơn Object trong hệ phân cấp). Quy tắc nạp chồng của Java quy định nếu có nhiều phương thức khớp, phương thức cụ thể nhất (most specific) sẽ được chọn. Vì String kế thừa Object nên foo(String) cụ thể hơn và được gọi.",
        "difficulty": "medium",
        "tags": ["Overloading", "Null", "Specific"]
    },
    {
        "id": "L1_Q59",
        "lessonId": 1,
        "type": "multiple",
        "title": "Những khai báo class nào sau đây là KHÔNG HỢP LỆ trong cú pháp Java?",
        "code": None,
        "options": [
            "public protected class MyClass {}",
            "final abstract class MyClass {}",
            "static class OuterClass {} (ở cấp độ top-level file)",
            "public final class MyClass {}"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1. Không thể kết hợp 2 mức truy cập (public protected). 2. Một class không thể vừa final (cấm kế thừa) vừa abstract (bắt buộc phải có lớp con kế thừa để thực thi). 3. Lớp top-level (ngoài cùng) không thể khai báo static (chỉ có nested class/inner class mới được static). Khai báo 'public final class' là hoàn toàn hợp lệ.",
        "difficulty": "medium",
        "tags": ["ClassDeclaration", "Modifiers", "Syntax"]
    },
    {
        "id": "L1_Q60",
        "lessonId": 1,
        "type": "single",
        "title": "Điều gì xảy ra khi cố tình gán lại giá trị cho tham số 'final' trong phương thức?",
        "code": "public class FinalParamTest {\n    void calculate(final int factor) {\n        factor = factor * 2; // DONG 3\n        System.out.println(factor);\n    }\n}",
        "options": [
            "Lỗi biên dịch tại DÒNG 3: cannot assign a value to final variable factor",
            "Biên dịch thành công và in ra giá trị gấp đôi",
            "Chỉ có cảnh báo warning, mã vẫn chạy bình thường",
            "Ném lỗi IllegalArgumentException tại runtime"
        ],
        "correctAnswer": 0,
        "explanation": "Khi một tham số của phương thức được đánh dấu là 'final', giá trị của nó được cố định ngay khi được truyền vào và không thể gán lại bất kỳ giá trị mới nào bên trong thân phương thức. Câu lệnh gán lại sẽ gây lỗi biên dịch 'cannot assign a value to final variable'.",
        "difficulty": "easy",
        "tags": ["Final", "Parameters", "CompileError"]
    }
]

L3_NEW = [
    # --- ĐỀ 3D (L3_Q46 - L3_Q60): Covariant Return Types, Overriding Exceptions & Super Chaining ---
    {
        "id": "L3_Q46",
        "lessonId": 3,
        "type": "single",
        "title": "Khái niệm Kiểu trả về đồng biến (Covariant Return Types) được giới thiệu từ Java 5 cho phép điều gì khi ghi đè phương thức (@Override)?",
        "code": None,
        "options": [
            "Phương thức ghi đè ở lớp con có thể khai báo kiểu trả về là một kiểu con (subtype) của kiểu trả về ở phương thức của lớp cha",
            "Phương thức ở lớp con có thể trả về bất kỳ kiểu dữ liệu nào kể cả kiểu nguyên thủy khác hoàn toàn",
            "Cho phép thay đổi kiểu trả về nhưng bắt buộc phải thay đổi cả danh sách tham số truyền vào",
            "Bắt buộc kiểu trả về ở lớp con phải rộng hơn kiểu trả về ở lớp cha"
        ],
        "correctAnswer": 0,
        "explanation": "Trước Java 5, phương thức ghi đè bắt buộc phải có kiểu trả về giống hệt lớp cha. Từ Java 5, Java hỗ trợ Covariant Return Type: phương thức ở lớp con được phép trả về kiểu con của kiểu ở lớp cha (ví dụ cha trả về Object, con có thể ghi đè trả về String; cha trả về Number, con trả về Integer).",
        "difficulty": "medium",
        "tags": ["Covariant", "Overriding", "Polymorphism"]
    },
    {
        "id": "L3_Q47",
        "lessonId": 3,
        "type": "single",
        "title": "Xem xét đoạn mã sau sử dụng Covariant Return Type. Đoạn mã có hợp lệ không và output là gì?",
        "code": "class SuperClass {\n    public Number getNum() {\n        return 10;\n    }\n}\nclass SubClass extends SuperClass {\n    @Override\n    public Integer getNum() {\n        return 20;\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        SubClass sub = new SubClass();\n        Integer result = sub.getNum();\n        System.out.println(result);\n    }\n}",
        "options": [
            "Hợp lệ hoàn toàn và in ra: 20",
            "Lỗi biên dịch vì phương thức ghi đè có kiểu trả về Integer khác với Number",
            "Lỗi biên dịch tại dòng gán result vì bắt buộc phải ép kiểu (Integer) sub.getNum()",
            "Ném ClassCastException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Vì Integer là lớp con của Number, SubClass ghi đè getNum() và khai báo kiểu trả về Integer là hoàn toàn hợp lệ theo quy tắc Covariant Return Type. Khi gọi qua tham chiếu SubClass, trình biên dịch nhận biết phương thức trả về Integer nên có thể gán trực tiếp vào biến Integer result mà không cần ép kiểu.",
        "difficulty": "medium",
        "tags": ["Covariant", "Integer", "Inheritance"]
    },
    {
        "id": "L3_Q48",
        "lessonId": 3,
        "type": "multiple",
        "title": "Khi một phương thức ở lớp con ghi đè một phương thức có mệnh đề 'throws CheckedException' từ lớp cha, phương thức ở lớp con ĐƯỢC PHÉP làm những điều nào sau đây?",
        "code": None,
        "options": [
            "Không khai báo ném bất kỳ ngoại lệ nào trong mệnh đề throws",
            "Khai báo ném cùng loại CheckedException hoặc một ngoại lệ con (subclass) của CheckedException đó",
            "Khai báo ném thêm bất kỳ Unchecked Exception nào (ví dụ NullPointerException, IllegalArgumentException)",
            "Khai báo ném một CheckedException mới hoàn toàn hoặc rộng hơn ngoại lệ của lớp cha (ví dụ cha ném IOException, con ném Exception)"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Quy tắc ghi đè ngoại lệ (Exception Overriding Rule): Phương thức con không bao giờ được ném Checked Exception rộng hơn hoặc mới hơn cha, vì điều này sẽ phá vỡ tính đa hình khi gọi qua tham chiếu cha. Phương thức con được phép: 1. Không ném gì, 2. Ném ngoại lệ con, 3. Ném bất kỳ RuntimeException (Unchecked Exception) nào.",
        "difficulty": "hard",
        "tags": ["ExceptionRules", "Overriding", "CheckedException"]
    },
    {
        "id": "L3_Q49",
        "lessonId": 3,
        "type": "single",
        "title": "Điều gì xảy ra khi biên dịch đoạn mã sau?",
        "code": "import java.io.IOException;\nclass A {\n    void readData() throws IOException {}\n}\nclass B extends A {\n    @Override\n    void readData() throws Exception {}\n}",
        "options": [
            "Lỗi biên dịch tại class B: readData() in B cannot override readData() in A; overridden method does not throw Exception",
            "Biên dịch thành công vì Exception là lớp cha của IOException",
            "Lỗi biên dịch vì bắt buộc phải khai báo try-catch bên trong hàm readData() của B",
            "Chỉ có cảnh báo warning khi biên dịch"
        ],
        "correctAnswer": 0,
        "explanation": "Phương thức lớp cha A ném IOException (một Checked Exception). Lớp con B cố tình khai báo throws Exception (là lớp cha rộng hơn IOException). Điều này vi phạm nghiêm trọng quy tắc ghi đè trong Java và gây lỗi biên dịch ngay lập tức.",
        "difficulty": "medium",
        "tags": ["ExceptionOverriding", "CompileError", "CheckedException"]
    },
    {
        "id": "L3_Q50",
        "lessonId": 3,
        "type": "single",
        "title": "Xác định output của chương trình sau khi xảy ra hiện tượng Che giấu thuộc tính (Field Hiding):",
        "code": "class Parent {\n    int val = 10;\n}\nclass Child extends Parent {\n    int val = 20;\n}\npublic class Main {\n    public static void main(String[] args) {\n        Parent p = new Child();\n        System.out.println(p.val + \" \" + ((Child) p).val);\n    }\n}",
        "options": [
            "10 20",
            "20 20",
            "10 10",
            "20 10"
        ],
        "correctAnswer": 0,
        "explanation": "Trong Java, các trường dữ liệu (fields) KHÔNG CÓ TÍNH ĐA HÌNH ĐỘNG (Fields are not polymorphic). Thuộc tính ở lớp con sẽ che giấu (hide) thuộc tính cùng tên ở lớp cha. Việc truy cập trường phụ thuộc hoàn toàn vào KIỂU CỦA BIẾN THAM CHIẾU tại thời điểm biên dịch. Vì biến 'p' có kiểu khai báo là Parent nên 'p.val' trỏ tới trường val của Parent (10). Khi ép kiểu '((Child) p).val' thì truy cập trường val của Child (20).",
        "difficulty": "hard",
        "tags": ["FieldHiding", "Polymorphism", "Binding"]
    },
    {
        "id": "L3_Q51",
        "lessonId": 3,
        "type": "multiple",
        "title": "Những thành phần nào sau đây trong một class Java KHÔNG THỂ bị ghi đè (@Override)?",
        "code": None,
        "options": [
            "Phương thức tĩnh (static methods) - vì chúng liên kết tĩnh tại compile-time và bị hiding",
            "Phương thức riêng tư (private methods) - vì không được kế thừa và không nhìn thấy ở lớp con",
            "Phương thức final (final methods) - vì từ khóa final tường minh ngăn cấm việc ghi đè",
            "Hàm khởi tạo (Constructors) - vì constructor không được kế thừa giữa các lớp"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Tất cả 4 thành phần trên đều không thể bị ghi đè: static methods (bị hiding), private methods (không được kế thừa), final methods (ngăn cấm ghi đè), constructors (không phải phương thức và không được kế thừa).",
        "difficulty": "medium",
        "tags": ["OverridingRules", "Static", "Final", "Private"]
    },
    {
        "id": "L3_Q52",
        "lessonId": 3,
        "type": "single",
        "title": "Điều gì xảy ra khi lớp cha chỉ có constructor nhận tham số và lớp con không gọi super(args)?",
        "code": "class Parent {\n    Parent(String name) {}\n}\nclass Child extends Parent {\n    Child() {}\n}",
        "options": [
            "Lỗi biên dịch: Implicit super constructor Parent() is undefined for default constructor",
            "Biên dịch thành công và JVM tự động truyền null vào constructor của Parent",
            "Lớp Child tự động tạo một constructor không tham số cho Parent",
            "Lỗi runtime khi khởi tạo đối tượng Child"
        ],
        "correctAnswer": 0,
        "explanation": "Khi một lớp con không gọi tường minh super(...) trong constructor của nó, trình biên dịch sẽ tự động chèn lời gọi super() không tham số. Nhưng lớp Parent đã định nghĩa một constructor nhận String, nên compiler không sinh constructor mặc định rỗng cho Parent nữa. Vì Parent() không tồn tại nên lệnh gọi ngầm định super() gây lỗi biên dịch.",
        "difficulty": "medium",
        "tags": ["ConstructorChaining", "Super", "CompileError"]
    },
    {
        "id": "L3_Q53",
        "lessonId": 3,
        "type": "single",
        "title": "Khi ghi đè một phương thức, điều gì xảy ra nếu lớp con cố tình thu hẹp phạm vi truy cập (narrowing access privileges)?",
        "code": "class Parent {\n    public void display() {}\n}\nclass Child extends Parent {\n    @Override\n    protected void display() {} // Thu hep tu public xuong protected\n}",
        "options": [
            "Lỗi biên dịch: Cannot reduce the visibility of the inherited method from Parent",
            "Biên dịch thành công bình thường",
            "Chỉ có cảnh báo bảo mật warning",
            "Lỗi ClassCastException tại runtime"
        ],
        "correctAnswer": 0,
        "explanation": "Quy tắc cơ bản của ghi đè trong OOP/Java là: Phạm vi truy cập của phương thức ghi đè ở lớp con không bao giờ được hẹp hơn phương thức ở lớp cha (quyền hạn chỉ có thể bằng hoặc rộng hơn: public -> public; protected -> protected hoặc public; default -> default, protected hoặc public).",
        "difficulty": "easy",
        "tags": ["AccessModifiers", "Overriding", "CompileError"]
    },
    {
        "id": "L3_Q54",
        "lessonId": 3,
        "type": "multiple",
        "title": "Chú thích '@Override' trong Java mang lại những lợi ích quan trọng nào?",
        "code": None,
        "options": [
            "Yêu cầu trình biên dịch kiểm tra chặt chẽ xem phương thức đó có thực sự ghi đè phương thức nào từ lớp cha hay không; nếu gõ sai tên hoặc sai kiểu tham số thì báo lỗi ngay",
            "Giúp người đọc mã nhận biết rõ ràng phương thức này được thiết kế để thay đổi hành vi của lớp cha",
            "Bắt buộc JVM phải dùng thuật toán tối ưu hóa vtable riêng để tăng tốc độ thực thi",
            "Tự động xóa bỏ hoàn toàn mã nguồn của phương thức lớp cha khỏi bộ nhớ"
        ],
        "correctAnswer": [0, 1],
        "explanation": "Annotation @Override là một compile-time check hữu hiệu giúp ngăn ngừa các lỗi đánh máy sai tên hàm hoặc sai chữ ký tham số (vô tình biến thành overloading thay vì overriding) và nâng cao tính dễ đọc của mã. Nó không can thiệp vào cơ chế tối ưu vtable hay xóa mã của JVM.",
        "difficulty": "easy",
        "tags": ["OverrideAnnotation", "BestPractice", "Compiler"]
    },
    {
        "id": "L3_Q55",
        "lessonId": 3,
        "type": "single",
        "title": "Xác định output của chương trình sau khi sử dụng từ khóa super trong phương thức ghi đè:",
        "code": "class Base {\n    void greet() {\n        System.out.print(\"Hello \");\n    }\n}\nclass Derived extends Base {\n    @Override\n    void greet() {\n        super.greet();\n        System.out.print(\"World\");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Base b = new Derived();\n        b.greet();\n    }\n}",
        "options": [
            "Hello World",
            "World Hello",
            "World",
            "Hello "
        ],
        "correctAnswer": 0,
        "explanation": "Biến b trỏ tới đối tượng Derived. Do liên kết động, b.greet() gọi Derived.greet(). Trong phương thức này, lệnh super.greet() gọi phiên bản của lớp Base in 'Hello ', sau đó in tiếp 'World'. Kết quả là 'Hello World'.",
        "difficulty": "easy",
        "tags": ["SuperMethod", "Overriding", "Output"]
    },
    {
        "id": "L3_Q56",
        "lessonId": 3,
        "type": "multiple",
        "title": "Những khẳng định nào sau đây về từ khóa 'super' trong Java là ĐÚNG?",
        "code": None,
        "options": [
            "Từ khóa 'super' dùng để gọi constructor của lớp cha trực tiếp thông qua cú pháp super(...) bên trong constructor của con",
            "Từ khóa 'super' dùng để truy cập các phương thức hoặc thuộc tính của lớp cha bị lớp con che giấu hoặc ghi đè",
            "Không thể sử dụng từ khóa 'super' bên trong các phương thức tĩnh (static methods) hoặc khối tĩnh",
            "Có thể dùng cú pháp 'super.super.method()' để gọi phương thức của lớp ông nội trong cây kế thừa"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Java không cho phép cú pháp 'super.super' (tính đóng gói của OOP quy định một lớp con chỉ tương tác trực tiếp với lớp cha trực tiếp của nó). Từ khóa super là tham chiếu instance nên không thể dùng trong static context.",
        "difficulty": "medium",
        "tags": ["Super", "StaticContext", "Syntax"]
    },
    {
        "id": "L3_Q57",
        "lessonId": 3,
        "type": "single",
        "title": "Trong cây kế thừa 3 cấp: Class A -> Class B -> Class C. Làm thế nào để từ phương thức của Class C gọi được trực tiếp phương thức do Class A định nghĩa mà đã bị Class B ghi đè?",
        "code": None,
        "options": [
            "Trong Java không có cú pháp nào (như super.super) cho phép lớp cháu gọi trực tiếp phương thức bị che bởi lớp cha trực tiếp",
            "Sử dụng cú pháp: super.super.method()",
            "Sử dụng cú pháp: ((A) super).method()",
            "Sử dụng cú pháp: A.super.method()"
        ],
        "correctAnswer": 0,
        "explanation": "Trong Java, bạn không thể bỏ qua lớp cha trực tiếp để gọi phương thức của lớp ông nội (không hỗ trợ super.super). Điều này nhằm bảo vệ nguyên lý đóng gói (Encapsulation). Cú pháp A.super.method() chỉ dùng cho interface default methods.",
        "difficulty": "hard",
        "tags": ["SuperSuper", "Encapsulation", "JavaRules"]
    },
    {
        "id": "L3_Q58",
        "lessonId": 3,
        "type": "single",
        "title": "Cho lớp cha ném SQLException, lớp con ghi đè không ném ngoại lệ nào. Khi gọi phương thức qua biến tham chiếu kiểu cha, điều gì xảy ra?",
        "code": "import java.sql.SQLException;\nclass Parent {\n    void query() throws SQLException {}\n}\nclass Child extends Parent {\n    @Override\n    void query() {} // Khong nem ngoai le\n}\npublic class Main {\n    public static void main(String[] args) {\n        Parent p = new Child();\n        p.query(); // DONG NAY\n    }\n}",
        "options": [
            "Dòng gọi p.query() vẫn bị lỗi biên dịch nếu không được đặt trong khối try-catch hoặc phương thức main khai báo throws SQLException",
            "Biên dịch hoàn toàn bình thường vì đối tượng thực tế Child không ném ngoại lệ nào",
            "Lỗi runtime khi chạy lệnh p.query()",
            "Trình biên dịch tự động loại bỏ SQLException tại runtime"
        ],
        "correctAnswer": 0,
        "explanation": "Trình biên dịch kiểm tra an toàn kiểu tại Compile-Time dựa trên KIỂU KHAI BÁO CỦA THAM CHIẾU (Static Type). Biến p có kiểu là Parent, mà phương thức query() của Parent khai báo throws SQLException, do đó compiler bắt buộc người gọi phải xử lý SQLException (try-catch hoặc throws) dù đối tượng thực tế tại runtime là Child không ném ngoại lệ.",
        "difficulty": "hard",
        "tags": ["CompileTimeCheck", "CheckedException", "Polymorphism"]
    },
    {
        "id": "L3_Q59",
        "lessonId": 3,
        "type": "multiple",
        "title": "Nguyên lý 'Ưu tiên kết hợp/bao hàm hơn kế thừa' (Favor Composition over Inheritance) được khuyến nghị trong OOP vì những lý do nào sau đây?",
        "code": None,
        "options": [
            "Kế thừa tạo ra mối liên kết chặt chẽ (tight coupling), làm lộ chi tiết cài đặt của lớp cha cho lớp con (phá vỡ tính đóng gói)",
            "Khi lớp cha thay đổi mã nguồn, các lớp con có nguy cơ bị lỗi ngoài dự kiến (Fragile Base Class problem)",
            "Composition (Bao hàm) cho phép thay đổi hành vi linh hoạt tại thời điểm thực thi (Runtime) bằng cách thay thế đối tượng thành phần",
            "Kế thừa tiêu tốn gấp 10 lần bộ nhớ Heap so với Composition trong mọi trường hợp"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Kế thừa là liên kết tĩnh chặt chẽ kiểu 'is-a' dễ dẫn tới lỗi Fragile Base Class khi lớp cha sửa đổi. Composition tạo liên kết lỏng kiểu 'has-a', bảo toàn tính đóng gói và có thể tráo đổi component linh hoạt tại runtime (như trong Strategy pattern). Tiêu tốn bộ nhớ không phải lý do chính và con số '10 lần' là vô căn cứ.",
        "difficulty": "medium",
        "tags": ["Composition", "Inheritance", "DesignPrinciple"]
    },
    {
        "id": "L3_Q60",
        "lessonId": 3,
        "type": "single",
        "title": "Xác định output của chương trình kết hợp cả ghi đè phương thức và che giấu thuộc tính:",
        "code": "class A {\n    String name = \"ClassA\";\n    String getName() { return name; }\n}\nclass B extends A {\n    String name = \"ClassB\";\n    String getName() { return name; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        A obj = new B();\n        System.out.println(obj.name + \"-\" + obj.getName());\n    }\n}",
        "options": [
            "ClassA-ClassB",
            "ClassB-ClassB",
            "ClassA-ClassA",
            "ClassB-ClassA"
        ],
        "correctAnswer": 0,
        "explanation": "obj có kiểu tham chiếu là A, đối tượng thực tế là B. 1. obj.name là truy cập thuộc tính (không đa hình) -> lấy thuộc tính name của Class A là 'ClassA'. 2. obj.getName() là gọi phương thức ảo (đa hình động) -> gọi phương thức getName() của Class B, trả về thuộc tính name của B là 'ClassB'. Kết hợp lại in ra 'ClassA-ClassB'.",
        "difficulty": "hard",
        "tags": ["FieldHiding", "MethodOverriding", "TrickyOutput"]
    },

    # --- ĐỀ 3E (L3_Q61 - L3_Q75): Dynamic Method Dispatch, Complex Downcasting & Instanceof ---
    {
        "id": "L3_Q61",
        "lessonId": 3,
        "type": "single",
        "title": "Bản chất của bảng phương thức ảo (Virtual Method Table - vtable) trong JVM phục vụ cơ chế Dynamic Method Dispatch là gì?",
        "code": None,
        "options": [
            "Là một mảng các con trỏ hàm/phương thức được tạo cho mỗi class tại thời điểm nạp lớp, giúp JVM tra cứu nhanh địa chỉ cài đặt thực tế của phương thức ứng với đối tượng trong Heap",
            "Là bảng băm chứa mã nguồn bytecode chưa được thông dịch của tất cả các hàm private",
            "Là vùng nhớ Stack lưu trữ các biến cục bộ của hàm main",
            "Là cơ chế chỉ áp dụng cho các phương thức tĩnh (static methods)"
        ],
        "correctAnswer": 0,
        "explanation": "Khi một class được load, JVM tạo ra một vtable cho class đó chứa địa chỉ của tất cả các virtual methods (instance methods có thể override). Khi gọi invokevirtual, JVM dùng offset cố định trong vtable của đối tượng runtime thực tế để nhảy đến mã thực thi, giúp thực hiện đa hình động cực nhanh O(1).",
        "difficulty": "hard",
        "tags": ["vtable", "DynamicDispatch", "JVMInternals"]
    },
    {
        "id": "L3_Q62",
        "lessonId": 3,
        "type": "single",
        "title": "Xác định output của đoạn mã Static Method Hiding sau:",
        "code": "class Writer {\n    public static void write() {\n        System.out.print(\"Writing...\");\n    }\n}\nclass Author extends Writer {\n    public static void write() {\n        System.out.print(\"Authoring...\");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Writer w = new Author();\n        w.write();\n        ((Author) w).write();\n    }\n}",
        "options": [
            "Writing...Authoring...",
            "Authoring...Authoring...",
            "Writing...Writing...",
            "Authoring...Writing..."
        ],
        "correctAnswer": 0,
        "explanation": "Phương thức static không được ghi đè mà bị che giấu (method hiding). Việc gọi phương thức static qua tham chiếu biến phụ thuộc vào KIỂU CỦA BIẾN THAM CHIẾU: 1. Biến w có kiểu Writer nên w.write() gọi Writer.write() in 'Writing...'. 2. Biến ép kiểu ((Author) w) có kiểu Author nên gọi Author.write() in 'Authoring...'.",
        "difficulty": "medium",
        "tags": ["StaticHiding", "StaticMethod", "Binding"]
    },
    {
        "id": "L3_Q63",
        "lessonId": 3,
        "type": "multiple",
        "title": "Những nhận định nào sau đây về cơ chế Ép kiểu đối tượng (Reference Type Casting) trong Java là ĐÚNG?",
        "code": None,
        "options": [
            "Upcasting (ép kiểu lên lớp cha) luôn an toàn và được JVM thực hiện tự động ngầm định",
            "Downcasting (ép kiểu xuống lớp con) bắt buộc phải viết cú pháp ép kiểu tường minh và tiềm ẩn nguy cơ ném ngoại lệ ClassCastException tại runtime",
            "Trình biên dịch chỉ cho phép ép kiểu giữa hai kiểu tham chiếu nếu chúng thuộc cùng một cây phân cấp kế thừa",
            "Ép kiểu trong Java làm thay đổi kiểu thực tế của đối tượng nằm trong vùng nhớ Heap"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Ép kiểu chỉ thay đổi góc nhìn (kiểu tham chiếu) của biến trỏ tới đối tượng, hoàn toàn KHÔNG THAY ĐỔI kiểu đối tượng thực sự trong Heap (đối tượng sinh ra bằng 'new X()' thì bản chất mãi mãi là X). 3 ý kiến đầu đều hoàn toàn chính xác theo đặc tả Java.",
        "difficulty": "medium",
        "tags": ["Casting", "Upcasting", "Downcasting"]
    },
    {
        "id": "L3_Q64",
        "lessonId": 3,
        "type": "single",
        "title": "Điều gì xảy ra khi chạy đoạn mã Downcasting sai đối tượng sau?",
        "code": "class Animal {}\nclass Dog extends Animal {}\nclass Cat extends Animal {}\npublic class Main {\n    public static void main(String[] args) {\n        Animal a = new Dog();\n        Cat c = (Cat) a;\n    }\n}",
        "options": [
            "Biên dịch thành công nhưng ném ngoại lệ ClassCastException tại thời điểm runtime",
            "Lỗi biên dịch ngay tại dòng Cat c = (Cat) a;",
            "Biến c sẽ nhận giá trị null mà không có lỗi",
            "Chương trình chạy bình thường không có lỗi"
        ],
        "correctAnswer": 0,
        "explanation": "Vì Animal và Cat cùng nằm trong một cây kế thừa, trình biên dịch cho phép phép ép kiểu (Cat) a qua cửa compile-time. Tuy nhiên, tại runtime, JVM kiểm tra thấy đối tượng thực tế trong Heap là Dog, không thể chuyển thành Cat, do đó ném ngoại lệ java.lang.ClassCastException.",
        "difficulty": "easy",
        "tags": ["ClassCastException", "Downcasting", "RuntimeError"]
    },
    {
        "id": "L3_Q65",
        "lessonId": 3,
        "type": "single",
        "title": "Điều gì xảy ra khi cố gắng ép kiểu giữa hai lớp không có quan hệ kế thừa:",
        "code": "public class Main {\n    public static void main(String[] args) {\n        String str = \"Hello\";\n        Integer num = (Integer) str;\n    }\n}",
        "options": [
            "Lỗi biên dịch: Cannot cast 'java.lang.String' to 'java.lang.Integer'",
            "Ném ClassCastException khi chạy",
            "Biến num nhận giá trị null",
            "Chuyển đổi chuỗi thành số nguyên 0"
        ],
        "correctAnswer": 0,
        "explanation": "String và Integer không cùng một nhánh kế thừa (String không kế thừa Integer và ngược lại, cả hai đều là lớp con trực tiếp của Object và đều là final). Trình biên dịch Java phát hiện điều này và báo lỗi biên dịch ngay lập tức (Inconvertible types).",
        "difficulty": "easy",
        "tags": ["CompileError", "Casting", "TypeHierarchy"]
    },
    {
        "id": "L3_Q66",
        "lessonId": 3,
        "type": "multiple",
        "title": "Cho phân cấp: Grandparent -> Parent -> Child. Với khai báo: Parent p = new Child(); Những biểu thức ép kiểu nào sau đây là HỢP LỆ và KHÔNG gây lỗi ClassCastException khi chạy?",
        "code": None,
        "options": [
            "Grandparent gp = (Grandparent) p;",
            "Child c = (Child) p;",
            "Object obj = (Object) p;",
            "String s = (String) p;"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Đối tượng thực tế trong Heap là Child. 1. Upcast lên Grandparent: an toàn. 2. Downcast xuống Child: an toàn vì đối tượng thực sự là Child. 3. Upcast lên Object: luôn an toàn. 4. Ép kiểu sang String: gây lỗi biên dịch ngay lập tức vì không cùng phân cấp.",
        "difficulty": "medium",
        "tags": ["Casting", "Hierarchy", "Upcasting"]
    },
    {
        "id": "L3_Q67",
        "lessonId": 3,
        "type": "single",
        "title": "Xác định kết quả của biểu thức 'null instanceof AnyClass' trong Java:",
        "code": "String s = null;\nSystem.out.println(s instanceof String);",
        "options": [
            "false",
            "true",
            "Ném NullPointerException",
            "Lỗi biên dịch"
        ],
        "correctAnswer": 0,
        "explanation": "Theo đặc tả JLS, toán tử instanceof luôn trả về false nếu toán hạng bên trái có giá trị là null, bất kể kiểu kiểm tra bên phải là lớp hay interface nào, và không bao giờ ném NullPointerException.",
        "difficulty": "easy",
        "tags": ["Instanceof", "Null", "Safety"]
    },
    {
        "id": "L3_Q68",
        "lessonId": 3,
        "type": "multiple",
        "title": "Toán tử 'instanceof' trong Java trả về 'true' khi biểu thức kiểm tra 'obj instanceof TargetType' thỏa mãn những điều kiện nào sau đây?",
        "code": None,
        "options": [
            "obj khác null",
            "Đối tượng thực tế trong Heap là thể hiện của lớp TargetType hoặc bất kỳ lớp con nào của TargetType",
            "TargetType là một Interface và lớp của obj có thực thi interface đó (hoặc kế thừa lớp thực thi interface đó)",
            "Chỉ cần biến tham chiếu obj được khai báo với kiểu TargetType ở compile-time"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "instanceof kiểm tra kiểu thực tế của đối tượng tại runtime. Nó trả về true nếu obj khác null và đối tượng là instance của TargetType hoặc con/thực thi của TargetType. Nó không phụ thuộc vào kiểu khai báo compile-time của biến.",
        "difficulty": "medium",
        "tags": ["Instanceof", "RuntimeCheck", "TypeRules"]
    },
    {
        "id": "L3_Q69",
        "lessonId": 3,
        "type": "single",
        "title": "Từ Java 16, tính năng 'Pattern Matching for instanceof' cho phép viết code như sau. Lợi ích lớn nhất là gì?",
        "code": "if (obj instanceof String s) {\n    System.out.println(s.length());\n}",
        "options": [
            "Tự động khai báo biến 's' và ép kiểu sang String an toàn nếu điều kiện đúng, loại bỏ hoàn toàn dòng ép kiểu thủ công '(String) obj'",
            "Làm cho toán tử instanceof có thể kiểm tra được cả các kiểu dữ liệu nguyên thủy như int, double",
            "Cho phép biến 's' tồn tại và sử dụng ở toàn bộ phạm vi bên ngoài câu lệnh if",
            "Chuyển đổi kiểu dữ liệu của biến obj từ Object sang String vĩnh viễn"
        ],
        "correctAnswer": 0,
        "explanation": "Pattern matching for instanceof kết hợp kiểm tra kiểu và ép kiểu trong một câu lệnh duy nhất. Nếu obj là String, biến 's' được tự động khởi tạo với kiểu String trong phạm vi của khối if, giúp code ngắn gọn, rõ ràng và tránh lỗi ép kiểu.",
        "difficulty": "easy",
        "tags": ["PatternMatching", "ModernJava", "CleanCode"]
    },
    {
        "id": "L3_Q70",
        "lessonId": 3,
        "type": "single",
        "title": "Xem xét đoạn mã sau với Interface và Downcasting. Điều gì xảy ra khi chạy?",
        "code": "import java.io.Serializable;\nimport java.util.*;\npublic class InterfaceCastTest {\n    public static void main(String[] args) {\n        List<String> list = new ArrayList<>();\n        Serializable s = (Serializable) list;\n        System.out.println(\"Success\");\n    }\n}",
        "options": [
            "Biên dịch và chạy thành công, in ra: Success (vì ArrayList có implements Serializable)",
            "Lỗi biên dịch vì List không kế thừa Serializable",
            "Ném ClassCastException tại runtime",
            "Lỗi biên dịch vì không thể ép kiểu sang Interface"
        ],
        "correctAnswer": 0,
        "explanation": "Trong Java, ArrayList có implements Serializable. Mặc dù biến tham chiếu 'list' có kiểu là List (interface này không extends Serializable), nhưng đối tượng thực tế là ArrayList. Trình biên dịch cho phép ép kiểu sang một interface bất kỳ nếu lớp của tham chiếu không phải là final class. Tại runtime, ArrayList thực sự implements Serializable nên phép cast thành công 100%.",
        "difficulty": "hard",
        "tags": ["InterfaceCast", "ArrayList", "Serializable"]
    },
    {
        "id": "L3_Q71",
        "lessonId": 3,
        "type": "multiple",
        "title": "Việc lạm dụng toán tử 'instanceof' và ép kiểu thủ công Downcasting trong thiết kế phần mềm thường phản ánh vấn đề gì và nên thay thế bằng giải pháp nào?",
        "code": None,
        "options": [
            "Vi phạm nguyên tắc Mở/Đóng (Open/Closed Principle) vì mỗi khi thêm lớp mới, phải sửa đổi chuỗi if-else instanceof",
            "Nên thay thế bằng tính Đa hình (Polymorphism): định nghĩa phương thức trừu tượng ở lớp cha/interface để mỗi lớp con tự cài đặt hành vi riêng",
            "Có thể áp dụng mẫu thiết kế Visitor Pattern để mở rộng xử lý trên tập hợp các lớp có phân cấp",
            "Việc dùng instanceof là phương pháp được khuyến khích hàng đầu trong mọi trường hợp xử lý kế thừa"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Chuỗi 'if (a instanceof Dog) ... else if (a instanceof Cat) ...' là một 'Code Smell' điển hình vi phạm OCP. Khi có thêm lớp mới, toàn bộ khối if-else phải sửa lại. Giải pháp hướng đối tượng chuẩn mực là dùng tính Đa hình hoặc Visitor pattern.",
        "difficulty": "medium",
        "tags": ["CodeSmell", "Polymorphism", "Refactoring", "OCP"]
    },
    {
        "id": "L3_Q72",
        "lessonId": 3,
        "type": "single",
        "title": "Cho phân cấp lớp: Class A, Class B extends A, Class C extends B. Dòng mã nào sau đây gây ra lỗi ném ClassCastException?",
        "code": "A a = new B();\n// Xet cac dong:\n// D1: B b = (B) a;\n// D2: C c = (C) a;\n// D3: A a2 = (A) a;",
        "options": [
            "D2 gây ClassCastException vì đối tượng thực tế là B, không thể ép kiểu xuống lớp con C",
            "D1 gây ClassCastException",
            "D3 gây ClassCastException",
            "Không có dòng nào gây lỗi, cả 3 dòng đều chạy bình thường"
        ],
        "correctAnswer": 0,
        "explanation": "Đối tượng trong Heap là thể hiện của lớp B. D1: ép sang B (hợp lệ). D3: ép sang A (upcast, hợp lệ). D2: cố downcast đối tượng B xuống C (trong khi B không phải là instance của C), do đó JVM ném ClassCastException.",
        "difficulty": "medium",
        "tags": ["Downcasting", "ClassCastException", "Hierarchy"]
    },
    {
        "id": "L3_Q73",
        "lessonId": 3,
        "type": "single",
        "title": "Điều gì xảy ra khi cố gắng gọi phương thức private của lớp cha thông qua biến tham chiếu của lớp cha trỏ tới lớp con?",
        "code": "class Parent {\n    private void secret() {\n        System.out.println(\"Parent Secret\");\n    }\n}\nclass Child extends Parent {\n    public void secret() {\n        System.out.println(\"Child Secret\");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Parent p = new Child();\n        p.secret(); // DONG NAY\n    }\n}",
        "options": [
            "Lỗi biên dịch: Phương thức secret() có mức truy cập private trong Parent nên không thể gọi từ bên ngoài",
            "In ra: Child Secret (do tính đa hình động)",
            "In ra: Parent Secret",
            "Ném ngoại lệ IllegalAccessException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Phương thức private trong lớp Parent không được kế thừa và chỉ có thể truy cập nội bộ trong Parent. Khi gọi p.secret() từ class Main, trình biên dịch kiểm tra kiểu của biến p là Parent và thấy phương thức là private, do đó báo lỗi biên dịch ngay tại dòng này. Không có đa hình đối với phương thức private.",
        "difficulty": "medium",
        "tags": ["PrivateMethods", "CompileError", "Encapsulation"]
    },
    {
        "id": "L3_Q74",
        "lessonId": 3,
        "type": "multiple",
        "title": "Những dòng mã nào sau đây thực hiện Upcasting hợp lệ trong Java?",
        "code": None,
        "options": [
            "Object obj = \"Java Programming\";",
            "Number num = Integer.valueOf(42);",
            "CharSequence cs = new StringBuilder(\"Test\");",
            "Integer val = (Integer) new Object();"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Upcasting là gán đối tượng của lớp con cho biến tham chiếu của lớp cha hoặc interface mà nó thực thi: String là Object, Integer là Number, StringBuilder implements CharSequence. Dòng 4 là Downcasting đối tượng Object xuống Integer và sẽ ném ClassCastException tại runtime.",
        "difficulty": "easy",
        "tags": ["Upcasting", "Reference", "TypeSafety"]
    },
    {
        "id": "L3_Q75",
        "lessonId": 3,
        "type": "single",
        "title": "Xác định output của chương trình tổng hợp phân cấp và đa hình sau:",
        "code": "class Vehicle {\n    String getType() { return \"Vehicle\"; }\n}\nclass Car extends Vehicle {\n    String getType() { return \"Car\"; }\n}\nclass SportsCar extends Car {\n    String getType() { return \"SportsCar\"; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Vehicle v = new SportsCar();\n        Car c = (Car) v;\n        System.out.println(v.getType() + \"-\" + c.getType());\n    }\n}",
        "options": [
            "SportsCar-SportsCar",
            "Vehicle-Car",
            "Vehicle-SportsCar",
            "Car-SportsCar"
        ],
        "correctAnswer": 0,
        "explanation": "Đối tượng thực sự duy nhất trong Heap là SportsCar. Cả v và c đều đang trỏ tới đối tượng này. Vì phương thức getType() là phương thức ảo được ghi đè, việc gọi phương thức luôn được liên kết động tới cài đặt của đối tượng thực tế trong Heap (SportsCar), bất kể biến tham chiếu là Vehicle hay Car. Do đó cả hai lời gọi đều trả về 'SportsCar', output là 'SportsCar-SportsCar'.",
        "difficulty": "medium",
        "tags": ["DynamicBinding", "Polymorphism", "Output"]
    }
]

L4_NEW = [
    # --- ĐỀ 4D (L4_Q46 - L4_Q60): Interface Default, Static, Private Methods & Multiple Inheritance Conflicts ---
    {
        "id": "L4_Q46",
        "lessonId": 4,
        "type": "single",
        "title": "Mục tiêu quan trọng nhất của việc Java 8 bổ sung phương thức 'default' vào Interface là gì?",
        "code": None,
        "options": [
            "Cho phép mở rộng thêm phương thức mới vào interface có sẵn mà không làm phá vỡ (breaking changes) mã nguồn của các lớp đã thực thi interface đó trước đây",
            "Để dần thay thế hoàn toàn lớp trừu tượng (Abstract class) trong mọi thiết kế",
            "Để biến tất cả các phương thức trong interface thành phương thức tĩnh",
            "Để tăng tốc độ biên dịch của trình biên dịch javac"
        ],
        "correctAnswer": 0,
        "explanation": "Trước Java 8, thêm một method mới vào interface sẽ làm mọi class đang implement interface đó bị lỗi biên dịch. Nhằm bổ sung Stream API và lambda vào Collections Framework (như List.sort(), Collection.stream()) mà không phá vỡ mã nguồn cũ, Java 8 đưa ra 'default method' để cung cấp sẵn phần thân cài đặt mặc định.",
        "difficulty": "medium",
        "tags": ["DefaultMethod", "BackwardCompatibility", "Interface"]
    },
    {
        "id": "L4_Q47",
        "lessonId": 4,
        "type": "single",
        "title": "Điều gì xảy ra khi một lớp implement cả hai Interface cùng có default method với chữ ký giống hệt nhau (The Diamond Problem)?",
        "code": "interface A {\n    default void msg() { System.out.println(\"A\"); }\n}\ninterface B {\n    default void msg() { System.out.println(\"B\"); }\n}\nclass C implements A, B {}\n",
        "options": [
            "Lỗi biên dịch tại class C: inherits unrelated defaults for msg() from types A and B",
            "Biên dịch thành công và ưu tiên thực thi phương thức của interface A vì khai báo trước",
            "Ném ngoại lệ AmbiguousMethodException tại runtime",
            "Biên dịch thành công và in ra cả hai chuỗi 'A' và 'B'"
        ],
        "correctAnswer": 0,
        "explanation": "Khi có xung đột giữa hai default method cùng cấp từ 2 interface, Java từ chối tự phán đoán và báo lỗi biên dịch ngay lập tức. Lớp C bắt buộc phải ghi đè lại phương thức msg() để giải quyết nhập nhằng.",
        "difficulty": "medium",
        "tags": ["DiamondProblem", "DefaultMethod", "CompileError"]
    },
    {
        "id": "L4_Q48",
        "lessonId": 4,
        "type": "single",
        "title": "Để giải quyết xung đột default method giữa hai interface A và B trong lớp C, cú pháp nào sau đây là CHÍNH XÁC?",
        "code": "class C implements A, B {\n    @Override\n    public void msg() {\n        // Goi cai dat cua interface A\n    }\n}",
        "options": [
            "A.super.msg();",
            "super.A.msg();",
            "A.this.msg();",
            "super(A).msg();"
        ],
        "correctAnswer": 0,
        "explanation": "Cú pháp chuẩn của Java để chỉ định gọi default method của một interface cụ thể là: InterfaceName.super.methodName(). Ví dụ: A.super.msg();",
        "difficulty": "easy",
        "tags": ["InterfaceSuper", "Syntax", "Resolution"]
    },
    {
        "id": "L4_Q49",
        "lessonId": 4,
        "type": "multiple",
        "title": "Theo các quy tắc giải quyết xung đột phương thức mặc định (Default Method Resolution Rules) trong Java 8, những quy tắc nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "Quy tắc 1 (Class always wins): Phương thức được cài đặt trong lớp cha (superclass) luôn được ưu tiên cao hơn bất kỳ default method nào từ interface",
            "Quy tắc 2 (Sub-interface wins): Interface con cụ thể hơn kế thừa từ interface cha sẽ được ưu tiên hơn interface cha",
            "Quy tắc 3: Nếu có xung đột giữa hai interface ngang hàng không có quan hệ kế thừa, lớp thực thi bắt buộc phải override tường minh",
            "Quy tắc 4: Interface nào có tên đứng trước theo thứ tự bảng chữ cái sẽ luôn được ưu tiên thực thi"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "3 quy tắc giải quyết xung đột default methods của Java là: 1. Lớp cha luôn thắng interface, 2. Interface con thắng interface cha, 3. Nếu vẫn xung đột ngang hàng thì class phải override. Thứ tự bảng chữ cái không có bất kỳ ý nghĩa nào trong JVM.",
        "difficulty": "hard",
        "tags": ["DefaultMethodRules", "JLS", "Resolution"]
    },
    {
        "id": "L4_Q50",
        "lessonId": 4,
        "type": "single",
        "title": "Xác định output của chương trình sau áp dụng quy tắc 'Class always wins':",
        "code": "interface Greeting {\n    default void hello() {\n        System.out.println(\"Interface Hello\");\n    }\n}\nclass Parent {\n    public void hello() {\n        System.out.println(\"Class Hello\");\n    }\n}\nclass Child extends Parent implements Greeting {}\npublic class Main {\n    public static void main(String[] args) {\n        new Child().hello();\n    }\n}",
        "options": [
            "Class Hello",
            "Interface Hello",
            "Lỗi biên dịch do xung đột phương thức",
            "In ra cả hai dòng"
        ],
        "correctAnswer": 0,
        "explanation": "Theo quy tắc 'Class always wins', cài đặt phương thức public void hello() từ lớp cha Parent luôn luôn chiếm ưu thế tuyệt đối so với default method cùng chữ ký của interface Greeting. Do đó in ra 'Class Hello' mà không có lỗi biên dịch.",
        "difficulty": "medium",
        "tags": ["ClassWins", "DefaultMethod", "Resolution"]
    },
    {
        "id": "L4_Q51",
        "lessonId": 4,
        "type": "multiple",
        "title": "Những khẳng định nào sau đây về phương thức 'static' trong Interface (từ Java 8) là ĐÚNG?",
        "code": None,
        "options": [
            "Phương thức static trong interface KHÔNG ĐƯỢC kế thừa bởi các lớp implement interface đó",
            "Chỉ có thể gọi phương thức static thông qua tên của chính Interface đó (ví dụ MyInterface.myStaticMethod())",
            "Không thể gọi phương thức static của interface thông qua tên lớp con hoặc thể hiện của lớp con (ví dụ MyClass.myStaticMethod() hoặc instance.myStaticMethod() đều gây lỗi biên dịch)",
            "Phương thức static trong interface có thể được ghi đè bằng annotation @Override ở lớp con"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Phương thức static trong interface thuộc về riêng interface đó và không được kế thừa xuống các class implement. Lớp con không thể gọi hay override phương thức static này. Muốn gọi bắt buộc phải dùng cú pháp InterfaceName.methodName().",
        "difficulty": "hard",
        "tags": ["InterfaceStatic", "StaticMethod", "Java8"]
    },
    {
        "id": "L4_Q52",
        "lessonId": 4,
        "type": "single",
        "title": "Điều gì xảy ra khi biên dịch đoạn mã sau?",
        "code": "interface Calculable {\n    static int add(int a, int b) {\n        return a + b;\n    }\n}\nclass Calculator implements Calculable {}\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(Calculator.add(2, 3));\n    }\n}",
        "options": [
            "Lỗi biên dịch: Cannot find symbol method add(int,int) in class Calculator",
            "In ra: 5",
            "Ném ngoại lệ UnsupportedOperationException",
            "Lỗi biên dịch vì interface không thể có phương thức static"
        ],
        "correctAnswer": 0,
        "explanation": "Phương thức static trong interface Calculable không được kế thừa sang class Calculator. Do đó lệnh gọi Calculator.add(...) gây lỗi biên dịch vì trong Calculator không có phương thức static nào như vậy. Cách viết đúng duy nhất là Calculable.add(2, 3).",
        "difficulty": "medium",
        "tags": ["InterfaceStatic", "CompileError", "Inheritance"]
    },
    {
        "id": "L4_Q53",
        "lessonId": 4,
        "type": "single",
        "title": "Từ Java 9, phương thức 'private' (và private static) được phép xuất hiện trong Interface với mục đích chính là gì?",
        "code": None,
        "options": [
            "Cho phép tái sử dụng mã nguồn và chia sẻ logic chung giữa các default method hoặc static method bên trong interface mà không để lộ phương thức ra bên ngoài public API",
            "Để ngăn chặn việc ghi đè phương thức bởi các lớp con",
            "Để lưu trữ dữ liệu trạng thái nhạy cảm của interface",
            "Để mã hóa bytecode của interface chống dịch ngược"
        ],
        "correctAnswer": 0,
        "explanation": "Java 9 bổ sung private methods cho interface để cải thiện việc đóng gói và tái sử dụng mã nguồn bên trong interface. Khi nhiều default method hoặc static method có chung một đoạn logic xử lý phức tạp, ta có thể trích xuất ra một private method phụ trợ (helper method) mà không làm ô nhiễm giao diện công khai của interface.",
        "difficulty": "medium",
        "tags": ["PrivateInterfaceMethod", "Java9", "Encapsulation"]
    },
    {
        "id": "L4_Q54",
        "lessonId": 4,
        "type": "multiple",
        "title": "Mọi trường dữ liệu (fields / variables) được khai báo trong một Interface ngầm định sở hữu những từ khóa bổ nghĩa nào sau đây?",
        "code": None,
        "options": [
            "public",
            "static",
            "final",
            "transient"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Trong Interface, bất kỳ biến nào được khai báo (dù có viết từ khóa hay không) đều ngầm định và bắt buộc phải là 'public static final' (tức là hằng số). Chúng không thể là private, protected hay non-static/non-final.",
        "difficulty": "easy",
        "tags": ["InterfaceFields", "Constants", "Modifiers"]
    },
    {
        "id": "L4_Q55",
        "lessonId": 4,
        "type": "single",
        "title": "Điều gì xảy ra khi cố tình gán lại giá trị cho trường của một Interface?",
        "code": "interface Config {\n    int TIMEOUT = 5000;\n}\npublic class Main {\n    public static void main(String[] args) {\n        Config.TIMEOUT = 10000;\n    }\n}",
        "options": [
            "Lỗi biên dịch: cannot assign a value to final variable TIMEOUT",
            "Biên dịch thành công và thay đổi giá trị cấu hình thành 10000",
            "Chỉ có warning cảnh báo",
            "Ném IllegalAccessException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Vì trường 'int TIMEOUT = 5000' trong interface Config ngầm định là 'public static final', nó là một hằng số. Mọi hành vi cố tình gán lại giá trị đều bị trình biên dịch từ chối với lỗi 'cannot assign a value to final variable'.",
        "difficulty": "easy",
        "tags": ["InterfaceConstants", "Final", "CompileError"]
    },
    {
        "id": "L4_Q56",
        "lessonId": 4,
        "type": "single",
        "title": "Lớp trừu tượng B kế thừa lớp trừu tượng A có bắt buộc phải cài đặt lại các phương thức trừu tượng của A hay không?",
        "code": "abstract class A {\n    abstract void execute();\n}\nabstract class B extends A {\n    // Khong override execute()\n}",
        "options": [
            "Không bắt buộc; lớp con trừu tượng có thể kế thừa và chuyển tiếp các phương thức trừu tượng cho các lớp con cụ thể (concrete class) phía sau cài đặt",
            "Bắt buộc; mọi lớp con kế thừa abstract class đều phải override toàn bộ phương thức trừu tượng ngay lập tức",
            "Lỗi biên dịch nếu không ghi đè execute()",
            "Chỉ bắt buộc nếu execute() là phương thức public"
        ],
        "correctAnswer": 0,
        "explanation": "Một abstract class kế thừa một abstract class khác không bắt buộc phải override các abstract method của lớp cha. Trách nhiệm cài đặt cụ thể chỉ bắt buộc khi có một lớp cụ thể (concrete class, non-abstract) đầu tiên kế thừa chuỗi này.",
        "difficulty": "easy",
        "tags": ["AbstractClass", "Inheritance", "Rules"]
    },
    {
        "id": "L4_Q57",
        "lessonId": 4,
        "type": "multiple",
        "title": "Những khai báo nào sau đây là BẤT HỢP LỆ trong cú pháp ngôn ngữ Java?",
        "code": None,
        "options": [
            "final abstract class MyClass {}",
            "abstract static void doWork(); (trong interface)",
            "private interface MyInterface {} (ở cấp độ top-level file)",
            "abstract class MyClass { void concreteMethod() {} }"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1. final abstract: mâu thuẫn (abstract bắt kế thừa, final cấm kế thừa). 2. abstract static: mâu thuẫn (static không thể bị override, abstract bắt buộc override). 3. private interface ở top-level: không hợp lệ (chỉ được public hoặc default). Lựa chọn 4 là hoàn toàn hợp lệ (abstract class được phép có phương thức cụ thể).",
        "difficulty": "medium",
        "tags": ["InvalidModifiers", "Syntax", "CompileError"]
    },
    {
        "id": "L4_Q58",
        "lessonId": 4,
        "type": "single",
        "title": "Trong Java, một Interface có thể kế thừa (extends) bao nhiêu Interface khác?",
        "code": None,
        "options": [
            "Có thể kế thừa nhiều Interface khác cùng lúc (Đa thừa kế interface, ví dụ: interface C extends A, B)",
            "Chỉ được kế thừa tối đa một Interface duy nhất (Đơn thừa kế)",
            "Interface không thể kế thừa bất kỳ Interface nào khác",
            "Chỉ được kế thừa nếu dùng từ khóa implements"
        ],
        "correctAnswer": 0,
        "explanation": "Mặc dù Java không hỗ trợ đa thừa kế lớp (Multiple inheritance of classes), nhưng Java CHO PHÉP ĐA THỪA KẾ INTERFACE. Một interface có thể extends nhiều interface khác cùng lúc bằng cách dùng dấu phẩy: interface C extends A, B.",
        "difficulty": "easy",
        "tags": ["MultipleInheritance", "InterfaceExtends", "Syntax"]
    },
    {
        "id": "L4_Q59",
        "lessonId": 4,
        "type": "multiple",
        "title": "Khái niệm Giao diện hàm (Functional Interface) trong Java được định nghĩa bởi những tiêu chuẩn nào?",
        "code": None,
        "options": [
            "Chứa đúng MỘT phương thức trừu tượng (Single Abstract Method - SAM)",
            "Có thể chứa thêm nhiều phương thức default hoặc phương thức static",
            "Có thể khai báo thêm các phương thức trừu tượng của lớp Object (như equals, hashCode, toString) mà không làm mất tính SAM",
            "Có thể được chú thích bằng annotation @FunctionalInterface để trình biên dịch kiểm tra tính hợp lệ"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Tất cả 4 đặc điểm trên đều đúng với Functional Interface (được dùng làm mục tiêu cho biểu thức Lambda). Nó chỉ có 1 abstract method duy nhất (SAM), nhưng được phép có default/static methods và các method kế thừa từ java.lang.Object.",
        "difficulty": "medium",
        "tags": ["FunctionalInterface", "Lambda", "Java8"]
    },
    {
        "id": "L4_Q60",
        "lessonId": 4,
        "type": "single",
        "title": "Xác định output của đoạn mã tích hợp Interface default method và static method sau:",
        "code": "interface Printable {\n    default void print() {\n        System.out.print(\"Default \");\n    }\n    static void info() {\n        System.out.print(\"Info \");\n    }\n}\nclass Doc implements Printable {}\npublic class Main {\n    public static void main(String[] args) {\n        Doc d = new Doc();\n        d.print();\n        Printable.info();\n    }\n}",
        "options": [
            "Default Info ",
            "Info Default ",
            "Lỗi biên dịch tại Printable.info()",
            "Lỗi biên dịch tại d.print()"
        ],
        "correctAnswer": 0,
        "explanation": "Lớp Doc implement Printable nên kế thừa default method print(), gọi d.print() in ra 'Default '. Phương thức static info() được gọi chuẩn xác qua tên interface Printable.info() in ra 'Info '. Kết quả là 'Default Info '.",
        "difficulty": "easy",
        "tags": ["DefaultMethod", "StaticMethod", "Output"]
    },

    # --- ĐỀ 4E (L4_Q61 - L4_Q75): Advanced Generics, PECS & Type Erasure Traps ---
    {
        "id": "L4_Q61",
        "lessonId": 4,
        "type": "single",
        "title": "Nguyên tắc PECS (Producer Extends, Consumer Super) trong thiết kế Java Generics hướng dẫn điều gì?",
        "code": None,
        "options": [
            "Dùng '? extends T' khi tham số chỉ cung cấp/sản xuất (read/produce) dữ liệu cho phương thức; dùng '? super T' khi tham số chỉ tiêu thụ/ghi nạp (write/consume) dữ liệu vào",
            "Dùng '? extends T' để thêm phần tử vào danh sách, dùng '? super T' để lấy phần tử ra khỏi danh sách",
            "Dùng '? extends T' cho kiểu trả về của phương thức, dùng '? super T' cho tham số truyền vào",
            "Dùng '? extends T' cho các lớp con và '? super T' cho các lớp cha"
        ],
        "correctAnswer": 0,
        "explanation": "PECS là nguyên tắc vàng trong Generics: 'Producer Extends, Consumer Super'. Nếu cấu trúc dữ liệu đóng vai trò là nhà sản xuất dữ liệu (bạn đọc get() phần tử ra khỏi nó), dùng '? extends T'. Nếu đóng vai trò người tiêu thụ (bạn ghi add() phần tử vào nó), dùng '? super T'.",
        "difficulty": "medium",
        "tags": ["PECS", "Generics", "Wildcards"]
    },
    {
        "id": "L4_Q62",
        "lessonId": 4,
        "type": "single",
        "title": "Cho khai báo danh sách với Upper Bounded Wildcard sau. Thao tác nào sẽ gây LỖI BIÊN DỊCH?",
        "code": "List<? extends Number> list = new ArrayList<Integer>();\n// Xet cac thao tac:\n// D1: Number n = list.get(0);\n// D2: list.add(10);\n// D3: list.add(null);\n// D4: Object obj = list.get(0);",
        "options": [
            "D2 gây lỗi biên dịch: không thể thêm bất kỳ giá trị cụ thể nào (kể cả số 10) vào List<? extends Number>",
            "D1 gây lỗi biên dịch",
            "D3 gây lỗi biên dịch",
            "Cả D2 và D3 đều gây lỗi biên dịch"
        ],
        "correctAnswer": 0,
        "explanation": "Với '? extends Number', trình biên dịch không thể biết chính xác danh sách thực tế là List<Integer>, List<Double> hay List<Float>. Để đảm bảo an toàn kiểu (Type Safety), Java cấm thêm bất kỳ phần tử nào vào danh sách này (D2 lỗi biên dịch), ngoại trừ hằng số null (D3 hợp lệ). Việc đọc phần tử (D1, D4) hoàn toàn an toàn.",
        "difficulty": "hard",
        "tags": ["UpperBoundedWildcard", "PECS", "CompileError"]
    },
    {
        "id": "L4_Q63",
        "lessonId": 4,
        "type": "single",
        "title": "Cho khai báo danh sách với Lower Bounded Wildcard sau. Thao tác nào là HỢP LỆ?",
        "code": "List<? super Integer> list = new ArrayList<Number>();",
        "options": [
            "list.add(42); (có thể thêm đối tượng kiểu Integer hoặc con của Integer vào danh sách)",
            "Integer val = list.get(0); (có thể đọc trực tiếp ra kiểu Integer mà không cần ép kiểu)",
            "list.add(3.14); (có thể thêm kiểu Double vào danh sách)",
            "list.add(new Object()); (có thể thêm đối tượng kiểu Object vào danh sách)"
        ],
        "correctAnswer": 0,
        "explanation": "Với '? super Integer', danh sách là của Integer hoặc cha của Integer (như Number, Object). Do đó, chắc chắn an toàn khi ghi thêm (consume) Integer vào danh sách (list.add(42) hợp lệ). Tuy nhiên, khi đọc get(0), JVM chỉ đảm bảo phần tử trả về có kiểu Object (muốn lấy Integer phải ép kiểu tường minh).",
        "difficulty": "hard",
        "tags": ["LowerBoundedWildcard", "PECS", "TypeSafety"]
    },
    {
        "id": "L4_Q64",
        "lessonId": 4,
        "type": "multiple",
        "title": "Những phát biểu nào sau đây là ĐÚNG về cơ chế Xóa kiểu (Type Erasure) trong Java Generics?",
        "code": None,
        "options": [
            "Tất cả thông tin tham số kiểu generic (<T>) bị trình biên dịch loại bỏ khỏi mã bytecode tại thời điểm biên dịch, tại runtime JVM không lưu giữ kiểu cụ thể này",
            "Kiểu không bị chặn <T> được thay thế bằng kiểu Object trong bytecode",
            "Kiểu có chặn <T extends Number> được thay thế bằng kiểu cận trên là Number trong bytecode",
            "Trình biên dịch tự động chèn các lệnh ép kiểu tường minh (casts) và phương thức cầu nối (bridge methods) vào bytecode để duy trì tính đa hình"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Cả 4 phát biểu trên đều mô tả chính xác bản chất cơ chế Type Erasure của Java. Cơ chế này được áp dụng từ Java 5 để đảm bảo tính tương thích nhị phân ngược (binary backward compatibility) với các thư viện viết trên Java 1.4 trở về trước.",
        "difficulty": "hard",
        "tags": ["TypeErasure", "Bytecode", "JVMInternals"]
    },
    {
        "id": "L4_Q65",
        "lessonId": 4,
        "type": "single",
        "title": "Xác định output của phép so sánh lớp tại thời điểm runtime do ảnh hưởng của Type Erasure:",
        "code": "List<String> list1 = new ArrayList<>();\nList<Integer> list2 = new ArrayList<>();\nSystem.out.println(list1.getClass() == list2.getClass());",
        "options": [
            "true (cả hai đều có kiểu runtime là java.util.ArrayList.class)",
            "false (một bên là ArrayList<String>, một bên là ArrayList<Integer>)",
            "Lỗi biên dịch tại phép so sánh ==",
            "Ném ClassCastException khi chạy"
        ],
        "correctAnswer": 0,
        "explanation": "Do cơ chế Type Erasure, thông tin <String> và <Integer> bị xóa sạch tại runtime. Cả list1 và list2 đều chỉ là thể hiện của lớp thô java.util.ArrayList. Do đó list1.getClass() và list2.getClass() trả về cùng một đối tượng Class duy nhất, kết quả là true.",
        "difficulty": "medium",
        "tags": ["TypeErasure", "GetClass", "Generics"]
    },
    {
        "id": "L4_Q66",
        "lessonId": 4,
        "type": "multiple",
        "title": "Những dòng mã nào sau đây GÂY LỖI BIÊN DỊCH do các giới hạn của cơ chế Type Erasure trong Java?",
        "code": None,
        "options": [
            "T obj = new T(); (không thể khởi tạo trực tiếp instance của kiểu tham số generic)",
            "T[] arr = new T[10]; (không thể tạo mảng của kiểu tham số generic)",
            "if (list instanceof List<String>) {} (không thể kiểm tra instanceof với generic có tham số cụ thể)",
            "private static T instanceVar; (không thể khai báo biến static có kiểu là type parameter của lớp)"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Do Type Erasure xóa mất kiểu tại runtime, JVM không biết T là kiểu gì để cấp phát bộ nhớ cho 'new T()' hoặc 'new T[10]'. Cũng không thể phân biệt List<String> với List<Integer> khi kiểm tra instanceof (chỉ được kiểm tra list instanceof List<?>). Biến static thuộc về class nên không thể phụ thuộc vào kiểu T của từng đối tượng. Cả 4 trường hợp đều lỗi biên dịch.",
        "difficulty": "hard",
        "tags": ["GenericsRestrictions", "TypeErasure", "CompileError"]
    },
    {
        "id": "L4_Q67",
        "lessonId": 4,
        "type": "single",
        "title": "Khi khai báo ràng buộc kép (Multiple Bounds) cho tham số kiểu: '<T extends ClassA & InterfaceB & InterfaceC>', quy tắc bắt buộc về cú pháp là gì?",
        "code": None,
        "options": [
            "Nếu có một lớp (Class) tham gia ràng buộc, lớp đó BẮT BUỘC phải được viết đầu tiên trước tất cả các Interface",
            "Các Interface phải được viết trước, Class viết sau cùng",
            "Có thể khai báo nhiều hơn một Class bằng cách nối thêm dấu '&'",
            "Thứ tự giữa Class và Interface là tùy ý không bị ràng buộc"
        ],
        "correctAnswer": 0,
        "explanation": "Theo quy tắc JLS: Nếu một tham số kiểu generic có nhiều ràng buộc (Multiple bounds), tối đa chỉ được có 1 Class và Class đó bắt buộc phải đứng đầu tiên danh sách. Các interface đi sau được nối bằng dấu '&'. Java không cho phép đa kế thừa class.",
        "difficulty": "medium",
        "tags": ["MultipleBounds", "GenericsSyntax", "JLS"]
    },
    {
        "id": "L4_Q68",
        "lessonId": 4,
        "type": "single",
        "title": "Trong Java, Integer là lớp con của Number. Điều gì xảy ra với dòng mã khai báo danh sách sau?",
        "code": "List<Number> list = new ArrayList<Integer>();",
        "options": [
            "Lỗi biên dịch: Type mismatch: cannot convert from ArrayList<Integer> to List<Number>",
            "Biên dịch thành công vì Integer kế thừa từ Number (tính đa hình)",
            "Chỉ có cảnh báo warning Unchecked conversion",
            "Ném ngoại lệ ClassCastException tại runtime"
        ],
        "correctAnswer": 0,
        "explanation": "Các kiểu generic trong Java là BẤT BIẾN (INVARIANT). Dù Integer là con của Number, List<Integer> KHÔNG PHẢI là con của List<Number>. Nếu cho phép gán, ta có thể viết list.add(new Double(3.14)) và phá hỏng tính an toàn của danh sách Integer ban đầu. Để gán được, phải dùng wildcard: List<? extends Number> list = new ArrayList<Integer>().",
        "difficulty": "medium",
        "tags": ["Invariance", "Generics", "CompileError"]
    },
    {
        "id": "L4_Q69",
        "lessonId": 4,
        "type": "multiple",
        "title": "So sánh sự khác nhau cốt lõi giữa Mảng (Array) và Danh sách Tổng quát (Generics) trong Java:",
        "code": None,
        "options": [
            "Mảng là Covariant (Đồng biến, Integer[] là con của Number[]), còn Generics là Invariant (Bất biến, List<Integer> không phải con của List<Number>)",
            "Mảng là Reifiable (Giữ nguyên thông tin kiểu tại runtime), còn Generics bị Type Erasure (Xóa kiểu tại runtime)",
            "Mảng phát hiện lỗi sai kiểu đối tượng tại Runtime (ném ArrayStoreException), còn Generics phát hiện lỗi tại Compile-time",
            "Mảng không bao giờ bị ném lỗi OutOfMemoryError"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "3 phát biểu đầu phân tích chính xác sự đối lập giữa Array (Covariant & Reifiable) và Generics (Invariant & Type-Erased). Mảng vẫn có thể gây OutOfMemoryError nếu cấp phát kích thước quá lớn vượt bộ nhớ Heap.",
        "difficulty": "hard",
        "tags": ["ArrayVsGenerics", "Covariant", "TypeSafety"]
    },
    {
        "id": "L4_Q70",
        "lessonId": 4,
        "type": "single",
        "title": "Điều gì xảy ra khi thực thi đoạn mã minh họa bẫy Covariant của Mảng sau?",
        "code": "Number[] numbers = new Integer[3];\nnumbers[0] = 3.14; // Gan so thuc Double",
        "options": [
            "Biên dịch thành công nhưng ném java.lang.ArrayStoreException tại thời điểm runtime",
            "Lỗi biên dịch ngay tại dòng numbers[0] = 3.14;",
            "Số 3.14 tự động ép kiểu thành số nguyên 3 và lưu vào mảng",
            "Chương trình chạy bình thường không có lỗi"
        ],
        "correctAnswer": 0,
        "explanation": "Vì mảng là Covariant, trình biên dịch cho phép gán 'new Integer[3]' cho 'Number[] numbers'. Ở dòng tiếp theo, 3.14 là Double (vốn là một Number) nên vượt qua kiểm tra compile-time. Nhưng tại runtime, mảng biết kiểu thực tế của nó là Integer[] và từ chối lưu phần tử Double, ném ngoại lệ java.lang.ArrayStoreException.",
        "difficulty": "medium",
        "tags": ["ArrayStoreException", "CovariantArray", "RuntimeTrap"]
    },
    {
        "id": "L4_Q71",
        "lessonId": 4,
        "type": "single",
        "title": "Vị trí đặt tham số kiểu generic <T> trong cú pháp khai báo một Generic Method độc lập là gì?",
        "code": None,
        "options": [
            "Nằm trước kiểu dữ liệu trả về của phương thức (ví dụ: public static <T> T getFirst(List<T> list))",
            "Nằm sau danh sách tham số của phương thức",
            "Nằm ngay sau tên phương thức",
            "Nằm bên trong ngoặc đơn của danh sách tham số"
        ],
        "correctAnswer": 0,
        "explanation": "Cú pháp chuẩn của Generic Method trong Java: các tham số kiểu (type parameters) phải được đặt trong cặp ngoặc nhọn '<...>' nằm TRƯỚC kiểu trả về của phương thức (ví dụ: public static <T> T getFirst(List<T> list)).",
        "difficulty": "easy",
        "tags": ["GenericMethod", "Syntax", "TypeParameter"]
    },
    {
        "id": "L4_Q72",
        "lessonId": 4,
        "type": "multiple",
        "title": "Phương thức sao chép dữ liệu từ danh sách nguồn (src) sang danh sách đích (dest) nào sau đây tuân thủ hoàn hảo nguyên lý PECS?",
        "code": None,
        "options": [
            "public static <T> void copy(List<? super T> dest, List<? extends T> src) { for (T item : src) dest.add(item); }",
            "public static <T> void copy(List<T> dest, List<T> src) { ... } (chỉ nhận đúng hai danh sách cùng kiểu chính xác)",
            "public static <T> void copy(List<? extends T> dest, List<? super T> src) { ... } (đảo ngược sai vai trò Producer và Consumer)",
            "Cài đặt phương thức Collections.copy() trong thư viện chuẩn Java JDK sử dụng cú pháp: (List<? super T> dest, List<? extends T> src)"
        ],
        "correctAnswer": [0, 3],
        "explanation": "Nguồn (src) sản xuất dữ liệu ra -> dùng '? extends T' (Producer Extends). Đích (dest) tiêu thụ và lưu trữ dữ liệu vào -> dùng '? super T' (Consumer Super). Đây chính là định nghĩa chuẩn của phương thức Collections.copy() trong thư viện chuẩn java.util.Collections.",
        "difficulty": "hard",
        "tags": ["PECS", "CollectionsCopy", "BestPractice"]
    },
    {
        "id": "L4_Q73",
        "lessonId": 4,
        "type": "single",
        "title": "Khi sử dụng Unbounded Wildcard 'List<?>', phát biểu nào sau đây là ĐÚNG?",
        "code": "List<?> list = new ArrayList<String>();",
        "options": [
            "Khi đọc phần tử từ list.get(0), kết quả trả về luôn có kiểu an toàn là Object; và không thể add bất kỳ phần tử nào vào list ngoại trừ giá trị null",
            "Có thể add thêm các đối tượng kiểu String vào list bình thường",
            "Không thể gọi bất kỳ phương thức nào của List như size(), clear(), isEmpty()",
            "List<?> tương đương hoàn toàn 100% với List<Object>"
        ],
        "correctAnswer": 0,
        "explanation": "List<?> đại diện cho danh sách của một kiểu chưa biết (list of an unknown type). Ta có thể đọc an toàn kiểu Object từ nó, gọi các hàm không phụ thuộc kiểu như size(), clear(). Nhưng không thể add bất kỳ giá trị cụ thể nào vào list (trừ null) vì không biết kiểu thực tế là gì.",
        "difficulty": "medium",
        "tags": ["UnboundedWildcard", "Generics", "Object"]
    },
    {
        "id": "L4_Q74",
        "lessonId": 4,
        "type": "single",
        "title": "Phương thức cầu nối (Bridge Method) được trình biên dịch Java tự động sinh ra trong trường hợp nào sau đây?",
        "code": "class Node<T> {\n    public void setData(T data) {}\n}\nclass MyNode extends Node<Integer> {\n    @Override\n    public void setData(Integer data) {}\n}",
        "options": [
            "Khi lớp con ghi đè một phương thức generic của lớp cha với kiểu cụ thể, compiler sinh ra phương thức cầu nối setData(Object) gọi tới setData(Integer) để đảm bảo tính đa hình vtable trong JVM",
            "Khi hai thread cùng truy cập vào một lớp generic",
            "Khi lớp implement cùng lúc Serializable và Cloneable",
            "Khi chuyển đổi kiểu từ ArrayList sang LinkedList"
        ],
        "correctAnswer": 0,
        "explanation": "Do Type Erasure, trong class Node phương thức là setData(Object). Nhưng trong MyNode phương thức là setData(Integer). Để đảm bảo cơ chế đa hình ảo (polymorphic dynamic dispatch), compiler tự động sinh ra một synthetic method: 'public void setData(Object data) { setData((Integer) data); }' gọi là Bridge Method.",
        "difficulty": "hard",
        "tags": ["BridgeMethod", "TypeErasure", "Compiler"]
    },
    {
        "id": "L4_Q75",
        "lessonId": 4,
        "type": "single",
        "title": "Xác định output của đoạn mã Generic Bounded Type sau:",
        "code": "class Box<T extends Number> {\n    private T val;\n    Box(T val) { this.val = val; }\n    double getDoubleVal() { return val.doubleValue(); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Box<Integer> b1 = new Box<>(10);\n        Box<Double> b2 = new Box<>(20.5);\n        System.out.println((b1.getDoubleVal() + b2.getDoubleVal()));\n    }\n}",
        "options": [
            "30.5",
            "30",
            "Lỗi biên dịch do không thể tạo Box<Double>",
            "Lỗi ClassCastException tại hàm getDoubleVal()"
        ],
        "correctAnswer": 0,
        "explanation": "Cả Integer và Double đều kế thừa lớp Number, do đó thỏa mãn ràng buộc 'T extends Number'. Lớp Number có phương thức doubleValue(), nên phương thức getDoubleVal() gọi hợp lệ. 10.0 + 20.5 = 30.5.",
        "difficulty": "easy",
        "tags": ["BoundedType", "Generics", "Output"]
    }
]

def update_file(filename, new_questions):
    path = os.path.join(r"D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\questions", filename)
    with open(path, "r", encoding="utf-8") as f:
        existing = json.load(f)
    
    # Check duplicate IDs
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
    update_file("lesson1.json", L1_NEW)
    update_file("lesson3.json", L3_NEW)
    update_file("lesson4.json", L4_NEW)
    print("All 90 questions generated and appended successfully.")
