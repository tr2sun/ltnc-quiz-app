export const LESSONS_METADATA = [
  {
    id: 1,
    title: "Bài 1 & 2: Cơ bản Java & OOP",
    subtitle: "Stack vs Heap, GC, Static, Final, Access Modifiers, Constructor chaining",
    description: "Nắm vững cơ chế bộ nhớ JVM, Garbage Collector, vòng đời biến, nạp chồng constructor, cơ chế chaining và các từ khóa đặc tả truy cập.",
    icon: "Cpu",
    badge: "Nền tảng",
    color: "from-blue-500 to-indigo-600",
    tags: ["JVM", "Stack-Heap", "Static", "GC", "Modifiers", "Constructor"]
  },
  {
    id: 3,
    title: "Bài 3: Thừa kế & Đa hình",
    subtitle: "Inheritance, Polymorphism, Dynamic Binding, Static Hiding, Casting",
    description: "Cơ chế liên kết động (Dynamic binding), ép kiểu Upcasting/Downcasting, phân biệt che giấu phương thức static (Static hiding) và ghi đè (Override).",
    icon: "Layers",
    badge: "Cốt lõi",
    color: "from-indigo-500 to-purple-600",
    tags: ["Inheritance", "Polymorphism", "DynamicBinding", "Hiding", "Downcasting"]
  },
  {
    id: 4,
    title: "Bài 4: Interface & Generics",
    subtitle: "Abstract Class, Interface, Default Methods, Generics, PECS",
    description: "Thiết kế trừu tượng hóa, phương thức default/static/private trong interface, cơ chế xóa kiểu (Type Erasure) và nguyên lý PECS (? extends / ? super).",
    icon: "Boxes",
    badge: "Kiến trúc",
    color: "from-purple-500 to-pink-600",
    tags: ["Abstract", "Interface", "Generics", "PECS", "TypeErasure"]
  },
  {
    id: 5,
    title: "Bài 5: Collections, Exception & I/O",
    subtitle: "List, Set, Map, equals & hashCode, Exceptions, I/O Streams, Serialization",
    description: "Cấu trúc dữ liệu Java, hợp đồng bất biến giữa equals và hashCode, phân cấp ngoại lệ Checked/Unchecked, try-with-resources và tuần tự hóa đối tượng.",
    icon: "Database",
    badge: "Quan trọng",
    color: "from-pink-500 to-rose-600",
    tags: ["Collections", "Exceptions", "Try-with-resources", "I/O", "Serialization"]
  },
  {
    id: 6,
    title: "Bài 6: Mẫu thiết kế (Design Patterns)",
    subtitle: "Creational, Structural, Behavioral & SOLID Principles",
    description: "Singleton (Thread-safe, Double-checked locking), Factory Method, Strategy, Observer, Decorator, Adapter, Composite, MVC & các nguyên lý SOLID.",
    icon: "LayoutGrid",
    badge: "Thiết kế",
    color: "from-amber-500 to-emerald-600",
    tags: ["Patterns", "Singleton", "Factory", "Strategy", "Observer", "SOLID"]
  },
  {
    id: 7,
    title: "Bài 7: Đa luồng (Multithreading)",
    subtitle: "Thread, Runnable, synchronized, Deadlock, wait/notify, ExecutorService",
    description: "Vòng đời Thread, cơ chế đồng bộ hóa Monitor lock, tránh Deadlock, giao tiếp inter-thread (wait/notify/notifyAll) và Thread Pool (ExecutorService/Future).",
    icon: "Zap",
    badge: "Chuyên sâu",
    color: "from-emerald-500 to-teal-600",
    tags: ["Concurrency", "Thread", "Deadlock", "Synchronized", "Executor"]
  },
  {
    id: 8,
    title: "Bài 8: Kiểm thử & Tái cấu trúc",
    subtitle: "JUnit 5, Black-box Testing, BVA, Equivalence Partitioning, Code Smells & Refactoring",
    description: "Kiểm thử JUnit 5, phân tích giá trị biên (BVA), phân lớp tương đương (EP), nhận diện các loại Code Smells và kỹ thuật Refactoring chuẩn.",
    icon: "CheckCircle",
    badge: "Chất lượng",
    color: "from-teal-500 to-cyan-600",
    tags: ["JUnit5", "BVA", "CodeSmell", "Refactoring"]
  },
  {
    id: 9,
    title: "Bài 9: Tích hợp & Triển khai (CI/CD)",
    subtitle: "Maven Lifecycle, Dependency Scopes, Checkstyle & CI/CD GitHub Actions",
    description: "Vòng đời Maven (validate, compile, test, package, verify, install, deploy), các phạm vi dependency scope, phân tích mã tĩnh Checkstyle và quy trình CI/CD.",
    icon: "FileCode",
    badge: "Triển khai",
    color: "from-cyan-500 to-blue-600",
    tags: ["Maven", "Dependency", "Checkstyle", "CICD", "Git"]
  }
];
