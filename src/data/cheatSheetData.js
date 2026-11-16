export const CHEAT_SHEETS = [
  {
    id: "access-modifiers",
    title: "1. Bảng Đặc tả Truy cập (Access Modifiers)",
    category: "Cơ bản Java",
    description: "Phạm vi truy cập của biến, phương thức và lớp trong Java.",
    content: {
      type: "table",
      headers: ["Modifier", "Cùng Class", "Cùng Package", "Subclass (khác pkg)", "Bên ngoài (World)"],
      rows: [
        ["public", " Có", " Có", " Có", " Có"],
        ["protected", " Có", " Có", " Có (qua kế thừa)", " Không"],
        ["default (no modifier)", " Có", " Có", " Không", " Không"],
        ["private", " Có", " Không", " Không", " Không"]
      ],
      notes: [
        "Lớp cấp cao (Top-level class) chỉ có thể là public hoặc default (không được private hay protected).",
        "Phương thức trong Interface: mặc định là public abstract (trừ default method và static method giới thiệu từ Java 8, private method từ Java 9).",
        "Quy tắc Overriding: Lớp con không được phép thu hẹp quyền truy cập của phương thức lớp cha (ví dụ cha là public thì con bắt buộc phải là public)."
      ]
    }
  },
  {
    id: "exception-hierarchy",
    title: "2. Cây phân cấp Ngoại lệ & Khối Finally",
    category: "Exception & I/O",
    description: "Phân biệt Checked Exception và Unchecked Exception (Runtime) trong JVM.",
    content: {
      type: "tree-and-rules",
      diagram: `
Throwable
├── Error (OutOfMemoryError, StackOverflowError - Hệ thống nghiêm trọng, không thể phục hồi)
└── Exception
    ├── RuntimeException (Unchecked Exception - Lỗi logic lập trình, không bắt buộc try-catch)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   ├── ArithmeticException
    │   ├── ClassCastException
    │   └── IllegalArgumentException
    └── Checked Exceptions (Ngoại cảnh, bắt buộc phải try-catch hoặc throws)
        ├── IOException (FileNotFoundException)
        ├── SQLException
        └── ClassNotFoundException
      `,
      rules: [
        {
          title: "Quy tắc Checked vs Unchecked",
          text: "Checked Exception kế thừa trực tiếp từ Exception (ngoại trừ RuntimeException). Trình biên dịch bắt buộc phải xử lý bằng try-catch hoặc khai báo throws ở chữ ký phương thức."
        },
        {
          title: "Khối finally luôn thực thi & Bẫy return",
          text: "Khối finally luôn được chạy ngay cả khi có lệnh 'return' trong khối try/catch! Nếu finally có lệnh return hoặc ném exception mới, nó sẽ ghi đè và nuốt chửng hoàn toàn return/exception của try/catch."
        },
        {
          title: "Try-with-resources (Java 7+)",
          text: "Các đối tượng triển khai java.lang.AutoCloseable sẽ tự động được đóng theo thứ tự ngược lại với thứ tự khai báo (LIFO). Ngoại lệ từ close() được đính kèm vào e.getSuppressed()."
        }
      ]
    }
  },
  {
    id: "generics-pecs",
    title: "3. Nguyên lý Generics & Nguyên tắc PECS",
    category: "Generics",
    description: "Hiểu sâu về Wildcard và quy tắc Producer Extends - Consumer Super của Joshua Bloch.",
    content: {
      type: "pecs-guide",
      mnemonic: "PECS: Producer Extends, Consumer Super",
      rules: [
        {
          keyword: "? extends T (Upper Bounded)",
          role: "PRODUCER (Chỉ đọc ra)",
          explanation: "Bộ sưu tập đóng vai trò cung cấp dữ liệu loại T. Bạn CÓ THỂ đọc ra phần tử kiểu T, nhưng KHÔNG THỂ thêm bất kỳ phần tử nào vào (ngoại trừ null) vì không chắc chắn kiểu con cụ thể.",
          code: "List<? extends Number> list = new ArrayList<Integer>();\nNumber n = list.get(0); // OK (Read safe)\n// list.add(10);        // COMPILE ERROR!"
        },
        {
          keyword: "? super T (Lower Bounded)",
          role: "CONSUMER (Chỉ ghi vào)",
          explanation: "Bộ sưu tập đóng vai trò tiêu thụ/tiếp nhận dữ liệu. Bạn CÓ THỂ thêm các đối tượng kiểu T (hoặc con của T) vào, nhưng khi đọc ra chỉ nhận được kiểu Object.",
          code: "List<? super Integer> list = new ArrayList<Number>();\nlist.add(100);          // OK (Write safe)\nObject o = list.get(0); // OK (chỉ an toàn với Object)\n// Integer x = list.get(0); // COMPILE ERROR!"
        }
      ],
      invarianceNotice: "List<String> KHÔNG PHẢI là kiểu con của List<Object> (Invariance), mặc dù String là con của Object!"
    }
  },
  {
    id: "collections-comparison",
    title: "4. So sánh Java Collections Framework & Hợp đồng Hash",
    category: "Cấu trúc dữ liệu",
    description: "Đặc tả tính chất lưu trữ, thứ tự, trùng lặp và độ phức tạp.",
    content: {
      type: "table",
      headers: ["Interface / Class", "Trùng lặp (Duplicate)", "Thứ tự sắp xếp", "Cho phép Null", "Cấu trúc ngầm định"],
      rows: [
        ["ArrayList", " Có", "Thứ tự chèn (Insertion)", " Có", "Mảng động O(1) get, O(n) insert/remove"],
        ["LinkedList", " Có", "Thứ tự chèn", " Có", "Danh sách liên kết đôi O(n) get, O(1) add/remove"],
        ["HashSet", " Không", "Không có thứ tự", " Có (1 phần tử)", "Bảng băm HashMap O(1) trung bình"],
        ["TreeSet", " Không", "Sắp xếp tự nhiên (Sorted/Comparator)", " Không (ném NPE)", "Cây Đỏ-Đen O(log n)"],
        ["HashMap", "Key: Không, Val: Có", "Không có thứ tự", "Key: 1 null, Val: nhiều", "Mảng Bucket + LinkedList / Red-Black Tree"],
        ["TreeMap", "Key: Không, Val: Có", "Key được sắp xếp", "Key: Không, Val: nhiều", "Cây Đỏ-Đen O(log n)"]
      ],
      notes: [
        "Hợp đồng equals() và hashCode(): Nếu hai đối tượng bằng nhau qua equals(), hashCode() của chúng BẮT BUỘC phải bằng nhau. Nếu vi phạm, HashSet/HashMap sẽ lưu trùng hoặc get() trả về null!",
        "Nếu hashCode() bằng nhau, hai đối tượng KHÔNG NHẤT THIẾT phải bằng nhau (xảy ra xung đột hash collision được giải quyết bằng Separate Chaining).",
        "Key của HashMap nên là bất biến (Immutable như String, Integer) để tránh thay đổi hashCode sau khi chèn."
      ]
    }
  },
  {
    id: "thread-lifecycle",
    title: "5. Vòng đời Thread & An toàn Đa luồng (Multithreading)",
    category: "Đa luồng",
    description: "Trạng thái luồng, Monitor Lock và nguyên lý tránh Deadlock.",
    content: {
      type: "thread-guide",
      states: [
        { state: "NEW", desc: "Thread được khởi tạo nhưng chưa gọi .start()" },
        { state: "RUNNABLE", desc: "Đang chạy hoặc sẵn sàng chạy trên CPU do OS lập lịch" },
        { state: "BLOCKED", desc: "Chờ lấy khóa monitor lock (synchronized block/method)" },
        { state: "WAITING", desc: "Chờ vô hạn đến khi có notify()/notifyAll() (gọi wait(), join())" },
        { state: "TIMED_WAITING", desc: "Chờ có thời hạn (sleep(ms), wait(ms), join(ms))" },
        { state: "TERMINATED", desc: "Đã hoàn thành phương thức run() hoặc ném ngoại lệ không xử lý" }
      ],
      goldenRules: [
        "Gọi run() thay vì start() sẽ chạy trên chính Thread hiện tại, KHÔNG tạo luồng mới!",
        "volatile đảm bảo tính nhìn thấy (visibility) giữa các CPU Cache, nhưng KHÔNG đảm bảo tính nguyên tử (atomicity) cho phép toán compound như count++.",
        "Deadlock xảy ra khi thỏa mãn 4 điều kiện Coffman: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait. Khắc phục bằng cách luôn chiếm khóa theo thứ tự cố định.",
        "wait(), notify(), notifyAll() bắt buộc phải được gọi bên trong khối synchronized trên cùng monitor object, nếu không sẽ ném IllegalMonitorStateException."
      ]
    }
  },
  {
    id: "solid-design-patterns",
    title: "6. Nguyên lý SOLID & Mẫu Thiết Kế Trọng Tâm",
    category: "Kiến trúc & Mẫu thiết kế",
    description: "Các nguyên lý thiết kế hướng đối tượng và mẫu thiết kế cốt lõi trong đề thi LTNC.",
    content: {
      type: "patterns-guide",
      solid: [
        { letter: "S", name: "Single Responsibility", desc: "Một lớp chỉ nên có một lý do duy nhất để thay đổi." },
        { letter: "O", name: "Open/Closed Principle", desc: "Mở để mở rộng (Open for extension), đóng để chỉnh sửa (Closed for modification)." },
        { letter: "L", name: "Liskov Substitution", desc: "Đối tượng lớp con có thể thay thế lớp cha mà không làm hỏng tính đúng đắn của chương trình." },
        { letter: "I", name: "Interface Segregation", desc: "Nhiều interface đặc tả tốt hơn một interface khổng lồ đa năng." },
        { letter: "D", name: "Dependency Inversion", desc: "Phụ thuộc vào trừu tượng (Interface/Abstract), không phụ thuộc vào triển khai cụ thể (Concrete)." }
      ],
      patterns: [
        {
          name: "Singleton Pattern",
          type: "Creational",
          purpose: "Đảm bảo một lớp chỉ có đúng một instance duy nhất và cung cấp điểm truy cập toàn cục. Double-checked locking đòi hỏi từ khóa volatile để tránh reordering.",
          code: `public class Singleton {\n    private static volatile Singleton instance;\n    private Singleton() {}\n    public static Singleton getInstance() {\n        if (instance == null) {\n            synchronized (Singleton.class) {\n                if (instance == null) instance = new Singleton();\n            }\n        }\n        return instance;\n    }\n}`
        },
        {
          name: "Factory Method Pattern",
          type: "Creational",
          purpose: "Định nghĩa interface để tạo đối tượng, để các lớp con quyết định lớp nào được khởi tạo (loose coupling)."
        },
        {
          name: "Strategy Pattern",
          type: "Behavioral",
          purpose: "Đóng gói họ các thuật toán thành các lớp riêng biệt để chúng có thể tráo đổi cho nhau khi đang chạy, loại bỏ chuỗi if-else/switch phức tạp."
        },
        {
          name: "Observer Pattern",
          type: "Behavioral",
          purpose: "Mối quan hệ 1-nhiều: khi trạng thái của Subject thay đổi, tất cả Observers tự động được thông báo và cập nhật."
        },
        {
          name: "Decorator Pattern",
          type: "Structural",
          purpose: "Gắn thêm trách nhiệm động cho đối tượng mà không cần can thiệp vào mã nguồn gốc hoặc dùng kế thừa lồng nhau."
        },
        {
          name: "Composite Pattern",
          type: "Structural",
          purpose: "Tạo cấu trúc cây, đối xử đồng nhất giữa đối tượng đơn lẻ (Leaf) và nhóm đối tượng (Composite), giải quyết smell kiểm tra instanceof giữa lá và thư mục."
        }
      ]
    }
  },
  {
    id: "testing-bva",
    title: "7. Kiểm thử Phần mềm & Phân tích Giá trị Biên (BVA)",
    category: "Kiểm thử & Chất lượng",
    description: "Kỹ thuật thiết kế ca kiểm thử hộp đen và kiểm thử đơn vị với JUnit 5.",
    content: {
      type: "testing-guide",
      concepts: [
        {
          name: "Equivalence Partitioning (EP)",
          desc: "Chia miền đầu vào thành các lớp tương đương: các phân hoạch hợp lệ (Valid) và không hợp lệ (Invalid). Chọn 1 ca kiểm thử đại diện cho mỗi phân hoạch."
        },
        {
          name: "Boundary Value Analysis (BVA)",
          desc: "Kiểm thử tại các biên ranh giới: {min-, min, min+, nom, max-, max, max+}. Các lỗi lập trình (off-by-one, nhầm < với <=) có xác suất xuất hiện cao nhất tại các điểm này."
        }
      ],
      junit5Annotations: [
        { tag: "@Test", desc: "Đánh dấu phương thức là một ca kiểm thử đơn vị" },
        { tag: "@BeforeEach / @AfterEach", desc: "Chạy trước / sau mỗi phương thức @Test" },
        { tag: "@BeforeAll / @AfterAll", desc: "Chạy một lần duy nhất trước / sau toàn bộ test class (bắt buộc phải là static)" },
        { tag: "assertThrows", desc: "Kiểm tra phương thức có ném đúng ngoại lệ mong đợi hay không" }
      ]
    }
  },
  {
    id: "code-smells-refactoring",
    title: "8. Mùi Mã Nguồn (Code Smells) & Kỹ thuật Tái cấu trúc",
    category: "Tái cấu trúc mã nguồn",
    description: "Nhận diện các vấn đề thiết kế mã nguồn theo Martin Fowler và các phương pháp chuẩn hóa.",
    content: {
      type: "refactoring-guide",
      smells: [
        { smell: "Long Method", solution: "Extract Method: Chia nhỏ phương thức dài thành các phương thức con mang tính mô tả cao." },
        { smell: "Long Parameter List", solution: "Introduce Parameter Object: Đóng gói các tham số thành một đối tượng DTO." },
        { smell: "Feature Envy", solution: "Move Method: Phương thức truy cập quá nhiều dữ liệu của lớp khác thì nên chuyển nó về lớp chứa dữ liệu đó." },
        { smell: "Switch Statements / Complex If-Else", solution: "Replace Conditional with Polymorphism hoặc Strategy Pattern." },
        { smell: "Distinguishing Leaf vs Container", solution: "Áp dụng Composite Pattern với interface Component dùng chung." }
      ]
    }
  },
  {
    id: "maven-cicd",
    title: "9. Apache Maven & Tự động hóa CI/CD",
    category: "Triển khai & DevOps",
    description: "Vòng đời Maven Build, quản lý phụ thuộc và quy trình GitHub Actions.",
    content: {
      type: "devops-guide",
      mavenPhases: [
        { phase: "validate", desc: "Xác thực cấu trúc và tính hợp lệ của project" },
        { phase: "compile", desc: "Biên dịch mã nguồn từ src/main/java sang target/classes" },
        { phase: "test", desc: "Chạy các ca kiểm thử unit test bằng Surefire Plugin" },
        { phase: "package", desc: "Đóng gói mã đã biên dịch ra định dạng JAR hoặc WAR" },
        { phase: "verify", desc: "Chạy integration tests và kiểm tra chất lượng code" },
        { phase: "install", desc: "Cài đặt gói thành phẩm vào Local Repository (~/.m2)" },
        { phase: "deploy", desc: "Sao chép gói thành phẩm lên Remote Repository (Nexus/Artifactory)" }
      ],
      scopes: [
        { scope: "compile", desc: "Mặc định, có sẵn ở mọi classpath (src/main, src/test, runtime JAR)" },
        { scope: "provided", desc: "Dùng khi biên dịch và test, giả định container môi trường chạy sẽ cung cấp (vd: servlet-api)" },
        { scope: "runtime", desc: "Chỉ cần khi chạy ứng dụng và test, không cần lúc compile (vd: JDBC Driver)" },
        { scope: "test", desc: "Chỉ có sẵn khi biên dịch và chạy src/test/java, src/main không thể import (vd: JUnit, Mockito)" }
      ],
      cicdNotice: "Trong GitHub Actions, máy ảo runner là môi trường sạch. BẮT BUỘC phải có bước 'actions/checkout@v4' để clone mã nguồn trước khi thực thi bất kỳ lệnh Maven nào."
    }
  }
];
