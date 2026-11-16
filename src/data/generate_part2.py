# -*- coding: utf-8 -*-
import json
import os

OUTPUT_DIR = r"d:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\questions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# LESSON 4: Lập trình tổng quát (Generics)
# ==============================================================================
lesson4_questions = [
  {
    "id": "L4_Q01",
    "lessonId": 4,
    "title": "Mục tiêu quan trọng nhất của việc giới thiệu Generics (Lập trình tổng quát) trong Java 5 là gì?",
    "code": None,
    "options": [
      "Đảm bảo an toàn kiểu (Type Safety) tại thời điểm biên dịch và loại bỏ các thao tác ép kiểu tường minh, ngăn ngừa ClassCastException tại runtime",
      "Tăng tốc độ thực thi của chương trình lên gấp nhiều lần nhờ tối ưu mã máy",
      "Cho phép một lớp có thể kế thừa từ nhiều lớp khác nhau",
      "Tự động chuyển đổi các kiểu dữ liệu nguyên thủy sang đối tượng mà không tốn bộ nhớ"
    ],
    "correctAnswer": 0,
    "explanation": "Trước Java 5, các Collection chỉ lưu trữ Object, đòi hỏi phải ép kiểu thủ công khi lấy ra và tiềm ẩn rủi ro ClassCastException khi chạy. Generics giúp phát hiện sai lệch kiểu dữ liệu ngay tại thời điểm biên dịch (Compile-time Type Safety) và loại bỏ hoàn toàn nhu cầu ép kiểu thủ công.",
    "difficulty": "easy",
    "tags": ["Generics", "Type-Safety", "Compile-Time"]
  },
  {
    "id": "L4_Q02",
    "lessonId": 4,
    "title": "Cơ chế 'Xóa kiểu' (Type Erasure) trong Java Generics hoạt động như thế nào?",
    "code": None,
    "options": [
      "Trình biên dịch kiểm tra tính an toàn kiểu tại compile-time, sau đó xóa bỏ toàn bộ thông tin tham số kiểu và thay thế bằng kiểu biên (bound) hoặc Object trong bytecode",
      "JVM lưu trữ toàn bộ các tham số kiểu generic vào siêu dữ liệu và kiểm tra kiểu tại mỗi câu lệnh thực thi",
      "Mỗi kiểu generic cụ thể (ví dụ List<Integer>, List<String>) sẽ được JVM biên dịch thành một file .class riêng biệt",
      "Kiểu dữ liệu generic chỉ bị xóa khi bộ nhớ Heap bị quá tải"
    ],
    "correctAnswer": 0,
    "explanation": "Java triển khai Generics thông qua cơ chế Type Erasure để đảm bảo tính tương thích ngược với các phiên bản Java cũ. Trình biên dịch kiểm tra an toàn kiểu ở compile-time, sau đó xóa các tham số kiểu (thay bằng Object hoặc bound type như Number) và tự động chèn các lệnh ép kiểu bytecode phù hợp. Do đó tại runtime, JVM không lưu thông tin kiểu cụ thể của Collection.",
    "difficulty": "hard",
    "tags": ["Type-Erasure", "JVM-Internals", "Bytecode"]
  },
  {
    "id": "L4_Q03",
    "lessonId": 4,
    "title": "Tính chất 'Bất biến kiểu' (Invariance) trong Generics của Java được thể hiện qua phát biểu nào sau đây?",
    "code": None,
    "options": [
      "Mặc dù Integer là lớp con của Number, nhưng List<Integer> KHÔNG PHẢI là kiểu con của List<Number>",
      "List<Integer> là kiểu con của List<Number> nên có thể gán tự do",
      "Một khi danh sách Generic đã tạo thì không thể thay đổi kích thước",
      "Các phương thức trong lớp Generic đều bắt buộc phải là final"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java Generics, các kiểu tham số hóa có tính chất Invariant (bất biến). Nếu A là con của B, GenericType<A> KHÔNG CÓ quan hệ kế thừa với GenericType<B>. Điều này nhằm ngăn ngừa lỗi type safety (nếu List<Integer> là con của List<Number>, ta có thể thêm một số thực Double vào List<Number> đó, làm hỏng List<Integer> ban đầu).",
    "difficulty": "medium",
    "tags": ["Generics", "Invariance", "Type-Safety"]
  },
  {
    "id": "L4_Q04",
    "lessonId": 4,
    "title": "Nguyên tắc PECS (Producer Extends, Consumer Super) của Joshua Bloch hướng dẫn sử dụng Wildcard như thế nào?",
    "code": None,
    "options": [
      "Dùng '? extends T' khi bộ sưu tập đóng vai trò cung cấp/đọc dữ liệu (Producer); Dùng '? super T' khi bộ sưu tập đóng vai trò tiêu thụ/ghi dữ liệu (Consumer)",
      "Dùng '? extends T' khi muốn ghi thêm phần tử mới; Dùng '? super T' khi chỉ muốn đọc phần tử ra",
      "Dùng '? extends T' cho kiểu nguyên thủy; Dùng '? super T' cho kiểu đối tượng",
      "Dùng '? extends T' cho phương thức static; Dùng '? super T' cho phương thức instance"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc kinh điển PECS: 1) Producer Extends: Khi bạn chỉ cần đọc dữ liệu kiểu T ra khỏi cấu trúc dữ liệu (cấu trúc sản xuất dữ liệu cho bạn), hãy dùng <? extends T>. 2) Consumer Super: Khi bạn cần thêm/ghi dữ liệu kiểu T vào cấu trúc dữ liệu (cấu trúc tiêu thụ dữ liệu từ bạn), hãy dùng <? super T>.",
    "difficulty": "hard",
    "tags": ["PECS", "Wildcard", "Effective-Java"]
  },
  {
    "id": "L4_Q05",
    "lessonId": 4,
    "title": "Đặc điểm của ký tự đại diện giới hạn trên (Upper Bounded Wildcard) '<? extends Number>' là gì?",
    "code": None,
    "options": [
      "Có thể đọc các phần tử ra với kiểu Number an toàn, nhưng KHÔNG THỂ thêm bất kỳ phần tử nào vào (ngoại trừ giá trị null)",
      "Có thể thêm bất kỳ đối tượng nào là con của Number vào danh sách",
      "Có thể thêm kiểu Integer nhưng không thể thêm kiểu Double",
      "Không thể đọc cũng không thể thêm phần tử"
    ],
    "correctAnswer": 0,
    "explanation": "Với List<? extends Number>, danh sách thực tế có thể là List<Integer>, List<Double>, v.v. Vì trình biên dịch không thể biết chắc chắn kiểu con cụ thể nào tại runtime, nó ngăn cấm mọi thao tác ghi (add) bất kỳ đối tượng nào (kể cả Integer hay Double) để đảm bảo type safety. Thao tác ghi duy nhất được phép là null.",
    "difficulty": "hard",
    "tags": ["Wildcard", "Upper-Bounded", "Read-Only"]
  },
  {
    "id": "L4_Q06",
    "lessonId": 4,
    "title": "Đặc điểm của ký tự đại diện giới hạn dưới (Lower Bounded Wildcard) '<? super Integer>' là gì?",
    "code": None,
    "options": [
      "Có thể thêm an toàn các phần tử kiểu Integer (hoặc lớp con của Integer) vào danh sách; Khi đọc ra chỉ đảm bảo kiểu Object",
      "Chỉ có thể đọc các phần tử ra với kiểu Integer an toàn",
      "Không thể thêm phần tử nào vào danh sách",
      "Có thể thêm bất kỳ đối tượng Number nào vào danh sách"
    ],
    "correctAnswer": 0,
    "explanation": "Với List<? super Integer>, danh sách thực tế có thể là List<Integer>, List<Number>, hoặc List<Object>. Do đó ta luôn có thể thêm đối tượng kiểu Integer (hoặc con của Integer) vào an toàn. Tuy nhiên khi đọc phần tử ra, kiểu chung an toàn duy nhất mà trình biên dịch biết chắc chắn là Object.",
    "difficulty": "hard",
    "tags": ["Wildcard", "Lower-Bounded", "Consumer-Super"]
  },
  {
    "id": "L4_Q07",
    "lessonId": 4,
    "title": "Cú pháp khai báo nhiều ràng buộc (Multiple Bounds) cho tham số kiểu Generic '<T extends A & B>' phải tuân theo quy tắc nào?",
    "code": None,
    "options": [
      "Nếu trong các ràng buộc có một lớp (class), lớp đó BẮT BUỘC phải đứng ở vị trí đầu tiên, theo sau là các interface",
      "Có thể chứa tối đa hai class và một interface",
      "Các interface phải đứng trước, class đứng ở cuối cùng",
      "Chỉ được phép chứa các interface, không được chứa class"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc JLS: Trong cú pháp multiple bounds <T extends Type1 & Type2 & Type3>, nếu có một class thì class đó bắt buộc phải đứng đầu tiên (Type1). Vì Java là đơn kế thừa class nên chỉ được có tối đa 1 class bound, các ràng buộc tiếp theo bắt buộc phải là interface.",
    "difficulty": "medium",
    "tags": ["Multiple-Bounds", "Generics-Syntax"]
  },
  {
    "id": "L4_Q08",
    "lessonId": 4,
    "title": "Vì sao các kiểu dữ liệu nguyên thủy (primitive types như int, double) KHÔNG THỂ dùng làm đối số kiểu trong Generics (ví dụ: List<int> là bất hợp lệ)?",
    "code": None,
    "options": [
      "Do cơ chế Type Erasure xóa kiểu về Object; các kiểu nguyên thủy không kế thừa từ java.lang.Object nên không thể tương thích",
      "Do kiểu nguyên thủy tốn nhiều bộ nhớ hơn kiểu đối tượng",
      "Do kiểu nguyên thủy không thể truyền qua mạng Internet",
      "Do trình biên dịch Java không hỗ trợ toán tử số học cho Generics"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, Type Erasure thay thế các type parameters bằng kiểu Object (hoặc bound của nó). Mọi tham chiếu kiểu đối tượng đều kế thừa từ java.lang.Object. Kiểu nguyên thủy (int, boolean, double) là các giá trị thô lưu trực tiếp trên stack chứ không phải con trỏ đối tượng kế thừa Object, do đó không thể gán cho biến kiểu Object.",
    "difficulty": "medium",
    "tags": ["Primitive-Types", "Type-Erasure", "Wrapper-Class"]
  },
  {
    "id": "L4_Q09",
    "lessonId": 4,
    "title": "Hạn chế nào sau đây là hệ quả trực tiếp của cơ chế xóa kiểu (Type Erasure) trong Java?",
    "code": None,
    "options": [
      "Không thể khởi tạo trực tiếp thể hiện của tham số kiểu 'new T()' hoặc mảng generic 'new T[10]'",
      "Không thể sử dụng câu lệnh if-else bên trong lớp generic",
      "Không thể định nghĩa phương thức trả về kiểu generic",
      "Lớp generic không thể chứa các thuộc tính private"
    ],
    "correctAnswer": 0,
    "explanation": "Vì tham số kiểu T bị xóa tại runtime (chỉ còn là Object), JVM không biết kiểu thực tế của T để cấp phát bộ nhớ chính xác. Do đó cú pháp new T() và new T[10] bị cấm hoàn toàn tại compile-time trong Java.",
    "difficulty": "hard",
    "tags": ["Type-Erasure", "Generic-Array", "Limitations"]
  },
  {
    "id": "L4_Q10",
    "lessonId": 4,
    "title": "Phát biểu nào sau đây là ĐÚNG về phương thức tĩnh generic (Generic Static Method)?",
    "code": None,
    "options": [
      "Phương thức tĩnh không thể sử dụng tham số kiểu của lớp (Class-level type parameter), mà phải tự khai báo tham số kiểu riêng trước kiểu trả về",
      "Phương thức tĩnh tự động kế thừa tham số kiểu của lớp khai báo",
      "Từ khóa static không thể kết hợp với generic",
      "Phương thức tĩnh generic bắt buộc phải trả về kiểu void"
    ],
    "correctAnswer": 0,
    "explanation": "Tham số kiểu ở cấp lớp (class-level type parameter) gắn liền với thể hiện (instance) của lớp. Phương thức static hoạt động ở cấp độ lớp và không có ngữ cảnh instance. Vì vậy phương thức static không thể dùng type parameter của lớp, mà phải tự định nghĩa tham số kiểu riêng, ví dụ: public static <T> void print(T item).",
    "difficulty": "medium",
    "tags": ["Generic-Method", "Static-Context"]
  },
  {
    "id": "L4_Q11",
    "lessonId": 4,
    "title": "Đoạn mã sau xảy ra lỗi gì khi biên dịch?",
    "code": "import java.util.*;\npublic class TestPECS {\n    public static void main(String[] args) {\n        List<? extends Number> list = new ArrayList<Integer>();\n        list.add(Integer.valueOf(10)); // Dong nay\n    }\n}",
    "options": [
      "Lỗi biên dịch: Không thể gọi phương thức add(Number) trên List<? extends Number>",
      "Biên dịch thành công và thêm số 10 vào danh sách",
      "Ném ngoại lệ UnsupportedOperationException tại runtime",
      "Ném ClassCastException tại thời điểm khởi tạo ArrayList"
    ],
    "correctAnswer": 0,
    "explanation": "Danh sách List<? extends Number> là một Producer (chỉ đọc). Kiểu thực tế có thể là List<Double>, List<Float>, v.v. Nếu cho phép thêm Integer vào thì sẽ phá vỡ an toàn kiểu của List<Double>. Do đó trình biên dịch cấm gọi add(...) với bất kỳ giá trị nào ngoài null: 'add(capture#1 of ? extends java.lang.Number) in List cannot be applied to (java.lang.Integer)'.",
    "difficulty": "hard",
    "tags": ["PECS", "Upper-Bounded", "Compile-Error"]
  },
  {
    "id": "L4_Q12",
    "lessonId": 4,
    "title": "Đoạn mã sau cho kết quả gì khi biên dịch và thực thi?",
    "code": "import java.util.*;\npublic class ConsumerSuperTest {\n    public static void main(String[] args) {\n        List<? super Integer> list = new ArrayList<Number>();\n        list.add(100);\n        Object obj = list.get(0);\n        System.out.println(obj.getClass().getSimpleName() + \" \" + obj);\n    }\n}",
    "options": [
      "Integer 100",
      "Number 100",
      "Lỗi biên dịch tại dòng list.add(100)",
      "Lỗi biên dịch tại dòng Object obj = list.get(0)"
    ],
    "correctAnswer": 0,
    "explanation": "Với List<? super Integer> (Consumer), ta hoàn toàn có thể thêm an toàn một đối tượng kiểu Integer (100 được autobox thành Integer). Khi đọc ra qua list.get(0), kiểu trả về an toàn được đảm bảo là Object. Tại runtime, đối tượng thực tế là một Integer -> obj.getClass().getSimpleName() trả về 'Integer', obj in ra 100.",
    "difficulty": "medium",
    "tags": ["Consumer-Super", "PECS", "Autoboxing"]
  },
  {
    "id": "L4_Q13",
    "lessonId": 4,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "import java.util.*;\npublic class InvarianceTest {\n    public static void main(String[] args) {\n        List<Object> list = new ArrayList<String>(); // Dong nay\n        list.add(123);\n    }\n}",
    "options": [
      "Lỗi biên dịch: Type mismatch không thể gán ArrayList<String> cho List<Object>",
      "Biên dịch thành công và thêm số 123 vào danh sách chuỗi",
      "Biên dịch thành công nhưng ném ClassCastException tại runtime",
      "Chương trình chạy bình thường không có lỗi"
    ],
    "correctAnswer": 0,
    "explanation": "Tính bất biến (Invariance) của Java Generics ngăn cản việc gán ArrayList<String> cho List<Object>. Nếu phép gán này hợp lệ, dòng tiếp theo ta có thể add một số nguyên 123 vào danh sách chuỗi, làm hỏng toàn bộ tính an toàn kiểu. Trình biên dịch ngăn chặn ngay từ đầu: 'incompatible types: ArrayList<String> cannot be converted to List<Object>'.",
    "difficulty": "easy",
    "tags": ["Invariance", "Type-Mismatch", "Compile-Error"]
  },
  {
    "id": "L4_Q14",
    "lessonId": 4,
    "title": "Đoạn mã sau sử dụng phương thức Generic có ràng buộc Comparable. Kết quả in ra là gì?",
    "code": "public class GenericMethodTest {\n    public static <T extends Comparable<T>> T maximum(T x, T y) {\n        return x.compareTo(y) > 0 ? x : y;\n    }\n    public static void main(String[] args) {\n        System.out.println(maximum(\"Apple\", \"Banana\") + \" \" + maximum(15, 8));\n    }\n}",
    "options": [
      "Banana 15",
      "Apple 15",
      "Banana 8",
      "Apple 8"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức generic maximum so sánh hai đối tượng có triển khai Comparable<T>. Với hai chuỗi \"Apple\" và \"Banana\", theo thứ tự bảng chữ cái thì \"Banana\".compareTo(\"Apple\") > 0, do đó maximum trả về \"Banana\". Với hai số nguyên 15 và 8, 15 > 8 nên trả về 15. Kết quả in ra là: 'Banana 15'.",
    "difficulty": "easy",
    "tags": ["Generic-Method", "Comparable", "Type-Inference"]
  },
  {
    "id": "L4_Q15",
    "lessonId": 4,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch (ảnh hưởng của Type Erasure)?",
    "code": "import java.util.List;\nclass ErasureClash {\n    public void process(List<String> list) {\n        System.out.println(\"Strings\");\n    }\n    public void process(List<Integer> list) {\n        System.out.println(\"Integers\");\n    }\n}",
    "options": [
      "Lỗi biên dịch: Cả hai phương thức có cùng chữ ký sau khi xóa kiểu (have the same erasure)",
      "Biên dịch thành công và nạp chồng bình thường",
      "Ném ngoại lệ AmbiguousMethodException tại runtime",
      "Chương trình chạy bình thường"
    ],
    "correctAnswer": 0,
    "explanation": "Do cơ chế Type Erasure, tại thời điểm biên dịch mã bytecode, cả List<String> và List<Integer> đều bị xóa tham số kiểu và trở thành kiểu thô List. Do đó cả hai phương thức đều có cùng chữ ký trong bytecode là process(List). Trình biên dịch Java phát hiện xung đột và báo lỗi: 'name clash: process(List<Integer>) and process(List<String>) have the same erasure'.",
    "difficulty": "hard",
    "tags": ["Type-Erasure", "Name-Clash", "Method-Signature"]
  },
  {
    "id": "L4_Q16",
    "lessonId": 4,
    "title": "Cho lớp Generic Storage trích từ Đề thi mẫu UET. Khai báo nào sau đây sẽ gây LỖI BIÊN DỊCH?",
    "code": "interface Printable { String print(); }\nclass Report implements Printable {\n    public String print() { return \"Report\"; }\n}\nclass Storage<T extends Printable> {\n    private T item;\n    void save(T item) { this.item = item; }\n}",
    "options": [
      "Storage<String> s = new Storage<>();",
      "Storage<Report> s = new Storage<>();",
      "Storage<Printable> s = new Storage<>();",
      "Storage<?> s = new Storage<Report>();"
    ],
    "correctAnswer": 0,
    "explanation": "Lớp Storage được định nghĩa với ràng buộc: <T extends Printable>, nghĩa là mọi tham số kiểu T bắt buộc phải là Printable hoặc một lớp triển khai Printable. Vì lớp String trong Java không implements Printable nên khai báo Storage<String> vi phạm ràng buộc kiểu và gây lỗi biên dịch: 'type argument java.lang.String is not within bounds of type-variable T'.",
    "difficulty": "medium",
    "tags": ["Bounded-Type", "UET-Exam", "Compile-Error"]
  },
  {
    "id": "L4_Q17",
    "lessonId": 4,
    "title": "Đoạn mã sau xảy ra lỗi gì khi biên dịch?",
    "code": "class GenericArray<T> {\n    private T[] data;\n    public GenericArray(int size) {\n        data = new T[size]; // Dong nay\n    }\n}",
    "options": [
      "Lỗi biên dịch: Không thể tạo mảng trực tiếp từ tham số kiểu generic (generic array creation)",
      "Lỗi biên dịch do thiếu import java.util.*",
      "Biên dịch thành công nhưng ném NegativeArraySizeException",
      "Chương trình chạy bình thường"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, mảng cần biết thông tin kiểu phần tử cụ thể tại runtime (reified type) để cấp phát bộ nhớ và kiểm tra an toàn kiểu. Nhưng tham số kiểu generic T bị xóa tại compile-time (Type Erasure). Do đó cú pháp new T[size] bị trình biên dịch cấm hoàn toàn: 'generic array creation'. Cách giải quyết chuẩn là tạo mảng (T[]) new Object[size] hoặc dùng Array.newInstance().",
    "difficulty": "hard",
    "tags": ["Generic-Array", "Type-Erasure", "Compile-Error"]
  },
  {
    "id": "L4_Q18",
    "lessonId": 4,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "class Box<T> {\n    private static T value; // Dong nay\n}",
    "options": [
      "Lỗi biên dịch: Không thể khai báo biến static có kiểu là tham số kiểu của lớp (non-static type variable T cannot be referenced from a static context)",
      "Biên dịch thành công và biến value được dùng chung cho mọi Box",
      "Biên dịch thành công nếu T là kiểu Number",
      "Lỗi do thiếu constructor"
    ],
    "correctAnswer": 0,
    "explanation": "Biến static là thành phần dùng chung cho toàn bộ lớp Box bất kể lớp đó được khởi tạo với kiểu nào (Box<String>, Box<Integer>). Nếu cho phép static T value, biến này sẽ không thể xác định được kiểu dữ liệu cụ thể nào. Vì vậy trình biên dịch cấm khai báo biến static bằng tham số kiểu của lớp.",
    "difficulty": "medium",
    "tags": ["Static-Context", "Type-Erasure", "Compile-Error"]
  },
  {
    "id": "L4_Q19",
    "lessonId": 4,
    "title": "Hiện tượng Ô nhiễm vùng nhớ Heap (Heap Pollution) bằng Raw Type. Kết quả khi chạy đoạn mã sau là gì?",
    "code": "import java.util.*;\npublic class RawTypeTrap {\n    public static void main(String[] args) {\n        List rawList = new ArrayList();\n        rawList.add(\"UET CS2043\");\n        rawList.add(100);\n\n        List<String> strList = rawList; // Warning raw type\n        for (String s : strList) {\n            System.out.println(s);\n        }\n    }\n}",
    "options": [
      "In ra 'UET CS2043' sau đó ném ClassCastException tại phần tử thứ hai khi ép kiểu sang String",
      "In ra cả 'UET CS2043' và '100' thành công",
      "Lỗi biên dịch tại dòng List<String> strList = rawList",
      "Ném NullPointerException khi duyệt danh sách"
    ],
    "correctAnswer": 0,
    "explanation": "Gán một danh sách thô (raw list) chứa các kiểu dữ liệu lẫn lộn vào một danh sách có kiểu List<String> chỉ gây ra compiler warning. Khi vòng lặp foreach chạy, trình biên dịch tự động chèn lệnh ép kiểu ngầm định (String) phần tử. Phần tử đầu tiên là chuỗi in ra thành công 'UET CS2043'. Phần tử thứ hai là Integer, khi ép kiểu sang String lập tức ném: java.lang.ClassCastException: class java.lang.Integer cannot be cast to class java.lang.String.",
    "difficulty": "hard",
    "tags": ["Heap-Pollution", "Raw-Type", "ClassCastException"]
  },
  {
    "id": "L4_Q20",
    "lessonId": 4,
    "title": "Đoạn mã sau áp dụng nguyên tắc PECS để sao chép danh sách. Kết quả in ra là gì?",
    "code": "import java.util.*;\npublic class CopyTest {\n    public static <T> void copy(List<? super T> dest, List<? extends T> src) {\n        for (T item : src) {\n            dest.add(item);\n        }\n    }\n    public static void main(String[] args) {\n        List<Number> dest = new ArrayList<>();\n        List<Integer> src = Arrays.asList(1, 2, 3);\n        copy(dest, src);\n        System.out.println(dest.size() + \" \" + dest.get(0));\n    }\n}",
    "options": [
      "3 1",
      "3 3",
      "Lỗi biên dịch tại lời gọi copy(dest, src)",
      "0 null"
    ],
    "correctAnswer": 0,
    "explanation": "Hàm copy tuân thủ hoàn hảo nguyên tắc PECS: 'dest' là Consumer (<? super T>) cho phép thêm các phần tử kiểu T vào; 'src' là Producer (<? extends T>) cho phép đọc các phần tử kiểu T ra. Với T suy diễn là Integer, Integer đọc từ src được thêm thành công vào dest kiểu Number. Kích thước dest là 3 và phần tử đầu tiên dest.get(0) là 1.",
    "difficulty": "medium",
    "tags": ["PECS", "Collections-Copy", "Type-Inference"]
  }
]

# ==============================================================================
# LESSON 5: Cấu trúc dữ liệu & Collections Framework
# ==============================================================================
lesson5_questions = [
  {
    "id": "L5_Q01",
    "lessonId": 5,
    "title": "Hợp đồng bất biến (Contract) giữa hai phương thức equals() và hashCode() trong lớp java.lang.Object quy định điều gì?",
    "code": None,
    "options": [
      "Nếu hai đối tượng bằng nhau theo equals(), thì mã hashCode() của chúng BẮT BUỘC phải bằng nhau",
      "Nếu hai đối tượng có hashCode() bằng nhau, thì chúng BẮT BUỘC phải bằng nhau theo equals()",
      "Hai đối tượng có mã hashCode() khác nhau vẫn có thể bằng nhau theo equals()",
      "Mọi lớp khi override equals() không nhất thiết phải override hashCode()"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc hợp đồng cốt lõi: 1) Nếu a.equals(b) là true, thì a.hashCode() BẮT BUỘC phải bằng b.hashCode(). 2) Nếu a.hashCode() == b.hashCode(), hai đối tượng CHƯA CHẮC đã bằng nhau theo equals() (xảy ra xung đột băm - hash collision). Nếu vi phạm quy tắc 1, các cấu trúc dữ liệu băm như HashSet và HashMap sẽ hoạt động sai hoàn toàn.",
    "difficulty": "medium",
    "tags": ["equals-hashCode", "Contract", "Object-Class"]
  },
  {
    "id": "L5_Q02",
    "lessonId": 5,
    "title": "Hiện tượng xung đột băm (Hash Collision) trong HashMap xảy ra khi nào và JVM xử lý như thế nào?",
    "code": None,
    "options": [
      "Xảy ra khi hai key khác nhau có cùng chỉ số bucket (hash code giống nhau hoặc cùng vị trí index); JVM lưu các phần tử này vào cùng một bucket dưới dạng danh sách liên kết hoặc cây Đỏ-Đen",
      "Xảy ra khi dung lượng mảng bị đầy; JVM lập tức ném ngoại lệ HashCollisionException",
      "Xảy ra khi key bị trùng lặp giá trị equals(); JVM ghi đè giá trị cũ",
      "Xảy ra khi HashMap không cho phép lưu trữ giá trị null"
    ],
    "correctAnswer": 0,
    "explanation": "Hash collision xảy ra khi hai key không bằng nhau nhưng hàm băm tính ra cùng một chỉ số bucket trong mảng nội bộ của HashMap. JVM giải quyết bằng phương pháp Separate Chaining: lưu các node va chạm thành một LinkedList. Từ Java 8, nếu một bucket có từ 8 phần tử trở lên, nó sẽ tự động chuyển thành cây Đỏ-Đen (Red-Black tree) để tối ưu tìm kiếm từ O(n) về O(log n).",
    "difficulty": "hard",
    "tags": ["HashMap", "Hash-Collision", "Separate-Chaining"]
  },
  {
    "id": "L5_Q03",
    "lessonId": 5,
    "title": "Phát biểu nào sau đây phân biệt đúng nhất về cây phân cấp trong Java Collections Framework?",
    "code": None,
    "options": [
      "Interface Collection là gốc của List, Set, Queue; Map KHÔNG kế thừa từ Collection mà là một phân nhánh độc lập quản lý cặp key-value",
      "Map là một interface con trực tiếp kế thừa từ Collection",
      "Set là một lớp con của List có thêm tính năng loại bỏ trùng lặp",
      "ArrayList và HashMap cùng kế thừa từ một lớp trừu tượng chung AbstractCollection"
    ],
    "correctAnswer": 0,
    "explanation": "Trong cấu trúc thiết kế của Java Collections Framework: Interface java.util.Collection là gốc của các cấu trúc lưu trữ tập hợp phần tử đơn lẻ (gồm List, Set, Queue). Riêng java.util.Map quản lý cặp khóa - giá trị (Key-Value) có cấu trúc hoàn toàn khác biệt nên KHÔNG kế thừa từ Collection mà đứng độc lập.",
    "difficulty": "easy",
    "tags": ["Collections-Hierarchy", "Collection-vs-Map"]
  },
  {
    "id": "L5_Q04",
    "lessonId": 5,
    "title": "So sánh độ phức tạp thuật toán thời gian giữa ArrayList và LinkedList khi truy cập ngẫu nhiên phần tử theo chỉ số index (get(i))?",
    "code": None,
    "options": [
      "ArrayList mất O(1) do dựa trên mảng liên tục; LinkedList mất O(n) do phải duyệt tuần tự từ đầu hoặc cuối danh sách",
      "LinkedList mất O(1); ArrayList mất O(n)",
      "Cả hai cấu trúc đều mất O(1) thời gian",
      "Cả hai cấu trúc đều mất O(log n) thời gian"
    ],
    "correctAnswer": 0,
    "explanation": "ArrayList sử dụng mảng động nội bộ (contiguous memory array), do đó việc truy cập theo chỉ số get(i) tính toán địa chỉ trực tiếp mất O(1). LinkedList sử dụng danh sách liên kết đôi (doubly-linked list), do không có địa chỉ liên tục nên muốn lấy phần tử ở chỉ số i phải duyệt tuần tự từ đầu hoặc cuối tới vị trí đó, mất thời gian O(n).",
    "difficulty": "easy",
    "tags": ["ArrayList", "LinkedList", "Time-Complexity"]
  },
  {
    "id": "L5_Q05",
    "lessonId": 5,
    "title": "Sự khác biệt cốt lõi giữa HashSet và TreeSet trong Java là gì?",
    "code": None,
    "options": [
      "HashSet dựa trên bảng băm (HashMap), không đảm bảo thứ tự, thao tác O(1); TreeSet dựa trên cây Đỏ-Đen (TreeMap), tự động sắp xếp có thứ tự, thao tác O(log n) và đòi hỏi phần tử phải so sánh được",
      "HashSet tự động sắp xếp phần tử tăng dần; TreeSet lưu theo thứ tự chèn",
      "TreeSet cho phép lưu nhiều phần tử null; HashSet cấm hoàn toàn giá trị null",
      "HashSet chỉ lưu trữ được kiểu nguyên thủy; TreeSet chỉ lưu trữ kiểu đối tượng"
    ],
    "correctAnswer": 0,
    "explanation": "HashSet sử dụng bảng băm nên không có bất kỳ thứ tự nào, độ phức tạp trung bình là O(1), cho phép 1 giá trị null. TreeSet được cài đặt bằng cây Đỏ-Đen tự cân bằng, luôn duy trì thứ tự sắp xếp của các phần tử (độ phức tạp O(log n)), không cho phép null và bắt buộc các phần tử phải implements Comparable hoặc cung cấp một Comparator.",
    "difficulty": "medium",
    "tags": ["HashSet", "TreeSet", "Data-Structures"]
  },
  {
    "id": "L5_Q06",
    "lessonId": 5,
    "title": "Cơ chế Fail-Fast của Iterator trong Java Collections hoạt động như thế nào?",
    "code": None,
    "options": [
      "Theo dõi biến modCount; nếu phát hiện tập hợp bị thay đổi cấu trúc trong khi đang duyệt (ngoài trừ dùng phương thức iterator.remove()), nó sẽ lập tức ném ConcurrentModificationException",
      "Tự động sửa lỗi cấu trúc khi phát hiện có luồng khác can thiệp",
      "Chờ đợi luồng khác kết thúc rồi mới tiếp tục duyệt",
      "Tạo một bản sao độc lập của tập hợp mỗi khi khởi tạo Iterator"
    ],
    "correctAnswer": 0,
    "explanation": "Các Iterator của ArrayList, HashMap,... là Fail-Fast. Chúng theo dõi biến đếm thay đổi cấu trúc modCount. Khi gọi next(), nếu phát hiện modCount khác với giá trị expectedModCount lúc khởi tạo iterator (do có thao tác add/remove từ ngoài), nó lập tức ném java.util.ConcurrentModificationException để ngăn chặn hành vi không đoán trước được.",
    "difficulty": "hard",
    "tags": ["Fail-Fast", "ConcurrentModificationException", "Iterator"]
  },
  {
    "id": "L5_Q07",
    "lessonId": 5,
    "title": "Sự khác nhau căn bản giữa interface java.lang.Comparable và java.util.Comparator là gì?",
    "code": None,
    "options": [
      "Comparable định nghĩa thứ tự tự nhiên (natural ordering) bên trong chính lớp qua compareTo(T o); Comparator định nghĩa chiến lược so sánh tùy biến bên ngoài qua compare(T o1, T o2)",
      "Comparable nằm ở gói java.util; Comparator nằm ở java.lang",
      "Comparable có thể định nghĩa nhiều tiêu chí sắp xếp; Comparator chỉ định nghĩa được một tiêu chí duy nhất",
      "Comparable chỉ dùng cho chuỗi; Comparator chỉ dùng cho số"
    ],
    "correctAnswer": 0,
    "explanation": "Comparable được triển khai trực tiếp bởi chính lớp cần sắp xếp để định nghĩa thứ tự tự nhiên duy nhất của đối tượng thông qua phương thức compareTo(T o). Comparator là một interface riêng biệt bên ngoài cho phép định nghĩa nhiều tiêu chí sắp xếp linh hoạt khác nhau thông qua compare(T o1, T o2) mà không cần can thiệp sửa đổi mã nguồn của lớp.",
    "difficulty": "medium",
    "tags": ["Comparable", "Comparator", "Sorting"]
  },
  {
    "id": "L5_Q08",
    "lessonId": 5,
    "title": "Trong HashMap của Java 8+, một bucket dạng danh sách liên kết sẽ được chuyển hóa thành Cây Đỏ-Đen (Treeify) khi thỏa mãn điều kiện nào?",
    "code": None,
    "options": [
      "Số lượng phần tử trong bucket đạt từ 8 trở lên (TREEIFY_THRESHOLD = 8) VÀ tổng dung lượng mảng bucket tối thiểu là 64 (MIN_TREEIFY_CAPACITY = 64)",
      "Chỉ cần số lượng phần tử trong bucket đạt từ 4 trở lên",
      "Chỉ cần tổng số phần tử trong toàn bộ HashMap vượt quá 100",
      "Khi có 2 phần tử có cùng hashCode()"
    ],
    "correctAnswer": 0,
    "explanation": "Cơ chế Treeification trong HashMap (Java 8): Khi số node va chạm trong 1 bucket đạt ngưỡng TREEIFY_THRESHOLD (8), JVM sẽ kiểm tra dung lượng bảng băm. Nếu dung lượng bảng < 64, nó ưu tiên resize phóng to bảng để phân tán node. Chỉ khi dung lượng bảng >= 64 VÀ số phần tử trong bucket >= 8, bucket đó mới chính thức được chuyển đổi thành Red-Black Tree.",
    "difficulty": "hard",
    "tags": ["HashMap", "Treeification", "Red-Black-Tree"]
  },
  {
    "id": "L5_Q09",
    "lessonId": 5,
    "title": "Vì sao các đối tượng làm Khóa (Key) trong HashMap nên được thiết kế là Bất biến (Immutable) như String hoặc Integer?",
    "code": None,
    "options": [
      "Nếu trạng thái của key bị thay đổi sau khi chèn vào Map, hashCode của nó sẽ đổi dẫn tới sai lệch chỉ số bucket, khiến phương thức get() không thể tìm lại được đối tượng",
      "Để giảm thiểu dung lượng RAM cấp phát cho HashMap",
      "Do Java cấm sử dụng các lớp tự định nghĩa làm key trong HashMap",
      "Để ngăn cản việc ghi đè giá trị (value) của key đó"
    ],
    "correctAnswer": 0,
    "explanation": "Khi lưu một phần tử vào HashMap, vị trí bucket được tính từ hashCode của key. Nếu key là mutable và bị thay đổi sau khi chèn, hashCode của nó sẽ bị thay đổi theo. Khi ta gọi map.get(key), HashMap sẽ tính hash mới và tìm ở bucket khác, dẫn đến không thể tìm thấy phần tử ban đầu (trả về null), gây rò rỉ bộ nhớ nghiêm trọng.",
    "difficulty": "hard",
    "tags": ["HashMap", "Immutable-Key", "Hash-Contract"]
  },
  {
    "id": "L5_Q10",
    "lessonId": 5,
    "title": "Điểm khác biệt giữa hai phương thức poll() và remove() khi lấy phần tử ra khỏi hàng đợi Queue rỗng trong Java là gì?",
    "code": None,
    "options": [
      "poll() trả về null; remove() ném ngoại lệ NoSuchElementException",
      "poll() ném NoSuchElementException; remove() trả về null",
      "Cả hai phương thức đều trả về null",
      "Cả hai phương thức đều ném NullPointerException"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Queue interface: nhóm phương thức kiểm tra an toàn gồm offer(), poll(), peek() sẽ trả về giá trị đặc biệt (false hoặc null) khi hàng đợi đầy/rỗng. Nhóm phương thức truyền thống gồm add(), remove(), element() sẽ ném ngoại lệ (IllegalStateException hoặc NoSuchElementException) khi thất bại.",
    "difficulty": "easy",
    "tags": ["Queue", "Collections-API"]
  },
  {
    "id": "L5_Q11",
    "lessonId": 5,
    "title": "Lớp Book ghi đè equals() nhưng KHÔNG ghi đè hashCode(). Kết quả in ra kích thước của HashSet sau đoạn mã là gì?",
    "code": "import java.util.*;\nclass Book {\n    int id;\n    Book(int id) { this.id = id; }\n    @Override\n    public boolean equals(Object o) {\n        if (this == o) return true;\n        if (!(o instanceof Book)) return false;\n        return id == ((Book) o).id;\n    }\n}\npublic class SetTest {\n    public static void main(String[] args) {\n        Set<Book> set = new HashSet<>();\n        set.add(new Book(101));\n        set.add(new Book(101));\n        System.out.println(set.size());\n    }\n}",
    "options": [
      "2",
      "1",
      "0",
      "Ném ngoại lệ IllegalStateException"
    ],
    "correctAnswer": 0,
    "explanation": "Bẫy vi phạm hợp đồng equals/hashCode! Mặc dù hai đối tượng Book(101) có cùng id và equals() trả về true, nhưng vì không override hashCode() nên chúng sử dụng hashCode mặc định của Object (dựa trên địa chỉ bộ nhớ). Do đó hai đối tượng có hashCode hoàn toàn khác nhau, được đưa vào hai bucket khác nhau trong HashSet. HashSet không phát hiện trùng lặp và kích thước tập hợp là 2!",
    "difficulty": "hard",
    "tags": ["equals-hashCode", "HashSet", "Bug-Analysis"]
  },
  {
    "id": "L5_Q12",
    "lessonId": 5,
    "title": "Hiện tượng gì xảy ra khi thay đổi trạng thái của Key sau khi đưa vào HashMap trong đoạn mã sau?",
    "code": "import java.util.*;\nclass Key {\n    int val;\n    Key(int v) { this.val = v; }\n    public int hashCode() { return val; }\n    public boolean equals(Object o) { return o instanceof Key && ((Key) o).val == this.val; }\n}\npublic class MapTrap {\n    public static void main(String[] args) {\n        Map<Key, String> map = new HashMap<>();\n        Key k = new Key(5);\n        map.put(k, \"Success\");\n        k.val = 10; // Thay doi gia tri key sau khi put\n        System.out.println(map.get(k) + \" \" + map.get(new Key(5)));\n    }\n}",
    "options": [
      "null null",
      "Success Success",
      "Success null",
      "null Success"
    ],
    "correctAnswer": 0,
    "explanation": "1) Khi k.val = 5, phần tử được lưu ở bucket 5. Khi sửa k.val = 10, k.hashCode() trở thành 10. Lệnh map.get(k) tìm ở bucket 10 -> rỗng -> trả về null. 2) Lệnh map.get(new Key(5)) tìm ở bucket 5: trong bucket 5 có đối tượng cũ k, nhưng khi so sánh equals() giữa new Key(5) và k (lúc này k.val đã là 10) thì trả về false -> trả về null. Do đó cả hai đều trả về 'null null'.",
    "difficulty": "hard",
    "tags": ["HashMap", "Mutable-Key", "Memory-Leak"]
  },
  {
    "id": "L5_Q13",
    "lessonId": 5,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi chạy?",
    "code": "import java.util.*;\nclass Product {\n    String name;\n    Product(String name) { this.name = name; }\n}\npublic class TreeSetTest {\n    public static void main(String[] args) {\n        Set<Product> set = new TreeSet<>();\n        set.add(new Product(\"Laptop\"));\n        set.add(new Product(\"Phone\"));\n    }\n}",
    "options": [
      "Ném ClassCastException tại runtime vì Product không triển khai Comparable",
      "Chương trình chạy bình thường và sắp xếp theo tên",
      "Lỗi biên dịch tại dòng set.add()",
      "Chương trình chạy nhưng chỉ lưu được một phần tử"
    ],
    "correctAnswer": 0,
    "explanation": "TreeSet hoạt động dựa trên cây Đỏ-Đen và bắt buộc các phần tử phải so sánh được với nhau để xác định vị trí trên cây. Vì Product không implements java.lang.Comparable và constructor của TreeSet không được cung cấp Comparator, khi gọi add() lần thứ hai (hoặc ngay lần đầu), JVM cố ép kiểu Product sang Comparable và ném ngoại lệ: java.lang.ClassCastException: class Product cannot be cast to class java.lang.Comparable.",
    "difficulty": "medium",
    "tags": ["TreeSet", "Comparable", "ClassCastException"]
  },
  {
    "id": "L5_Q14",
    "lessonId": 5,
    "title": "Đoạn mã sau xảy ra lỗi gì khi thực thi?",
    "code": "import java.util.*;\npublic class ForeachRemove {\n    public static void main(String[] args) {\n        List<String> list = new ArrayList<>(Arrays.asList(\"A\", \"B\", \"C\"));\n        for (String s : list) {\n            if (s.equals(\"A\")) {\n                list.remove(s); // Xoa truc tiep tu list\n            }\n        }\n    }\n}",
    "options": [
      "Ném ngoại lệ ConcurrentModificationException",
      "Xóa thành công phần tử 'A' và danh sách còn ['B', 'C']",
      "Lỗi biên dịch tại dòng list.remove(s)",
      "Vòng lặp chạy vô tận"
    ],
    "correctAnswer": 0,
    "explanation": "Vòng lặp foreach trong Java thực chất sử dụng Iterator ngầm định. Khi gọi list.remove(s) trực tiếp trên List, cấu trúc mảng bị thay đổi làm tăng biến modCount. Ở lần lặp kế tiếp, phương thức iterator.next() phát hiện modCount != expectedModCount nên lập tức ném ConcurrentModificationException. Muốn xóa an toàn khi đang duyệt phải dùng iterator.remove().",
    "difficulty": "medium",
    "tags": ["ConcurrentModificationException", "Iterator", "Fail-Fast"]
  },
  {
    "id": "L5_Q15",
    "lessonId": 5,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi chạy?",
    "code": "import java.util.*;\npublic class ArraysAsListTest {\n    public static void main(String[] args) {\n        List<String> list = Arrays.asList(\"Java\", \"Python\", \"C++\");\n        list.add(\"Go\"); // Dong nay\n        System.out.println(list.size());\n    }\n}",
    "options": [
      "Ném ngoại lệ UnsupportedOperationException tại dòng list.add(\"Go\")",
      "Chương trình in ra 4",
      "Lỗi biên dịch do Arrays.asList trả về kiểu không thể ép sang List<String>",
      "Ném IndexOutOfBoundsException"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức Arrays.asList() trả về một thể hiện của lớp tĩnh nội bộ Arrays$ArrayList có kích thước cố định bọc quanh mảng gốc. Lớp này không hỗ trợ các thao tác làm thay đổi kích thước danh sách như add() hoặc remove(). Khi gọi list.add(), nó ném ngoại lệ: java.lang.UnsupportedOperationException.",
    "difficulty": "medium",
    "tags": ["Arrays-asList", "UnsupportedOperationException"]
  },
  {
    "id": "L5_Q16",
    "lessonId": 5,
    "title": "Bẫy nạp chồng phương thức remove() trong List<Integer>! Kết quả in ra là gì?",
    "code": "import java.util.*;\npublic class ListRemoveTrap {\n    public static void main(String[] args) {\n        List<Integer> list = new ArrayList<>();\n        list.add(10); // index 0\n        list.add(20); // index 1\n        list.add(30); // index 2\n        list.remove(1); // Goi remove(int index) hay remove(Object o)?\n        System.out.println(list);\n    }\n}",
    "options": [
      "[10, 30]",
      "[20, 30]",
      "[10, 20]",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Lớp List có 2 phương thức remove: remove(int index) và remove(Object o). Khi truyền vào số nguyên nguyên thủy 1 (kiểu int), trình biên dịch ưu tiên khớp chính xác với kiểu nguyên thủy mà không thực hiện autoboxing sang Integer. Do đó nó gọi remove(int index = 1), xóa phần tử tại chỉ số 1 (giá trị 20). Danh sách còn lại là: [10, 30]. Nếu muốn xóa giá trị 1 thì phải truyền list.remove(Integer.valueOf(1)).",
    "difficulty": "hard",
    "tags": ["List-Remove", "Overloading-Trap", "Autoboxing"]
  },
  {
    "id": "L5_Q17",
    "lessonId": 5,
    "title": "Giá trị trả về của phương thức map.put(K, V) trong Java là gì?",
    "code": "import java.util.*;\npublic class MapPutTest {\n    public static void main(String[] args) {\n        Map<String, Integer> map = new HashMap<>();\n        Integer v1 = map.put(\"A\", 100);\n        Integer v2 = map.put(\"A\", 200);\n        System.out.println(v1 + \" \" + v2);\n    }\n}",
    "options": [
      "null 100",
      "100 200",
      "null 200",
      "100 null"
    ],
    "correctAnswer": 0,
    "explanation": "Theo đặc tả của Map.put(key, value): Phương thức sẽ trả về giá trị CŨ (previous value) đã từng liên kết với key đó, hoặc trả về null nếu key đó chưa từng tồn tại trong map (hoặc trước đó liên kết với null). Lần put đầu tiên key 'A' chưa có -> v1 = null. Lần put thứ hai key 'A' đã có giá trị 100 -> v2 nhận giá trị cũ 100 và giá trị mới của key 'A' được cập nhật thành 200. Kết quả in ra: 'null 100'.",
    "difficulty": "medium",
    "tags": ["HashMap", "Map-Put-API"]
  },
  {
    "id": "L5_Q18",
    "lessonId": 5,
    "title": "Đoạn mã sau sử dụng Comparator.thenComparing để sắp xếp danh sách. Kết quả in ra là gì?",
    "code": "import java.util.*;\nclass Student {\n    String name;\n    int score;\n    Student(String n, int s) { this.name = n; this.score = s; }\n    public String toString() { return name + \":\" + score; }\n}\npublic class SortTest {\n    public static void main(String[] args) {\n        List<Student> list = Arrays.asList(\n            new Student(\"An\", 8),\n            new Student(\"Binh\", 9),\n            new Student(\"An\", 10)\n        );\n        list.sort(Comparator.comparing((Student s) -> s.name)\n                            .thenComparingInt(s -> s.score));\n        System.out.println(list);\n    }\n}",
    "options": [
      "[An:8, An:10, Binh:9]",
      "[An:10, An:8, Binh:9]",
      "[Binh:9, An:8, An:10]",
      "[An:8, Binh:9, An:10]"
    ],
    "correctAnswer": 0,
    "explanation": "Comparator đầu tiên so sánh theo name tăng dần: \"An\" đứng trước \"Binh\". Khi hai sinh viên cùng tên \"An\", tiêu chí thenComparingInt so sánh theo score tăng dần: điểm 8 đứng trước điểm 10. Do đó thứ tự là: An:8, An:10, rồi đến Binh:9. Kết quả in ra: '[An:8, An:10, Binh:9]'.",
    "difficulty": "medium",
    "tags": ["Comparator", "thenComparing", "Sorting"]
  },
  {
    "id": "L5_Q19",
    "lessonId": 5,
    "title": "Đoạn mã sau kiểm tra thứ tự lưu trữ của LinkedHashSet. Kết quả in ra là gì?",
    "code": "import java.util.*;\npublic class LinkedHashSetTest {\n    public static void main(String[] args) {\n        Set<String> set = new LinkedHashSet<>();\n        set.add(\"Banana\");\n        set.add(\"Apple\");\n        set.add(\"Mango\");\n        set.add(\"Apple\"); // trung lap\n        System.out.println(String.join(\" \", set));\n    }\n}",
    "options": [
      "Banana Apple Mango",
      "Apple Banana Mango",
      "Apple Mango Banana",
      "Banana Apple Mango Apple"
    ],
    "correctAnswer": 0,
    "explanation": "LinkedHashSet vừa đảm bảo tính chất của Set (loại bỏ phần tử trùng lặp) vừa duy trì một danh sách liên kết kép chạy qua các phần tử để bảo toàn thứ tự chèn (insertion-order). Khi thêm lại \"Apple\" lần thứ hai, phần tử bị từ chối và vị trí thứ tự chèn ban đầu không đổi. Kết quả in ra theo đúng thứ tự chèn: 'Banana Apple Mango'.",
    "difficulty": "easy",
    "tags": ["LinkedHashSet", "Insertion-Order"]
  },
  {
    "id": "L5_Q20",
    "lessonId": 5,
    "title": "Đoạn mã sau sử dụng PriorityQueue (Hàng đợi ưu tiên). Kết quả in ra là gì?",
    "code": "import java.util.*;\npublic class PQTest {\n    public static void main(String[] args) {\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        pq.add(40);\n        pq.add(10);\n        pq.add(30);\n        pq.add(20);\n        while (!pq.isEmpty()) {\n            System.out.print(pq.poll() + \" \");\n        }\n    }\n}",
    "options": [
      "10 20 30 40 ",
      "40 10 30 20 ",
      "40 30 20 10 ",
      "10 40 30 20 "
    ],
    "correctAnswer": 0,
    "explanation": "PriorityQueue trong Java mặc định là Min-Heap (cây vun đống cực tiểu). Mỗi lần gọi poll(), phần tử có độ ưu tiên nhỏ nhất (theo thứ tự tự nhiên của Comparable) sẽ được lấy ra đầu tiên. Vì vậy các số được lấy ra theo thứ tự tăng dần từ bé đến lớn: '10 20 30 40 '.",
    "difficulty": "easy",
    "tags": ["PriorityQueue", "Min-Heap", "Natural-Ordering"]
  }
]

# ==============================================================================
# LESSON 6: Xử lý ngoại lệ & Luồng I/O
# ==============================================================================
lesson6_questions = [
  {
    "id": "L6_Q01",
    "lessonId": 6,
    "title": "Trong cây phân cấp ngoại lệ của Java, phát biểu nào sau đây phân biệt chính xác giữa Error và Exception?",
    "code": None,
    "options": [
      "Error đại diện cho các sự cố nghiêm trọng của hệ thống/JVM (như OutOfMemoryError, StackOverflowError) mà ứng dụng không nên và thường không thể phục hồi; Exception đại diện cho các điều kiện bất thường mà ứng dụng có thể bắt và xử lý",
      "Error là ngoại lệ kiểm tra (Checked Exception); Exception là ngoại lệ không kiểm tra (Unchecked Exception)",
      "Error chỉ xảy ra trong thời gian biên dịch; Exception chỉ xảy ra khi chạy chương trình",
      "Lớp Exception kế thừa trực tiếp từ Error"
    ],
    "correctAnswer": 0,
    "explanation": "Cả Error và Exception đều kế thừa từ Throwable. Error biểu thị các lỗi nghiêm trọng ở cấp độ tài nguyên phần cứng hoặc máy ảo JVM (OutOfMemoryError, StackOverflowError) mà chương trình không có khả năng khắc phục. Exception biểu thị các tình huống lỗi nghiệp vụ hoặc ngoại cảnh mà chương trình có thể bắt (catch) và phục hồi xử lý an toàn.",
    "difficulty": "easy",
    "tags": ["Exception-Hierarchy", "Error-vs-Exception"]
  },
  {
    "id": "L6_Q02",
    "lessonId": 6,
    "title": "Ngoại lệ không kiểm tra (Unchecked Exception) trong Java bao gồm những ngoại lệ nào?",
    "code": None,
    "options": [
      "Bao gồm RuntimeException và tất cả các lớp con của nó (như NullPointerException, ArrayIndexOutOfBoundsException), cùng với Error",
      "Bao gồm tất cả các lớp kế thừa trực tiếp từ Exception trừ RuntimeException",
      "Chỉ bao gồm IOException và SQLException",
      "Tất cả các ngoại lệ được khai báo bằng từ khóa throws"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Java, Unchecked Exception bao gồm lớp java.lang.RuntimeException cùng các lớp con của nó (biểu thị lỗi logic lập trình như chia cho 0, trỏ null, vượt biên mảng) và các lớp Error. Trình biên dịch không bắt buộc lập trình viên phải bắt try-catch hay khai báo throws đối với Unchecked Exceptions.",
    "difficulty": "medium",
    "tags": ["Unchecked-Exception", "RuntimeException"]
  },
  {
    "id": "L6_Q03",
    "lessonId": 6,
    "title": "Khối lệnh finally trong cấu trúc try-catch-finally được đảm bảo thực thi trong trường hợp nào?",
    "code": None,
    "options": [
      "Luôn luôn thực thi dù khối try có kết thúc bình thường, ném ngoại lệ, hay có lệnh return; Chỉ bị bỏ qua khi gọi System.exit() hoặc JVM gặp sự cố sập nguồn",
      "Chỉ thực thi khi có ngoại lệ xảy ra trong khối try",
      "Chỉ thực thi khi không có bất kỳ lệnh return nào trong khối try hoặc catch",
      "Không thực thi nếu khối catch đã bắt được ngoại lệ"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc JVM: Khối finally luôn được chạy ngay cả khi try/catch chứa lệnh return, break, continue hoặc ném ngoại lệ. Trường hợp duy nhất khối finally không chạy là tiến trình JVM bị chấm dứt đột ngột bằng System.exit(0), bị hệ điều hành kill process, hoặc gặp lỗi phần cứng/mất nguồn.",
    "difficulty": "medium",
    "tags": ["Finally-Block", "Execution-Guarantee"]
  },
  {
    "id": "L6_Q04",
    "lessonId": 6,
    "title": "Điều gì xảy ra nếu khối finally chứa một câu lệnh return hoặc ném một ngoại lệ mới?",
    "code": None,
    "options": [
      "Nó sẽ ghi đè và nuốt chửng (swallow/suppress) hoàn toàn bất kỳ giá trị return nào hoặc ngoại lệ nào từng được ném ra trong khối try hoặc catch",
      "Trình biên dịch báo lỗi cú pháp cấm dùng return trong finally",
      "Giá trị return trong finally được cộng dồn với giá trị return trong try",
      "Cả hai ngoại lệ sẽ cùng được ném ra đồng thời tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Một quy tắc rất nguy hiểm trong Java: Nếu khối finally thực thi lệnh return hoặc throw exception, nó sẽ ghi đè và hủy bỏ hoàn toàn trạng thái return hoặc ngoại lệ đang chờ xử lý từ khối try/catch trước đó. Vì lý do này, các quy chuẩn Clean Code (như SonarLint) luôn cấm viết lệnh return trong khối finally.",
    "difficulty": "hard",
    "tags": ["Finally-Block", "Return-Override", "Code-Smell"]
  },
  {
    "id": "L6_Q05",
    "lessonId": 6,
    "title": "Cơ chế try-with-resources (giới thiệu từ Java 7) đòi hỏi tài nguyên khai báo phải thỏa mãn điều kiện gì?",
    "code": None,
    "options": [
      "Phải triển khai interface java.lang.AutoCloseable hoặc java.io.Closeable",
      "Phải là một luồng (Thread) đang chạy",
      "Bắt buộc phải có từ khóa final ở dòng khai báo",
      "Phải kế thừa từ lớp trừu tượng java.io.InputStream"
    ],
    "correctAnswer": 0,
    "explanation": "Cú pháp try (ResourceType res = new ResourceType()) { ... } yêu cầu đối tượng tài nguyên phải triển khai interface java.lang.AutoCloseable (hoặc Closeable). Khi kết thúc khối try, phương thức close() của tài nguyên sẽ được JVM tự động gọi theo thứ tự ngược lại với thứ tự khai báo.",
    "difficulty": "easy",
    "tags": ["Try-with-resources", "AutoCloseable", "Java7"]
  },
  {
    "id": "L6_Q06",
    "lessonId": 6,
    "title": "Quy tắc sắp xếp thứ tự giữa các khối catch liên tiếp trong Java là gì?",
    "code": None,
    "options": [
      "Khối catch ngoại lệ con (cụ thể hơn) bắt buộc phải đứng trước khối catch ngoại lệ cha (tổng quát hơn); Viết ngược lại sẽ bị lỗi biên dịch (unreachable code)",
      "Khối catch ngoại lệ cha phải đứng trước khối catch ngoại lệ con",
      "Thứ tự sắp xếp các khối catch là hoàn toàn ngẫu nhiên không ảnh hưởng",
      "Chỉ được phép có duy nhất một khối catch cho mỗi khối try"
    ],
    "correctAnswer": 0,
    "explanation": "Cơ chế bắt ngoại lệ kiểm tra từ trên xuống dưới. Nếu khối catch ngoại lệ tổng quát (như Exception) đứng trước khối catch ngoại lệ con (như IOException), khối catch con sẽ không bao giờ có cơ hội thực thi. Trình biên dịch Java phát hiện điều này và báo lỗi: 'exception IOException has already been caught' (unreachable catch block).",
    "difficulty": "medium",
    "tags": ["Catch-Order", "Compile-Error", "Unreachable-Code"]
  },
  {
    "id": "L6_Q07",
    "lessonId": 6,
    "title": "Sự khác biệt căn bản giữa Luồng Byte (Byte Streams) và Luồng Ký tự (Character Streams) trong Java I/O là gì?",
    "code": None,
    "options": [
      "Byte Streams (InputStream/OutputStream) xử lý dữ liệu nhị phân thô theo từng byte 8-bit; Character Streams (Reader/Writer) xử lý văn bản theo từng ký tự Unicode 16-bit và tự động ánh xạ bảng mã (encoding)",
      "Byte Streams chỉ đọc được file văn bản; Character Streams chỉ đọc được ảnh và video",
      "Character Streams nhanh hơn Byte Streams gấp 10 lần",
      "Byte Streams không hỗ trợ cơ chế đệm bộ nhớ (Buffering)"
    ],
    "correctAnswer": 0,
    "explanation": "Byte Streams (gốc là InputStream và OutputStream) đọc/ghi dữ liệu nhị phân thô (raw 8-bit bytes), thích hợp cho file ảnh, video, file thực thi. Character Streams (gốc là Reader và Writer) được thiết kế chuyên biệt cho văn bản (Unicode 16-bit characters), tự động chuyển đổi giữa byte và ký tự theo charset mã hóa (như UTF-8).",
    "difficulty": "easy",
    "tags": ["Java-IO", "Byte-Stream", "Character-Stream"]
  },
  {
    "id": "L6_Q08",
    "lessonId": 6,
    "title": "Mục đích của việc khai báo hằng số 'private static final long serialVersionUID' trong lớp triển khai java.io.Serializable là gì?",
    "code": None,
    "options": [
      "Kiểm soát phiên bản của lớp trong quá trình tuần tự hóa (Serialization) và giải tuần tự hóa (Deserialization), đảm bảo tính tương thích của đối tượng giữa người gửi và người nhận",
      "Tăng tốc độ ghi dữ liệu của đối tượng vào đĩa cứng",
      "Mã hóa bảo mật các trường dữ liệu mật khẩu",
      "Bắt buộc JVM phải cấp phát dung lượng bộ nhớ cố định cho đối tượng"
    ],
    "correctAnswer": 0,
    "explanation": "serialVersionUID đóng vai trò là mã nhận dạng phiên bản cho lớp Serializable. Khi giải tuần tự hóa, JVM so sánh serialVersionUID trong luồng dữ liệu với serialVersionUID của lớp hiện tại trong máy. Nếu không trùng khớp, JVM ném InvalidClassException. Nếu không khai báo tường minh, JVM tự tính toán hash từ cấu trúc lớp, rất dễ gãy tương thích khi lớp bị sửa đổi nhẹ.",
    "difficulty": "medium",
    "tags": ["Serialization", "serialVersionUID", "Versioning"]
  },
  {
    "id": "L6_Q09",
    "lessonId": 6,
    "title": "Từ khóa transient khi áp dụng cho một trường dữ liệu (field) trong Java có ý nghĩa gì?",
    "code": None,
    "options": [
      "Loại trừ trường dữ liệu đó khỏi quá trình tuần tự hóa (Serialization); Khi giải tuần tự hóa, trường này sẽ nhận giá trị mặc định (0, null, false)",
      "Biến trường đó thành biến chỉ đọc giống như final",
      "Lưu trường dữ liệu đó vào bộ nhớ vĩnh viễn trên ổ cứng",
      "Cho phép trường đó được truy cập bởi nhiều luồng mà không cần đồng bộ"
    ],
    "correctAnswer": 0,
    "explanation": "Từ khóa transient thông báo cho cơ chế tuần tự hóa mặc định của Java bỏ qua trường dữ liệu này (thường dùng cho thông tin nhạy cảm như password, hoặc các tài nguyên phụ thuộc môi trường như database connection, thread). Khi deserialize lại, trường transient sẽ nhận giá trị mặc định của kiểu dữ liệu (null cho object, 0 cho số).",
    "difficulty": "easy",
    "tags": ["Transient", "Serialization"]
  },
  {
    "id": "L6_Q10",
    "lessonId": 6,
    "title": "Biến tĩnh (static field) có được lưu trữ trong quá trình tuần tự hóa (Serialization) của đối tượng hay không? Vì sao?",
    "code": None,
    "options": [
      "Không được lưu, vì biến static thuộc về phạm vi lớp (Class) chứ không phải là một phần trạng thái của thể hiện đối tượng (Instance State)",
      "Có được lưu bình thường như các trường instance khác",
      "Chỉ được lưu nếu biến static đó có từ khóa final",
      "Làm cho quá trình tuần tự hóa bị ném NotSerializableException"
    ],
    "correctAnswer": 0,
    "explanation": "Tuần tự hóa đối tượng (Object Serialization) chỉ lưu trữ trạng thái của thể hiện (instance state). Biến static thuộc về lớp (class state) và được chia sẻ giữa mọi đối tượng. Vì vậy cơ chế Serialization mặc định của Java không bao giờ lưu biến static vào luồng ObjectOutputStream.",
    "difficulty": "medium",
    "tags": ["Serialization", "Static-Field"]
  },
  {
    "id": "L6_Q11",
    "lessonId": 6,
    "title": "Đoạn mã sau cho kết quả trả về là gì khi thực thi phương thức test()?",
    "code": "public class FinallyReturn {\n    public static int test() {\n        try {\n            return 10;\n        } finally {\n            return 20;\n        }\n    }\n    public static void main(String[] args) {\n        System.out.println(test());\n    }\n}",
    "options": [
      "20",
      "10",
      "30",
      "Lỗi biên dịch do có hai lệnh return"
    ],
    "correctAnswer": 0,
    "explanation": "Khi khối try gặp lệnh return 10, JVM lưu tạm giá trị 10 vào vùng nhớ stack nhưng chưa hoàn tất phương thức mà chuyển sang thực thi khối finally. Bên trong finally có lệnh return 20, lệnh này lập tức ghi đè lên giá trị trả về trước đó và kết thúc hàm ngay lập tức. Do đó hàm test() trả về 20.",
    "difficulty": "medium",
    "tags": ["Finally-Block", "Return-Value", "JVM-Stack"]
  },
  {
    "id": "L6_Q12",
    "lessonId": 6,
    "title": "Hiện tượng gì xảy ra khi khối finally ném ra một ngoại lệ mới trong đoạn mã sau?",
    "code": "public class ExceptionMasking {\n    public static void main(String[] args) {\n        try {\n            throw new NullPointerException(\"Loi o Try\");\n        } finally {\n            throw new IllegalArgumentException(\"Loi o Finally\");\n        }\n    }\n}",
    "options": [
      "Ném ra IllegalArgumentException (\"Loi o Finally\"), ngoại lệ NullPointerException bị che giấu hoàn toàn",
      "Ném ra NullPointerException (\"Loi o Try\")",
      "Cả hai ngoại lệ được in ra màn hình cùng lúc",
      "Lỗi biên dịch tại khối finally"
    ],
    "correctAnswer": 0,
    "explanation": "Khi một ngoại lệ được ném ra từ khối try, JVM bắt đầu tìm catch hoặc finally. Khi nhảy vào khối finally, nếu khối finally ném ra một ngoại lệ mới (IllegalArgumentException), ngoại lệ mới này sẽ thay thế và nuốt chửng (mask/suppress) ngoại lệ ban đầu của try. Ngoại lệ NullPointerException bị thất lạc hoàn toàn.",
    "difficulty": "hard",
    "tags": ["Exception-Masking", "Finally-Block"]
  },
  {
    "id": "L6_Q13",
    "lessonId": 6,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi biên dịch?",
    "code": "import java.io.*;\npublic class CatchOrderTest {\n    public static void main(String[] args) {\n        try {\n            FileInputStream fis = new FileInputStream(\"file.txt\");\n        } catch (Exception e) {\n            System.out.println(\"Exception caught\");\n        } catch (FileNotFoundException e) { // Dong nay\n            System.out.println(\"File not found\");\n        }\n    }\n}",
    "options": [
      "Lỗi biên dịch: FileNotFoundException đã được bắt bởi khối catch (Exception) ở trước (unreachable catch block)",
      "Biên dịch thành công và in ra 'File not found'",
      "Biên dịch thành công và in ra 'Exception caught'",
      "Chương trình chạy bình thường không có lỗi"
    ],
    "correctAnswer": 0,
    "explanation": "FileNotFoundException là lớp con của IOException và Exception. Vì khối catch(Exception e) đứng ở phía trên, nó sẽ bắt mọi ngoại lệ con, khiến cho khối catch(FileNotFoundException e) phía dưới không bao giờ có thể tiếp cận được (unreachable code). Trình biên dịch Java phát hiện và báo lỗi biên dịch.",
    "difficulty": "easy",
    "tags": ["Catch-Order", "Compile-Error", "Unreachable-Catch"]
  },
  {
    "id": "L6_Q14",
    "lessonId": 6,
    "title": "Thứ tự đóng các tài nguyên khi sử dụng try-with-resources trong đoạn mã sau là gì?",
    "code": "class Res implements AutoCloseable {\n    String name;\n    Res(String name) { this.name = name; }\n    public void close() { System.out.print(\"Close \" + name + \" \"); }\n}\npublic class TryWithResourcesTest {\n    public static void main(String[] args) {\n        try (Res r1 = new Res(\"R1\"); Res r2 = new Res(\"R2\")) {\n            System.out.print(\"Work \");\n        }\n    }\n}",
    "options": [
      "Work Close R2 Close R1 ",
      "Work Close R1 Close R2 ",
      "Close R1 Close R2 Work ",
      "Work Close R1 "
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc của try-with-resources: Các tài nguyên AutoCloseable được đóng tự động khi thoát khỏi khối try theo thứ tự NGƯỢC LẠI với thứ tự khai báo (nguyên lý LIFO - Last-In, First-Out, tương tự đóng ngăn xếp). Đầu tiên thân try in 'Work ', sau đó r2 được đóng in 'Close R2 ', rồi r1 được đóng in 'Close R1 '. Kết quả: 'Work Close R2 Close R1 '.",
    "difficulty": "medium",
    "tags": ["Try-with-resources", "Closing-Order", "LIFO"]
  },
  {
    "id": "L6_Q15",
    "lessonId": 6,
    "title": "Đoạn mã sau kiểm tra quá trình tuần tự hóa đối tượng chứa trường transient. Kết quả in ra là gì?",
    "code": "import java.io.*;\nclass User implements Serializable {\n    String username;\n    transient int pin;\n    User(String u, int p) { this.username = u; this.pin = p; }\n}\npublic class SerializeTest {\n    public static void main(String[] args) throws Exception {\n        ByteArrayOutputStream baos = new ByteArrayOutputStream();\n        ObjectOutputStream oos = new ObjectOutputStream(baos);\n        oos.writeObject(new User(\"vietanh\", 1234));\n\n        ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(baos.toByteArray()));\n        User u = (User) ois.readObject();\n        System.out.println(u.username + \" \" + u.pin);\n    }\n}",
    "options": [
      "vietanh 0",
      "vietanh 1234",
      "null 0",
      "Ném NotSerializableException"
    ],
    "correctAnswer": 0,
    "explanation": "Trường 'pin' được đánh dấu là transient nên không được ghi vào luồng ObjectOutputStream trong quá trình tuần tự hóa. Khi giải tuần tự hóa (readObject), đối tượng được tái tạo lại và trường transient nhận giá trị mặc định của kiểu int là 0. Trường username được serialize bình thường nên giữ nguyên 'vietanh'. Kết quả in ra: 'vietanh 0'.",
    "difficulty": "medium",
    "tags": ["Serialization", "Transient", "Default-Value"]
  },
  {
    "id": "L6_Q16",
    "lessonId": 6,
    "title": "Đoạn mã sau có khối finally chứa System.out.println. Kết quả in ra màn hình là gì?",
    "code": "public class ExitTest {\n    public static void main(String[] args) {\n        try {\n            System.out.print(\"A \");\n            System.exit(0);\n        } finally {\n            System.out.print(\"B \");\n        }\n    }\n}",
    "options": [
      "A ",
      "A B ",
      "B ",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Lệnh System.exit(0) gửi tín hiệu kết thúc ngay lập tức cho tiến trình máy ảo JVM. Khi JVM bị tắt đột ngột, mọi luồng thực thi bị hủy và khối finally sẽ KHÔNG ĐƯỢC CHẠY. Do đó chương trình chỉ in ra 'A '.",
    "difficulty": "easy",
    "tags": ["System-exit", "Finally-Block"]
  },
  {
    "id": "L6_Q17",
    "lessonId": 6,
    "title": "Đoạn mã sau xảy ra lỗi gì khi biên dịch (tính chất của Multi-catch)?",
    "code": "import java.io.*;\nimport java.sql.*;\npublic class MultiCatchTest {\n    public static void main(String[] args) {\n        try {\n            if (args.length == 0) throw new IOException();\n            else throw new SQLException();\n        } catch (IOException | SQLException e) {\n            e = new IOException(); // Dong nay\n        }\n    }\n}",
    "options": [
      "Lỗi biên dịch: Biến ngoại lệ 'e' trong khối multi-catch ngầm định là final, không thể gán lại",
      "Lỗi biên dịch: Không được phép gộp IOException và SQLException trong cùng một catch",
      "Biên dịch thành công và gán lại bình thường",
      "Ném NullPointerException tại runtime"
    ],
    "correctAnswer": 0,
    "explanation": "Từ Java 7, cú pháp multi-catch (catch (TypeA | TypeB e)) quy định biến tham chiếu ngoại lệ e ngầm định mang thuộc tính final (implicitly final). Do đó, bất kỳ câu lệnh gán lại giá trị cho e bên trong khối catch đều bị trình biên dịch từ chối: 'cannot assign a value to final variable e'.",
    "difficulty": "hard",
    "tags": ["Multi-Catch", "Implicitly-Final", "Compile-Error"]
  },
  {
    "id": "L6_Q18",
    "lessonId": 6,
    "title": "Đoạn mã sau xảy ra lỗi gì khi biên dịch?",
    "code": "class SuperClass {\n    void execute() {}\n}\nclass SubClass extends SuperClass {\n    @Override\n    void execute() throws Exception {} // Dong nay\n}",
    "options": [
      "Lỗi biên dịch: Phương thức ghi đè không được khai báo ném ngoại lệ Checked mới nếu phương thức ở lớp cha không khai báo",
      "Lỗi biên dịch: Lớp SubClass phải là abstract",
      "Biên dịch thành công vì Exception là ngoại lệ chuẩn của Java",
      "Chương trình chạy bình thường"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc ghi đè phương thức: Phương thức ở lớp con không được phép ném ngoại lệ Checked mới (hoặc rộng hơn) so với danh sách ngoại lệ được khai báo ở phương thức lớp cha. Ở đây phương thức execute() của SuperClass không ném ngoại lệ nào, nhưng SubClass lại khai báo throws Exception (Checked Exception), vi phạm quy tắc kế thừa nên báo lỗi biên dịch.",
    "difficulty": "medium",
    "tags": ["Overriding", "Throws-Rule", "Compile-Error"]
  },
  {
    "id": "L6_Q19",
    "lessonId": 6,
    "title": "Cơ chế Ngoại lệ bị áp chế (Suppressed Exceptions) trong try-with-resources. Kết quả in ra là gì?",
    "code": "class FaultyRes implements AutoCloseable {\n    public void close() throws Exception {\n        throw new Exception(\"Close Exception\");\n    }\n}\npublic class SuppressedTest {\n    public static void main(String[] args) {\n        try (FaultyRes r = new FaultyRes()) {\n            throw new Exception(\"Try Exception\");\n        } catch (Exception e) {\n            System.out.println(e.getMessage() + \" | Suppressed: \" + e.getSuppressed().length);\n        }\n    }\n}",
    "options": [
      "Try Exception | Suppressed: 1",
      "Close Exception | Suppressed: 1",
      "Try Exception | Suppressed: 0",
      "Close Exception | Suppressed: 0"
    ],
    "correctAnswer": 0,
    "explanation": "Trong try-with-resources, nếu cả thân try và phương thức close() đều ném ngoại lệ, thì ngoại lệ từ thân try ('Try Exception') được ưu tiên ném ra làm ngoại lệ chính. Ngoại lệ phát sinh từ close() ('Close Exception') không bị nuốt chửng như khối finally truyền thống, mà được JVM tự động đính kèm vào danh sách suppressed của ngoại lệ chính. Do đó e.getMessage() là 'Try Exception' và e.getSuppressed().length là 1.",
    "difficulty": "hard",
    "tags": ["Try-with-resources", "Suppressed-Exceptions", "Java7"]
  },
  {
    "id": "L6_Q20",
    "lessonId": 6,
    "title": "Đoạn mã sau xảy ra lỗi gì khi biên dịch?",
    "code": "class CustomCheckedException extends Exception {}\npublic class TestCustom {\n    static void doWork() {\n        throw new CustomCheckedException(); // Dong nay\n    }\n    public static void main(String[] args) {\n        doWork();\n    }\n}",
    "options": [
      "Lỗi biên dịch: Ngoại lệ Checked CustomCheckedException chưa được bắt bằng try-catch hoặc khai báo trong mệnh đề throws của phương thức doWork()",
      "Lỗi biên dịch do CustomCheckedException không có constructor nhận String",
      "Biên dịch thành công và ném lỗi tại runtime",
      "Lỗi biên dịch tại hàm main do thiếu static"
    ],
    "correctAnswer": 0,
    "explanation": "Vì CustomCheckedException kế thừa trực tiếp từ Exception (mà không phải RuntimeException), nó là một Checked Exception. Bất kỳ phương thức nào ném ra một Checked Exception BẮT BUỘC phải xử lý bằng khối try-catch hoặc khai báo throws ở chữ ký phương thức (ví dụ: static void doWork() throws CustomCheckedException). Do không làm cả hai, trình biên dịch báo lỗi: 'unreported exception CustomCheckedException; must be caught or declared to be thrown'.",
    "difficulty": "easy",
    "tags": ["Custom-Exception", "Checked-Exception", "Compile-Error"]
  }
]

def save(lesson_id, data):
    p = os.path.join(OUTPUT_DIR, f"lesson{lesson_id}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Lesson {lesson_id}: {len(data)} questions saved.")

save(4, lesson4_questions)
save(5, lesson5_questions)
save(6, lesson6_questions)
