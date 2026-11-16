# -*- coding: utf-8 -*-
import json
import os

OUTPUT_DIR = r"d:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\questions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# LESSON 1: Cơ bản Java & OOP
# ==============================================================================
lesson1_questions = [
  {
    "id": "L1_Q01",
    "lessonId": 1,
    "title": "Biến cục bộ (local variable) và đối tượng (object instance) trong Java được lưu trữ ở các phân vùng bộ nhớ nào của JVM?",
    "code": None,
    "options": [
      "Biến cục bộ nằm trên Stack của luồng, đối tượng thực sự luôn nằm trên Heap",
      "Cả biến cục bộ và đối tượng đều nằm hoàn toàn trên Heap",
      "Cả biến cục bộ và đối tượng đều nằm hoàn toàn trên Stack",
      "Biến cục bộ nằm trong Metaspace, đối tượng nằm trên Stack"
    ],
    "correctAnswer": 0,
    "explanation": "Trong kiến trúc bộ nhớ JVM, mỗi luồng có một ngăn xếp Stack riêng. Các biến cục bộ (cả kiểu nguyên thủy và biến tham chiếu) được lưu trong Stack Frame của phương thức đang thực thi. Trong khi đó, các đối tượng thực sự luôn được cấp phát động trên vùng nhớ dùng chung Heap.",
    "difficulty": "easy",
    "tags": ["JVM", "Stack-Heap", "Memory"]
  },
  {
    "id": "L1_Q02",
    "lessonId": 1,
    "title": "Bộ thu gom rác (Garbage Collector - GC) trong JVM xác định một đối tượng đủ điều kiện giải phóng bộ nhớ dựa trên nguyên lý nào?",
    "code": None,
    "options": [
      "Đối tượng không còn khả năng tiếp cận (unreachable) từ bất kỳ GC Root nào",
      "Đối tượng không được gọi phương thức nào trong vòng 10 giây",
      "Biến tham chiếu đầu tiên tạo ra đối tượng bị gán bằng null",
      "Lập trình viên bắt buộc phải giải phóng thủ công bằng hàm free() hoặc delete()"
    ],
    "correctAnswer": 0,
    "explanation": "JVM sử dụng thuật toán phân tích khả năng tiếp cận (Reachability Analysis). GC Roots bao gồm các biến cục bộ trên Stack, biến static trong Metaspace, và tham chiếu JNI. Khi không còn đường đi tham chiếu hợp lệ nào từ bất kỳ GC Root nào tới đối tượng (unreachable), đối tượng đó đủ điều kiện để GC thu hồi bộ nhớ.",
    "difficulty": "medium",
    "tags": ["JVM", "Garbage-Collector", "Reachability"]
  },
  {
    "id": "L1_Q03",
    "lessonId": 1,
    "title": "Phát biểu nào sau đây là ĐÚNG về phương thức System.gc() trong Java?",
    "code": None,
    "options": [
      "Chỉ là lời gợi ý (hint) gửi tới JVM, không đảm bảo GC sẽ được thực thi ngay lập tức",
      "Bắt buộc JVM phải dừng toàn bộ ứng dụng và dọn sạch bộ nhớ Heap ngay lập tức",
      "Giải phóng toàn bộ các biến tĩnh (static) và nạp lại class loader",
      "Là phương thức private nên không thể gọi từ bên ngoài thư viện java.lang"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức System.gc() hoặc Runtime.getRuntime().gc() chỉ gửi tín hiệu gợi ý tới máy ảo JVM rằng hệ thống muốn thu gom rác. JVM có toàn quyền quyết định thời điểm và thuật toán thu gom rác tối ưu, không có gì đảm bảo GC sẽ chạy ngay tức khắc.",
    "difficulty": "easy",
    "tags": ["JVM", "Garbage-Collector"]
  },
  {
    "id": "L1_Q04",
    "lessonId": 1,
    "title": "Mức truy cập mặc định (default / package-private) khi không khai báo từ khóa đặc tả truy cập có phạm vi như thế nào?",
    "code": None,
    "options": [
      "Chỉ các lớp nằm trong cùng một package mới có thể truy cập",
      "Tất cả các lớp trong toàn bộ project đều có thể truy cập",
      "Chỉ các lớp con kế thừa mới có thể truy cập, kể cả ở package khác",
      "Chỉ duy nhất bên trong nội bộ lớp khai báo mới truy cập được"
    ],
    "correctAnswer": 0,
    "explanation": "Mức truy cập default (package-private) trong Java giới hạn quyền truy cập chỉ cho các class nằm trong cùng package. Các lớp ở ngoài package, dù có kế thừa lớp này, cũng không thể truy cập các thành phần default.",
    "difficulty": "easy",
    "tags": ["Access-Modifiers", "Package"]
  },
  {
    "id": "L1_Q05",
    "lessonId": 1,
    "title": "Một lớp ở mức ngoài cùng (Top-level class) trong Java được phép khai báo với những mức truy cập nào?",
    "code": None,
    "options": [
      "Chỉ có thể là public hoặc default (package-private)",
      "Có thể là public, protected, private hoặc default",
      "Bắt buộc phải là public",
      "Có thể là protected hoặc default, nhưng không được là public"
    ],
    "correctAnswer": 0,
    "explanation": "Lớp ở mức cao nhất (top-level class, không nằm lồng trong lớp khác) trong tệp Java chỉ được phép có 2 mức truy cập: public hoặc default. Khai báo private hoặc protected ở top-level sẽ gây lỗi biên dịch: 'modifier private/protected not allowed here'.",
    "difficulty": "medium",
    "tags": ["Access-Modifiers", "Class-Structure"]
  },
  {
    "id": "L1_Q06",
    "lessonId": 1,
    "title": "Khi khai báo một biến tham chiếu đối tượng với từ khóa final (ví dụ: final List<String> list = new ArrayList<>()), điều đó có ý nghĩa gì?",
    "code": None,
    "options": [
      "Biến list không thể trỏ sang đối tượng khác, nhưng nội dung đối tượng ArrayList vẫn có thể thêm/bớt phần tử",
      "Đối tượng ArrayList bị đóng băng bất biến hoàn toàn, không thể thêm hoặc xóa phần tử",
      "Các phần tử trong danh sách tự động chuyển thành hằng số",
      "Phương thức clear() của list sẽ gây lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Từ khóa final trên biến tham chiếu chỉ cố định địa chỉ tham chiếu (không thể gán list = new ArrayList<>() khác). Trạng thái nội tại (internal state) của đối tượng mà nó trỏ tới vẫn có thể thay đổi bình thường trừ khi lớp đó được thiết kế immutable.",
    "difficulty": "medium",
    "tags": ["Final", "Reference", "Immutability"]
  },
  {
    "id": "L1_Q07",
    "lessonId": 1,
    "title": "Cơ chế truyền tham số vào phương thức trong Java tuân theo nguyên lý nào?",
    "code": None,
    "options": [
      "Hoàn toàn là truyền theo giá trị (Pass-by-value) cho mọi kiểu dữ liệu",
      "Truyền theo giá trị cho kiểu nguyên thủy, truyền theo tham chiếu cho kiểu đối tượng",
      "Hoàn toàn là truyền theo tham chiếu (Pass-by-reference)",
      "Truyền tham chiếu nếu đối tượng có kiểu mutable, truyền giá trị nếu immutable"
    ],
    "correctAnswer": 0,
    "explanation": "Java 100% là Pass-by-value. Khi truyền một đối tượng vào phương thức, giá trị của biến tham chiếu (chính là địa chỉ bộ nhớ trỏ tới đối tượng) được sao chép và truyền vào. Việc gán lại biến tham số bên trong phương thức không làm thay đổi biến tham chiếu ban đầu ở nơi gọi.",
    "difficulty": "hard",
    "tags": ["Pass-by-value", "JVM-Internals"]
  },
  {
    "id": "L1_Q08",
    "lessonId": 1,
    "title": "Phương thức khởi tạo mặc định (default no-arg constructor) được trình biên dịch Java tự động sinh ra khi nào?",
    "code": None,
    "options": [
      "Khi và chỉ khi lớp không định nghĩa bất kỳ constructor nào",
      "Luôn luôn được sinh ra trong mọi lớp dù có constructor khác hay không",
      "Khi lớp có ít nhất một constructor có tham số",
      "Khi lớp kế thừa trực tiếp từ lớp Object"
    ],
    "correctAnswer": 0,
    "explanation": "Trình biên dịch Java chỉ tự động cung cấp default no-arg constructor khi trong mã nguồn lớp hoàn toàn không khai báo bất kỳ constructor nào. Nếu đã khai báo ít nhất một constructor (dù có hay không có tham số), trình biên dịch sẽ không tự động sinh constructor mặc định nữa.",
    "difficulty": "easy",
    "tags": ["Constructor", "Compiler"]
  },
  {
    "id": "L1_Q09",
    "lessonId": 1,
    "title": "Vùng nhớ Metaspace (từ Java 8 thay thế cho PermGen) trong JVM được cấp phát ở đâu và lưu trữ dữ liệu gì?",
    "code": None,
    "options": [
      "Được cấp phát từ bộ nhớ gốc của hệ điều hành (Native Memory), lưu Class Metadata, Bytecode và Constant Pool",
      "Nằm trong Heap, lưu trữ toàn bộ các chuỗi ký tự String",
      "Nằm trong Stack, lưu trữ biến cục bộ của phương thức tĩnh",
      "Nằm trong CPU Cache L1, lưu trữ mã máy sau khi JIT biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Từ Java 8, PermGen bị loại bỏ và thay bằng Metaspace. Metaspace sử dụng trực tiếp Native Memory của hệ điều hành (không bị giới hạn bởi dung lượng Heap cố định) để lưu trữ Class metadata, Constant pool, Method tables và Bytecode của các lớp đã nạp.",
    "difficulty": "hard",
    "tags": ["JVM", "Metaspace", "Memory"]
  },
  {
    "id": "L1_Q10",
    "lessonId": 1,
    "title": "Hiện tượng gì xảy ra khi hai constructor trong cùng một lớp gọi vòng tròn lẫn nhau thông qua từ khóa this()?",
    "code": None,
    "options": [
      "Lỗi biên dịch (Compile-time error): recursive constructor invocation",
      "Biên dịch thành công nhưng ném ngoại lệ StackOverflowError khi chạy",
      "Chương trình chạy lặp vô tận làm treo máy",
      "Biên dịch thành công và JVM tự động ngắt chu trình đệ quy"
    ],
    "correctAnswer": 0,
    "explanation": "Trình biên dịch Java kiểm tra tĩnh luồng gọi constructor và sẽ báo lỗi biên dịch ngay lập tức: 'recursive constructor invocation' nếu phát hiện chu trình gọi đệ quy giữa các constructor qua this().",
    "difficulty": "medium",
    "tags": ["Constructor", "Compile-Error"]
  },
  {
    "id": "L1_Q11",
    "lessonId": 1,
    "title": "Đoạn mã sau cho kết quả in ra màn hình là gì?",
    "code": "class Counter {\n    static int count = 0;\n    int id = 0;\n    Counter() {\n        count++;\n        id++;\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Counter c1 = new Counter();\n        Counter c2 = new Counter();\n        System.out.println(c1.count + \" \" + c1.id + \" \" + c2.count + \" \" + c2.id);\n    }\n}",
    "options": [
      "2 1 2 1",
      "1 1 2 2",
      "2 2 2 2",
      "1 1 1 1"
    ],
    "correctAnswer": 0,
    "explanation": "Biến static 'count' thuộc về phạm vi class và được chia sẻ giữa mọi instance. Khi c1 khởi tạo count=1, khi c2 khởi tạo count=2 (c1.count và c2.count đều trỏ vào biến static này). Biến 'id' là instance variable độc lập cho mỗi đối tượng, nên c1.id=1 và c2.id=1. Kết quả in ra là: 2 1 2 1.",
    "difficulty": "medium",
    "tags": ["Static", "Instance-Variable"]
  },
  {
    "id": "L1_Q12",
    "lessonId": 1,
    "title": "Đoạn mã sau cho kết quả in ra là gì?",
    "code": "public class StringTest {\n    public static void main(String[] args) {\n        String s1 = \"UET\";\n        String s2 = \"UET\";\n        String s3 = new String(\"UET\");\n        String s4 = s3.intern();\n        System.out.println((s1 == s2) + \" \" + (s1 == s3) + \" \" + (s1 == s4));\n    }\n}",
    "options": [
      "true false true",
      "true true true",
      "false false true",
      "true false false"
    ],
    "correctAnswer": 0,
    "explanation": "s1 và s2 là chuỗi hằng số (literal) nên cùng trỏ tới một đối tượng duy nhất trong String Constant Pool -> s1 == s2 là true. s3 được tạo bằng toán tử new nên tạo một đối tượng mới độc lập trên Heap -> s1 == s3 là false. Lệnh s3.intern() tìm và trả về tham chiếu từ String Pool (chính là s1) -> s1 == s4 là true.",
    "difficulty": "medium",
    "tags": ["String-Pool", "Intern", "Equality"]
  },
  {
    "id": "L1_Q13",
    "lessonId": 1,
    "title": "Kết quả in ra màn hình của đoạn mã sau là gì?",
    "code": "public class PassTest {\n    static void update(int x, StringBuilder sb) {\n        x = 99;\n        sb.append(\" World\");\n        sb = new StringBuilder(\"New Object\");\n    }\n    public static void main(String[] args) {\n        int a = 10;\n        StringBuilder b = new StringBuilder(\"Hello\");\n        update(a, b);\n        System.out.println(a + \" | \" + b.toString());\n    }\n}",
    "options": [
      "10 | Hello World",
      "99 | Hello World",
      "10 | New Object",
      "99 | New Object"
    ],
    "correctAnswer": 0,
    "explanation": "Java truyền tham số theo giá trị. Biến nguyên thủy a được sao chép giá trị nên sau hàm update giá trị vẫn là 10. Biến tham chiếu b truyền bản sao địa chỉ: lệnh sb.append(\" World\") làm thay đổi nội dung đối tượng gốc trên Heap thành \"Hello World\". Lệnh sb = new StringBuilder(\"New Object\") chỉ làm biến cục bộ sb trỏ sang đối tượng mới, không ảnh hưởng tới biến b ở hàm main.",
    "difficulty": "hard",
    "tags": ["Pass-by-value", "StringBuilder"]
  },
  {
    "id": "L1_Q14",
    "lessonId": 1,
    "title": "Thứ tự in ra màn hình của đoạn mã sau khi khởi chạy là gì?",
    "code": "class Sample {\n    static {\n        System.out.print(\"S1 \");\n    }\n    {\n        System.out.print(\"I1 \");\n    }\n    Sample() {\n        System.out.print(\"C1 \");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        System.out.print(\"M \");\n        new Sample();\n        new Sample();\n    }\n}",
    "options": [
      "M S1 I1 C1 I1 C1 ",
      "S1 M I1 C1 I1 C1 ",
      "M I1 C1 S1 I1 C1 ",
      "S1 I1 C1 M I1 C1 "
    ],
    "correctAnswer": 0,
    "explanation": "Lớp Main được nạp đầu tiên và chạy phương thức main(), in ra 'M '. Khi gặp lệnh new Sample() lần đầu, lớp Sample được nạp vào JVM: static block chạy một lần duy nhất in 'S1 '. Tiếp đó instance block in 'I1 ' rồi constructor in 'C1 '. Ở lần new Sample() thứ hai, static block không chạy lại, chỉ có instance block và constructor chạy in 'I1 C1 '. Tổng cộng: 'M S1 I1 C1 I1 C1 '.",
    "difficulty": "hard",
    "tags": ["Init-Order", "Static-Block", "Instance-Block"]
  },
  {
    "id": "L1_Q15",
    "lessonId": 1,
    "title": "Đoạn mã sau in ra kết quả gì (cơ chế Integer Cache)?",
    "code": "public class CacheTest {\n    public static void main(String[] args) {\n        Integer a = 127;\n        Integer b = 127;\n        Integer c = 128;\n        Integer d = 128;\n        System.out.println((a == b) + \" \" + (c == d));\n    }\n}",
    "options": [
      "true false",
      "true true",
      "false false",
      "false true"
    ],
    "correctAnswer": 0,
    "explanation": "Khi gán int cho Integer, Java tự động gọi Integer.valueOf(). Lớp Integer duy trì bộ nhớ đệm IntegerCache cho các giá trị từ -128 đến 127. Vì 127 nằm trong cache nên a và b trỏ tới cùng một instance -> a == b là true. Với 128 vượt quá 127, JVM tạo hai đối tượng Integer riêng biệt trên Heap -> c == d là false.",
    "difficulty": "medium",
    "tags": ["Autoboxing", "IntegerCache", "Equality"]
  },
  {
    "id": "L1_Q16",
    "lessonId": 1,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "class Entity {\n    final int id;\n    Entity() {\n        // khong gan gia tri cho id\n    }\n    Entity(int id) {\n        this.id = id;\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Entity e = new Entity(5);\n    }\n}",
    "options": [
      "Lỗi biên dịch tại constructor Entity(): biến final 'id' chưa được khởi tạo",
      "Biên dịch thành công và biến id tự động nhận giá trị mặc định 0",
      "Lỗi biên dịch tại hàm main khi gọi new Entity(5)",
      "Chương trình chạy bình thường và ném NullPointerException tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Biến blank final (khai báo final nhưng không khởi tạo ngay tại dòng khai báo) bắt buộc phải được gán giá trị chính xác một lần trong TẤT CẢ các constructor của lớp (trừ khi gọi constructor khác qua this()). Vì constructor Entity() không gán giá trị cho id, trình biên dịch sẽ báo lỗi: 'variable id might not have been initialized'.",
    "difficulty": "medium",
    "tags": ["Final", "Blank-Final", "Compile-Error"]
  },
  {
    "id": "L1_Q17",
    "lessonId": 1,
    "title": "Đoạn mã sau xảy ra lỗi gì khi biên dịch?",
    "code": "class Student {\n    String name;\n    int age;\n    Student(String name) {\n        System.out.println(\"Khoi tao sinh vien: \" + name);\n        this(name, 18); // loi tai dong nay\n    }\n    Student(String name, int age) {\n        this.name = name;\n        this.age = age;\n    }\n}",
    "options": [
      "Lỗi biên dịch: Lời gọi this(...) phải là câu lệnh đầu tiên trong phương thức khởi tạo",
      "Lỗi biên dịch: Không được phép nạp chồng constructor có số lượng tham số khác nhau",
      "Lỗi biên dịch: Biến age chưa được khởi tạo",
      "Biên dịch thành công nhưng xảy ra vòng lặp vô tận"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc ngữ pháp của Java (JLS): Lời gọi constructor khác trong cùng lớp bằng this(...) hoặc gọi constructor lớp cha bằng super(...) BẮT BUỘC phải là câu lệnh đầu tiên trong thân constructor. Do có lệnh System.out.println đứng trước this(...) nên trình biên dịch báo lỗi: 'call to this must be first statement in constructor'.",
    "difficulty": "easy",
    "tags": ["Constructor-Chaining", "Compile-Error"]
  },
  {
    "id": "L1_Q18",
    "lessonId": 1,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "class Calculator {\n    int scale = 10;\n    public static int compute(int val) {\n        return val * scale;\n    }\n}",
    "options": [
      "Lỗi biên dịch: Phương thức static không thể truy cập trực tiếp trường non-static 'scale'",
      "Biên dịch thành công và biến scale được coi là static ngầm định",
      "Lỗi biên dịch do từ khóa static không thể áp dụng cho hàm trả về int",
      "Chương trình chạy bình thường không có lỗi"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức static thuộc về phạm vi lớp và có thể được gọi mà không cần bất kỳ đối tượng nào (không có con trỏ 'this'). Do đó nó không thể truy cập trực tiếp các trường dữ liệu non-static (instance fields) của lớp. Lỗi biên dịch: 'non-static variable scale cannot be referenced from a static context'.",
    "difficulty": "easy",
    "tags": ["Static", "Compile-Error"]
  },
  {
    "id": "L1_Q19",
    "lessonId": 1,
    "title": "Sau khi thực hiện xong hàm main, có bao nhiêu đối tượng Node bị thu hồi bởi Garbage Collector?",
    "code": "class Node {\n    int val;\n    Node(int val) { this.val = val; }\n}\npublic class GCTest {\n    public static void main(String[] args) {\n        Node n1 = new Node(1); // Obj 1\n        Node n2 = new Node(2); // Obj 2\n        Node n3 = new Node(3); // Obj 3\n        n1 = n2;\n        n2 = n3;\n        n3 = null;\n        // Tai diem nay co bao nhieu doi tuong du dieu kien cho GC?\n    }\n}",
    "options": [
      "1 đối tượng (Obj 1)",
      "2 đối tượng (Obj 1 và Obj 3)",
      "3 đối tượng",
      "0 đối tượng"
    ],
    "correctAnswer": 0,
    "explanation": "Phân tích tham chiếu: Ban đầu có 3 đối tượng riêng biệt. Khi n1 = n2: n1 trỏ sang Obj 2. Lúc này Obj 1 không còn bất kỳ biến nào trỏ tới -> Obj 1 trở thành unreachable (đủ điều kiện cho GC). Khi n2 = n3: n2 trỏ sang Obj 3. Khi n3 = null: n3 không trỏ Obj 3 nữa nhưng n2 vẫn đang trỏ tới Obj 3 -> Obj 3 vẫn sống. Biến n1 vẫn trỏ Obj 2 -> Obj 2 vẫn sống. Vậy chỉ có duy nhất 1 đối tượng là Obj 1 đủ điều kiện cho GC thu hồi.",
    "difficulty": "hard",
    "tags": ["GC-Reachability", "Memory-Analysis"]
  },
  {
    "id": "L1_Q20",
    "lessonId": 1,
    "title": "Đoạn mã sau minh họa cơ chế copy constructor nông (shallow copy). Kết quả in ra là gì?",
    "code": "class Battery {\n    int capacity;\n    Battery(int cap) { this.capacity = cap; }\n}\nclass Phone {\n    Battery bat;\n    Phone(Battery bat) { this.bat = bat; }\n    Phone(Phone p) { this.bat = p.bat; } // Shallow copy\n}\npublic class Main {\n    public static void main(String[] args) {\n        Phone p1 = new Phone(new Battery(3000));\n        Phone p2 = new Phone(p1);\n        p2.bat.capacity = 4500;\n        System.out.println(p1.bat.capacity + \" \" + p2.bat.capacity);\n    }\n}",
    "options": [
      "4500 4500",
      "3000 4500",
      "3000 3000",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Copy constructor của Phone chỉ sao chép biến tham chiếu bat (this.bat = p.bat). Cả p1 và p2 cùng trỏ chung vào một đối tượng Battery duy nhất trên Heap. Khi thay đổi dung lượng qua p2.bat.capacity = 4500, đối tượng dùng chung bị biến đổi, nên p1.bat.capacity cũng mang giá trị 4500.",
    "difficulty": "medium",
    "tags": ["Copy-Constructor", "Shallow-Copy"]
  }
]

# ==============================================================================
# LESSON 2: Kế thừa & Đa hình (Inheritance & Polymorphism)
# ==============================================================================
lesson2_questions = [
  {
    "id": "L2_Q01",
    "lessonId": 2,
    "title": "Phát biểu nào sau đây phân biệt chính xác nhất giữa Ghi đè phương thức (Method Overriding) và Che giấu phương thức (Method Hiding) trong Java?",
    "code": None,
    "options": [
      "Phương thức instance được override và giải quyết tại runtime (liên kết động); phương thức static bị che giấu (hiding) và giải quyết tại compile-time dựa trên kiểu tham chiếu",
      "Cả phương thức static và instance đều được ghi đè đa hình tại runtime",
      "Phương thức static không thể kế thừa nên không xảy ra hiện tượng hiding",
      "Method hiding chỉ áp dụng cho biến dữ liệu (field), không áp dụng cho phương thức static"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, chỉ có instance methods mới tham gia vào cơ chế đa hình động (Dynamic Binding / Late Binding) thông qua bảng phương thức ảo (vtable). Phương thức static gắn liền với Class chứ không gắn với instance, do đó khi lớp con định nghĩa phương thức static trùng chữ ký với lớp cha, nó chỉ che giấu (hiding) phương thức của cha. Lời gọi static method được gắn kết tại compile-time dựa vào kiểu khai báo của biến tham chiếu.",
    "difficulty": "hard",
    "tags": ["Polymorphism", "Overriding", "Hiding", "Dynamic-Binding"]
  },
  {
    "id": "L2_Q02",
    "lessonId": 2,
    "title": "Quy tắc nào sau đây về đặc tả truy cập (Access Modifier) BẮT BUỘC phải tuân thủ khi ghi đè (override) phương thức của lớp cha?",
    "code": None,
    "options": [
      "Phương thức ghi đè ở lớp con không được phép thu hẹp quyền truy cập so với phương thức ở lớp cha",
      "Phương thức ghi đè ở lớp con phải có cùng chính xác đặc tả truy cập với lớp cha",
      "Phương thức ở lớp con luôn bắt buộc phải là public",
      "Phương thức ghi đè có thể thu hẹp quyền truy cập nếu phương thức đó trả về void"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc Liskov Substitution Principle và JLS quy định: phương thức ghi đè ở lớp con không được thu hẹp quyền truy cập (không được giảm độ mở). Ví dụ: nếu lớp cha là public thì con bắt buộc phải là public; nếu cha là protected thì con có thể là protected hoặc public, nhưng không được là default hay private.",
    "difficulty": "medium",
    "tags": ["Overriding", "Access-Modifiers", "LSP"]
  },
  {
    "id": "L2_Q03",
    "lessonId": 2,
    "title": "Khái niệm 'Kiểu trả về đồng biến' (Covariant Return Type) từ Java 5 cho phép điều gì khi ghi đè phương thức?",
    "code": None,
    "options": [
      "Phương thức ở lớp con có thể trả về một kiểu dữ liệu con (subtype) của kiểu trả về ở lớp cha",
      "Phương thức ở lớp con có thể trả về kiểu dữ liệu hoàn toàn bất kỳ",
      "Phương thức ở lớp con có thể đổi kiểu trả về từ void sang Object",
      "Phương thức ở lớp con có thể đổi kiểu trả về giữa các kiểu nguyên thủy (ví dụ int sang double)"
    ],
    "correctAnswer": 0,
    "explanation": "Covariant Return Type cho phép phương thức ghi đè ở lớp con trả về kiểu đối tượng là lớp con (subtype) của kiểu trả về trong phương thức lớp cha. Ví dụ: nếu lớp cha trả về Number thì lớp con có thể ghi đè và trả về Integer.",
    "difficulty": "medium",
    "tags": ["Overriding", "Covariant-Return"]
  },
  {
    "id": "L2_Q04",
    "lessonId": 2,
    "title": "Phát biểu nào sau đây là ĐÚNG về Upcasting và Downcasting trong Java?",
    "code": None,
    "options": [
      "Upcasting luôn an toàn và được thực hiện ngầm định; Downcasting phải ép kiểu tường minh và có thể gây lỗi ClassCastException tại runtime",
      "Cả Upcasting và Downcasting đều hoàn toàn an toàn và được tự động thực hiện ngầm định",
      "Downcasting luôn được kiểm tra an toàn tại thời điểm biên dịch nên không bao giờ ném ngoại lệ khi chạy",
      "Upcasting đòi hỏi phải ép kiểu tường minh bằng dấu ngoặc đơn (Parent) child"
    ],
    "correctAnswer": 0,
    "explanation": "Upcasting (ép kiểu từ con lên cha) luôn an toàn vì mọi đối tượng con đều 'is-a' đối tượng cha, JVM thực hiện ngầm định. Downcasting (ép kiểu từ cha xuống con) tiềm ẩn rủi ro vì đối tượng thực tế trên Heap có thể không phải là thể hiện của lớp con đó; nếu sai kiểu, JVM sẽ ném ClassCastException tại runtime.",
    "difficulty": "easy",
    "tags": ["Upcasting", "Downcasting", "ClassCastException"]
  },
  {
    "id": "L2_Q05",
    "lessonId": 2,
    "title": "Điều gì xảy ra nếu constructor của lớp con không gọi tường minh super(...) và lớp cha không có constructor không tham số (no-arg constructor)?",
    "code": None,
    "options": [
      "Trình biên dịch báo lỗi tại constructor của lớp con vì không tìm thấy constructor mặc định của lớp cha",
      "Chương trình biên dịch bình thường và JVM tự động gán giá trị 0/null cho các trường của cha",
      "Chương trình ném NullPointerException tại thời điểm khởi tạo đối tượng",
      "Lớp con tự động bỏ qua việc khởi tạo các trường dữ liệu của lớp cha"
    ],
    "correctAnswer": 0,
    "explanation": "Nếu constructor lớp con không gọi super(...) tường minh, trình biên dịch sẽ tự động chèn super() không tham số vào dòng đầu tiên. Nếu lớp cha đã định nghĩa constructor có tham số mà không có constructor không tham số, super() sẽ không tồn tại, dẫn đến lỗi biên dịch: 'constructor Parent in class Parent cannot be applied to given types'.",
    "difficulty": "medium",
    "tags": ["Inheritance", "Constructor", "Super"]
  },
  {
    "id": "L2_Q06",
    "lessonId": 2,
    "title": "Hiện tượng 'Cắt gọt đối tượng' (Object Slicing) xảy ra trong C++ khi truyền đối tượng theo giá trị có xảy ra trong Java hay không? Vì sao?",
    "code": None,
    "options": [
      "Không xảy ra, vì trong Java mọi biến đối tượng đều là biến tham chiếu; đối tượng thực sự trên Heap luôn giữ đầy đủ kiểu dữ liệu và thuộc tính của lớp con",
      "Có xảy ra khi ép kiểu Upcasting về kiểu lớp cha",
      "Có xảy ra khi truyền đối tượng làm tham số cho phương thức",
      "Chỉ xảy ra khi lớp cha là một abstract class"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, không bao giờ có hiện tượng Object Slicing như trong C++. Mọi đối tượng đều nằm trên Heap và các biến chỉ lưu tham chiếu (địa chỉ). Khi gán một đối tượng con cho biến tham chiếu kiểu cha (Upcasting), đối tượng trên Heap vẫn giữ nguyên vẹn 100% cấu trúc, kiểu thực tế và các trường dữ liệu của lớp con.",
    "difficulty": "hard",
    "tags": ["Object-Slicing", "JVM-Memory", "Polymorphism"]
  },
  {
    "id": "L2_Q07",
    "lessonId": 2,
    "title": "Biểu thức (null instanceof AnyClass) trong Java sẽ trả về kết quả gì?",
    "code": None,
    "options": [
      "Luôn luôn trả về false cho bất kỳ class hay interface nào",
      "Ném ngoại lệ NullPointerException tại runtime",
      "Trả về true nếu AnyClass là lớp Object",
      "Lỗi biên dịch: không thể áp dụng instanceof cho null"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc chuẩn của toán tử instanceof trong JLS: nếu toán hạng bên trái là null, biểu thức luôn đánh giá là false với bất kỳ kiểu dữ liệu nào mà không ném NullPointerException.",
    "difficulty": "easy",
    "tags": ["Instanceof", "Null-Safety"]
  },
  {
    "id": "L2_Q08",
    "lessonId": 2,
    "title": "Từ khóa final khi được áp dụng cho một phương thức (method) và một lớp (class) có tác dụng gì?",
    "code": None,
    "options": [
      "Phương thức final không thể bị ghi đè (override) ở lớp con; Lớp final không thể bị kế thừa (extend)",
      "Phương thức final không thể bị nạp chồng (overload); Lớp final không thể chứa phương thức static",
      "Phương thức final chỉ được gọi một lần duy nhất; Lớp final không thể khởi tạo đối tượng",
      "Phương thức final tự động chạy đa luồng an toàn; Lớp final tự động lưu trong bộ nhớ cache"
    ],
    "correctAnswer": 0,
    "explanation": "Từ khóa final ngăn chặn sự thay đổi: Trên phương thức, nó ngăn các lớp con ghi đè phương thức đó (đảm bảo tính toàn vẹn logic, ví dụ Object.getClass()). Trên lớp, nó ngăn cản bất kỳ lớp nào kế thừa nó (ví dụ lớp String, Math, Integer).",
    "difficulty": "easy",
    "tags": ["Final", "Inheritance", "Overriding"]
  },
  {
    "id": "L2_Q09",
    "lessonId": 2,
    "title": "Thành phần protected của một lớp ở Package A có thể được truy cập từ Package B trong trường hợp nào?",
    "code": None,
    "options": [
      "Chỉ bên trong các lớp con (subclass) ở Package B kế thừa từ lớp ở Package A, thông qua cơ chế kế thừa",
      "Mọi lớp ở Package B đều truy cập được nếu import lớp ở Package A",
      "Hoàn toàn không thể truy cập được từ package khác dưới bất kỳ hình thức nào",
      "Chỉ truy cập được nếu lớp ở Package B là lớp tĩnh (static class)"
    ],
    "correctAnswer": 0,
    "explanation": "Quyền protected cho phép truy cập: 1) Trong cùng package (giống default); 2) Khác package: CHỈ các lớp con kế thừa từ lớp đó mới có thể truy cập thành phần protected thông qua quan hệ kế thừa (hoặc qua con trỏ super/this của chính lớp con đó).",
    "difficulty": "medium",
    "tags": ["Protected", "Access-Modifiers", "Package"]
  },
  {
    "id": "L2_Q10",
    "lessonId": 2,
    "title": "Sự khác biệt cốt lõi giữa Nạp chồng phương thức (Overloading) và Ghi đè phương thức (Overriding) là gì?",
    "code": None,
    "options": [
      "Overloading là đa hình lúc biên dịch (Compile-time / Static binding) dựa vào số lượng/kiểu tham số; Overriding là đa hình lúc thực thi (Runtime / Dynamic binding) dựa vào đối tượng thực tế",
      "Overloading chỉ xảy ra giữa hai lớp cha con; Overriding chỉ xảy ra trong nội bộ cùng một lớp",
      "Overloading bắt buộc phải có annotation @Override; Overriding không cần",
      "Overloading giải quyết tại runtime; Overriding giải quyết tại compile-time"
    ],
    "correctAnswer": 0,
    "explanation": "Overloading (nạp chồng) xảy ra trong cùng một lớp hoặc qua kế thừa khi các phương thức cùng tên nhưng khác danh sách tham số (khác chữ ký). Trình biên dịch quyết định phương thức nào được gọi ngay tại compile-time (Static binding). Overriding (ghi đè) xảy ra khi lớp con định nghĩa lại phương thức của lớp cha có cùng chữ ký. JVM quyết định phương thức thực thi tại runtime dựa vào đối tượng thực tế trên Heap (Dynamic binding).",
    "difficulty": "medium",
    "tags": ["Overloading", "Overriding", "Static-Binding", "Dynamic-Binding"]
  },
  {
    "id": "L2_Q11",
    "lessonId": 2,
    "title": "Cho đoạn mã sau (trích từ Đề thi mẫu UET). Kết quả in ra màn hình là gì?",
    "code": "class Employee {\n    public String role() { return \"Employee\"; }\n    public static String policy() { return \"standard\"; }\n}\nclass Manager extends Employee {\n    @Override\n    public String role() { return \"Manager\"; }\n    public static String policy() { return \"management\"; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Employee e = new Manager();\n        System.out.println(e.role());\n        System.out.println(e.policy());\n        System.out.println(((Manager) e).policy());\n    }\n}",
    "options": [
      "Manager\\nstandard\\nmanagement",
      "Manager\\nmanagement\\nmanagement",
      "Employee\\nstandard\\nmanagement",
      "Manager\\nstandard\\nstandard"
    ],
    "correctAnswer": 0,
    "explanation": "1) e.role(): role() là instance method được override, JVM sử dụng dynamic binding gọi phương thức của đối tượng thực tế trên Heap (Manager) -> in ra 'Manager'.\\n2) e.policy(): policy() là static method bị che giấu (hiding). Lời gọi gắn kết tại compile-time dựa vào kiểu khai báo của biến tham chiếu e (kiểu Employee) -> in ra 'standard'.\\n3) ((Manager) e).policy(): Ép kiểu tham chiếu sang Manager tại compile-time, nên gọi policy() của lớp Manager -> in ra 'management'.",
    "difficulty": "hard",
    "tags": ["Static-Hiding", "Dynamic-Binding", "UET-Exam"]
  },
  {
    "id": "L2_Q12",
    "lessonId": 2,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi chạy?",
    "code": "class Parent {}\nclass Child extends Parent {\n    void secret() { System.out.println(\"Secret\"); }\n}\npublic class TestCast {\n    public static void main(String[] args) {\n        Parent p = new Parent();\n        Child c = (Child) p;\n        c.secret();\n    }\n}",
    "options": [
      "Ném ngoại lệ ClassCastException tại dòng ép kiểu Child c = (Child) p",
      "Chương trình in ra 'Secret'",
      "Lỗi biên dịch tại dòng Child c = (Child) p",
      "In ra null và kết thúc bình thường"
    ],
    "correctAnswer": 0,
    "explanation": "Biến p tham chiếu tới một đối tượng thực sự kiểu Parent trên Heap. Đối tượng này không phải là một instance của Child. Khi cố gắng ép kiểu xuống (Downcasting) bằng (Child) p, trình biên dịch cho phép vì Child là con của Parent, nhưng khi chạy JVM kiểm tra kiểu thực tế và ném ClassCastException: class Parent cannot be cast to class Child.",
    "difficulty": "medium",
    "tags": ["Downcasting", "ClassCastException"]
  },
  {
    "id": "L2_Q13",
    "lessonId": 2,
    "title": "Đoạn mã sau kiểm tra tính đa hình của thuộc tính (field). Kết quả in ra là gì?",
    "code": "class Base {\n    int val = 10;\n    void show() { System.out.print(\"Base:\" + val + \" \"); }\n}\nclass Sub extends Base {\n    int val = 20;\n    void show() { System.out.print(\"Sub:\" + val + \" \"); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Base b = new Sub();\n        System.out.print(b.val + \" \");\n        b.show();\n    }\n}",
    "options": [
      "10 Sub:20 ",
      "20 Sub:20 ",
      "10 Base:10 ",
      "20 Base:10 "
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, thuộc tính (fields) KHÔNG có tính đa hình (không bị override mà chỉ bị shadow/hide). Truy cập thuộc tính b.val được giải quyết tại compile-time dựa vào kiểu khai báo của biến tham chiếu b (kiểu Base) -> lấy Base.val là 10. Trong khi đó, phương thức show() có tính đa hình (dynamic binding) nên gọi show() của Sub -> in ra 'Sub:20'. Kết quả là: '10 Sub:20 '.",
    "difficulty": "hard",
    "tags": ["Field-Hiding", "Polymorphism", "Dynamic-Binding"]
  },
  {
    "id": "L2_Q14",
    "lessonId": 2,
    "title": "Thứ tự in ra màn hình khi chạy chương trình sau là gì?",
    "code": "class GrandParent {\n    GrandParent() { System.out.print(\"G \"); }\n}\nclass Parent extends GrandParent {\n    Parent() { System.out.print(\"P \"); }\n}\nclass Child extends Parent {\n    Child() { System.out.print(\"C \"); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        new Child();\n    }\n}",
    "options": [
      "G P C ",
      "C P G ",
      "P G C ",
      "C G P "
    ],
    "correctAnswer": 0,
    "explanation": "Khi khởi tạo đối tượng Child, constructor của Child tự động gọi super() của Parent, constructor Parent lại tự động gọi super() của GrandParent, constructor GrandParent gọi super() của Object. Các constructor hoàn thành từ trên đỉnh cây phả hệ xuống dưới: GrandParent ('G ') -> Parent ('P ') -> Child ('C '). Kết quả in ra là 'G P C '.",
    "difficulty": "easy",
    "tags": ["Constructor-Chaining", "Inheritance-Order"]
  },
  {
    "id": "L2_Q15",
    "lessonId": 2,
    "title": "Bẫy gọi phương thức đa hình bên trong constructor của lớp cha! Kết quả in ra màn hình là gì?",
    "code": "class Super {\n    Super() { printThree(); }\n    void printThree() { System.out.print(\"three \"); }\n}\nclass Sub extends Super {\n    int three = 3;\n    @Override\n    void printThree() { System.out.print(three + \" \"); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        new Sub();\n    }\n}",
    "options": [
      "0 ",
      "3 ",
      "three ",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Đây là một bẫy kinh điển trong OOP Java! Khi new Sub() chạy, constructor của Super được thực thi trước tiên. Bên trong constructor Super có lời gọi printThree(). Do cơ chế dynamic binding, phương thức printThree() của Sub được gọi. Tuy nhiên tại thời điểm này, constructor của Sub CHƯA hề chạy, nên biến instance 'three' của Sub chưa được gán giá trị 3 mà vẫn giữ giá trị mặc định của kiểu int là 0! Do đó in ra '0 '.",
    "difficulty": "hard",
    "tags": ["Polymorphism", "Constructor-Trap", "JVM-Internals"]
  },
  {
    "id": "L2_Q16",
    "lessonId": 2,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "import java.io.IOException;\nclass A {\n    void readFile() throws IOException {}\n}\nclass B extends A {\n    @Override\n    void readFile() throws Exception {} // Dong nay\n}",
    "options": [
      "Lỗi biên dịch: Phương thức ghi đè không được khai báo ném ngoại lệ Checked rộng hơn phương thức của lớp cha",
      "Biên dịch thành công vì Exception là lớp cha của IOException",
      "Lỗi biên dịch do thiếu từ khóa public",
      "Chương trình chạy bình thường không có lỗi"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc ghi đè phương thức với ngoại lệ kiểm tra (Checked Exception): Phương thức ghi đè ở lớp con không được phép ném ngoại lệ Checked mới hoặc rộng hơn (broader) so với phương thức ở lớp cha. Ở đây lớp cha ném IOException, nhưng lớp con ném Exception (rộng hơn IOException), do đó trình biên dịch sẽ báo lỗi: 'readFile() in B cannot override readFile() in A; overridden method does not throw java.lang.Exception'.",
    "difficulty": "hard",
    "tags": ["Overriding", "Exception-Rules", "Compile-Error"]
  },
  {
    "id": "L2_Q17",
    "lessonId": 2,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "class Parent {\n    public void display() { System.out.println(\"Parent\"); }\n}\nclass Child extends Parent {\n    @Override\n    protected void display() { System.out.println(\"Child\"); }\n}",
    "options": [
      "Lỗi biên dịch: Không thể thu hẹp quyền truy cập từ public xuống protected khi ghi đè",
      "Biên dịch thành công và phương thức display của Child có quyền protected",
      "Lỗi biên dịch do thiếu phương thức main",
      "Chương trình chạy bình thường"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức display() trong lớp Parent có mức truy cập là public. Lớp Child cố gắng ghi đè với mức protected, vi phạm quy tắc: không được giảm độ mở (thu hẹp quyền truy cập) của phương thức ghi đè. Trình biên dịch báo lỗi: 'display() in Child cannot override display() in Parent; attempting to assign weaker access privileges; was public'.",
    "difficulty": "medium",
    "tags": ["Overriding", "Access-Modifiers", "Compile-Error"]
  },
  {
    "id": "L2_Q18",
    "lessonId": 2,
    "title": "Đoạn mã sau kiểm tra cơ chế giải quyết nạp chồng (Overloading resolution). Kết quả in ra là gì?",
    "code": "public class OverloadTest {\n    static void print(Object o) { System.out.print(\"Object \"); }\n    static void print(String s) { System.out.print(\"String \"); }\n    public static void main(String[] args) {\n        print(null);\n    }\n}",
    "options": [
      "String ",
      "Object ",
      "Lỗi biên dịch do mập mờ (ambiguous method call)",
      "Ném ngoại lệ NullPointerException tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Khi giải quyết nạp chồng phương thức với đối số null, trình biên dịch Java luôn ưu tiên chọn phương thức có kiểu tham số cụ thể nhất (most specific). Do String kế thừa từ Object nên String là kiểu cụ thể hơn (subtype). Vì vậy trình biên dịch chọn print(String s) và in ra 'String '.",
    "difficulty": "hard",
    "tags": ["Overloading", "Most-Specific", "Null-Argument"]
  },
  {
    "id": "L2_Q19",
    "lessonId": 2,
    "title": "Đoạn mã sau in ra kết quả gì khi chạy?",
    "code": "interface Flyable {}\nclass Bird implements Flyable {}\nclass Airplane implements Flyable {}\npublic class TestInstanceof {\n    public static void main(String[] args) {\n        Flyable f = new Airplane();\n        System.out.println((f instanceof Airplane) + \" \" + (f instanceof Bird) + \" \" + (f instanceof Flyable));\n    }\n}",
    "options": [
      "true false true",
      "true true true",
      "false false true",
      "true false false"
    ],
    "correctAnswer": 0,
    "explanation": "Đối tượng thực tế trên Heap được tạo bởi new Airplane(). Nó là một thể hiện của lớp Airplane -> f instanceof Airplane là true. Nó không phải là Bird -> f instanceof Bird là false. Nó triển khai interface Flyable -> f instanceof Flyable là true. Kết quả là 'true false true'.",
    "difficulty": "easy",
    "tags": ["Instanceof", "Interface-Check"]
  },
  {
    "id": "L2_Q20",
    "lessonId": 2,
    "title": "Bẫy đồng biến mảng (Array Covariance) trong Java! Hiện tượng gì xảy ra khi chạy đoạn mã sau?",
    "code": "public class ArrayTrap {\n    public static void main(String[] args) {\n        Object[] arr = new String[3];\n        arr[0] = \"Hello\";\n        arr[1] = Integer.valueOf(100); // Dong nay\n    }\n}",
    "options": [
      "Ném ngoại lệ ArrayStoreException tại runtime khi gán Integer vào arr[1]",
      "Lỗi biên dịch tại dòng arr[1] = Integer.valueOf(100)",
      "Chương trình chạy bình thường không có lỗi",
      "Ném ClassCastException tại thời điểm khởi tạo Object[]"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, mảng có tính đồng biến (covariant), tức String[] có thể được gán cho Object[]. Do đó mã nguồn vượt qua khâu biên dịch thành công. Tuy nhiên tại runtime, mảng lưu giữ thông tin kiểu thực tế của nó (reified type là String[]). Khi cố gắng ghi một Integer vào mảng String, JVM phát hiện xung đột kiểu và lập tức ném java.lang.ArrayStoreException.",
    "difficulty": "hard",
    "tags": ["Array-Covariance", "ArrayStoreException", "Runtime-Exception"]
  }
]

# ==============================================================================
# LESSON 3: Abstract Class & Interface
# ==============================================================================
lesson3_questions = [
  {
    "id": "L3_Q01",
    "lessonId": 3,
    "title": "Điểm khác biệt căn bản nhất về mặt lưu trữ trạng thái (state) giữa Abstract Class và Interface trong Java là gì?",
    "code": None,
    "options": [
      "Abstract Class có thể chứa các biến thực thể (instance fields) có trạng thái thay đổi; Interface chỉ có thể chứa hằng số (public static final)",
      "Interface có thể chứa biến thực thể private, Abstract Class thì không",
      "Abstract Class không thể có constructor; Interface có constructor mặc định",
      "Interface cho phép kế thừa đơn, Abstract Class cho phép đa kế thừa"
    ],
    "correctAnswer": 0,
    "explanation": "Khác biệt cốt lõi: Abstract Class đại diện cho bản chất đối tượng ('is-a') và có thể lưu giữ trạng thái riêng thông qua các biến thực thể non-static, non-final, đồng thời có constructor để khởi tạo trạng thái đó. Ngược lại, Interface đại diện cho hợp đồng hành vi ('can-do'), mọi thuộc tính khai báo trong interface đều ngầm định là hằng số public static final, không có constructor và không lưu trạng thái đối tượng.",
    "difficulty": "medium",
    "tags": ["Abstract-Class", "Interface", "OOP-Design"]
  },
  {
    "id": "L3_Q02",
    "lessonId": 3,
    "title": "Mẫu thiết kế Template Method (Phương thức khuôn mẫu) thường được cài đặt bằng Abstract Class như thế nào?",
    "code": None,
    "options": [
      "Lớp cha định nghĩa khung sườn thuật toán trong một phương thức cụ thể (thường là final), và ủy quyền các bước chi tiết cho các phương thức trừu tượng (abstract methods) để lớp con cài đặt",
      "Lớp con ghi đè toàn bộ phương thức khung sườn của lớp cha",
      "Tất cả các phương thức trong Abstract Class đều bắt buộc phải là abstract",
      "Sử dụng interface để thay thế hoàn toàn thuật toán tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Template Method pattern định nghĩa khung sườn của một thuật toán trong một phương thức (thường đánh dấu là final để ngăn lớp con phá vỡ cấu trúc thuật toán). Các bước cụ thể trong thuật toán được khai báo là abstract methods hoặc hook methods để các lớp con tự do triển khai theo nghiệp vụ riêng.",
    "difficulty": "medium",
    "tags": ["Template-Method", "Design-Patterns", "Abstract-Class"]
  },
  {
    "id": "L3_Q03",
    "lessonId": 3,
    "title": "Mọi trường dữ liệu (fields) khai báo bên trong một Interface trong Java có đặc tính ngầm định nào?",
    "code": None,
    "options": [
      "Luôn luôn là public static final",
      "Mặc định là private final",
      "Mặc định là protected static",
      "Là biến thực thể bình thường có thể sửa đổi bởi lớp triển khai"
    ],
    "correctAnswer": 0,
    "explanation": "Theo đặc tả JLS, bất kỳ biến nào khai báo trong interface, dù bạn không ghi modifier nào, đều ngầm định (implicitly) có ba từ khóa: public static final (tức là hằng số dùng chung mức interface).",
    "difficulty": "easy",
    "tags": ["Interface", "Modifiers", "Constants"]
  },
  {
    "id": "L3_Q04",
    "lessonId": 3,
    "title": "Từ Java 8, phương thức mặc định (default method) trong Interface được giới thiệu nhằm mục đích chủ yếu nào?",
    "code": None,
    "options": [
      "Cho phép bổ sung phương thức mới vào interface mà không làm hỏng tính tương thích ngược (backward compatibility) của các lớp đã triển khai trước đó",
      "Thay thế hoàn toàn Abstract Class trong mọi tình huống thiết kế",
      "Cho phép interface lưu trữ biến thực thể động",
      "Cho phép phương thức trong interface chạy nhanh hơn gấp 2 lần"
    ],
    "correctAnswer": 0,
    "explanation": "Mục đích lớn nhất của default method trong Java 8 là 'Interface Evolution' và tương thích ngược (Backward Compatibility). Nhờ có default method, các kỹ sư Java có thể bổ sung các phương thức như forEach(), stream(), removeIf() vào Collection interface mà không làm lỗi hàng triệu lớp của người dùng đang triển khai Collection từ Java 7 trở về trước.",
    "difficulty": "medium",
    "tags": ["Interface", "Default-Method", "Java8"]
  },
  {
    "id": "L3_Q05",
    "lessonId": 3,
    "title": "Phát biểu nào sau đây là ĐÚNG về phương thức static trong Interface (từ Java 8)?",
    "code": None,
    "options": [
      "Thuộc về phạm vi của chính interface đó, chỉ có thể được gọi qua TênInterface.tênPhươngThức() và không được kế thừa bởi lớp triển khai",
      "Được kế thừa bình thường và có thể gọi qua tên lớp con hoặc đối tượng lớp con",
      "Có thể bị ghi đè (override) bởi các lớp triển khai interface",
      "Không được phép có phần thân mã lệnh (body)"
    ],
    "correctAnswer": 0,
    "explanation": "Static method trong interface thuộc về namespace của interface. Nó KHÔNG được kế thừa bởi các lớp triển khai interface đó. Bạn bắt buộc phải gọi bằng cú pháp: InterfaceName.staticMethod(). Gọi qua instance hoặc tên lớp con sẽ gây lỗi biên dịch.",
    "difficulty": "hard",
    "tags": ["Interface", "Static-Method", "Java8"]
  },
  {
    "id": "L3_Q06",
    "lessonId": 3,
    "title": "Quy tắc giải quyết xung đột khi một lớp triển khai 2 interface cùng định nghĩa một default method có cùng chữ ký (Diamond Problem) là gì?",
    "code": None,
    "options": [
      "Trình biên dịch báo lỗi và bắt buộc lớp đó phải ghi đè (override) phương thức để giải quyết mập mờ tường minh",
      "JVM tự động chọn interface được khai báo đầu tiên trong mệnh đề implements",
      "JVM tự động chọn ngẫu nhiên một trong hai phương thức khi chạy",
      "Chương trình tự động ghép nối phần thân của cả hai phương thức lại với nhau"
    ],
    "correctAnswer": 0,
    "explanation": "Khi xảy ra xung đột default method (hai interface có cùng method signature và không có quan hệ kế thừa lẫn nhau), trình biên dịch Java sẽ báo lỗi 'inherits unrelated defaults'. Lập trình viên bắt buộc phải ghi đè phương thức đó trong lớp triển khai, và có thể tùy ý chọn gọi implementation của interface nào bằng cú pháp InterfaceA.super.methodName().",
    "difficulty": "hard",
    "tags": ["Diamond-Problem", "Default-Method", "Interface"]
  },
  {
    "id": "L3_Q07",
    "lessonId": 3,
    "title": "Nguyên tắc 'Lớp luôn chiến thắng' (Class Wins Rule) trong Java 8 giải quyết xung đột phương thức như thế nào?",
    "code": None,
    "options": [
      "Phương thức được cài đặt trong lớp cha (superclass) luôn được ưu tiên áp dụng và ghi đè hoàn toàn default method của interface",
      "Default method của interface luôn ghi đè phương thức của lớp cha",
      "Trình biên dịch báo lỗi bắt buộc lớp con phải tự viết lại",
      "Phương thức nào ngắn hơn sẽ được JVM ưu tiên chọn"
    ],
    "correctAnswer": 0,
    "explanation": "Theo quy tắc 'Classes win' của JLS: Nếu một lớp vừa kế thừa một phương thức cụ thể từ lớp cha (hoặc lớp ông bà), vừa implements một interface có default method cùng chữ ký, thì cài đặt ở lớp cha LUÔN ĐƯỢC CHỌN và default method của interface sẽ bị bỏ qua hoàn toàn.",
    "difficulty": "medium",
    "tags": ["Class-Wins", "Default-Method", "Java8"]
  },
  {
    "id": "L3_Q08",
    "lessonId": 3,
    "title": "Giao diện hàm (Functional Interface) được định nghĩa là interface thỏa mãn điều kiện nào sau đây?",
    "code": None,
    "options": [
      "Chứa duy nhất một phương thức trừu tượng (Single Abstract Method - SAM), có thể có thêm default hoặc static methods",
      "Không được phép chứa bất kỳ phương thức nào có phần thân",
      "Bắt buộc phải có đúng một phương thức duy nhất (kể cả default và static)",
      "Bắt buộc phải khai báo annotation @FunctionalInterface nếu không sẽ bị lỗi"
    ],
    "correctAnswer": 0,
    "explanation": "Functional Interface là interface chứa CHÍNH XÁC một phương thức trừu tượng (Single Abstract Method - SAM). Nó có thể có tùy ý số lượng default methods hoặc static methods. Annotation @FunctionalInterface là tùy chọn (optional) giúp trình biên dịch kiểm tra tính hợp lệ của SAM.",
    "difficulty": "easy",
    "tags": ["Functional-Interface", "SAM", "Java8"]
  },
  {
    "id": "L3_Q09",
    "lessonId": 3,
    "title": "Vì sao một Abstract Class KHÔNG THỂ khởi tạo đối tượng trực tiếp bằng toán tử new nhưng VẪN ĐƯỢC PHÉP có constructor?",
    "code": None,
    "options": [
      "Constructor của abstract class dùng để khởi tạo các thuộc tính của chính nó khi lớp con được khởi tạo thông qua lệnh super(...)",
      "Constructor đó chỉ dùng cho reflection của JVM chứ không chạy khi có kế thừa",
      "Đó là lỗi cú pháp tồn tại từ phiên bản Java cũ",
      "Constructor của abstract class chỉ dùng để tạo các đối tượng tĩnh (static)"
    ],
    "correctAnswer": 0,
    "explanation": "Abstract Class đại diện cho lớp cha chưa hoàn chỉnh nên không thể tạo instance trực tiếp bằng new. Tuy nhiên nó vẫn có trạng thái riêng (các trường dữ liệu). Constructor của Abstract Class được tạo ra để các lớp con gọi tới thông qua super(...) nhằm khởi tạo phần trạng thái kế thừa đó.",
    "difficulty": "medium",
    "tags": ["Abstract-Class", "Constructor", "OOP-Concept"]
  },
  {
    "id": "L3_Q10",
    "lessonId": 3,
    "title": "Mối quan hệ kế thừa giữa các Interface trong Java tuân theo quy tắc nào?",
    "code": None,
    "options": [
      "Một interface có thể kế thừa (extends) cùng lúc nhiều interface khác",
      "Một interface chỉ có thể kế thừa (extends) duy nhất một interface khác",
      "Một interface có thể implements các interface khác",
      "Interface không được phép kế thừa từ bất kỳ interface nào"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, trong khi Class chỉ được phép đơn kế thừa từ một Class khác (single inheritance), thì Interface ĐƯỢC PHÉP đa kế thừa từ nhiều interface khác bằng cú pháp: interface C extends A, B. Interface không dùng từ khóa implements.",
    "difficulty": "easy",
    "tags": ["Interface", "Multiple-Inheritance"]
  },
  {
    "id": "L3_Q11",
    "lessonId": 3,
    "title": "Đoạn mã sau giải quyết xung đột default method như thế nào? Kết quả in ra là gì?",
    "code": "interface Alpha {\n    default void hello() { System.out.print(\"Alpha \"); }\n}\ninterface Beta {\n    default void hello() { System.out.print(\"Beta \"); }\n}\nclass Combined implements Alpha, Beta {\n    public void hello() {\n        Alpha.super.hello();\n        System.out.print(\"Combined \");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        new Combined().hello();\n    }\n}",
    "options": [
      "Alpha Combined ",
      "Beta Combined ",
      "Lỗi biên dịch tại lớp Combined",
      "Combined "
    ],
    "correctAnswer": 0,
    "explanation": "Lớp Combined implements cả Alpha và Beta có cùng default method hello(). Lớp Combined đã override lại hello() một cách hợp lệ để xóa bỏ xung đột, đồng thời gọi đích danh Alpha.super.hello() để tái sử dụng mã của interface Alpha. Kết quả in ra: 'Alpha Combined '.",
    "difficulty": "medium",
    "tags": ["Diamond-Problem", "Default-Method", "Super-Call"]
  },
  {
    "id": "L3_Q12",
    "lessonId": 3,
    "title": "Áp dụng quy tắc 'Class Wins'. Kết quả in ra màn hình của đoạn mã sau là gì?",
    "code": "interface Greeting {\n    default void greet() { System.out.print(\"Interface Greet \"); }\n}\nclass Base {\n    public void greet() { System.out.print(\"Base Greet \"); }\n}\nclass Sub extends Base implements Greeting {}\npublic class Main {\n    public static void main(String[] args) {\n        Greeting g = new Sub();\n        g.greet();\n    }\n}",
    "options": [
      "Base Greet ",
      "Interface Greet ",
      "Lỗi biên dịch do xung đột phương thức greet()",
      "Ném ngoại lệ AbstractMethodError"
    ],
    "correctAnswer": 0,
    "explanation": "Theo quy tắc 'Class Wins' của Java 8: cài đặt của phương thức trong lớp cha (Base.greet()) luôn được ưu tiên hơn so với default method của interface (Greeting.greet()). Do đó khi gọi g.greet(), phương thức của lớp Base được thực thi -> in ra 'Base Greet '.",
    "difficulty": "medium",
    "tags": ["Class-Wins", "Default-Method", "Java8"]
  },
  {
    "id": "L3_Q13",
    "lessonId": 3,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch hoặc thực thi?",
    "code": "interface Printable {\n    static void print() { System.out.println(\"Printable Static\"); }\n}\nclass Doc implements Printable {}\npublic class Main {\n    public static void main(String[] args) {\n        Doc.print(); // Dong nay\n    }\n}",
    "options": [
      "Lỗi biên dịch: static method của interface không thể gọi thông qua lớp triển khai Doc",
      "In ra 'Printable Static'",
      "Ném NullPointerException tại runtime",
      "In ra 'Doc'"
    ],
    "correctAnswer": 0,
    "explanation": "Static method trong interface không được kế thừa bởi các class cài đặt nó. Vì vậy, gọi Doc.print() hoặc new Doc().print() đều gây lỗi biên dịch: 'cannot find symbol method print()'. Muốn gọi static method này, bắt buộc phải dùng tên interface: Printable.print().",
    "difficulty": "hard",
    "tags": ["Interface", "Static-Method", "Compile-Error"]
  },
  {
    "id": "L3_Q14",
    "lessonId": 3,
    "title": "Đoạn mã sau có lỗi gì khi biên dịch?",
    "code": "interface Config {\n    int TIMEOUT = 5000;\n}\npublic class Main {\n    public static void main(String[] args) {\n        Config.TIMEOUT += 1000;\n        System.out.println(Config.TIMEOUT);\n    }\n}",
    "options": [
      "Lỗi biên dịch: Không thể gán lại giá trị cho biến final TIMEOUT",
      "Lỗi biên dịch: Không thể truy cập trực tiếp biến TIMEOUT qua tên interface",
      "Biên dịch thành công và in ra 6000",
      "Ném IllegalAccessException tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Mọi thuộc tính khai báo trong interface ngầm định là 'public static final'. Do TIMEOUT là hằng số final, lệnh gán Config.TIMEOUT += 1000 cố gắng thay đổi giá trị của nó sẽ bị trình biên dịch từ chối: 'cannot assign a value to final variable TIMEOUT'.",
    "difficulty": "easy",
    "tags": ["Interface", "Final-Field", "Compile-Error"]
  },
  {
    "id": "L3_Q15",
    "lessonId": 3,
    "title": "Đoạn mã sau xảy ra lỗi gì khi biên dịch?",
    "code": "interface Worker {\n    void work();\n}\nclass Developer implements Worker {\n    void work() { // Dong nay\n        System.out.println(\"Coding...\");\n    }\n}",
    "options": [
      "Lỗi biên dịch: Phương thức work() trong Developer cố tình thu hẹp quyền truy cập từ public xuống default (package-private)",
      "Lỗi biên dịch: Thiếu annotation @Override",
      "Lỗi biên dịch: Developer phải khai báo là abstract",
      "Biên dịch thành công và in ra bình thường"
    ],
    "correctAnswer": 0,
    "explanation": "Mọi phương thức trừu tượng trong interface ngầm định có quyền truy cập là public. Khi lớp Developer triển khai phương thức work() mà không ghi rõ từ khóa public, phương thức đó sẽ có quyền mặc định (package-private). Điều này vi phạm quy tắc: không được thu hẹp quyền truy cập của phương thức ghi đè. Trình biên dịch báo lỗi: 'attempting to assign weaker access privileges; was public'.",
    "difficulty": "medium",
    "tags": ["Interface", "Access-Modifiers", "Compile-Error"]
  },
  {
    "id": "L3_Q16",
    "lessonId": 3,
    "title": "Đoạn mã sau minh họa constructor của Abstract Class. Kết quả in ra là gì?",
    "code": "abstract class Shape {\n    String color;\n    Shape(String color) {\n        this.color = color;\n        System.out.print(\"Shape:\" + color + \" \");\n    }\n}\nclass Circle extends Shape {\n    Circle(String color) {\n        super(color);\n        System.out.print(\"Circle \");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        new Circle(\"Red\");\n    }\n}",
    "options": [
      "Shape:Red Circle ",
      "Circle Shape:Red ",
      "Circle ",
      "Lỗi biên dịch: Abstract Class không được phép có constructor"
    ],
    "correctAnswer": 0,
    "explanation": "Abstract Class hoàn toàn có thể có constructor. Khi new Circle(\"Red\") được gọi, nó gọi super(color) lên constructor của Shape. Constructor Shape chạy in ra 'Shape:Red ', sau đó constructor Circle chạy tiếp in ra 'Circle '. Tổng cộng: 'Shape:Red Circle '.",
    "difficulty": "easy",
    "tags": ["Abstract-Class", "Constructor", "Inheritance"]
  },
  {
    "id": "L3_Q17",
    "lessonId": 3,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "@FunctionalInterface\ninterface Transformer {\n    int transform(int x);\n    int reverse(int x);\n}",
    "options": [
      "Lỗi biên dịch: Transformer không phải là một Functional Interface hợp lệ vì chứa nhiều hơn 1 phương thức trừu tượng",
      "Biên dịch thành công vì cả 2 phương thức đều có kiểu trả về là int",
      "Biên dịch thành công nếu có ít nhất 1 default method",
      "Cảnh báo của trình biên dịch nhưng vẫn chạy được"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc: Một Functional Interface chỉ được phép có DUY NHẤT một phương thức trừu tượng (Single Abstract Method - SAM). Ở đây Transformer chứa 2 abstract methods (transform và reverse). Annotation @FunctionalInterface yêu cầu trình biên dịch xác thực, nên trình biên dịch sẽ báo lỗi: 'Unexpected @FunctionalInterface annotation; Transformer is not a functional interface (multiple non-overriding abstract methods)'.",
    "difficulty": "easy",
    "tags": ["Functional-Interface", "Compile-Error"]
  },
  {
    "id": "L3_Q18",
    "lessonId": 3,
    "title": "Đoạn mã sau kiểm tra việc khởi tạo Anonymous Inner Class từ một Abstract Class. Kết quả in ra là gì?",
    "code": "abstract class Greeter {\n    abstract void sayHi();\n    void sayBye() { System.out.print(\"Bye \"); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Greeter g = new Greeter() {\n            void sayHi() { System.out.print(\"Hi \"); }\n        };\n        g.sayHi();\n        g.sayBye();\n    }\n}",
    "options": [
      "Hi Bye ",
      "Hi ",
      "Lỗi biên dịch: Không thể new một Abstract Class",
      "Ném InstantiationException tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Cú pháp new Greeter() { ... } không phải là khởi tạo trực tiếp Abstract Class, mà là định nghĩa và khởi tạo một lớp nội danh (Anonymous Inner Class) kế thừa từ Greeter và ghi đè phương thức sayHi(). Do đó chương trình biên dịch và chạy hoàn toàn hợp lệ, in ra 'Hi Bye '.",
    "difficulty": "medium",
    "tags": ["Anonymous-Class", "Abstract-Class"]
  },
  {
    "id": "L3_Q19",
    "lessonId": 3,
    "title": "Đoạn mã sau triển khai Template Method Pattern. Kết quả in ra là gì?",
    "code": "abstract class Beverage {\n    final void prepareRecipe() {\n        boilWater();\n        brew();\n        pourInCup();\n    }\n    void boilWater() { System.out.print(\"Boil \"); }\n    void pourInCup() { System.out.print(\"Pour \"); }\n    abstract void brew();\n}\nclass Tea extends Beverage {\n    void brew() { System.out.print(\"SteepTea \"); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Beverage b = new Tea();\n        b.prepareRecipe();\n    }\n}",
    "options": [
      "Boil SteepTea Pour ",
      "SteepTea Boil Pour ",
      "Boil Pour SteepTea ",
      "Lỗi biên dịch do brew() là abstract"
    ],
    "correctAnswer": 0,
    "explanation": "Mẫu Template Method: Phương thức prepareRecipe() định nghĩa khung sườn 3 bước: boilWater() in 'Boil ', brew() gọi phương thức override của Tea in 'SteepTea ', pourInCup() in 'Pour '. Kết quả là 'Boil SteepTea Pour '.",
    "difficulty": "easy",
    "tags": ["Template-Method", "Design-Patterns", "Abstract-Class"]
  },
  {
    "id": "L3_Q20",
    "lessonId": 3,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "abstract class Device {\n    int code;\n    Device(int code) { this.code = code; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Device d = new Device(101); // Dong nay\n        System.out.println(d.code);\n    }\n}",
    "options": [
      "Lỗi biên dịch: Device là một abstract class nên không thể khởi tạo trực tiếp bằng toán tử new",
      "Biên dịch thành công và in ra 101",
      "Ném ngoại lệ InstantiationError tại runtime",
      "Biên dịch thành công nhưng ném NullPointerException tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Abstract Class đại diện cho một khái niệm trừu tượng chưa hoàn chỉnh. Theo quy tắc cốt lõi của Java, bạn không bao giờ có thể tạo instance trực tiếp từ một abstract class bằng toán tử new Device(...). Muốn sử dụng, bắt buộc phải có một lớp con cụ thể (concrete subclass) kế thừa và khởi tạo lớp con đó. Trình biên dịch báo lỗi: 'Device is abstract; cannot be instantiated'.",
    "difficulty": "easy",
    "tags": ["Abstract-Class", "Instantiation-Error", "Compile-Error"]
  }
]

def save(lesson_id, data):
    p = os.path.join(OUTPUT_DIR, f"lesson{lesson_id}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Lesson {lesson_id}: {len(data)} questions saved.")

save(1, lesson1_questions)
save(2, lesson2_questions)
save(3, lesson3_questions)
