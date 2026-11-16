# -*- coding: utf-8 -*-
import json
import os

OUTPUT_DIR = r"d:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\questions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# LESSON 7: Mẫu thiết kế (Design Patterns & SOLID)
# ==============================================================================
lesson7_questions = [
  {
    "id": "L7_Q01",
    "lessonId": 7,
    "title": "Nguyên lý Trách nhiệm Đơn lẻ (Single Responsibility Principle - SRP) và Đóng/Mở (Open/Closed Principle - OCP) trong SOLID quy định điều gì?",
    "code": None,
    "options": [
      "SRP: Một lớp chỉ nên có một lý do duy nhất để thay đổi; OCP: Phần mềm nên mở cho việc mở rộng (Open for extension) nhưng đóng cho việc sửa đổi (Closed for modification)",
      "SRP: Mỗi project chỉ có duy nhất một lớp chính; OCP: Không cho phép kế thừa lớp đã biên dịch",
      "SRP: Mỗi phương thức chỉ có tối đa một tham số; OCP: Mọi biến phải là private",
      "SRP: Một interface chỉ có duy nhất một phương thức; OCP: Mã nguồn phải được bảo mật mã hóa"
    ],
    "correctAnswer": 0,
    "explanation": "SRP quy định mỗi lớp chỉ nên đảm nhận một trách nhiệm nghiệp vụ duy nhất (chỉ có 1 lý do để thay đổi). OCP quy định hệ thống phải dễ dàng mở rộng hành vi mới (bằng cách bổ sung lớp mới, kế thừa, implements) mà không cần phải can thiệp chỉnh sửa mã nguồn cũ đã được kiểm thử ổn định.",
    "difficulty": "easy",
    "tags": ["SOLID", "SRP", "OCP"]
  },
  {
    "id": "L7_Q02",
    "lessonId": 7,
    "title": "Nguyên lý Thay thế Liskov (Liskov Substitution Principle - LSP) yêu cầu điều kiện gì đối với quan hệ kế thừa?",
    "code": None,
    "options": [
      "Các đối tượng của lớp con phải có thể thay thế hoàn toàn cho đối tượng của lớp cha mà không làm thay đổi tính đúng đắn của chương trình",
      "Lớp con bắt buộc phải ghi đè toàn bộ các phương thức của lớp cha",
      "Lớp cha phải có khả năng ép kiểu xuống lớp con mà không bị ngoại lệ",
      "Mọi thuộc tính của lớp cha phải được chuyển thành public trong lớp con"
    ],
    "correctAnswer": 0,
    "explanation": "LSP phát biểu rằng nếu S là kiểu con của T, thì các đối tượng kiểu T trong chương trình có thể được thay thế bằng các đối tượng kiểu S mà không làm thay đổi bất kỳ tính chất đúng đắn nào của chương trình. Vi phạm kinh điển của LSP là thiết kế hình Vuông (Square) kế thừa từ hình Chữ Nhật (Rectangle).",
    "difficulty": "medium",
    "tags": ["SOLID", "LSP", "Inheritance"]
  },
  {
    "id": "L7_Q03",
    "lessonId": 7,
    "title": "Nguyên lý Phân tách Giao diện (ISP) và Đảo ngược Phụ thuộc (DIP) có ý nghĩa như thế nào trong thiết kế kiến trúc phần mềm?",
    "code": None,
    "options": [
      "ISP: Nhiều interface hẹp đặc tả tốt hơn một interface khổng lồ; DIP: Các module cấp cao không nên phụ thuộc trực tiếp vào module cấp thấp, cả hai nên phụ thuộc vào trừu tượng (Abstraction)",
      "ISP: Tất cả các lớp phải dùng chung một interface; DIP: Module cấp cao phải gọi trực tiếp module cấp thấp",
      "ISP: Interface không được phép có default method; DIP: Phải dùng từ khóa static thay vì interface",
      "ISP: Phân tách interface theo từng package; DIP: Đảo ngược thứ tự các tham số trong hàm"
    ],
    "correctAnswer": 0,
    "explanation": "ISP (Interface Segregation Principle) khuyên không nên ép client phụ thuộc vào các phương thức mà họ không sử dụng (chia nhỏ 'fat interface'). DIP (Dependency Inversion Principle) khuyến khích lập trình dựa trên trừu tượng (interface/abstract class) thay vì phụ thuộc cứng vào các lớp triển khai cụ thể (concrete classes).",
    "difficulty": "medium",
    "tags": ["SOLID", "ISP", "DIP"]
  },
  {
    "id": "L7_Q04",
    "lessonId": 7,
    "title": "Các mẫu thiết kế Singleton, Factory Method, Strategy, Decorator, Adapter, Composite được phân loại vào các nhóm GoF nào?",
    "code": None,
    "options": [
      "Khởi tạo (Creational): Singleton, Factory Method; Cấu trúc (Structural): Adapter, Decorator, Composite; Hành vi (Behavioral): Strategy",
      "Khởi tạo: Strategy, Decorator; Cấu trúc: Singleton; Hành vi: Factory Method, Adapter",
      "Khởi tạo: Composite, Adapter; Cấu trúc: Factory Method; Hành vi: Singleton, Decorator",
      "Tất cả các mẫu thiết kế trên đều thuộc nhóm Kiến trúc (Architectural Patterns)"
    ],
    "correctAnswer": 0,
    "explanation": "Theo chuẩn Gang of Four (GoF): 1) Creational (Khởi tạo): Singleton, Factory Method, Abstract Factory, Builder, Prototype. 2) Structural (Cấu trúc): Adapter, Decorator, Composite, Proxy, Facade, Bridge. 3) Behavioral (Hành vi): Strategy, Observer, Command, Template Method, State.",
    "difficulty": "easy",
    "tags": ["Design-Patterns", "GoF-Classification"]
  },
  {
    "id": "L7_Q05",
    "lessonId": 7,
    "title": "Trong kỹ thuật Double-Checked Locking khi cài đặt Singleton lười (Lazy Singleton), từ khóa volatile trên biến instance có vai trò quyết định gì?",
    "code": None,
    "options": [
      "Ngăn chặn hiện tượng sắp xếp lại lệnh (Instruction Reordering) của trình biên dịch và CPU, đảm bảo đối tượng được khởi tạo hoàn tất trước khi gán tham chiếu cho các luồng khác thấy",
      "Đảm bảo phương thức getInstance() chạy nhanh hơn gấp 10 lần",
      "Ngăn cản việc kế thừa lớp Singleton",
      "Tự động giải phóng bộ nhớ khi Singleton không còn được sử dụng"
    ],
    "correctAnswer": 0,
    "explanation": "Lệnh instance = new Singleton() bao gồm 3 bước: 1) Cấp phát bộ nhớ, 2) Chạy constructor khởi tạo, 3) Gán địa chỉ cho biến instance. Do CPU/Compiler tối ưu có thể đảo bước 3 lên trước bước 2 (Instruction Reordering), luồng khác có thể thấy instance != null và sử dụng đối tượng khi nó CHƯA được khởi tạo xong (partially initialized object). Từ khóa volatile thiết lập rào cản bộ nhớ (Memory Barrier) ngăn chặn việc đảo lệnh này.",
    "difficulty": "hard",
    "tags": ["Singleton", "Double-Checked-Locking", "Volatile", "Concurrency"]
  },
  {
    "id": "L7_Q06",
    "lessonId": 7,
    "title": "Mục đích cốt lõi của mẫu thiết kế Factory Method Pattern là gì?",
    "code": None,
    "options": [
      "Định nghĩa một giao diện để tạo đối tượng, nhưng để các lớp con quyết định lớp cụ thể nào sẽ được khởi tạo",
      "Đảm bảo chỉ có một đối tượng duy nhất tồn tại trong toàn bộ ứng dụng",
      "Chuyển đổi giao diện của một lớp thành một giao diện khác mà client mong đợi",
      "Bọc quanh một đối tượng để bổ sung thêm các tính năng động mà không dùng kế thừa"
    ],
    "correctAnswer": 0,
    "explanation": "Factory Method định nghĩa một phương thức trừu tượng để tạo đối tượng (createProduct()), cho phép lớp cha ủy quyền (delegate) việc khởi tạo đối tượng thực tế cho các lớp con. Điều này giúp tách biệt mã nguồn sử dụng đối tượng khỏi lớp cụ thể của đối tượng đó (Loose Coupling).",
    "difficulty": "easy",
    "tags": ["Factory-Method", "Creational-Pattern"]
  },
  {
    "id": "L7_Q07",
    "lessonId": 7,
    "title": "Mẫu thiết kế Chiến lược (Strategy Pattern) giúp giải quyết vấn đề thiết kế nào phổ biến nhất?",
    "code": None,
    "options": [
      "Loại bỏ các cấu trúc rẽ nhánh if-else hoặc switch-case phức tạp bằng cách đóng gói từng thuật toán vào các lớp chiến lược riêng biệt có thể tráo đổi khi đang chạy",
      "Tạo bản sao của đối tượng mà không phụ thuộc vào lớp của chúng",
      "Ngăn ngừa việc tạo nhiều kết nối tới cơ sở dữ liệu",
      "Đồng bộ hóa các thao tác trên luồng vào ra"
    ],
    "correctAnswer": 0,
    "explanation": "Strategy Pattern định nghĩa một họ các thuật toán, đóng gói từng thuật toán lại và làm cho chúng có thể tráo đổi lẫn nhau (interchangeable). Nó giúp tuân thủ nguyên lý Open/Closed Principle bằng cách loại bỏ các khối if-else/switch khổng lồ kiểm tra loại thuật toán (ví dụ: tính giá khuyến mãi, thuật toán thanh toán).",
    "difficulty": "medium",
    "tags": ["Strategy-Pattern", "OCP", "Code-Smell"]
  },
  {
    "id": "L7_Q08",
    "lessonId": 7,
    "title": "Mối quan hệ giữa Đối tượng được quan sát (Subject) và Các đối tượng quan sát (Observers) trong Observer Pattern là quan hệ loại nào?",
    "code": None,
    "options": [
      "Quan hệ phụ thuộc một - nhiều (One-to-Many): khi Subject thay đổi trạng thái, tất cả Observers đã đăng ký sẽ tự động được thông báo và cập nhật",
      "Quan hệ phụ thuộc một - một (One-to-One)",
      "Quan hệ kế thừa trực tiếp nhiều tầng",
      "Quan hệ độc lập không liên quan lẫn nhau"
    ],
    "correctAnswer": 0,
    "explanation": "Observer Pattern thiết lập mối quan hệ một-nhiều (One-to-Many) lỏng lẻo (loose coupling) giữa Subject và các Observers. Khi trạng thái nội tại của Subject thay đổi, nó duyệt qua danh sách các Observer đã đăng ký và gọi phương thức notify()/update() để các Observer tự đồng bộ trạng thái mới.",
    "difficulty": "easy",
    "tags": ["Observer-Pattern", "Loose-Coupling"]
  },
  {
    "id": "L7_Q09",
    "lessonId": 7,
    "title": "Ưu điểm nổi bật nhất của mẫu thiết kế Trang trí (Decorator Pattern) so với việc sử dụng Kế thừa truyền thống là gì?",
    "code": None,
    "options": [
      "Cho phép bổ sung hành vi/trách nhiệm mới cho đối tượng một cách linh hoạt tại thời điểm thực thi (runtime) mà không làm bùng nổ số lượng lớp con (Class Explosion)",
      "Tăng tốc độ truy xuất thuộc tính của đối tượng",
      "Cho phép đối tượng truy cập các phương thức private của lớp khác",
      "Giảm dung lượng bộ nhớ Heap xuống mức tối thiểu"
    ],
    "correctAnswer": 0,
    "explanation": "Kế thừa mở rộng chức năng ở compile-time và dễ dẫn đến 'Class Explosion' khi có nhiều tổ hợp tính năng (ví dụ: Cà phê có sữa, cà phê có đường, cà phê có cả sữa và đường...). Decorator Pattern giải quyết bằng cách bọc đối tượng (composition), cho phép gắn thêm các lớp vỏ trang trí linh hoạt tại runtime.",
    "difficulty": "medium",
    "tags": ["Decorator-Pattern", "Structural-Pattern", "Composition"]
  },
  {
    "id": "L7_Q10",
    "lessonId": 7,
    "title": "Mẫu thiết kế Composite giải quyết 'Mùi mã nguồn' (Code Smell) nào thường gặp trong cấu trúc cây phân cấp?",
    "code": None,
    "options": [
      "Mùi mã nguồn phải dùng if-else kiểm tra kiểu (instanceof) để phân biệt giữa phần tử lá (Leaf) và phần tử chứa (Container/Composite)",
      "Mùi mã nguồn phương thức quá dài (Long Method)",
      "Mùi mã nguồn danh sách tham số quá dài (Long Parameter List)",
      "Mùi mã nguồn trùng lặp chuỗi ký tự (Duplicate String)"
    ],
    "correctAnswer": 0,
    "explanation": "Slide bài giảng LTNC chỉ rõ: Code Smell: Distinguishing Between Leaves and Containers. Nếu không dùng Composite, mã nguồn phải liên tục kiểm tra xem một node là file hay thư mục bằng instanceof hoặc cờ isFolder. Composite Pattern giải quyết bằng cách định nghĩa interface Component chung, giúp client đối xử đồng nhất (uniform treatment) với cả phần tử đơn lẻ và tập hợp lồng nhau.",
    "difficulty": "hard",
    "tags": ["Composite-Pattern", "Code-Smell", "UET-Slide"]
  },
  {
    "id": "L7_Q11",
    "lessonId": 7,
    "title": "Đoạn mã Singleton sau gặp lỗi gì trong môi trường đa luồng (Multithreading)?",
    "code": "public class BrokenSingleton {\n    private static BrokenSingleton instance; // Thieu tu khoa gi?\n    private BrokenSingleton() {}\n    public static BrokenSingleton getInstance() {\n        if (instance == null) {\n            synchronized (BrokenSingleton.class) {\n                if (instance == null) {\n                    instance = new BrokenSingleton();\n                }\n            }\n        }\n        return instance;\n    }\n}",
    "options": [
      "Thiếu từ khóa volatile trên biến instance, có thể dẫn đến việc luồng khác đọc phải đối tượng chưa được khởi tạo hoàn tất do hiện tượng đảo lệnh (Instruction Reordering)",
      "Lỗi biên dịch do constructor là private",
      "Lỗi biên dịch do từ khóa synchronized không thể áp dụng cho BrokenSingleton.class",
      "Phương thức getInstance() bị deadlock mỗi khi gọi"
    ],
    "correctAnswer": 0,
    "explanation": "Đây là mẫu Double-Checked Locking kinh điển bị lỗi nếu thiếu từ khóa volatile. Khi lệnh new BrokenSingleton() được thực hiện, do hiện tượng instruction reordering, biến instance có thể được gán địa chỉ bộ nhớ trước khi constructor chạy xong. Luồng khác kiểm tra vòng ngoài thấy instance != null sẽ trả về ngay đối tượng chưa hoàn tất, gây lỗi NullPointerException hoặc dữ liệu rác.",
    "difficulty": "hard",
    "tags": ["Singleton", "Double-Checked-Locking", "Volatile"]
  },
  {
    "id": "L7_Q12",
    "lessonId": 7,
    "title": "Đoạn mã sau áp dụng Strategy Pattern. Kết quả in ra là gì?",
    "code": "interface DiscountStrategy {\n    double applyDiscount(double amount);\n}\nclass VipDiscount implements DiscountStrategy {\n    public double applyDiscount(double amount) { return amount * 0.8; }\n}\nclass Order {\n    DiscountStrategy strategy;\n    Order(DiscountStrategy s) { this.strategy = s; }\n    double checkout(double total) { return strategy.applyDiscount(total); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Order order = new Order(new VipDiscount());\n        System.out.println((int) order.checkout(1000));\n    }\n}",
    "options": [
      "800",
      "1000",
      "200",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Lớp Order nhận chiến lược VipDiscount thông qua Dependency Injection. Khi gọi order.checkout(1000), phương thức ủy quyền cho strategy.applyDiscount(1000) tính toán 1000 * 0.8 = 800.0. Ép kiểu (int) in ra màn hình giá trị 800.",
    "difficulty": "easy",
    "tags": ["Strategy-Pattern", "Polymorphism"]
  },
  {
    "id": "L7_Q13",
    "lessonId": 7,
    "title": "Đoạn mã sau sử dụng Decorator Pattern để tính tiền đồ uống. Kết quả in ra là gì?",
    "code": "interface Coffee { int cost(); }\nclass SimpleCoffee implements Coffee {\n    public int cost() { return 10; }\n}\nabstract class CoffeeDecorator implements Coffee {\n    protected Coffee coffee;\n    CoffeeDecorator(Coffee c) { this.coffee = c; }\n}\nclass Milk extends CoffeeDecorator {\n    Milk(Coffee c) { super(c); }\n    public int cost() { return coffee.cost() + 5; }\n}\nclass Sugar extends CoffeeDecorator {\n    Sugar(Coffee c) { super(c); }\n    public int cost() { return coffee.cost() + 2; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Coffee c = new Sugar(new Milk(new SimpleCoffee()));\n        System.out.println(c.cost());\n    }\n}",
    "options": [
      "17",
      "15",
      "12",
      "10"
    ],
    "correctAnswer": 0,
    "explanation": "Cơ chế Decorator xếp lồng (Wrapping): 1) new SimpleCoffee().cost() = 10; 2) new Milk(...).cost() = 10 + 5 = 15; 3) new Sugar(...).cost() = 15 + 2 = 17. Lời gọi c.cost() kích hoạt tính toán từ ngoài vào trong và trả về tổng chi phí là 17.",
    "difficulty": "medium",
    "tags": ["Decorator-Pattern", "Calculation"]
  },
  {
    "id": "L7_Q14",
    "lessonId": 7,
    "title": "Đoạn mã sau cài đặt Observer Pattern. Kết quả in ra màn hình là gì?",
    "code": "import java.util.*;\ninterface Observer { void update(String msg); }\nclass Subject {\n    private List<Observer> list = new ArrayList<>();\n    void attach(Observer o) { list.add(o); }\n    void notifyAllObservers(String msg) {\n        for (Observer o : list) o.update(msg);\n    }\n}\npublic class ObserverTest {\n    public static void main(String[] args) {\n        Subject s = new Subject();\n        s.attach(msg -> System.out.print(\"O1:\" + msg + \" \"));\n        s.attach(msg -> System.out.print(\"O2:\" + msg + \" \"));\n        s.notifyAllObservers(\"News\");\n    }\n}",
    "options": [
      "O1:News O2:News ",
      "O2:News O1:News ",
      "O1:News ",
      "Lỗi biên dịch do dùng biểu thức Lambda"
    ],
    "correctAnswer": 0,
    "explanation": "Subject lưu các observers trong ArrayList theo thứ tự đăng ký. Khi notifyAllObservers(\"News\") được gọi, nó duyệt tuần tự qua danh sách: observer 1 in 'O1:News ', sau đó observer 2 in 'O2:News '. Kết quả in ra là 'O1:News O2:News '.",
    "difficulty": "easy",
    "tags": ["Observer-Pattern", "Lambda"]
  },
  {
    "id": "L7_Q15",
    "lessonId": 7,
    "title": "Đoạn mã sau áp dụng Adapter Pattern để tương thích giao diện. Kết quả in ra là gì?",
    "code": "interface ModernPrinter { void printDocument(String text); }\nclass LegacyPrinter {\n    void printOldFormat(String text) { System.out.print(\"Legacy: \" + text); }\n}\nclass PrinterAdapter implements ModernPrinter {\n    private LegacyPrinter legacy;\n    PrinterAdapter(LegacyPrinter l) { this.legacy = l; }\n    public void printDocument(String text) { legacy.printOldFormat(text); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        ModernPrinter printer = new PrinterAdapter(new LegacyPrinter());\n        printer.printDocument(\"Hello\");\n    }\n}",
    "options": [
      "Legacy: Hello",
      "Hello",
      "Modern: Hello",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "PrinterAdapter triển khai giao diện ModernPrinter và bọc lấy đối tượng LegacyPrinter (Object Adapter). Khi client gọi printer.printDocument(\"Hello\"), adapter chuyển đổi lời gọi thành legacy.printOldFormat(\"Hello\"), in ra màn hình 'Legacy: Hello'.",
    "difficulty": "easy",
    "tags": ["Adapter-Pattern", "Structural-Pattern"]
  },
  {
    "id": "L7_Q16",
    "lessonId": 7,
    "title": "Đoạn mã sau minh họa Factory Method Pattern. Kết quả in ra là gì?",
    "code": "interface Doc { void open(); }\nclass PdfDoc implements Doc { public void open() { System.out.print(\"Open PDF \"); } }\nabstract class App {\n    abstract Doc createDoc();\n    void openDocument() { Doc d = createDoc(); d.open(); }\n}\nclass PdfApp extends App {\n    Doc createDoc() { return new PdfDoc(); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        App app = new PdfApp();\n        app.openDocument();\n    }\n}",
    "options": [
      "Open PDF ",
      "Open Document ",
      "Lỗi biên dịch: Không thể gọi createDoc() từ App",
      "Ném NullPointerException"
    ],
    "correctAnswer": 0,
    "explanation": "Mẫu Factory Method: Lớp cha App định nghĩa phương thức nghiệp vụ openDocument(), trong đó ủy quyền việc tạo đối tượng cho phương thức trừu tượng createDoc(). Lớp con PdfApp ghi đè createDoc() và trả về PdfDoc. Khi gọi app.openDocument(), đối tượng PdfDoc được tạo và in ra 'Open PDF '.",
    "difficulty": "easy",
    "tags": ["Factory-Method", "Polymorphism"]
  },
  {
    "id": "L7_Q17",
    "lessonId": 7,
    "title": "Đoạn mã sau áp dụng Composite Pattern để tính dung lượng cây thư mục. Kết quả in ra là gì?",
    "code": "import java.util.*;\ninterface Component { int getSize(); }\nclass FileLeaf implements Component {\n    int size;\n    FileLeaf(int s) { this.size = s; }\n    public int getSize() { return size; }\n}\nclass FolderComposite implements Component {\n    List<Component> children = new ArrayList<>();\n    void add(Component c) { children.add(c); }\n    public int getSize() {\n        int total = 0;\n        for (Component c : children) total += c.getSize();\n        return total;\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        FolderComposite root = new FolderComposite();\n        root.add(new FileLeaf(10));\n        FolderComposite sub = new FolderComposite();\n        sub.add(new FileLeaf(20));\n        sub.add(new FileLeaf(30));\n        root.add(sub);\n        System.out.println(root.getSize());\n    }\n}",
    "options": [
      "60",
      "50",
      "10",
      "Lỗi biên dịch do đệ quy"
    ],
    "correctAnswer": 0,
    "explanation": "Cấu trúc Composite cho phép tính toán đệ quy trên toàn bộ cây: root chứa FileLeaf(10) và sub. Bản thân sub lại chứa FileLeaf(20) và FileLeaf(30) -> sub.getSize() = 20 + 30 = 50. Tổng dung lượng root.getSize() = 10 + 50 = 60.",
    "difficulty": "medium",
    "tags": ["Composite-Pattern", "Tree-Structure", "Recursion"]
  },
  {
    "id": "L7_Q18",
    "lessonId": 7,
    "title": "Cơ chế khởi tạo Singleton của Bill Pugh (Initialization-on-demand holder idiom) hoạt động như thế nào trong đoạn mã sau?",
    "code": "public class BillPughSingleton {\n    private BillPughSingleton() { System.out.print(\"Init \"); }\n    private static class Holder {\n        private static final BillPughSingleton INSTANCE = new BillPughSingleton();\n    }\n    public static BillPughSingleton getInstance() {\n        return Holder.INSTANCE;\n    }\n    public static void dummy() { System.out.print(\"Dummy \"); }\n    public static void main(String[] args) {\n        BillPughSingleton.dummy();\n        BillPughSingleton.getInstance();\n    }\n}",
    "options": [
      "Dummy Init ",
      "Init Dummy ",
      "Init Init ",
      "Dummy "
    ],
    "correctAnswer": 0,
    "explanation": "Kỹ thuật Bill Pugh lợi dụng cơ chế Class Loading của JVM: Lớp nội tĩnh static nested class Holder CHỈ ĐƯỢC NẠP vào bộ nhớ khi nó được tham chiếu lần đầu tiên. Khi gọi BillPughSingleton.dummy(), lớp cha được nạp và in 'Dummy ', nhưng lớp Holder chưa được đụng tới nên constructor Singleton chưa chạy. Chỉ khi gọi getInstance(), Holder mới được nạp và khởi tạo INSTANCE, in ra 'Init '. Kết quả: 'Dummy Init '.",
    "difficulty": "hard",
    "tags": ["Bill-Pugh", "Singleton", "Class-Loading"]
  },
  {
    "id": "L7_Q19",
    "lessonId": 7,
    "title": "Cho đoạn mã Logger trích từ Đề thi mẫu UET Bài 4. Thiết kế này vi phạm nghiêm trọng nguyên lý nào trong SOLID?",
    "code": "class Logger {\n    void log(String level, String message) {\n        if (level.equals(\"INFO\")) {\n            System.out.println(\"INFO: \" + message);\n        } else if (level.equals(\"ERROR\")) {\n            System.out.println(\"ERROR: \" + message);\n        } else if (level.equals(\"DEBUG\")) {\n            System.out.println(\"DEBUG: \" + message);\n        }\n    }\n}",
    "options": [
      "Vi phạm Open/Closed Principle (OCP): Mỗi khi bổ sung một loại log mới (ví dụ WARN, FATAL), ta buộc phải sửa đổi mã nguồn phương thức log() cũ bằng cách chèn thêm else-if",
      "Vi phạm Liskov Substitution Principle do Logger không có lớp con",
      "Vi phạm Interface Segregation Principle do thiếu interface",
      "Vi phạm Single Responsibility Principle do có quá nhiều tham số"
    ],
    "correctAnswer": 0,
    "explanation": "Bài 4 đề thi mẫu UET: Lớp Logger dùng chuỗi if-else so sánh string 'level' là code smell kinh điển (Switch Statements / Conditional Complexity) và vi phạm trực tiếp Open/Closed Principle (OCP). Để thêm mức log mới phải sửa code cũ, dễ sinh lỗi. Giải pháp refactoring chuẩn là áp dụng Đa hình (Polymorphism) hoặc Strategy Pattern (interface LogStrategy với các lớp InfoLogger, ErrorLogger...).",
    "difficulty": "medium",
    "tags": ["SOLID", "OCP", "Code-Smell", "UET-Exam"]
  },
  {
    "id": "L7_Q20",
    "lessonId": 7,
    "title": "Đoạn mã kinh điển sau vi phạm nguyên lý SOLID nào (Liskov Substitution Principle)?",
    "code": "class Rectangle {\n    protected int width, height;\n    public void setWidth(int w) { this.width = w; }\n    public void setHeight(int h) { this.height = h; }\n    public int getArea() { return width * height; }\n}\nclass Square extends Rectangle {\n    @Override\n    public void setWidth(int w) { this.width = w; this.height = w; }\n    @Override\n    public void setHeight(int h) { this.width = h; this.height = h; }\n}\npublic class Main {\n    static void resize(Rectangle r) {\n        r.setWidth(5);\n        r.setHeight(4);\n        System.out.println(r.getArea()); // Ky vong: 5 * 4 = 20\n    }\n    public static void main(String[] args) {\n        resize(new Square());\n    }\n}",
    "options": [
      "In ra 16, vi phạm Liskov Substitution Principle (LSP) vì Square không thể thay thế cho Rectangle mà vẫn giữ đúng hành vi kỳ vọng",
      "In ra 20, tuân thủ hoàn hảo LSP",
      "Lỗi biên dịch do không thể override setWidth",
      "Ném ClassCastException tại hàm resize"
    ],
    "correctAnswer": 0,
    "explanation": "Ví dụ kinh điển vi phạm LSP: Trong hình học toán học Hình vuông là Hình chữ nhật, nhưng trong OOP hành vi của chúng khác nhau. Hàm resize kỳ vọng với bất kỳ Rectangle nào khi setWidth(5) và setHeight(4) thì diện tích phải là 20. Nhưng khi truyền Square vào, lệnh setHeight(4) lại đổi cả width thành 4 -> getArea() = 16. Lớp con Square phá vỡ hợp đồng hành vi của lớp cha Rectangle, vi phạm LSP.",
    "difficulty": "hard",
    "tags": ["SOLID", "LSP", "Square-Rectangle-Trap"]
  }
]

# ==============================================================================
# LESSON 8: Đa luồng (Multithreading & Concurrency)
# ==============================================================================
lesson8_questions = [
  {
    "id": "L8_Q01",
    "lessonId": 8,
    "title": "Sự khác biệt cốt lõi về phân vùng bộ nhớ giữa Tiến trình (Process) và Luồng (Thread) trong hệ điều hành và JVM là gì?",
    "code": None,
    "options": [
      "Mỗi Process sở hữu không gian địa chỉ bộ nhớ độc lập; Các Thread trong cùng một Process chia sẻ chung vùng nhớ Heap nhưng sở hữu Stack và Con trỏ lệnh (PC Register) riêng biệt",
      "Các Process chia sẻ chung bộ nhớ Heap; Các Thread có không gian bộ nhớ hoàn toàn độc lập",
      "Thread không có ngăn xếp Stack riêng mà dùng chung với Process",
      "Process và Thread có cấu trúc bộ nhớ hoàn toàn giống hệt nhau"
    ],
    "correctAnswer": 0,
    "explanation": "Process là một đơn vị thực thi độc lập có không gian bộ nhớ riêng (không chia sẻ trực tiếp với process khác). Thread là một đơn vị thực thi nhẹ (lightweight) bên trong process. Tất cả các luồng trong cùng một JVM process cùng chia sẻ vùng nhớ Heap và Metaspace, nhưng mỗi luồng có ngăn xếp Stack riêng để lưu biến cục bộ và call frame, cùng bộ đếm chương trình PC riêng.",
    "difficulty": "medium",
    "tags": ["Process-vs-Thread", "JVM-Memory", "Stack-Sharing"]
  },
  {
    "id": "L8_Q02",
    "lessonId": 8,
    "title": "So sánh giữa interface java.lang.Runnable và java.util.concurrent.Callable<V>, phát biểu nào sau đây là ĐÚNG?",
    "code": None,
    "options": [
      "Runnable.run() trả về void và không thể ném Checked Exception; Callable.call() trả về một giá trị có kiểu generic V và có thể ném Checked Exception",
      "Runnable có thể trả về giá trị kiểu int; Callable không thể trả về giá trị",
      "Runnable dùng cho luồng đơn; Callable chỉ dùng cho luồng nền daemon",
      "Callable kế thừa trực tiếp từ Runnable"
    ],
    "correctAnswer": 0,
    "explanation": "Trích Đề thi mẫu UET Bài 1 Câu 14: Runnable định nghĩa phương thức 'void run()' không có giá trị trả về và không khai báo throws Checked Exception. Ngược lại, Callable<V> định nghĩa 'V call() throws Exception' có khả năng trả về kết quả tính toán kiểu V và cho phép ném ra Checked Exception.",
    "difficulty": "easy",
    "tags": ["Runnable", "Callable", "Concurrency", "UET-Exam"]
  },
  {
    "id": "L8_Q03",
    "lessonId": 8,
    "title": "Vòng đời của một Thread trong Java (lớp Thread.State) bao gồm các trạng thái chuẩn nào?",
    "code": None,
    "options": [
      "NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED",
      "START, RUNNING, SLEEPING, DEAD",
      "INIT, RUNNING, WAITING, STOPPED",
      "READY, EXECUTING, PAUSED, FINISHED"
    ],
    "correctAnswer": 0,
    "explanation": "Theo enum java.lang.Thread.State trong JVM chuẩn, vòng đời Thread có đúng 6 trạng thái: 1) NEW (mới tạo, chưa start), 2) RUNNABLE (đang chạy hoặc sẵn sàng chạy), 3) BLOCKED (chờ lấy monitor lock synchronized), 4) WAITING (chờ vô hạn qua wait(), join()), 5) TIMED_WAITING (chờ có thời hạn qua sleep(), wait(timeout)), 6) TERMINATED (đã hoàn thành run() hoặc gặp lỗi).",
    "difficulty": "medium",
    "tags": ["Thread-Lifecycle", "Thread-State"]
  },
  {
    "id": "L8_Q04",
    "lessonId": 8,
    "title": "Hiện tượng gì xảy ra khi lập trình viên gọi trực tiếp phương thức thread.run() thay vì thread.start()?",
    "code": None,
    "options": [
      "Phương thức run() sẽ được thực thi tuần tự trên chính luồng hiện tại (calling thread, thường là main), KHÔNG CÓ luồng mới nào được hệ điều hành tạo ra",
      "JVM ném ngoại lệ IllegalThreadStateException",
      "Hệ điều hành vẫn tạo một luồng mới chạy ngầm song song",
      "Chương trình bị treo vô hạn"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức start() yêu cầu JVM đăng ký với hệ điều hành để tạo ra một luồng native mới và luồng đó sẽ gọi run(). Nếu gọi trực tiếp run(), nó chỉ là một lời gọi phương thức thông thường, chạy tuần tự trên luồng gọi nó (ví dụ thread 'main') mà không có bất kỳ tính toán song song nào.",
    "difficulty": "easy",
    "tags": ["Thread-Start", "Thread-Run", "Concurrency"]
  },
  {
    "id": "L8_Q05",
    "lessonId": 8,
    "title": "Khóa nội tại (Intrinsic Lock / Monitor Lock) trong phương thức synchronized hoạt động như thế nào giữa instance method và static method?",
    "code": None,
    "options": [
      "Phương thức instance synchronized khóa trên đối tượng thực thể hiện tại (this); Phương thức static synchronized khóa trên đối tượng Class (ClassName.class)",
      "Cả hai phương thức đều khóa trên đối tượng this",
      "Cả hai phương thức đều khóa trên toàn bộ máy ảo JVM",
      "Static synchronized không sử dụng khóa mà dùng cơ chế hàng đợi"
    ],
    "correctAnswer": 0,
    "explanation": "Mỗi đối tượng Java đều có một Monitor lock. Khi một luồng vào phương thức synchronized non-static, nó chiếm khóa của thể hiện đó (this). Nhưng khi vào static synchronized method, nó chiếm khóa của đối tượng java.lang.Class đại diện cho lớp đó. Do hai khóa này là hai đối tượng khác nhau trên Heap, một luồng chạy instance method và một luồng chạy static method của cùng một lớp có thể chạy đồng thời mà không chặn nhau.",
    "difficulty": "hard",
    "tags": ["Synchronized", "Monitor-Lock", "Class-Lock"]
  },
  {
    "id": "L8_Q06",
    "lessonId": 8,
    "title": "Từ khóa volatile trong Java cung cấp những bảo đảm gì và KHÔNG bảo đảm điều gì?",
    "code": None,
    "options": [
      "Bảo đảm tính hiển thị (Visibility) giữa các CPU Cache và ngăn đảo lệnh (Instruction Reordering); KHÔNG bảo đảm tính nguyên tử (Atomicity) cho các thao tác phức hợp như count++",
      "Bảo đảm tuyệt đối tính nguyên tử cho mọi thao tác toán học",
      "Tự động khóa đối tượng giống hệt như từ khóa synchronized",
      "Bảo đảm phương thức chạy nhanh hơn mà không cần bộ nhớ đệm"
    ],
    "correctAnswer": 0,
    "explanation": "Từ khóa volatile buộc các luồng đọc/ghi trực tiếp từ bộ nhớ chính (Main Memory) thay vì CPU Cache riêng, đảm bảo mọi thay đổi của một luồng được các luồng khác thấy ngay lập tức (Visibility) và thiết lập rào cản bộ nhớ. Tuy nhiên nó KHÔNG đảm bảo tính nguyên tử: thao tác count++ thực chất là 3 bước đọc-sửa-ghi, nên vẫn bị Race Condition nếu nhiều luồng cùng thực hiện.",
    "difficulty": "hard",
    "tags": ["Volatile", "Visibility", "Atomicity", "Race-Condition"]
  },
  {
    "id": "L8_Q07",
    "lessonId": 8,
    "title": "Bốn điều kiện Coffman cần và đủ để xảy ra Bế tắc (Deadlock) giữa các luồng là gì?",
    "code": None,
    "options": [
      "Loại trừ lẫn nhau (Mutual Exclusion), Giữ và chờ (Hold and Wait), Không chiếm đoạt (No Preemption), Chờ đợi vòng tròn (Circular Wait)",
      "Đa luồng, Thiếu bộ nhớ, Mạng chậm, Lỗi CPU",
      "Dùng synchronized, Dùng volatile, Dùng Thread.sleep, Dùng wait()",
      "Quá nhiều tiến trình, Bộ nhớ Heap quá nhỏ, Bộ nhớ Stack quá lớn, Lỗi JIT"
    ],
    "correctAnswer": 0,
    "explanation": "Deadlock xảy ra khi và chỉ khi cả 4 điều kiện Coffman đồng thời thỏa mãn: 1) Mutual Exclusion (tài nguyên không thể chia sẻ đồng thời), 2) Hold and Wait (luồng đang giữ tài nguyên này lại yêu cầu thêm tài nguyên khác), 3) No Preemption (không thể cướp tài nguyên đang bị giữ), 4) Circular Wait (chu trình chờ đợi vòng tròn T1 chờ T2, T2 chờ T1). Biện pháp phá deadlock phổ biến nhất là phá vỡ Circular Wait bằng cách luôn chiếm khóa theo một thứ tự cố định.",
    "difficulty": "hard",
    "tags": ["Deadlock", "Coffman-Conditions"]
  },
  {
    "id": "L8_Q08",
    "lessonId": 8,
    "title": "Quy tắc bắt buộc khi gọi các phương thức wait(), notify(), notifyAll() trong Java là gì?",
    "code": None,
    "options": [
      "Bắt buộc phải được gọi bên trong một khối hoặc phương thức synchronized trên chính đối tượng monitor đó, nếu không sẽ ném IllegalMonitorStateException",
      "Chỉ có thể gọi từ bên trong phương thức run() của lớp Thread",
      "Chỉ có thể gọi từ luồng chính (main thread)",
      "Bắt buộc phải truyền tham số thời gian timeout"
    ],
    "correctAnswer": 0,
    "explanation": "wait(), notify() và notifyAll() là các phương thức giao tiếp liên luồng thuộc lớp Object. Cơ chế hoạt động của chúng yêu cầu luồng hiện tại phải đang nắm giữ Monitor lock của đối tượng đó. Nếu gọi chúng mà không sở hữu khóa (bên ngoài khối synchronized), JVM sẽ ném ngay java.lang.IllegalMonitorStateException tại runtime.",
    "difficulty": "medium",
    "tags": ["wait-notify", "IllegalMonitorStateException", "Synchronization"]
  },
  {
    "id": "L8_Q09",
    "lessonId": 8,
    "title": "Việc sử dụng Thread Pool (như ExecutorService) giải quyết những nhược điểm lớn nào của việc tự tạo Thread bằng tay (new Thread())?",
    "code": None,
    "options": [
      "Tái sử dụng các luồng có sẵn để tránh chi phí tạo/hủy luồng đắt đỏ của hệ điều hành, đồng thời kiểm soát giới hạn số lượng luồng tối đa để tránh cạn kiệt tài nguyên hệ thống (OutOfMemoryError)",
      "Giúp các luồng tự động không bị lỗi NullPointerException",
      "Tăng tốc độ mạng Internet khi tải dữ liệu",
      "Tự động giải phóng các biến static không dùng"
    ],
    "correctAnswer": 0,
    "explanation": "Trích Đề thi mẫu UET Bài 1 Câu 20: Tự tạo luồng bằng new Thread() tốn kém tài nguyên lớn của OS (cấp phát ~1MB Stack cho mỗi luồng, chi phí ngữ cảnh Context Switching). Nếu tạo hàng ngàn luồng có thể làm crash hệ thống với lỗi OutOfMemoryError. Thread Pool giúp tái sử dụng lại các worker threads và đặt hàng đợi công việc (BlockingQueue) có kiểm soát giới hạn tài nguyên an toàn.",
    "difficulty": "medium",
    "tags": ["ExecutorService", "Thread-Pool", "UET-Exam"]
  },
  {
    "id": "L8_Q10",
    "lessonId": 8,
    "title": "Hành vi của phương thức Future.get() trong Java Concurrency là gì?",
    "code": None,
    "options": [
      "Là phương thức đồng bộ chặn (blocking): nếu tác vụ chưa hoàn thành, luồng gọi nó sẽ bị tạm dừng (chuyển sang WAITING) cho đến khi tác vụ có kết quả hoặc ném ngoại lệ",
      "Luôn trả về kết quả ngay lập tức; nếu chưa xong trả về null",
      "Hủy bỏ tác vụ đang chạy nếu mất hơn 1 giây",
      "Tự động tạo ra một luồng mới để tính toán"
    ],
    "correctAnswer": 0,
    "explanation": "Trích Đề thi mẫu UET Bài 1 Câu 16: Future.get() là lời gọi chặn (blocking call). Nếu công việc tính toán chưa xong, luồng gọi get() sẽ bị block và chuyển vào trạng thái WAITING cho đến khi worker thread hoàn tất phương thức call() và gán kết quả vào Future.",
    "difficulty": "easy",
    "tags": ["Future", "Blocking", "Concurrency", "UET-Exam"]
  },
  {
    "id": "L8_Q11",
    "lessonId": 8,
    "title": "Đoạn mã sau in ra tên luồng thực thi là gì khi gọi phương thức run()?",
    "code": "public class ThreadNameTest {\n    public static void main(String[] args) {\n        Thread t = new Thread(() -> {\n            System.out.println(Thread.currentThread().getName());\n        });\n        t.setName(\"Worker-1\");\n        t.run(); // Luu y goi run() thay vi start()\n    }\n}",
    "options": [
      "main",
      "Worker-1",
      "Thread-0",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Vì gọi t.run() thay vì t.start(), không có luồng mới nào được khởi tạo. Khối lambda bên trong run() được thực thi đồng bộ trên chính luồng hiện tại đang gọi nó, tức là luồng 'main'. Do đó Thread.currentThread().getName() trả về 'main'.",
    "difficulty": "easy",
    "tags": ["Thread-Run", "Thread-Name"]
  },
  {
    "id": "L8_Q12",
    "lessonId": 8,
    "title": "Hiện tượng Tranh chấp điều kiện (Race Condition) trong đoạn mã sau dẫn đến kết quả gì?",
    "code": "class Counter {\n    int count = 0;\n    void increment() { count++; }\n}\npublic class RaceTest {\n    public static void main(String[] args) throws InterruptedException {\n        Counter c = new Counter();\n        Thread t1 = new Thread(() -> { for (int i = 0; i < 1000; i++) c.increment(); });\n        Thread t2 = new Thread(() -> { for (int i = 0; i < 1000; i++) c.increment(); });\n        t1.start(); t2.start();\n        t1.join(); t2.join();\n        System.out.println(c.count);\n    }\n}",
    "options": [
      "Giá trị in ra có thể nhỏ hơn hoặc bằng 2000 (thường < 2000) và không thể đoán trước chính xác do mất mát cập nhật (lost update)",
      "Luôn luôn bằng chính xác 2000 trong mọi lần chạy",
      "Luôn luôn bằng 1000",
      "Chương trình bị deadlock và không bao giờ kết thúc"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức increment() không được đồng bộ hóa (synchronized). Thao tác count++ bao gồm 3 bước: đọc count, tăng 1, ghi lại. Khi 2 luồng chạy đồng thời trên các lõi CPU, chúng có thể đọc cùng một giá trị cũ và ghi đè lẫn nhau (Lost Update). Do đó kết quả thực tế thường nhỏ hơn 2000 và thay đổi tùy mỗi lần chạy.",
    "difficulty": "medium",
    "tags": ["Race-Condition", "Lost-Update", "Synchronization"]
  },
  {
    "id": "L8_Q13",
    "lessonId": 8,
    "title": "Đoạn mã sau sử dụng từ khóa volatile cho biến đếm count. Kết quả in ra có chắc chắn bằng 2000 hay không?",
    "code": "class VolatileCounter {\n    volatile int count = 0;\n    void increment() { count++; }\n}\npublic class VolatileTest {\n    public static void main(String[] args) throws InterruptedException {\n        VolatileCounter c = new VolatileCounter();\n        Thread t1 = new Thread(() -> { for (int i = 0; i < 1000; i++) c.increment(); });\n        Thread t2 = new Thread(() -> { for (int i = 0; i < 1000; i++) c.increment(); });\n        t1.start(); t2.start();\n        t1.join(); t2.join();\n        System.out.println(c.count);\n    }\n}",
    "options": [
      "Không chắc chắn bằng 2000, giá trị vẫn có thể nhỏ hơn 2000 vì volatile không đảm bảo tính nguyên tử cho phép toán count++",
      "Chắc chắn bằng 2000 vì volatile đã đồng bộ hóa toàn diện",
      "Lỗi biên dịch do biến volatile không thể dùng toán tử ++",
      "Luôn luôn bằng 0"
    ],
    "correctAnswer": 0,
    "explanation": "Bẫy rất phổ biến về từ khóa volatile: volatile chỉ đảm bảo tính nhìn thấy (visibility) giá trị mới nhất trong bộ nhớ chính, nhưng count++ là một phép toán phức hợp (compound action) không nguyên tử. Hai luồng vẫn có thể đọc cùng một giá trị đồng thời và ghi đè giá trị tăng, gây thất thoát cập nhật. Để đảm bảo đúng 2000, phải dùng synchronized hoặc AtomicInteger.",
    "difficulty": "hard",
    "tags": ["Volatile", "Non-Atomic", "Compound-Operation"]
  },
  {
    "id": "L8_Q14",
    "lessonId": 8,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi hai luồng cùng chạy?",
    "code": "public class DeadlockDemo {\n    static final Object lockA = new Object();\n    static final Object lockB = new Object();\n    public static void main(String[] args) {\n        Thread t1 = new Thread(() -> {\n            synchronized (lockA) {\n                try { Thread.sleep(50); } catch (Exception e) {}\n                synchronized (lockB) { System.out.println(\"T1 finished\"); }\n            }\n        });\n        Thread t2 = new Thread(() -> {\n            synchronized (lockB) {\n                try { Thread.sleep(50); } catch (Exception e) {}\n                synchronized (lockA) { System.out.println(\"T2 finished\"); }\n            }\n        });\n        t1.start(); t2.start();\n    }\n}",
    "options": [
      "Xảy ra Bế tắc (Deadlock): T1 giữ lockA chờ lockB, trong khi T2 giữ lockB chờ lockA; chương trình bị treo vô hạn",
      "Chương trình in ra 'T1 finished' rồi 'T2 finished' bình thường",
      "Ném ngoại lệ IllegalMonitorStateException tại runtime",
      "Lỗi biên dịch do sleep trong khối synchronized"
    ],
    "correctAnswer": 0,
    "explanation": "Kịch bản Deadlock kinh điển do khóa chéo (Circular Wait): Luồng T1 chiếm lockA rồi ngủ 50ms; trong lúc đó luồng T2 chiếm lockB rồi ngủ 50ms. Khi thức dậy, T1 cố gắng lấy lockB (đang bị T2 giữ) nên bị chặn; T2 cố gắng lấy lockA (đang bị T1 giữ) nên cũng bị chặn. Cả hai luồng chờ đợi lẫn nhau vô hạn tạo thành chu trình bế tắc.",
    "difficulty": "medium",
    "tags": ["Deadlock", "Circular-Wait", "Monitor-Lock"]
  },
  {
    "id": "L8_Q15",
    "lessonId": 8,
    "title": "Đoạn mã sau xảy ra hiện tượng gì khi chạy phương thức doWait()?",
    "code": "public class WaitTest {\n    static Object lock = new Object();\n    public static void main(String[] args) throws InterruptedException {\n        lock.wait(); // Goi wait() truc tiep khong co synchronized\n    }\n}",
    "options": [
      "Ném ngoại lệ IllegalMonitorStateException tại runtime",
      "Luồng main bị tạm dừng vô hạn không lỗi",
      "Lỗi biên dịch do thiếu khối try-catch",
      "Chương trình kết thúc ngay lập tức"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức wait() của Object yêu cầu luồng hiện tại phải đang sở hữu Monitor lock của đối tượng đó trước khi gọi (tức là phải nằm bên trong khối synchronized (lock) { ... }). Do luồng main chưa chiếm lock của biến lock mà đã gọi lock.wait(), JVM lập tức ném: java.lang.IllegalMonitorStateException: current thread is not owner.",
    "difficulty": "medium",
    "tags": ["wait()", "IllegalMonitorStateException", "Monitor-Owner"]
  },
  {
    "id": "L8_Q16",
    "lessonId": 8,
    "title": "Cho đoạn mã trích từ Đề thi mẫu UET Bài 1 (Đoạn code 3). Kết quả in ra là gì?",
    "code": "import java.util.concurrent.*;\nclass DownloadTask implements Callable<String> {\n    private final String file;\n    DownloadTask(String file) { this.file = file; }\n    public String call() throws Exception {\n        Thread.sleep(100);\n        return \"Done:\" + file;\n    }\n}\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        ExecutorService pool = Executors.newFixedThreadPool(2);\n        Future<String> f1 = pool.submit(new DownloadTask(\"A\"));\n        Future<String> f2 = pool.submit(new DownloadTask(\"B\"));\n        System.out.println(f1.get());\n        System.out.println(f2.get());\n        pool.shutdown();\n    }\n}",
    "options": [
      "Done:A\\nDone:B",
      "Done:B\\nDone:A",
      "Lỗi biên dịch tại submit(DownloadTask)",
      "In ra null do Future chưa tính toán xong"
    ],
    "correctAnswer": 0,
    "explanation": "Đề thi mẫu UET Bài 1: Hai tác vụ DownloadTask được gửi vào pool gồm 2 worker threads. f1.get() chặn luồng main chờ tác vụ tải file A hoàn thành và in ra 'Done:A'. Tiếp đó f2.get() lấy kết quả tác vụ tải file B và in ra 'Done:B'. Sau đó pool được đóng bằng shutdown().",
    "difficulty": "easy",
    "tags": ["ExecutorService", "Callable", "Future", "UET-Exam"]
  },
  {
    "id": "L8_Q17",
    "lessonId": 8,
    "title": "Theo Đề thi mẫu UET Câu 19: Điều gì xảy ra nếu gọi liên tiếp hai lần f1.get() trên cùng một đối tượng Future?",
    "code": "Future<String> f1 = pool.submit(new DownloadTask(\"A\"));\nSystem.out.println(f1.get());\nSystem.out.println(f1.get());",
    "options": [
      "Lần gọi get() thứ hai trả về ngay kết quả đã lưu trong bộ đệm (cached result) mà KHÔNG thực thi lại tác vụ DownloadTask",
      "Tác vụ DownloadTask sẽ được đưa vào pool để thực thi lại từ đầu lần thứ hai",
      "Ném ngoại lệ IllegalStateException vì Future chỉ được get() một lần duy nhất",
      "Lần thứ hai trả về null"
    ],
    "correctAnswer": 0,
    "explanation": "Trích Đề thi mẫu UET Bài 1 Câu 19: Đối tượng Future lưu giữ trạng thái kết quả của tác vụ một khi nó đã hoàn thành. Lần gọi f1.get() thứ hai nhận thấy trạng thái tác vụ đã là DONE, do đó nó trả về ngay kết quả tính toán đã có mà không cần chờ đợi và hoàn toàn không chạy lại tác vụ.",
    "difficulty": "medium",
    "tags": ["Future", "Caching", "UET-Exam"]
  },
  {
    "id": "L8_Q18",
    "lessonId": 8,
    "title": "Hai phương thức sau trong cùng một lớp có thể được thực thi đồng thời bởi hai luồng khác nhau hay không? Vì sao?",
    "code": "class SyncDual {\n    public synchronized void methodA() {\n        // Instance synchronized method\n    }\n    public static synchronized void methodB() {\n        // Static synchronized method\n    }\n}",
    "options": [
      "Có thể chạy đồng thời, vì methodA chiếm khóa trên đối tượng thực thể (this), còn methodB chiếm khóa trên đối tượng Class (SyncDual.class)",
      "Không thể chạy đồng thời, vì từ khóa synchronized khóa toàn bộ các phương thức của lớp",
      "Chỉ chạy đồng thời nếu hai phương thức có tham số khác nhau",
      "Lỗi biên dịch: không thể vừa có method synchronized vừa có static synchronized"
    ],
    "correctAnswer": 0,
    "explanation": "Cơ chế khóa của JVM: methodA là instance method nên khi chạy luồng chiếm monitor lock của đối tượng thực thể (this). methodB là static method nên luồng chiếm monitor lock của đối tượng Class (SyncDual.class). Vì hai khóa này là hai thực thể hoàn toàn độc lập trong bộ nhớ Heap, hai luồng có thể thực thi methodA và methodB cùng lúc mà không hề bị chặn nhau.",
    "difficulty": "hard",
    "tags": ["Monitor-Lock", "Instance-vs-Static-Lock"]
  },
  {
    "id": "L8_Q19",
    "lessonId": 8,
    "title": "Phương thức join() trong đoạn mã sau điều khiển thứ tự thực thi như thế nào?",
    "code": "public class JoinTest {\n    public static void main(String[] args) throws InterruptedException {\n        Thread t = new Thread(() -> {\n            try { Thread.sleep(100); } catch (Exception e) {}\n            System.out.print(\"ThreadDone \");\n        });\n        t.start();\n        t.join(); // Main thread cho t ket thuc\n        System.out.print(\"MainDone \");\n    }\n}",
    "options": [
      "ThreadDone MainDone ",
      "MainDone ThreadDone ",
      "In ngẫu nhiên một trong hai thứ tự",
      "Lỗi biên dịch"
    ],
    "correctAnswer": 0,
    "explanation": "Lời gọi t.join() khiến cho luồng hiện tại (luồng main) chuyển sang trạng thái WAITING và tạm dừng thực thi cho tới khi luồng t hoàn thành phương thức run(). Sau khi luồng t in ra 'ThreadDone ' và kết thúc, luồng main mới được đánh thức để in tiếp 'MainDone '. Thứ tự luôn luôn được đảm bảo là: 'ThreadDone MainDone '.",
    "difficulty": "easy",
    "tags": ["Thread-Join", "Execution-Order"]
  },
  {
    "id": "L8_Q20",
    "lessonId": 8,
    "title": "Theo Đề thi mẫu UET Câu 17: Điều gì xảy ra nếu chương trình kết thúc hàm main() mà KHÔNG gọi phương thức pool.shutdown() trên ExecutorService?",
    "code": "public static void main(String[] args) throws Exception {\n    ExecutorService pool = Executors.newFixedThreadPool(2);\n    pool.submit(() -> System.out.println(\"Running...\"));\n    // Khong co pool.shutdown();\n}",
    "options": [
      "Tiến trình JVM vẫn tiếp tục chạy ngầm và không thể kết thúc, vì các worker threads trong pool mặc định là Non-Daemon threads",
      "JVM tự động giải phóng pool và thoát ngay lập tức",
      "JVM ném ngoại lệ ThreadPoolLeakException khi hàm main return",
      "Hệ điều hành sẽ tự động gửi tín hiệu kill process sau 5 giây"
    ],
    "correctAnswer": 0,
    "explanation": "Trích Đề thi mẫu UET Bài 1 Câu 17: JVM chỉ tự động chấm dứt khi tất cả các luồng còn sống đều là Daemon threads. Mặc định, các luồng thợ (worker threads) do Executors.newFixedThreadPool tạo ra là Non-Daemon threads và luôn chờ công việc mới trong hàng đợi. Nếu không gọi pool.shutdown(), các luồng này không bao giờ kết thúc, khiến tiến trình JVM tiếp tục chạy mãi mãi.",
    "difficulty": "hard",
    "tags": ["ExecutorService", "Shutdown", "Non-Daemon-Thread", "UET-Exam"]
  }
]

# ==============================================================================
# LESSON 9: Kiểm thử & Tái cấu trúc (Testing, Refactoring & CI/CD)
# ==============================================================================
lesson9_questions = [
  {
    "id": "L9_Q01",
    "lessonId": 9,
    "title": "Thứ tự phân cấp từ mức thấp nhất đến mức cao nhất của các cấp độ kiểm thử phần mềm (Testing Levels) là gì?",
    "code": None,
    "options": [
      "Unit Testing (Kiểm thử đơn vị) -> Integration Testing (Tích hợp) -> System Testing (Hệ thống) -> Acceptance Testing (Chấp nhận)",
      "Acceptance Testing -> System Testing -> Integration Testing -> Unit Testing",
      "Unit Testing -> System Testing -> Integration Testing -> Regression Testing",
      "White-box Testing -> Black-box Testing -> Grey-box Testing"
    ],
    "correctAnswer": 0,
    "explanation": "Trong kỹ thuật công nghệ phần mềm và slide LTNC, 4 cấp độ kiểm thử chuẩn đi từ nhỏ đến lớn: 1) Unit Test: kiểm thử từng hàm/lớp đơn lẻ; 2) Integration Test: kiểm thử sự tương tác giữa các module; 3) System Test: kiểm thử toàn bộ hệ thống hoàn chỉnh; 4) Acceptance Test: kiểm thử sự chấp nhận của người dùng cuối.",
    "difficulty": "easy",
    "tags": ["Testing-Levels", "Unit-Testing", "Software-Engineering"]
  },
  {
    "id": "L9_Q02",
    "lessonId": 9,
    "title": "Mục tiêu của kỹ thuật kiểm thử Phân hoạch tương đương (Equivalence Partitioning - EP) là gì?",
    "code": None,
    "options": [
      "Chia miền đầu vào của chương trình thành các lớp tương đương (hợp lệ và không hợp lệ), sao cho chỉ cần chọn 1 ca kiểm thử đại diện từ mỗi lớp là đủ để kiểm tra toàn bộ lớp đó",
      "Chỉ tập trung kiểm thử các giá trị cực đại và cực tiểu của miền dữ liệu",
      "Chạy lặp lại ca kiểm thử hàng triệu lần để kiểm tra rò rỉ bộ nhớ",
      "Tự động sinh mã nguồn thay thế cho lập trình viên"
    ],
    "correctAnswer": 0,
    "explanation": "Phân hoạch tương đương (Equivalence Partitioning) là kỹ thuật kiểm thử hộp đen chia miền đầu vào thành các phân hoạch tương đương (valid và invalid partitions). Giả thiết là mọi giá trị trong cùng một lớp phân hoạch đều được hệ thống xử lý tương tự nhau, do đó chỉ cần chọn 1 giá trị đại diện cho mỗi lớp để giảm thiểu số lượng test case mà vẫn đảm bảo độ bao phủ.",
    "difficulty": "easy",
    "tags": ["Equivalence-Partitioning", "Black-box-Testing"]
  },
  {
    "id": "L9_Q03",
    "lessonId": 9,
    "title": "Kỹ thuật Phân tích giá trị biên (Boundary Value Analysis - BVA) dựa trên nguyên lý thực nghiệm nào trong kiểm thử phần mềm?",
    "code": None,
    "options": [
      "Lỗi phần mềm thường tập trung xuất hiện với xác suất cao nhất tại các ranh giới/biên của miền dữ liệu đầu vào (như điều kiện so sánh < thay vì <=, lỗi off-by-one)",
      "Lỗi phần mềm chỉ xuất hiện ở giữa miền dữ liệu",
      "Giá trị biên luôn làm cho chương trình chạy chậm nhất",
      "Các giá trị biên luôn gây ra lỗi tràn bộ nhớ StackOverflowError"
    ],
    "correctAnswer": 0,
    "explanation": "Thực tế kiểm thử phần mềm chỉ ra rằng các lỗi lập trình (đặc biệt là lỗi sai lệch 1 đơn vị - off-by-one, nhầm lẫn giữa < và <=) có xác suất xuất hiện cao nhất tại các ranh giới của các phân hoạch tương đương. Kỹ thuật BVA tập trung chọn các ca kiểm thử: Giá trị cực tiểu (min), ngay trên cực tiểu (min+), giá trị danh định (nom), ngay dưới cực đại (max-), cực đại (max), cùng các giá trị ngoài biên (min-, max+).",
    "difficulty": "medium",
    "tags": ["BVA", "Boundary-Value-Analysis", "Testing-Theory"]
  },
  {
    "id": "L9_Q04",
    "lessonId": 9,
    "title": "Trong JUnit 5, phát biểu nào sau đây phân biệt ĐÚNG về hai annotation @BeforeEach và @BeforeAll?",
    "code": None,
    "options": [
      "@BeforeEach thực thi trước MỖI phương thức kiểm thử @Test; @BeforeAll thực thi DUY NHẤT MỘT LẦN trước toàn bộ các test trong class và bắt buộc phải là phương thức static (mặc định)",
      "@BeforeEach bắt buộc phải là static; @BeforeAll là non-static",
      "@BeforeAll thực thi sau khi tất cả các test kết thúc",
      "Cả @BeforeEach và @BeforeAll đều thực thi trước mỗi phương thức test"
    ],
    "correctAnswer": 0,
    "explanation": "Trong JUnit 5: @BeforeEach chạy trước mỗi phương thức @Test (dùng để khởi tạo lại dữ liệu kiểm thử mới). @BeforeAll chạy một lần duy nhất trước khi bất kỳ phương thức test nào trong class được chạy (thường dùng để mở kết nối database hoặc khởi tạo tài nguyên nặng dùng chung), và mặc định bắt buộc phải khai báo với từ khóa static.",
    "difficulty": "easy",
    "tags": ["JUnit5", "Lifecycle-Annotations"]
  },
  {
    "id": "L9_Q05",
    "lessonId": 9,
    "title": "Mùi mã nguồn 'Feature Envy' (Ghen tị tính năng) được định nghĩa như thế nào theo Martin Fowler?",
    "code": None,
    "options": [
      "Một phương thức của lớp A lại quan tâm và truy cập dữ liệu (thông qua getters/fields) của lớp B nhiều hơn chính dữ liệu của lớp A",
      "Hai lớp có tên gọi và chức năng giống hệt nhau",
      "Một lớp có quá nhiều tính năng mà không sử dụng hết",
      "Một phương thức chứa quá nhiều biến cục bộ"
    ],
    "correctAnswer": 0,
    "explanation": "Slide bài giảng LTNC về Refactoring định nghĩa Feature Envy: Một phương thức dường như quan tâm đến dữ liệu của một đối tượng khác hơn là đối tượng mà nó đang thuộc về (nó liên tục gọi các getter của lớp khác để tính toán). Cách refactoring chuẩn là dùng Move Method để chuyển phương thức đó sang lớp chứa dữ liệu tương ứng.",
    "difficulty": "medium",
    "tags": ["Code-Smells", "Feature-Envy", "Refactoring"]
  },
  {
    "id": "L9_Q06",
    "lessonId": 9,
    "title": "Kỹ thuật tái cấu trúc 'Thay thế điều kiện bằng Đa hình' (Replace Conditional with Polymorphism) nên được áp dụng khi nào?",
    "code": None,
    "options": [
      "Khi có một lệnh switch-case hoặc chuỗi if-else dài thực hiện các hành vi khác nhau dựa trên kiểu của đối tượng hoặc mã loại (type code)",
      "Khi một phương thức quá ngắn chỉ có một dòng lệnh",
      "Khi một lớp không có bất kỳ phương thức nào",
      "Khi cần tăng tốc độ chạy của vòng lặp for"
    ],
    "correctAnswer": 0,
    "explanation": "Slide LTNC chỉ rõ: Khi có các khối lệnh điều kiện phức tạp rẽ nhánh dựa trên kiểu của đối tượng (như switch(employeeType) hoặc if(shape.equals(\"Circle\"))), ta nên tạo các lớp con kế thừa lớp cha chung và chuyển các nhánh điều kiện thành các phương thức ghi đè đa hình. Điều này giúp loại bỏ code smell và tuân thủ OCP.",
    "difficulty": "medium",
    "tags": ["Refactoring", "Polymorphism", "Code-Smell"]
  },
  {
    "id": "L9_Q07",
    "lessonId": 9,
    "title": "Thứ tự các pha chuẩn trong Vòng đời Xây dựng (Build Lifecycle) mặc định của Apache Maven là gì?",
    "code": None,
    "options": [
      "validate -> compile -> test -> package -> verify -> install -> deploy",
      "compile -> test -> validate -> install -> package -> deploy",
      "test -> compile -> package -> verify -> deploy -> install",
      "validate -> package -> compile -> test -> deploy"
    ],
    "correctAnswer": 0,
    "explanation": "Vòng đời Default Lifecycle của Maven tuân theo trình tự nghiêm ngặt: 1) validate (kiểm tra tính hợp lệ của project), 2) compile (biên dịch mã nguồn), 3) test (chạy unit test), 4) package (đóng gói ra JAR/WAR), 5) verify (kiểm tra tính toàn vẹn của gói), 6) install (cài gói vào local repository), 7) deploy (đẩy gói lên remote repository). Khi gọi một pha, Maven tự động chạy toàn bộ các pha trước nó.",
    "difficulty": "medium",
    "tags": ["Maven", "Build-Lifecycle", "DevOps"]
  },
  {
    "id": "L9_Q08",
    "lessonId": 9,
    "title": "Phạm vi phụ thuộc (Dependency Scope) là 'test' trong file pom.xml của Maven có ý nghĩa gì?",
    "code": None,
    "options": [
      "Thư viện chỉ có sẵn trong classpath khi biên dịch và chạy các ca kiểm thử ở thư mục src/test/java; Hoàn toàn không có sẵn trong src/main/java và không được đóng gói vào sản phẩm cuối",
      "Thư viện được đóng gói kèm theo ứng dụng để kiểm thử trên môi trường sản xuất (production)",
      "Thư viện chỉ dùng cho server container cung cấp sẵn tại runtime",
      "Thư viện bị bỏ qua khi chạy lệnh mvn test"
    ],
    "correctAnswer": 0,
    "explanation": "Trong Maven: scope 'test' (ví dụ như JUnit, Mockito) chỉ xuất hiện trong classpath của các tác vụ kiểm thử (src/test/java). Mã nguồn ứng dụng chính (src/main/java) không thể import được thư viện này (gây lỗi biên dịch) và gói JAR thành phẩm sẽ không chứa thư viện đó, giúp tối ưu dung lượng.",
    "difficulty": "easy",
    "tags": ["Maven", "Dependency-Scope", "pom.xml"]
  },
  {
    "id": "L9_Q09",
    "lessonId": 9,
    "title": "Độ phức tạp lặp (Cyclomatic Complexity - McCabe) đo lường điều gì trong mã nguồn phần mềm?",
    "code": None,
    "options": [
      "Số lượng đường đi độc lập tuyến tính qua mã nguồn (Linear Independent Paths), phản ánh độ phức tạp logic và số ca kiểm thử tối thiểu cần thiết để phủ hết các nhánh",
      "Số lượng dòng mã (Lines of Code) của toàn bộ project",
      "Thời gian thực thi trung bình tính bằng mili giây của một hàm",
      "Số lượng biến toàn cục được khai báo trong chương trình"
    ],
    "correctAnswer": 0,
    "explanation": "Cyclomatic Complexity là một chỉ số đo lường định lượng cấu trúc điều khiển của chương trình dựa trên đồ thị dòng điều khiển: M = E - N + 2P (hoặc đơn giản là Số điểm quyết định if, while, for, case + 1). Điểm số này cho biết số ca kiểm thử tối thiểu cần có để bao phủ toàn bộ các nhánh logic của phương thức. Chỉ số > 10 thường bị Checkstyle cảnh báo là nguy cơ lỗi cao.",
    "difficulty": "medium",
    "tags": ["Cyclomatic-Complexity", "Checkstyle", "Code-Quality"]
  },
  {
    "id": "L9_Q10",
    "lessonId": 9,
    "title": "Vì sao cơ chế ghi log tham số hóa (Parameterized Logging) trong SLF4J (ví dụ: logger.debug(\"User {}\", name)) lại vượt trội hơn phép nối chuỗi (System.out.println(\"User \" + name))?",
    "code": None,
    "options": [
      "Tránh lãng phí tài nguyên CPU và bộ nhớ để thực hiện nối chuỗi String khi mức log DEBUG đang bị tắt",
      "Cho phép ghi log ra file nhanh gấp 100 lần",
      "Tự động mã hóa thông tin người dùng",
      "Bắt buộc log phải được lưu vào cơ sở dữ liệu"
    ],
    "correctAnswer": 0,
    "explanation": "Slide LTNC về Logging Strategy: Nếu dùng phép cộng chuỗi 'User ' + name, JVM luôn luôn phải cấp phát bộ nhớ StringBuilder để nối chuỗi ngay cả khi mức log DEBUG đang bị tắt trong cấu hình Logback. Với Parameterized logging (logger.debug(\"User {}\", name)), SLF4J chỉ kiểm tra mức log trước; nếu DEBUG tắt, hàm return ngay lập tức mà không tốn chi phí định dạng chuỗi.",
    "difficulty": "medium",
    "tags": ["Logging", "SLF4J", "Performance"]
  },
  {
    "id": "L9_Q11",
    "lessonId": 9,
    "title": "Đoạn mã kiểm thử JUnit 5 sau xảy ra hiện tượng gì khi chạy?",
    "code": "import org.junit.jupiter.api.*;\npublic class LifecycleTest {\n    @BeforeAll\n    void initAll() { // Luu y: khong co tu khoa static\n        System.out.println(\"Init\");\n    }\n    @Test\n    void sampleTest() {\n        Assertions.assertTrue(true);\n    }\n}",
    "options": [
      "Báo lỗi JUnitException tại runtime: phương thức @BeforeAll bắt buộc phải là static (khi dùng vòng đời mặc định PER_METHOD)",
      "Chương trình chạy bình thường và in ra 'Init'",
      "Lỗi biên dịch tại dòng @BeforeAll",
      "Bỏ qua phương thức initAll() và chỉ chạy sampleTest()"
    ],
    "correctAnswer": 0,
    "explanation": "Trong JUnit 5, mặc định chế độ vòng đời kiểm thử là PER_METHOD (mỗi test case tạo một thể hiện mới của class test). Do đó phương thức @BeforeAll và @AfterAll bắt buộc phải được khai báo với từ khóa static. Nếu khai báo non-static, JUnit 5 sẽ ném ngoại lệ org.junit.platform.commons.JUnitException: @BeforeAll method must be static unless Lifecycle.PER_CLASS is used.",
    "difficulty": "hard",
    "tags": ["JUnit5", "BeforeAll", "Static-Requirement"]
  },
  {
    "id": "L9_Q12",
    "lessonId": 9,
    "title": "Đoạn mã sau sử dụng assertion của JUnit 5 để kiểm tra ngoại lệ. Kết quả là gì?",
    "code": "import org.junit.jupiter.api.Assertions;\npublic class AssertExceptionTest {\n    static int divide(int a, int b) {\n        return a / b;\n    }\n    public static void main(String[] args) {\n        ArithmeticException ex = Assertions.assertThrows(\n            ArithmeticException.class,\n            () -> divide(10, 0)\n        );\n        System.out.println(ex.getMessage());\n    }\n}",
    "options": [
      "/ by zero",
      "ArithmeticException",
      "Ném ngoại lệ AssertionFailedError do phép chia thất bại",
      "Lỗi biên dịch tại lambda expression"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức Assertions.assertThrows mong đợi đoạn code trong lambda ném ra đúng ngoại lệ ArithmeticException. Khi gọi divide(10, 0), JVM ném ArithmeticException: / by zero. assertThrows bắt lấy ngoại lệ này thành công và trả về instance của ngoại lệ đó. Lệnh in ex.getMessage() in ra thông điệp chuẩn của JVM là '/ by zero'.",
    "difficulty": "medium",
    "tags": ["JUnit5", "assertThrows", "Exception-Testing"]
  },
  {
    "id": "L9_Q13",
    "lessonId": 9,
    "title": "Theo kỹ thuật Phân tích giá trị biên (BVA) cho quy tắc mượn sách trong Đề thi mẫu UET Bài 3: 'Người dùng được mượn sách nếu borrowedBooks < 5 và dữ liệu hợp lệ khi borrowedBooks >= 0'. Bộ giá trị biên cần kiểm thử cho borrowedBooks là gì?",
    "code": "// boolean canBorrow(int borrowedBooks, boolean hasOverdue, int membershipLevel)\n// Dieu kien: 0 <= borrowedBooks < 5 (hop le)\n// borrowedBooks < 0: khong hop le",
    "options": [
      "-1, 0, 1 (biên dưới) và 4, 5, 6 (biên trên)",
      "Chỉ cần kiểm tra số 0 và số 5",
      "Chỉ cần kiểm tra số 1, 2, 3, 4",
      "-10, 0, 10"
    ],
    "correctAnswer": 0,
    "explanation": "Trích Đề thi mẫu UET Bài 3: Miền giá trị cho borrowedBooks có biên dưới là 0 (điểm chia giữa không hợp lệ < 0 và hợp lệ >= 0), các giá trị biên cần xét là: -1 (ngoài biên dưới), 0 (biên dưới), 1 (ngay trên biên dưới). Ranh giới mượn được là < 5 (tức <= 4), các giá trị biên trên cần xét là: 4 (biên trên được mượn), 5 (biên không được mượn), 6 (ngay ngoài biên). Bộ giá trị biên chuẩn là: {-1, 0, 1, 4, 5, 6}.",
    "difficulty": "medium",
    "tags": ["BVA", "Boundary-Testing", "UET-Exam"]
  },
  {
    "id": "L9_Q14",
    "lessonId": 9,
    "title": "Phương thức sau đây mắc phải Mùi mã nguồn (Code Smell) nào?",
    "code": "class OrderReceipt {\n    void printCustomerAddress(Customer customer) {\n        String street = customer.getAddress().getStreet();\n        String city = customer.getAddress().getCity();\n        String zip = customer.getAddress().getZipCode();\n        System.out.println(street + \", \" + city + \" \" + zip);\n    }\n}",
    "options": [
      "Feature Envy (Ghen tị tính năng) kết hợp với Inappropriate Intimacy (Thân mật thái quá): phương thức thuộc lớp OrderReceipt nhưng chỉ toàn thao tác truy xuất dữ liệu nội bộ của lớp Customer/Address",
      "Dead Code: mã nguồn không bao giờ được gọi",
      "Lazy Class: lớp không thực hiện chức năng gì",
      "Speculative Generality: khái quát hóa suy đoán"
    ],
    "correctAnswer": 0,
    "explanation": "Phương thức printCustomerAddress nằm trong OrderReceipt nhưng không hề dùng bất kỳ trường nào của OrderReceipt, mà liên tục truy cập dữ liệu sâu của Customer và Address (vi phạm cả Luật Demeter - Law of Demeter). Đây là biểu hiện điển hình của Code Smell 'Feature Envy'. Nên chuyển phương thức này sang lớp Address hoặc Customer bằng kỹ thuật Move Method.",
    "difficulty": "medium",
    "tags": ["Code-Smells", "Feature-Envy", "Law-of-Demeter"]
  },
  {
    "id": "L9_Q15",
    "lessonId": 9,
    "title": "Đoạn mã sau được tái cấu trúc từ cấu trúc if-else sang kế thừa. Kỹ thuật tái cấu trúc này có tên là gì?",
    "code": "// Truoc khi refactor: if (type == BIRD) fly(); else if (type == DOG) bark();\n// Sau khi refactor:\nabstract class Animal { abstract void makeSound(); }\nclass Dog extends Animal { void makeSound() { System.out.println(\"Gau\"); } }\nclass Bird extends Animal { void makeSound() { System.out.println(\"Hot\"); } }",
    "options": [
      "Replace Conditional with Polymorphism (Thay thế câu lệnh điều kiện bằng Đa hình)",
      "Extract Method (Trích xuất phương thức)",
      "Inline Class (Nội suy lớp)",
      "Pull Up Field (Kéo thuộc tính lên lớp cha)"
    ],
    "correctAnswer": 0,
    "explanation": "Đây là mẫu tái cấu trúc kinh điển 'Replace Conditional with Polymorphism' (Martin Fowler). Các nhánh rẽ if-else hoặc switch-case kiểm tra cờ loại đối tượng được thay thế bằng các lớp con đa hình kế thừa từ lớp cha chung, cho phép hệ thống mở rộng loài vật mới mà không cần chỉnh sửa code cũ.",
    "difficulty": "easy",
    "tags": ["Refactoring", "Replace-Conditional-with-Polymorphism"]
  },
  {
    "id": "L9_Q16",
    "lessonId": 9,
    "title": "Khi một lập trình viên thực hiện câu lệnh 'mvn test' trong một dự án Apache Maven, những pha (phases) nào sẽ được tự động thực thi?",
    "code": "// Console terminal:\n// $ mvn test",
    "options": [
      "Các pha validate, compile, và test sẽ lần lượt được thực thi theo thứ tự",
      "Chỉ duy nhất pha test được thực thi",
      "Tất cả các pha bao gồm cả package, install và deploy",
      "Pha compile và deploy"
    ],
    "correctAnswer": 0,
    "explanation": "Quy tắc Maven Lifecycle: Khi bạn gọi một pha cụ thể (như test), Maven sẽ tự động chạy tuần tự TẤT CẢ các pha đứng trước nó trong cùng một build lifecycle trước khi chạy pha đó. Trong default lifecycle, validate và compile đứng trước test, do đó Maven sẽ validate project -> compile mã nguồn -> rồi mới chạy test.",
    "difficulty": "medium",
    "tags": ["Maven", "Build-Phases", "Automation"]
  },
  {
    "id": "L9_Q17",
    "lessonId": 9,
    "title": "Đoạn mã sau nằm trong tệp 'src/main/java/App.java'. Điều gì xảy ra khi dự án có thư viện JUnit khai báo với scope là 'test' trong pom.xml?",
    "code": "// Tep: src/main/java/App.java\nimport org.junit.jupiter.api.Assertions; // Dong nay\n\npublic class App {\n    public static void main(String[] args) {\n        Assertions.assertEquals(1, 1);\n    }\n}",
    "options": [
      "Lỗi biên dịch: Package org.junit.jupiter.api does not exist, vì dependency có scope 'test' không xuất hiện trong classpath của src/main/java",
      "Biên dịch thành công và chạy bình thường",
      "Biên dịch được nhưng ném NoClassDefFoundError khi chạy",
      "Maven tự động đổi scope thành compile"
    ],
    "correctAnswer": 0,
    "explanation": "Trong cấu trúc chuẩn của Maven, thư viện có scope 'test' chỉ được đưa vào classpath khi biên dịch thư mục kiểm thử 'src/test/java'. Thư mục mã nguồn chính 'src/main/java' hoàn toàn không nhìn thấy các thư viện test scope, do đó việc import org.junit.* trong src/main/java sẽ bị trình biên dịch javac báo lỗi: 'package org.junit.jupiter.api does not exist'.",
    "difficulty": "hard",
    "tags": ["Maven", "Dependency-Scope", "Compile-Error"]
  },
  {
    "id": "L9_Q18",
    "lessonId": 9,
    "title": "Tính Độ phức tạp lặp (Cyclomatic Complexity) của phương thức sau:",
    "code": "public int process(int a, int b) {\n    int result = 0;\n    if (a > 0) { // Diem quyet dinh 1\n        result += a;\n    }\n    if (b > 0) { // Diem quyet dinh 2\n        result += b;\n    }\n    for (int i = 0; i < a; i++) { // Diem quyet dinh 3\n        result++;\n    }\n    return result;\n}",
    "options": [
      "4",
      "3",
      "2",
      "5"
    ],
    "correctAnswer": 0,
    "explanation": "Công thức tính Cyclomatic Complexity nhanh: M = Số điểm quyết định (Decision Points: if, while, for, case, &&, ||) + 1. Trong hàm có: 1 câu lệnh if (a > 0), 1 câu lệnh if (b > 0), 1 vòng lặp for (i < a). Tổng cộng có 3 điểm quyết định. Độ phức tạp Cyclomatic = 3 + 1 = 4.",
    "difficulty": "medium",
    "tags": ["Cyclomatic-Complexity", "Code-Metrics"]
  },
  {
    "id": "L9_Q19",
    "lessonId": 9,
    "title": "Bẫy chi phí đánh giá tham số trong SLF4J! Phương thức nặng tính toán sau có được thực thi hay không khi mức log DEBUG bị tắt?",
    "code": "public class LoggingTrap {\n    static String getExpensiveDetails() {\n        System.out.print(\"Expensive \");\n        return \"detail_info\";\n    }\n    public static void main(String[] args) {\n        // Gia su muc log cua logger dang la INFO (DEBUG bi tat)\n        org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(LoggingTrap.class);\n        logger.debug(\"Data: {}\", getExpensiveDetails());\n    }\n}",
    "options": [
      "Có được thực thi và in ra 'Expensive ', vì theo ngữ nghĩa ngôn ngữ Java, đối số getExpensiveDetails() bắt buộc phải được tính toán trước khi truyền vào phương thức",
      "Không được thực thi vì SLF4J tự động bỏ qua",
      "Lỗi biên dịch do truyền hàm vào log",
      "Chỉ thực thi nếu dùng System.out.println"
    ],
    "correctAnswer": 0,
    "explanation": "Một cạm bẫy hiệu năng rất tinh tế: Trong Java, trước khi một phương thức được gọi, tất cả các biểu thức đối số của nó BẮT BUỘC phải được tính toán giá trị (eager evaluation). Lệnh getExpensiveDetails() sẽ chạy và in ra 'Expensive ' trước khi được truyền vào hàm debug. Dù sau đó logger.debug thấy mức DEBUG bị tắt và không ghi log ra file, chi phí tính toán của getExpensiveDetails() đã bị lãng phí. Cách khắc phục chuẩn là kiểm tra 'if (logger.isDebugEnabled())' hoặc dùng Supplier trong Java 8.",
    "difficulty": "hard",
    "tags": ["SLF4J", "Eager-Evaluation", "Performance-Trap"]
  },
  {
    "id": "L9_Q20",
    "lessonId": 9,
    "title": "Trong tệp cấu hình CI/CD GitHub Actions (.github/workflows/maven.yml), bước nào sau đây BẮT BUỘC phải thực hiện trước khi chạy lệnh biên dịch 'mvn package'?",
    "code": "name: Java CI with Maven\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n    # Buoc can thiet nhat o day la gi?\n    - name: Build with Maven\n      run: mvn clean package",
    "options": [
      "Sử dụng action 'actions/checkout@v4' để clone mã nguồn của repository về máy ảo runner",
      "Cài đặt trình duyệt Google Chrome",
      "Cấu hình tài khoản Docker Hub",
      "Chạy lệnh git push origin master"
    ],
    "correctAnswer": 0,
    "explanation": "Trong GitHub Actions, máy ảo runner (ubuntu-latest) khi mới khởi tạo là một môi trường sạch hoàn toàn chưa có mã nguồn dự án. Nếu không có bước '- uses: actions/checkout@v4', runner sẽ không có bất kỳ tệp tin nào (không có pom.xml, không có src/), dẫn tới lệnh 'mvn clean package' lập tức báo lỗi: 'The goal you specified requires a project to execute but there is no POM in this directory'.",
    "difficulty": "medium",
    "tags": ["GitHub-Actions", "CI-CD", "DevOps"]
  }
]

def save(lesson_id, data):
    p = os.path.join(OUTPUT_DIR, f"lesson{lesson_id}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Lesson {lesson_id}: {len(data)} questions saved.")

save(7, lesson7_questions)
save(8, lesson8_questions)
save(9, lesson9_questions)
