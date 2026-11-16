export const LESSONS_METADATA = [
  {
    id: 1,
    title: "Bài 1: Cơ bản Java & OOP",
    subtitle: "Stack vs Heap, GC, Static, Final, Access Modifiers",
    description: "Nắm vững cơ chế bộ nhớ JVM, Garbage Collector, vòng đời biến, nạp chồng constructor và các từ khóa đặc tả truy cập.",
    icon: "Cpu",
    badge: "Nền tảng",
    color: "from-blue-500 to-indigo-600",
    tags: ["JVM", "Stack-Heap", "Static", "GC", "Modifiers"]
  },
  {
    id: 2,
    title: "Bài 2: Kế thừa & Đa hình",
    subtitle: "Inheritance, Dynamic Binding, Static Hiding, Polymorphism",
    description: "Cơ chế liên kết động, ép kiểu Upcasting/Downcasting, phân biệt che giấu phương thức static và ghi đè.",
    icon: "Layers",
    badge: "Cốt lõi",
    color: "from-indigo-500 to-purple-600",
    tags: ["Inheritance", "Polymorphism", "DynamicBinding", "Hiding"]
  },
  {
    id: 3,
    title: "Bài 3: Abstract Class & Interface",
    subtitle: "Default methods, Static methods, Multiple Inheritance",
    description: "Thiết kế trừu tượng hóa, xung đột phương thức mặc định trong giao diện, phân biệt kế thừa đơn và đa giao diện.",
    icon: "FileCode",
    badge: "Kiến trúc",
    color: "from-purple-500 to-pink-600",
    tags: ["Abstract", "Interface", "DefaultMethod", "Contract"]
  },
  {
    id: 4,
    title: "Bài 4: Lập trình tổng quát (Generics)",
    subtitle: "Type Erasure, Wildcards, PECS (Producer Extends)",
    description: "Nguyên lý Generic trong Java, cơ chế xóa kiểu (Type Erasure), quy tắc PECS (? extends T vs ? super T).",
    icon: "Boxes",
    badge: "Nâng cao",
    color: "from-pink-500 to-rose-600",
    tags: ["Generics", "PECS", "Wildcard", "TypeErasure"]
  },
  {
    id: 5,
    title: "Bài 5: Java Collections Framework",
    subtitle: "List, Set, Map, equals() & hashCode() contract",
    description: "Đặc tính các cấu trúc dữ liệu Java, hợp đồng bất biến giữa equals và hashCode, xử lý xung đột băm (Hash collision).",
    icon: "Database",
    badge: "Quan trọng",
    color: "from-rose-500 to-amber-600",
    tags: ["Collections", "HashMap", "equals-hashCode", "TreeSet"]
  },
  {
    id: 6,
    title: "Bài 6: Xử lý ngoại lệ & Luồng I/O",
    subtitle: "Checked vs Unchecked, try-with-resources, Serialization",
    description: "Cây phân cấp ngoại lệ, luồng thực thi finally, cơ chế AutoCloseable và tuần tự hóa đối tượng (transient, serialVersionUID).",
    icon: "AlertTriangle",
    badge: "Thực chiến",
    color: "from-amber-500 to-emerald-600",
    tags: ["Exception", "Try-with-resources", "I/O", "Serialization"]
  },
  {
    id: 7,
    title: "Bài 7: Mẫu thiết kế (Design Patterns)",
    subtitle: "Creational, Structural, Behavioral & SOLID Principles",
    description: "Singleton (Thread-safe, Double-checked locking), Factory Method, Strategy, Observer, Decorator, Adapter, Composite, MVC.",
    icon: "LayoutGrid",
    badge: "Thiết kế",
    color: "from-emerald-500 to-teal-600",
    tags: ["Patterns", "Singleton", "Factory", "Strategy", "Observer", "SOLID"]
  },
  {
    id: 8,
    title: "Bài 8: Đa luồng (Multithreading)",
    subtitle: "Thread, Runnable, synchronized, Deadlock, ExecutorService",
    description: "Vòng đời Thread, cơ chế đồng bộ Monitor lock, tranh chấp Race Condition, tránh Deadlock và Thread Pool.",
    icon: "Zap",
    badge: "Chuyên sâu",
    color: "from-teal-500 to-cyan-600",
    tags: ["Concurrency", "Thread", "Deadlock", "Synchronized", "Executor"]
  },
  {
    id: 9,
    title: "Bài 9: Kiểm thử, Tái cấu trúc & CI/CD",
    subtitle: "JUnit 5, BVA/EP, Code Smells, Refactoring & CI/CD Maven",
    description: "Kiểm thử phần mềm JUnit 5, phân tích giá trị biên BVA, nhận diện Code Smells, kỹ thuật Refactoring, công cụ Maven và GitHub Actions CI/CD.",
    icon: "CheckCircle",
    badge: "Chất lượng",
    color: "from-cyan-500 to-blue-600",
    tags: ["JUnit5", "BVA", "CodeSmell", "Refactoring", "Maven", "CICD"]
  }
];
