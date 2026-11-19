# -*- coding: utf-8 -*-
"""
Script to generate 60 new questions for Lessons 8 and 9
- Lesson 8: L8_Q31 to L8_Q60 (Đề 8C: 15 questions, Đề 8D: 15 questions)
- Lesson 9: L9_Q31 to L9_Q60 (Đề 9C: 15 questions, Đề 9D: 15 questions)
"""

import json
import os

L8_NEW = [
    # --- ĐỀ 8C (L8_Q31 - L8_Q45): JUnit 5 Deep-Dive, Assertions & BVA ---
    {
        "id": "L8_Q31",
        "lessonId": 8,
        "type": "single",
        "title": "Trong JUnit 5, chế độ vòng đời mặc định của một Test Class (@TestInstance(Lifecycle.PER_METHOD)) có cơ chế hoạt động như thế nào?",
        "code": None,
        "options": [
            "Mỗi phương thức kiểm thử (@Test) sẽ được thực thi trên một thể hiện (instance) hoàn toàn mới của lớp test; do đó các phương thức @BeforeAll và @AfterAll bắt buộc phải được khai báo là 'static'",
            "Tất cả các phương thức @Test dùng chung duy nhất một instance trong suốt vòng đời",
            "Mỗi @Test method sẽ được chạy trong một tiến trình (process) hệ điều hành riêng biệt",
            "JUnit 5 không hỗ trợ phương thức @BeforeAll và @AfterAll"
        ],
        "correctAnswer": 0,
        "explanation": "Mặc định trong JUnit (từ JUnit 4 đến JUnit 5), để đảm bảo tính độc lập tuyệt đối giữa các bài test (Test Isolation), mỗi test method được chạy trên một đối tượng test class mới. Vì chưa có instance nào được tạo khi chuẩn bị test class, phương thức @BeforeAll và @AfterAll bắt buộc phải là static (trừ khi cấu hình @TestInstance(Lifecycle.PER_CLASS)).",
        "difficulty": "medium",
        "tags": ["JUnit5", "TestInstance", "Lifecycle"]
    },
    {
        "id": "L8_Q32",
        "lessonId": 8,
        "type": "single",
        "title": "Ưu điểm vượt trội lớn nhất của phương thức 'assertAll()' trong JUnit 5 so với việc viết nhiều lệnh 'assertEquals()' liên tiếp truyền thống là gì?",
        "code": "assertAll(\"Kiem tra sinh vien\",\n    () -> assertEquals(\"Nam\", student.getName()),\n    () -> assertEquals(20, student.getAge()),\n    () -> assertEquals(\"IT\", student.getMajor())\n);",
        "options": [
            "Tất cả các assertions bên trong đều được thực thi và báo cáo lỗi đầy đủ, kể cả khi có một assertion ở giữa bị thất bại (không bị dừng chương trình đột ngột)",
            "Chạy các assertions song song trên 3 luồng CPU khác nhau",
            "Tự động sửa chữa dữ liệu của đối tượng nếu assertion bị sai",
            "Chỉ dùng được cho các kiểu dữ liệu số nguyên"
        ],
        "correctAnswer": 0,
        "explanation": "Trong kiểm thử truyền thống, nếu assertion thứ nhất thất bại (ném AssertionError), phương thức test sẽ dừng ngay lập tức và bạn không thể biết các assertion 2 và 3 phía sau pass hay fail. assertAll() thực hiện gom nhóm (Grouped Assertions): nó chạy hết toàn bộ các assertions bên trong và báo cáo tổng hợp tất cả các lỗi xảy ra.",
        "difficulty": "medium",
        "tags": ["assertAll", "JUnit5", "Assertions"]
    },
    {
        "id": "L8_Q33",
        "lessonId": 8,
        "type": "single",
        "title": "Để kiểm tra một đoạn mã có ném đúng loại ngoại lệ mong muốn hay không trong JUnit 5, phương thức nào sau đây là chuẩn mực và hiện đại nhất?",
        "code": "Exception ex = assertThrows(IllegalArgumentException.class, () -> {\n    calculator.divide(10, 0);\n});\nassertEquals(\"Khong the chia cho 0\", ex.getMessage());",
        "options": [
            "assertThrows(ExpectedException.class, Executable) - trả về chính đối tượng ngoại lệ để tiếp tục kiểm tra thông điệp lỗi (message)",
            "Sử dụng thuộc tính @Test(expected = IllegalArgumentException.class) giống JUnit 4",
            "Bọc trong khối try-catch thủ công và gọi fail() ở cuối khối try",
            "assertEquals(IllegalArgumentException.class, calculator.divide(10, 0))"
        ],
        "correctAnswer": 0,
        "explanation": "JUnit 5 loại bỏ thuộc tính 'expected' của @Test và thay thế bằng phương thức hàm (Functional Assertion) 'assertThrows()'. Nó nhận một biểu thức Lambda (Executable), kiểm tra chính xác ngoại lệ được ném ra, và trả về đối tượng exception đó để lập trình viên có thể kiểm tra sâu hơn (như ex.getMessage(), ex.getCause()).",
        "difficulty": "medium",
        "tags": ["assertThrows", "ExceptionTesting", "JUnit5"]
    },
    {
        "id": "L8_Q34",
        "lessonId": 8,
        "type": "multiple",
        "title": "Về tính năng Kiểm thử tham số hóa (@ParameterizedTest) trong JUnit 5, những nguồn cung cấp dữ liệu nào sau đây được hỗ trợ chính thức?",
        "code": None,
        "options": [
            "@ValueSource: cung cấp một mảng các giá trị nguyên thủy hoặc chuỗi (ví dụ: ints = {1, 2, 3}, strings = {\"a\", \"b\"})",
            "@CsvSource: cung cấp danh sách các dòng dữ liệu dạng CSV (ví dụ: {\"apple, 1\", \"banana, 2\"})",
            "@MethodSource: chỉ định một phương thức static trả về Stream/Collection các đối số phức tạp",
            "@EnumSource: tự động duyệt qua các hằng số của một kiểu enum cụ thể"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "JUnit 5 hỗ trợ đầy đủ và đa dạng các nguồn cấp dữ liệu cho @ParameterizedTest: @ValueSource (mảng đơn giản), @EnumSource (duyệt enum), @CsvSource (nhiều tham số trên dòng), @CsvFileSource (đọc từ file .csv bên ngoài), và @MethodSource (dùng Stream/List tùy biến linh hoạt).",
        "difficulty": "easy",
        "tags": ["ParameterizedTest", "ValueSource", "CsvSource", "MethodSource"]
    },
    {
        "id": "L8_Q35",
        "lessonId": 8,
        "type": "single",
        "title": "Cho biến nguyên 'age' có miền giá trị hợp lệ là [18, 60]. Theo kỹ thuật Phân tích giá trị biên 2-giá trị (2-value Boundary Value Analysis chuẩn), bộ giá trị kiểm thử tối thiểu là gì?",
        "code": None,
        "options": [
            "{17, 18, 60, 61}",
            "{18, 60}",
            "{17, 18, 19, 59, 60, 61}",
            "{0, 18, 60, 100}"
        ],
        "correctAnswer": 0,
        "explanation": "Trong kỹ thuật phân tích giá trị biên 2-value tiêu chuẩn (Standard 2-value BVA): tại mỗi biên (Min và Max), ta kiểm tra đúng giá trị tại biên và giá trị ngay sát ngoài biên không hợp lệ. Với đoạn [18, 60]: Biên dưới có 18 (hợp lệ) và 17 (ngay ngoài biên dưới); Biên trên có 60 (hợp lệ) và 61 (ngay ngoài biên trên). Bộ giá trị biên là {17, 18, 60, 61}.",
        "difficulty": "medium",
        "tags": ["BVA", "BoundaryValueAnalysis", "BlackBoxTesting"]
    },
    {
        "id": "L8_Q36",
        "lessonId": 8,
        "type": "single",
        "title": "Cho một trường nhập điểm thi có miền giá trị hợp lệ là các số nguyên từ 0 đến 10. Kỹ thuật Phân hoạch tương đương (Equivalence Partitioning) chia miền đầu vào thành các lớp nào?",
        "code": None,
        "options": [
            "1 lớp hợp lệ: [0, 10] và 2 lớp không hợp lệ: (< 0) và (> 10)",
            "Chỉ có 1 lớp duy nhất là [0, 10]",
            "11 lớp riêng biệt từ 0 đến 10",
            "2 lớp: số chẵn và số lẻ"
        ],
        "correctAnswer": 0,
        "explanation": "Theo lý thuyết phân hoạch tương đương (Equivalence Partitioning), ta chia miền giá trị thành: 1 Phân lớp tương đương hợp lệ (Valid equivalence class: 0 <= score <= 10) và các Phân lớp không hợp lệ (Invalid equivalence classes: score < 0 và score > 10). Mỗi lớp chỉ cần chọn 1 giá trị đại diện để kiểm thử.",
        "difficulty": "easy",
        "tags": ["EquivalencePartitioning", "BlackBoxTesting", "TestDesign"]
    },
    {
        "id": "L8_Q37",
        "lessonId": 8,
        "type": "multiple",
        "title": "Phân biệt các cấp độ bao phủ kiểm thử (Test Coverage) trong kiểm thử hộp trắng (White-box Testing):",
        "code": None,
        "options": [
            "Statement Coverage (Bao phủ dòng lệnh): Đo lường tỷ lệ phần trăm các câu lệnh mã nguồn được thực thi ít nhất một lần",
            "Branch Coverage (Bao phủ nhánh / Decision Coverage): Đo lường tỷ lệ phần trăm các nhánh rẽ điều kiện (True/False) của các khối if/switch được duyệt qua",
            "Branch Coverage luôn đảm bảo độ tin cậy và khắt khe hơn Statement Coverage (100% Branch Coverage đảm bảo 100% Statement Coverage, nhưng chiều ngược lại không đúng)",
            "Statement Coverage là tiêu chuẩn kiểm thử duy nhất cần đạt để đảm bảo phần mềm không còn lỗi"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 đều chính xác: Branch coverage yêu cầu cả nhánh True và False của câu lệnh rẽ nhánh đều phải được test, do đó nó bao hàm Statement coverage. Statement coverage không thể phát hiện lỗi khi thiếu nhánh else rỗng.",
        "difficulty": "medium",
        "tags": ["TestCoverage", "BranchCoverage", "StatementCoverage"]
    },
    {
        "id": "L8_Q38",
        "lessonId": 8,
        "type": "single",
        "title": "Trong JUnit 5, sự khác biệt giữa 'assertTimeout()' và 'assertTimeoutPreemptively()' là gì?",
        "code": None,
        "options": [
            "assertTimeoutPreemptively() sẽ thực thi tác vụ trong một luồng riêng biệt và ngắt cưỡng bức (preemptively abort) tác vụ đó ngay khi hết thời gian quy định; còn assertTimeout() để tác vụ chạy hết rồi mới so sánh tổng thời gian thực thi",
            "assertTimeout() dùng đơn vị micro giây, còn assertTimeoutPreemptively() dùng đơn vị giây",
            "assertTimeout() chỉ chạy được trên hệ điều hành Linux",
            "Không có sự khác biệt nào giữa hai phương thức"
        ],
        "correctAnswer": 0,
        "explanation": "Nếu tác vụ bị rơi vào vòng lặp vô hạn (Infinite Loop), assertTimeout() sẽ bị treo mãi mãi không dừng cho đến khi toàn bộ quá trình test bị kill. Ngược lại, assertTimeoutPreemptively() chạy tác vụ trên một Thread khác và lập tức ngắt luồng đó khi chạm ngưỡng timeout, giúp bộ test không bị treo cứng.",
        "difficulty": "hard",
        "tags": ["assertTimeout", "TimeoutPreemptively", "JUnit5"]
    },
    {
        "id": "L8_Q39",
        "lessonId": 8,
        "type": "single",
        "title": "Xem xét đoạn mã test JUnit 5 sau. Kết quả chạy bài test là gì?",
        "code": "@Test\nvoid testMath() {\n    assertEquals(10, 5 + 5);\n    assertEquals(20, 10 * 3, \"Nhan sai!\");\n    assertEquals(4, 8 / 2);\n}",
        "options": [
            "Bài test bị THẤT BẠI (Failed) tại câu lệnh thứ 2 với thông điệp 'Nhan sai!', và câu lệnh thứ 3 (8 / 2) KHÔNG BAO GIỜ được chạy",
            "Cả 3 câu lệnh đều được thực thi và in ra thông báo lỗi ở cuối",
            "Bài test vẫn được đánh dấu là Passed vì câu lệnh 1 và 3 đúng",
            "Ném ngoại lệ ArithmeticException"
        ],
        "correctAnswer": 0,
        "explanation": "Trong JUnit, một câu lệnh assert thất bại sẽ ném ra lỗi java.lang.AssertionError. Khi câu lệnh thứ 2 (10 * 3 == 30 != 20) thất bại, phương thức test bị ngắt luồng ngay tại đó, câu lệnh thứ 3 hoàn toàn không được thực thi. Để chạy được cả 3 câu lệnh, phải dùng assertAll().",
        "difficulty": "easy",
        "tags": ["AssertionError", "JUnitExecutionFlow", "Output"]
    },
    {
        "id": "L8_Q40",
        "lessonId": 8,
        "type": "multiple",
        "title": "Những khẳng định nào sau đây về thư viện Mockito (Mocking framework trong Java) là ĐÚNG?",
        "code": None,
        "options": [
            "Mockito cho phép tạo ra các đối tượng giả lập (Mock objects) để cô lập đơn vị cần kiểm thử (Unit under test) khỏi các thành phần phụ thuộc bên ngoài như Database, Network, API",
            "Phương thức when(mock.method()).thenReturn(value) dùng để định nghĩa trước hành vi (Stubbing) cho phương thức của đối tượng mock",
            "Phương thức verify(mock, times(1)).someMethod() dùng để kiểm tra xem phương thức của mock object có thực sự được gọi đúng số lần kỳ vọng hay không",
            "Mockito chỉ có thể chạy được khi máy tính được kết nối Internet"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Mockito là framework mock hàng đầu cho Java, hỗ trợ tạo mock object, stubbing (when-thenReturn) và xác minh tương tác (verify). Nó hoạt động cục bộ trong bộ nhớ JVM, không cần internet.",
        "difficulty": "medium",
        "tags": ["Mockito", "Mocking", "Stubbing", "Verify"]
    },
    {
        "id": "L8_Q41",
        "lessonId": 8,
        "type": "single",
        "title": "Annotation nào trong JUnit 5 được sử dụng để tạm thời vô hiệu hóa (bỏ qua không chạy) một phương thức test hoặc toàn bộ một test class?",
        "code": None,
        "options": [
            "@Disabled (có thể truyền kèm lý do: @Disabled(\"Chờ fix bug #102\"))",
            "@Ignore",
            "@Skip",
            "@Deprecated"
        ],
        "correctAnswer": 0,
        "explanation": "Trong JUnit 4 người ta dùng @Ignore. Sang JUnit 5 (JUnit Jupiter), annotation này được đổi tên thành @Disabled. Khi chạy test, JUnit 5 sẽ bỏ qua và đánh dấu test case là Skipped/Disabled.",
        "difficulty": "easy",
        "tags": ["DisabledAnnotation", "JUnit5VsJUnit4", "Annotations"]
    },
    {
        "id": "L8_Q42",
        "lessonId": 8,
        "type": "single",
        "title": "Cho phương thức tính tiền giảm giá: nếu số lượng mua >= 100 thì giảm 10%, nếu < 100 thì không giảm. Dữ liệu kiểm thử theo Phân tích giá trị biên (BVA) để kiểm tra điểm biên này là:",
        "code": None,
        "options": [
            "99 và 100",
            "50 và 150",
            "0 và 1000",
            "100 và 101"
        ],
        "correctAnswer": 0,
        "explanation": "Biên quyết định thay đổi hành vi logic ở đây là giá trị 100. Điểm 99 (< 100: không giảm) và điểm 100 (>= 100: được giảm 10%) là hai giá trị biên sát nhau quyết định tính đúng đắn của phép so sánh (>= vs >).",
        "difficulty": "easy",
        "tags": ["BVA", "DiscountTesting", "BoundaryPoints"]
    },
    {
        "id": "L8_Q43",
        "lessonId": 8,
        "type": "multiple",
        "title": "Nguyên tắc F.I.R.S.T trong kiểm thử đơn vị (Unit Testing) chuẩn mực bao gồm những yếu tố nào?",
        "code": None,
        "options": [
            "Fast (Nhanh): Các bài unit test phải chạy cực nhanh (vài mili-giây) để lập trình viên có thể chạy thường xuyên",
            "Independent / Isolated (Độc lập): Các bài test không được phụ thuộc lẫn nhau, thứ tự chạy các test case không làm thay đổi kết quả",
            "Repeatable (Lặp lại được): Bài test phải cho kết quả giống hệt nhau trong mọi môi trường (máy dev, máy CI, máy test)",
            "Self-validating (Tự kiểm chứng): Bài test phải tự động xác định Pass hoặc Fail qua assertion mà không cần con người đọc log kiểm tra bằng mắt"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Nguyên tắc FIRST gồm: Fast (nhanh), Independent (độc lập), Repeatable (lặp lại được ở mọi môi trường), Self-validating (tự động báo kết quả), Timely/Thorough (kịp thời, viết song hành hoặc trước code - TDD). Cả 4 ý đều đúng.",
        "difficulty": "medium",
        "tags": ["FIRSTPrinciples", "BestPractices", "UnitTesting"]
    },
    {
        "id": "L8_Q44",
        "lessonId": 8,
        "type": "single",
        "title": "Trong JUnit 5, nếu muốn hiển thị một tên mô tả bài kiểm thử bằng tiếng Việt rõ ràng trên giao diện báo cáo (thay vì tên hàm tiếng Anh camelCase), ta sử dụng annotation nào?",
        "code": "@Test\n@DisplayName(\"Kiem tra dang nhap voi mat khau rong\")\nvoid testEmptyPassword() { ... }",
        "options": [
            "@DisplayName",
            "@TestName",
            "@Description",
            "@Label"
        ],
        "correctAnswer": 0,
        "explanation": "JUnit 5 cung cấp annotation @DisplayName cho phép lập trình viên đặt tiêu đề tùy chỉnh cho test class hoặc test method, hỗ trợ cả ký tự đặc biệt, khoảng trắng và emoji, giúp báo cáo kiểm thử cực kỳ trực quan và dễ hiểu.",
        "difficulty": "easy",
        "tags": ["DisplayName", "JUnit5", "Annotations"]
    },
    {
        "id": "L8_Q45",
        "lessonId": 8,
        "type": "single",
        "title": "Khái niệm 'Regression Testing' (Kiểm thử hồi quy) có mục tiêu chính là gì?",
        "code": None,
        "options": [
            "Chạy lại bộ kiểm thử tự động sau khi mã nguồn được sửa đổi hoặc thêm tính năng mới nhằm đảm bảo các chức năng cũ đã hoạt động ổn định trước đây không bị hỏng hóc",
            "Kiểm thử khả năng chịu tải của hệ thống khi có 10.000 người dùng truy cập",
            "Chỉ kiểm tra giao diện người dùng trên điện thoại di động",
            "Kiểm tra tính tương thích của máy in"
        ],
        "correctAnswer": 0,
        "explanation": "Kiểm thử hồi quy (Regression Testing) là việc thực thi lại các ca kiểm thử sẵn có để kiểm chứng rằng việc sửa lỗi (bug fix), tái cấu trúc (refactoring) hoặc bổ sung tính năng mới không vô tình gây ra các lỗi mới trên các tính năng đang hoạt động bình thường.",
        "difficulty": "easy",
        "tags": ["RegressionTesting", "SoftwareTesting", "QualityAssurance"]
    },

    # --- ĐỀ 8D (L8_Q46 - L8_Q60): Code Smells & Refactoring Techniques ---
    {
        "id": "L8_Q46",
        "lessonId": 8,
        "type": "single",
        "title": "Theo định nghĩa của Martin Fowler, 'Tái cấu trúc mã nguồn' (Refactoring) là quá trình gì?",
        "code": None,
        "options": [
            "Thay đổi cấu trúc nội bộ của phần mềm để làm cho mã nguồn dễ hiểu hơn, sạch hơn và chi phí sửa đổi rẻ hơn mà KHÔNG LÀM THAY ĐỔI hành vi bên ngoài (observable behavior) của phần mềm",
            "Viết lại toàn bộ phần mềm từ đầu bằng một ngôn ngữ lập trình khác",
            "Bổ sung thêm thật nhiều tính năng mới cho người dùng",
            "Sửa chữa các lỗi chức năng và thay đổi giao diện phần mềm"
        ],
        "correctAnswer": 0,
        "explanation": "Quy tắc cốt lõi của Refactoring: Cải thiện thiết kế nội bộ (clean code, giảm nợ kỹ thuật) nhưng hành vi bên ngoài nhìn từ phía người dùng/client phải được giữ nguyên vẹn 100% (mọi bài unit test đang pass phải tiếp tục pass sau khi refactor).",
        "difficulty": "easy",
        "tags": ["RefactoringDefinition", "MartinFowler", "CleanCode"]
    },
    {
        "id": "L8_Q47",
        "lessonId": 8,
        "type": "single",
        "title": "Code Smell 'Feature Envy' (Ghen tị tính năng) được định nghĩa như thế nào?",
        "code": "class Order {\n    double calculateDiscount(Customer c) {\n        // Phuong thuc nay lien tuc goi cac getter cua Customer:\n        if (c.getMembership().equals(\"VIP\") && c.getPoints() > 100 && c.getCity().equals(\"HN\")) {\n            return c.getBaseDiscount() * 1.5;\n        }\n        return 0;\n    }\n}",
        "options": [
            "Một phương thức trong lớp A truy cập dữ liệu và gọi các phương thức của lớp B nhiều hơn hẳn so với việc tương tác với dữ liệu của chính lớp A",
            "Một lớp có quá nhiều thuộc tính nguyên thủy",
            "Hai lớp kế thừa lẫn nhau tạo thành chu trình",
            "Một phương thức có quá nhiều lệnh if-else"
        ],
        "correctAnswer": 0,
        "explanation": "Feature Envy xảy ra khi một method dường như 'thích' sống trong lớp khác hơn là lớp hiện tại của nó vì nó thao tác trên dữ liệu của lớp kia nhiều hơn. Giải pháp tái cấu trúc tiêu chuẩn cho Feature Envy là dùng kỹ thuật 'Move Method' để chuyển phương thức đó sang lớp sở hữu dữ liệu.",
        "difficulty": "medium",
        "tags": ["FeatureEnvy", "CodeSmells", "MoveMethod"]
    },
    {
        "id": "L8_Q48",
        "lessonId": 8,
        "type": "single",
        "title": "Kỹ thuật tái cấu trúc nào là giải pháp phù hợp nhất để khắc phục Code Smell 'Long Method' (Phương thức quá dài)?",
        "code": None,
        "options": [
            "Extract Method (Trích xuất các đoạn mã con có cùng một mục đích logic thành các phương thức nhỏ, độc lập và đặt tên rõ nghĩa)",
            "Inline Method (Gộp tất cả các phương thức nhỏ lại thành một phương thức duy nhất)",
            "Thêm thật nhiều dòng ghi chú (comments) vào giữa phương thức",
            "Chuyển phương thức đó thành phương thức static"
        ],
        "correctAnswer": 0,
        "explanation": "Extract Method là kỹ thuật refactoring phổ biến và hiệu quả nhất cho Long Method. Ta tìm những đoạn mã thực hiện một nhiệm vụ cụ thể, trích xuất nó thành một phương thức riêng và đặt tên theo đúng ý định (Intention-revealing name), biến code trở thành tài liệu tự giải thích.",
        "difficulty": "easy",
        "tags": ["ExtractMethod", "LongMethod", "Refactoring"]
    },
    {
        "id": "L8_Q49",
        "lessonId": 8,
        "type": "single",
        "title": "Đoạn mã sau vi phạm Code Smell 'Switch Statements / Complex Conditionals' (giống Bài 4 trong Đề thi mẫu UET). Kỹ thuật tái cấu trúc hướng đối tượng chuẩn mực nhất là gì?",
        "code": "class Logger {\n    void log(String level, String message) {\n        if (level.equals(\"INFO\")) {\n            System.out.println(\"INFO: \" + message);\n        } else if (level.equals(\"ERROR\")) {\n            System.out.println(\"ERROR: \" + message);\n        } else if (level.equals(\"DEBUG\")) {\n            System.out.println(\"DEBUG: \" + message);\n        }\n    }\n}",
        "options": [
            "Replace Conditional with Polymorphism: Tạo interface/abstract class LogFormatter hoặc LogStrategy và triển khai các lớp con InfoLogger, ErrorLogger, DebugLogger độc lập tuân thủ Open/Closed Principle",
            "Chuyển đổi chuỗi if-else thành câu lệnh switch-case để chạy nhanh hơn",
            "Gộp tất cả các loại log thành một dòng duy nhất",
            "Khai báo các biến level thành các số nguyên int 1, 2, 3"
        ],
        "correctAnswer": 0,
        "explanation": "Chuỗi if-else hoặc switch kiểm tra loại đối tượng (Type checking) vi phạm nguyên lý Open/Closed (mỗi khi thêm log level mới như WARN, TRACE bắt buộc phải sửa mã nguồn cũ). Kỹ thuật chuẩn là 'Replace Conditional with Polymorphism' hoặc áp dụng Strategy Pattern.",
        "difficulty": "medium",
        "tags": ["ReplaceConditionalWithPolymorphism", "SampleExamTopic", "CodeSmell"]
    },
    {
        "id": "L8_Q50",
        "lessonId": 8,
        "type": "single",
        "title": "Code Smell 'God Class' (hoặc Large Class / Blob) là gì và gây ra tác hại gì lớn nhất cho dự án?",
        "code": None,
        "options": [
            "Một lớp phình to nắm giữ quá nhiều thuộc tính, hàng trăm phương thức và ôm đồm quá nhiều trách nhiệm khác nhau; làm phá vỡ nguyên lý Đơn trách nhiệm (SRP), cực kỳ khó bảo trì và dễ gây lỗi dây chuyền",
            "Một lớp có quá nhiều lớp con kế thừa",
            "Một lớp không có bất kỳ phương thức nào",
            "Một lớp được viết bằng ngôn ngữ C++"
        ],
        "correctAnswer": 0,
        "explanation": "God Class là một phản mẫu (anti-pattern) nơi mà một lớp duy nhất biết quá nhiều và làm quá nhiều (từ tính toán logic, kết nối DB đến vẽ giao diện). Giải pháp là dùng kỹ thuật 'Extract Class' để phân tách các trách nhiệm độc lập ra các lớp chuyên biệt.",
        "difficulty": "easy",
        "tags": ["GodClass", "LargeClass", "SRP"]
    },
    {
        "id": "L8_Q51",
        "lessonId": 8,
        "type": "multiple",
        "title": "Code Smell 'Primitive Obsession' (Ám ảnh kiểu nguyên thủy) thể hiện qua những dấu hiệu nào sau đây?",
        "code": None,
        "options": [
            "Lạm dụng kiểu dữ liệu nguyên thủy (như int, String, double) để đại diện cho các khái niệm nghiệp vụ có ràng buộc (như Số điện thoại, Email, Địa chỉ, Số tiền tệ) thay vì tạo các lớp Value Object nhỏ riêng biệt",
            "Sử dụng các hằng số chuỗi hoặc số nguyên (Magic Strings/Numbers) làm mã định danh loại thay vì dùng Enum",
            "Dùng mảng hoặc List các số nguyên để mô phỏng một cấu trúc bản ghi phức tạp",
            "Sử dụng kiểu boolean cho các biến cờ hiệu logic đúng/sai"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Primitive Obsession là thói quen ngại tạo class mới, dùng String biểu diễn ZipCode/Email/Phone dẫn đến việc phải lặp lại logic validation ở khắp nơi. Giải pháp là 'Replace Data Value with Object' hoặc tạo Enum.",
        "difficulty": "medium",
        "tags": ["PrimitiveObsession", "ValueObject", "CodeSmells"]
    },
    {
        "id": "L8_Q52",
        "lessonId": 8,
        "type": "single",
        "title": "Khi một phương thức nhận quá nhiều tham số (Long Parameter List, ví dụ: 7-8 tham số), kỹ thuật tái cấu trúc nào được khuyến nghị áp dụng?",
        "code": "void drawWindow(int x, int y, int width, int height, String title, boolean resizable, boolean modal, Color bg);",
        "options": [
            "Introduce Parameter Object: Đóng gói các tham số có liên quan chặt chẽ thành một đối tượng độc lập (ví dụ WindowConfig hoặc WindowBounds)",
            "Chuyển tất cả các tham số thành biến toàn cục (global variables)",
            "Chuyển tất cả các tham số thành một mảng Object[]",
            "Nối tất cả các tham số thành một chuỗi String duy nhất cách nhau bởi dấu phẩy"
        ],
        "correctAnswer": 0,
        "explanation": "Introduce Parameter Object gom các nhóm dữ liệu thường xuyên đi cùng nhau (Data Clumps) thành một lớp độc lập. Điều này giúp chữ ký phương thức ngắn gọn, dễ mở rộng và dễ đọc hiểu hơn.",
        "difficulty": "easy",
        "tags": ["IntroduceParameterObject", "LongParameterList", "Refactoring"]
    },
    {
        "id": "L8_Q53",
        "lessonId": 8,
        "type": "single",
        "title": "Code Smell 'Refused Bequest' (Từ chối thừa kế) xảy ra trong tình huống nào?",
        "code": "class Bird {\n    void fly() { System.out.println(\"Flying\"); }\n}\nclass Penguin extends Bird {\n    @Override\n    void fly() {\n        throw new UnsupportedOperationException(\"Chim cánh cụt không biết bay!\");\n    }\n}",
        "options": [
            "Lớp con kế thừa từ lớp cha nhưng không sử dụng hoặc từ chối hỗ trợ hành vi của lớp cha (bằng cách override thân hàm rỗng hoặc ném ngoại lệ UnsupportedOperationException), vi phạm nguyên lý LSP",
            "Lớp cha từ chối cho lớp con kế thừa bằng từ khóa private",
            "Lớp con không có hàm khởi tạo constructor",
            "Hai lớp có tên giống nhau"
        ],
        "correctAnswer": 0,
        "explanation": "Refused Bequest chỉ ra rằng quan hệ kế thừa ('is-a') đã bị áp dụng sai lầm trong mô hình hóa. Nếu chim cánh cụt không biết bay, việc cho Penguin kế thừa Bird có hàm fly() vi phạm nguyên lý Liskov (LSP). Giải pháp: Tách nhỏ interface (Flyable) hoặc chuyển từ Kế thừa sang Composition.",
        "difficulty": "hard",
        "tags": ["RefusedBequest", "LSP", "InheritanceAbuse"]
    },
    {
        "id": "L8_Q54",
        "lessonId": 8,
        "type": "multiple",
        "title": "Phân biệt giữa hai Code Smells đối lập: 'Divergent Change' và 'Shotgun Surgery':",
        "code": None,
        "options": [
            "Divergent Change: Xảy ra khi MỘT lớp duy nhất liên tục bị sửa đổi vì NHIỀU lý do khác nhau (vi phạm nguyên lý Single Responsibility - SRP)",
            "Shotgun Surgery: Xảy ra khi MỖI LẦN có một thay đổi nhỏ lại buộc bạn phải đi sửa đổi rải rác ở NHIỀU lớp khác nhau trong hệ thống",
            "Giải pháp cho Divergent Change thường là 'Extract Class' để tách các trách nhiệm ra các lớp riêng",
            "Giải pháp cho Shotgun Surgery thường là 'Move Method' và 'Move Field' để gom các phần liên quan về cùng một lớp"
        ],
        "correctAnswer": [0, 1, 2, 3],
        "explanation": "Cả 4 phát biểu đều chính xác. Đây là hai mùi mã kinh điển về sự phân tán trách nhiệm: Divergent Change là '1 class bị sửa bởi nhiều lý do'; Shotgun Surgery là '1 lý do sửa bắt buộc phải bắn đạn hoa cải vào hàng loạt class'.",
        "difficulty": "hard",
        "tags": ["DivergentChange", "ShotgunSurgery", "Comparison"]
    },
    {
        "id": "L8_Q55",
        "lessonId": 8,
        "type": "single",
        "title": "Kỹ thuật tái cấu trúc 'Replace Temp with Query' nhằm mục đích gì?",
        "code": "// Truoc:\ndouble basePrice = quantity * itemPrice;\nif (basePrice > 1000) return basePrice * 0.95;\n// Sau:\nif (getBasePrice() > 1000) return getBasePrice() * 0.95;",
        "options": [
            "Thay thế một biến tạm thời (local temp variable) bằng việc gọi một phương thức tính toán riêng (Query method), giúp dễ dàng tái sử dụng logic tính toán đó ở các phương thức khác",
            "Chuyển biến tạm thành câu lệnh truy vấn SQL",
            "Xóa bỏ hoàn toàn phương thức",
            "Làm cho biến tạm trở thành biến static"
        ],
        "correctAnswer": 0,
        "explanation": "Biến tạm cục bộ chỉ có phạm vi bên trong một hàm và kích thích hàm đó dài thêm. Trích xuất biến tạm thành một query method (như getBasePrice()) giúp loại bỏ biến thừa và cho phép các hàm khác trong class tái sử dụng logic tính giá cơ sở.",
        "difficulty": "medium",
        "tags": ["ReplaceTempWithQuery", "Refactoring", "CleanCode"]
    },
    {
        "id": "L8_Q56",
        "lessonId": 8,
        "type": "multiple",
        "title": "Thời điểm nào sau đây là thích hợp nhất để tiến hành Tái cấu trúc (Refactoring)?",
        "code": None,
        "options": [
            "Quy tắc 3 lần (Rule of Three): Lần đầu viết code cứ viết; lần 2 thấy tương tự thì lưu ý; lần thứ 3 thấy lặp lại y hệt thì bắt buộc phải refactor (Don't Repeat Yourself - DRY)",
            "Khi chuẩn bị thêm một tính năng mới: tái cấu trúc trước để việc thêm tính năng mới trở nên dễ dàng và tự nhiên hơn",
            "Khi sửa một con bug: tái cấu trúc để làm cho luồng logic rõ ràng, giúp tìm ra nguyên nhân gốc của bug",
            "Chờ đến cuối dự án (sau 2 năm) mới dành 1 tháng duy nhất để refactor toàn bộ hệ thống"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Martin Fowler nhấn mạnh: Refactoring là hoạt động diễn ra thường xuyên, liên tục trong quá trình phát triển phần mềm (theo quy tắc 3 lần, khi thêm feature, khi fix bug). Trì hoãn refactor đến cuối dự án là công thức dẫn tới thất bại.",
        "difficulty": "easy",
        "tags": ["WhenToRefactor", "RuleOfThree", "BestPractices"]
    },
    {
        "id": "L8_Q57",
        "lessonId": 8,
        "type": "single",
        "title": "Điều kiện tiên quyết quan trọng nhất để có thể tự tin tiến hành Refactoring mã nguồn một cách an toàn là gì?",
        "code": None,
        "options": [
            "Hệ thống phải có sẵn một bộ Kiểm thử tự động (Automated Unit Tests) đáng tin cậy với độ bao phủ tốt để chạy lại sau mỗi bước thay đổi nhỏ",
            "Phải xin phép giám đốc dự án trước mỗi lần đổi tên biến",
            "Phải tắt máy tính và khởi động lại",
            "Phải cài đặt phần mềm chống virus"
        ],
        "correctAnswer": 0,
        "explanation": "Nền tảng của Refactoring an toàn là 'Solid Suite of Tests'. Không có bộ unit test tự động bảo vệ, lập trình viên sẽ luôn lo sợ việc dọn dẹp code làm hỏng các chức năng đang chạy, dẫn đến việc không ai dám chạm vào mã nguồn cũ (mã nguồn bị thối rữa theo thời gian).",
        "difficulty": "easy",
        "tags": ["RefactoringPrerequisite", "UnitTesting", "Safety"]
    },
    {
        "id": "L8_Q58",
        "lessonId": 8,
        "type": "single",
        "title": "Code Smell 'Speculative Generality' (Tổng quát hóa suy đoán) là gì?",
        "code": None,
        "options": [
            "Tạo ra các class trừu tượng, interface phức tạp và các tham số không dùng đến chỉ vì suy đoán rằng 'trong tương lai có thể ta sẽ cần tới nó' (vi phạm nguyên lý YAGNI - You Aren't Gonna Need It)",
            "Viết code mà không có chú thích",
            "Chỉ viết code chạy được trên một hệ điều hành",
            "Đặt tên biến quá ngắn"
        ],
        "correctAnswer": 0,
        "explanation": "Speculative Generality xảy ra khi lập trình viên cố gắng thiết kế thừa thãi các móc nối, các tham số trừu tượng để đón đầu tương lai. Hậu quả là code trở nên cồng kềnh, khó hiểu mà các tính năng đón đầu đó hầu như không bao giờ được sử dụng thực tế. Nguyên lý YAGNI khuyên chỉ viết những gì hiện tại thực sự cần.",
        "difficulty": "medium",
        "tags": ["SpeculativeGenerality", "YAGNI", "CodeSmell"]
    },
    {
        "id": "L8_Q59",
        "lessonId": 8,
        "type": "single",
        "title": "Kỹ thuật 'Extract Interface' thường được áp dụng trong tình huống nào sau đây?",
        "code": None,
        "options": [
            "Khi có nhiều client sử dụng cùng một tập con các phương thức của một class, hoặc khi cần tạo đối tượng Mock phục vụ kiểm thử đơn vị",
            "Khi muốn gộp hai class thành một",
            "Khi class có quá ít phương thức",
            "Khi muốn tăng tốc độ thực thi của CPU"
        ],
        "correctAnswer": 0,
        "explanation": "Extract Interface tách một tập hợp các phương thức thành một giao diện riêng biệt. Điều này giúp áp dụng nguyên lý Phân tách giao diện (ISP) và cho phép các framework như Mockito dễ dàng tạo Mock Object phục vụ unit testing.",
        "difficulty": "medium",
        "tags": ["ExtractInterface", "ISP", "RefactoringTechniques"]
    },
    {
        "id": "L8_Q60",
        "lessonId": 8,
        "type": "single",
        "title": "Kỹ thuật 'Inline Method' là thao tác ngược lại của 'Extract Method'. Khi nào ta nên sử dụng 'Inline Method'?",
        "code": None,
        "options": [
            "Khi phần thân của phương thức cũng rõ nghĩa và ngắn gọn ngang ngửa với tên của chính phương thức đó, làm cho việc gọi gián tiếp qua phương thức trở nên thừa thãi",
            "Khi phương thức dài hơn 500 dòng code",
            "Khi phương thức chứa quá nhiều vòng lặp lồng nhau",
            "Khi muốn biến phương thức thành private"
        ],
        "correctAnswer": 0,
        "explanation": "Nếu bạn có một hàm chỉ đơn giản là: 'boolean isMoreThanFive() { return numberOfItems > 5; }' và hàm này chỉ được gọi ở 1 nơi, việc giữ một hàm riêng biệt như vậy làm rối mắt và tăng số tầng gọi hàm không cần thiết. Ta nên 'Inline Method' đặt trực tiếp biểu thức vào nơi gọi.",
        "difficulty": "medium",
        "tags": ["InlineMethod", "Refactoring", "CleanCode"]
    }
]

L9_NEW = [
    # --- ĐỀ 9C (L9_Q31 - L9_Q45): Maven Lifecycle, Scopes & Dependency Management ---
    {
        "id": "L9_Q31",
        "lessonId": 9,
        "type": "single",
        "title": "Trong Apache Maven, toạ độ nhận diện duy nhất một thư viện/artifact (GAV Coordinates) bao gồm 3 thành phần cốt lõi nào?",
        "code": "<dependency>\n    <groupId>org.junit.jupiter</groupId>\n    <artifactId>junit-jupiter</artifactId>\n    <version>5.10.0</version>\n</dependency>",
        "options": [
            "groupId (định danh tổ chức/công ty), artifactId (tên sản phẩm/module), version (phiên bản cụ thể)",
            "fileName, filePath, fileSize",
            "url, username, password",
            "package, class, method"
        ],
        "correctAnswer": 0,
        "explanation": "Toạ độ GAV (GroupId - ArtifactId - Version) là chuẩn mực định danh toàn cầu của Maven để phân biệt và định vị chính xác bất kỳ thư viện nhị phân nào trên Maven Central Repository hoặc kho cục bộ ~/.m2/repository.",
        "difficulty": "easy",
        "tags": ["Maven", "GAV", "Coordinates", "pom.xml"]
    },
    {
        "id": "L9_Q32",
        "lessonId": 9,
        "type": "multiple",
        "title": "Apache Maven tích hợp sẵn 3 Vòng đời xây dựng (Build Lifecycles) độc lập nào sau đây?",
        "code": None,
        "options": [
            "default (xử lý toàn bộ quá trình biên dịch, kiểm thử, đóng gói và triển khai ứng dụng)",
            "clean (chịu trách nhiệm dọn dẹp thư mục đầu ra target/ để chuẩn bị cho lần build mới)",
            "site (chịu trách nhiệm tạo tài liệu báo cáo web của dự án)",
            "compile (là vòng đời riêng biệt chạy song song với clean)"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Maven chỉ có đúng 3 vòng đời tích hợp sẵn: 1. default (core build lifecycle), 2. clean (dọn dẹp), 3. site (tạo báo cáo site). 'compile' là một phase nằm bên trong vòng đời default chứ không phải một lifecycle độc lập.",
        "difficulty": "medium",
        "tags": ["MavenLifecycles", "CleanDefaultSite", "BuildAutomation"]
    },
    {
        "id": "L9_Q33",
        "lessonId": 9,
        "type": "single",
        "title": "Thứ tự sắp xếp đúng của các pha (Phases) cốt lõi trong Vòng đời mặc định (Default Lifecycle) của Maven là gì?",
        "code": None,
        "options": [
            "validate -> compile -> test -> package -> verify -> install -> deploy",
            "compile -> validate -> test -> install -> package -> deploy",
            "clean -> compile -> package -> test -> deploy",
            "test -> compile -> validate -> package -> install"
        ],
        "correctAnswer": 0,
        "explanation": "Trình tự chuẩn của Default Lifecycle trong Maven là: 1. validate (kiểm tra dự án hợp lệ) -> 2. compile (biên dịch mã nguồn src/main) -> 3. test (chạy unit test src/test) -> 4. package (đóng gói ra .jar/.war) -> 5. verify (chạy integration test kiểm tra gói) -> 6. install (cài gói vào local repo ~/.m2) -> 7. deploy (đẩy lên remote repo).",
        "difficulty": "medium",
        "tags": ["MavenPhases", "DefaultLifecycle", "Order"]
    },
    {
        "id": "L9_Q34",
        "lessonId": 9,
        "type": "single",
        "title": "Khi bạn chạy lệnh 'mvn install' trong terminal, Maven sẽ thực thi như thế nào?",
        "code": None,
        "options": [
            "Tự động thực thi tuần tự TẤT CẢ các pha đứng trước pha install trong default lifecycle (validate, compile, test, package, verify) rồi mới thực hiện pha install",
            "Chỉ thực hiện duy nhất pha install mà không biên dịch hay kiểm thử mã nguồn",
            "Chỉ chạy các bài unit test rồi dừng lại",
            "Lỗi vì bắt buộc phải gõ đầy đủ tên của tất cả các pha"
        ],
        "correctAnswer": 0,
        "explanation": "Tính chất tuần tự (Sequential nature) của Maven: Khi gọi một phase bất kỳ, Maven sẽ tự động chạy toàn bộ các phase đứng trước nó trong lifecycle đó theo đúng thứ tự. Do đó 'mvn install' sẽ tự động compile, test, package trước khi đưa file jar vào local repository.",
        "difficulty": "easy",
        "tags": ["SequentialExecution", "MvnInstall", "MavenPhases"]
    },
    {
        "id": "L9_Q35",
        "lessonId": 9,
        "type": "single",
        "title": "Phạm vi phụ thuộc 'provided' (<scope>provided</scope>) trong file pom.xml của Maven có đặc điểm gì?",
        "code": "<dependency>\n    <groupId>javax.servlet</groupId>\n    <artifactId>javax.servlet-api</artifactId>\n    <version>4.0.1</version>\n    <scope>provided</scope>\n</dependency>",
        "options": [
            "Thư viện chỉ có mặt trong classpath tại thời điểm Biên dịch (Compile) và Kiểm thử (Test), nhưng KHÔNG ĐƯỢC đóng gói vào file .jar/.war cuối cùng vì môi trường thực thi (như Tomcat, WildFly, JDK) đã cung cấp sẵn thư viện này",
            "Thư viện chỉ dùng khi chạy unit test",
            "Thư viện chỉ có mặt khi ứng dụng chạy trên production",
            "Bắt buộc người dùng phải tự tải file jar thủ công từ Google Drive"
        ],
        "correctAnswer": 0,
        "explanation": "Scope 'provided' thông báo cho Maven rằng: Tôi cần thư viện này để code biên dịch không lỗi (compile-time), nhưng khi đóng gói ra file WAR, đừng nhét file jar này vào WEB-INF/lib vì máy chủ ứng dụng (như Tomcat đã có sẵn servlet-api.jar), giúp tránh xung đột phiên bản tại runtime.",
        "difficulty": "medium",
        "tags": ["ProvidedScope", "DependencyScopes", "Maven"]
    },
    {
        "id": "L9_Q36",
        "lessonId": 9,
        "type": "multiple",
        "title": "Phân biệt các Dependency Scope trong Maven, những khẳng định nào sau đây là ĐÚNG?",
        "code": None,
        "options": [
            "compile (mặc định): Thư viện có mặt ở cả 3 classpath (compile, test, runtime) và được đóng gói vào sản phẩm cuối cùng",
            "test: Thư viện chỉ có mặt khi biên dịch và chạy test trong thư mục src/test (như JUnit, Mockito) và không bao giờ bị đóng gói vào sản phẩm phân phối",
            "runtime: Thư viện không cần thiết khi biên dịch mã nguồn nhưng bắt buộc phải có khi chạy chương trình (ví dụ JDBC Driver của MySQL)",
            "system: Hoàn toàn giống hệt scope compile"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 là định nghĩa chuẩn xác của 3 scope quan trọng nhất: compile (default, mọi nơi), test (chỉ khi test), runtime (chỉ khi chạy). 4 sai: scope system đòi hỏi phải cấu hình thẻ <systemPath> trỏ vào đường dẫn vật lý cố định trên máy.",
        "difficulty": "medium",
        "tags": ["DependencyScopes", "CompileScope", "TestScope", "RuntimeScope"]
    },
    {
        "id": "L9_Q37",
        "lessonId": 9,
        "type": "single",
        "title": "Khi xảy ra hiện tượng Xung đột phụ thuộc bắc cầu (Transitive Dependency Conflict) giữa hai phiên bản của cùng một thư viện, Maven áp dụng quy tắc nào để quyết định phiên bản chiến thắng?",
        "code": "Project -> LibA -> LibC v1.0 (Độ sâu 2)\nProject -> LibB -> SubB -> LibC v2.0 (Độ sâu 3)",
        "options": [
            "Quy tắc 'Định nghĩa gần nhất' (Nearest-definition wins): Phiên bản nào nằm ở độ sâu nông hơn (gần với project gốc hơn trong cây phụ thuộc) sẽ được chọn (trong ví dụ trên là LibC v1.0)",
            "Quy tắc phiên bản cao nhất: Luôn chọn LibC v2.0 vì số phiên bản lớn hơn",
            "Maven sẽ báo lỗi biên dịch và bắt người dùng xóa bớt 1 thư viện",
            "Chọn ngẫu nhiên 1 trong 2 phiên bản"
        ],
        "correctAnswer": 0,
        "explanation": "Maven giải quyết xung đột dependency theo quy tắc 'Nearest-definition' (Gần nhất thắng). Ở đây LibC v1.0 có độ sâu 2, còn LibC v2.0 có độ sâu 3, do đó v1.0 chiến thắng. Nếu hai phiên bản ở cùng độ sâu, Maven áp dụng quy tắc phụ 'First-declared wins' (khai báo trước thắng).",
        "difficulty": "hard",
        "tags": ["TransitiveDependency", "ConflictResolution", "NearestDefinition"]
    },
    {
        "id": "L9_Q38",
        "lessonId": 9,
        "type": "single",
        "title": "Thư mục nào sau đây là kho lưu trữ Maven cục bộ mặc định (Local Repository) trên máy của lập trình viên?",
        "code": None,
        "options": [
            "~/.m2/repository (trên Linux/macOS) hoặc C:\\Users\\<Username>\\.m2\\repository (trên Windows)",
            "C:\\Program Files\\Maven\\repo",
            "Thư mục target/ bên trong mỗi project",
            "C:\\Windows\\System32\\maven"
        ],
        "correctAnswer": 0,
        "explanation": "Maven tải các thư viện từ Central Repository về lưu trữ tại Local Repository ở thư mục ẩn '.m2/repository' trong user home. Các project khác trên cùng máy tính có thể tái sử dụng các file .jar này mà không cần tải lại từ internet.",
        "difficulty": "easy",
        "tags": ["LocalRepository", "M2Folder", "MavenArchitecture"]
    },
    {
        "id": "L9_Q39",
        "lessonId": 9,
        "type": "single",
        "title": "Trong công cụ xây dựng hiện đại Gradle (build.gradle), cấu trúc đồ thị thực thi các tác vụ (Tasks) được xây dựng dựa trên mô hình toán học nào?",
        "code": None,
        "options": [
            "Đồ thị có hướng không chu trình (DAG - Directed Acyclic Graph)",
            "Cây nhị phân tìm kiếm cân bằng",
            "Danh sách liên kết vòng tròn",
            "Ma trận kề vô hướng"
        ],
        "correctAnswer": 0,
        "explanation": "Gradle sử dụng mô hình DAG (Directed Acyclic Graph) để mô hình hóa sự phụ thuộc giữa các Task (Task Dependency Graph). Nhờ đó Gradle có thể thực thi song song các task độc lập và bỏ qua các task không có sự thay đổi đầu vào/đầu ra (Incremental Build / Up-to-date checks).",
        "difficulty": "medium",
        "tags": ["Gradle", "DAG", "TaskGraph", "BuildTools"]
    },
    {
        "id": "L9_Q40",
        "lessonId": 9,
        "type": "multiple",
        "title": "Trong Gradle (từ phiên bản 3.4+), phân biệt giữa hai cấu hình khai báo phụ thuộc 'implementation' và 'api':",
        "code": None,
        "options": [
            "'implementation' ngăn chặn rò rỉ phụ thuộc bắc cầu (Transitive dependency leakage) sang các module khác, giúp giảm thời gian biên dịch lại khi module nội bộ thay đổi",
            "'api' xuất bản công khai thư viện đó sang cho các module phụ thuộc phía sau cùng sử dụng",
            "'implementation' được khuyến khích sử dụng mặc định thay thế cho cấu hình 'compile' cũ",
            "'api' làm cho file build chạy nhanh gấp 10 lần 'implementation'"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "1, 2 và 3 là lý do Gradle thay thế 'compile' bằng 'implementation' và 'api'. Dùng 'implementation' che giấu dependency nội bộ, khi library nội bộ update thì các module khác không bị buộc phải recompile lại.",
        "difficulty": "hard",
        "tags": ["Gradle", "ImplementationVsApi", "BuildOptimization"]
    },
    {
        "id": "L9_Q41",
        "lessonId": 9,
        "type": "single",
        "title": "Lệnh Maven nào sau đây biên dịch mã nguồn, chạy toàn bộ unit tests và đóng gói sản phẩm ra file .jar trong thư mục target/ mà KHÔNG cài đặt vào local repo?",
        "code": None,
        "options": [
            "mvn package",
            "mvn compile",
            "mvn install",
            "mvn validate"
        ],
        "correctAnswer": 0,
        "explanation": "Lệnh 'mvn package' thực hiện validate -> compile -> test -> package và tạo ra file artifact (.jar hoặc .war) nằm trong thư mục target/. Nó dừng lại ở phase package và không chạy tiếp sang phase install.",
        "difficulty": "easy",
        "tags": ["MvnPackage", "MavenPhases", "Packaging"]
    },
    {
        "id": "L9_Q42",
        "lessonId": 9,
        "type": "single",
        "title": "Nếu bạn muốn bỏ qua việc chạy các bài kiểm thử unit tests khi build dự án Maven (ví dụ để build nhanh thử nghiệm), tham số dòng lệnh nào sau đây là CHÍNH XÁC?",
        "code": None,
        "options": [
            "mvn package -DskipTests (hoặc -Dmaven.test.skip=true)",
            "mvn package --no-tests",
            "mvn package -without-test",
            "mvn package --ignore-errors"
        ],
        "correctAnswer": 0,
        "explanation": "Cờ '-DskipTests' bỏ qua việc chạy các test case nhưng vẫn biên dịch mã nguồn test. Cờ '-Dmaven.test.skip=true' bỏ qua cả việc biên dịch mã nguồn test lẫn chạy test.",
        "difficulty": "easy",
        "tags": ["SkipTests", "MavenFlags", "CLI"]
    },
    {
        "id": "L9_Q43",
        "lessonId": 9,
        "type": "multiple",
        "title": "Khối thẻ '<dependencyManagement>' trong file pom.xml của dự án Maven đa module (Multi-module project) có vai trò gì?",
        "code": "<dependencyManagement>\n    <dependencies>\n        <dependency>\n            <groupId>org.springframework.boot</groupId>\n            <artifactId>spring-boot-dependencies</artifactId>\n            <version>3.2.0</version>\n            <type>pom</type>\n            <scope>import</scope>\n        </dependency>\n    </dependencies>\n</dependencyManagement>",
        "options": [
            "Tập trung quản lý phiên bản (Version) và cấu hình của các thư viện ở một nơi duy nhất tại pom cha mà không thực sự tải hoặc thêm thư viện đó vào các module con",
            "Cho phép các module con chỉ cần khai báo groupId và artifactId mà không cần ghi rõ thẻ <version>",
            "Đảm bảo sự đồng nhất tuyệt đối về phiên bản thư viện giữa tất cả các module con trong toàn bộ hệ thống",
            "Tự động tải về tất cả các file jar trên internet ngay khi mở dự án"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Thẻ <dependencyManagement> đóng vai trò là bảng tra cứu phiên bản tập trung (BOM - Bill of Materials). Nó không tự động kéo dependency vào module nếu module đó không khai báo trong thẻ <dependencies> bình thường.",
        "difficulty": "hard",
        "tags": ["DependencyManagement", "BOM", "MultiModule"]
    },
    {
        "id": "L9_Q44",
        "lessonId": 9,
        "type": "single",
        "title": "Plugin nào của Maven chịu trách nhiệm thực thi các bài kiểm tra đơn vị (Unit Tests) trong pha 'test'?",
        "code": None,
        "options": [
            "maven-surefire-plugin",
            "maven-failsafe-plugin (chuyên dùng cho integration tests)",
            "maven-compiler-plugin",
            "maven-jar-plugin"
        ],
        "correctAnswer": 0,
        "explanation": "Trong Maven: 'maven-surefire-plugin' được gắn mặc định vào phase 'test' để chạy các unit test (các file kết thúc bằng *Test.java). Ngược lại, 'maven-failsafe-plugin' được gắn vào phase 'integration-test' và 'verify' để chạy integration tests (*IT.java).",
        "difficulty": "medium",
        "tags": ["SurefirePlugin", "FailsafePlugin", "MavenPlugins"]
    },
    {
        "id": "L9_Q45",
        "lessonId": 9,
        "type": "single",
        "title": "Trong Maven, file cấu hình 'settings.xml' (thường nằm ở ~/.m2/settings.xml) khác với file 'pom.xml' ở điểm cơ bản nào?",
        "code": None,
        "options": [
            "pom.xml cấu hình riêng cho từng dự án cụ thể (Project-level); còn settings.xml cấu hình mang tính toàn cục cho môi trường máy của lập trình viên (User/Machine-level, như cấu hình proxy, thông tin xác thực mirrors, server credentials)",
            "settings.xml chỉ dùng cho ngôn ngữ Python",
            "pom.xml chỉ có thể đọc được trên hệ điều hành Windows",
            "settings.xml bắt buộc phải được commit lên kho Git cùng mã nguồn dự án"
        ],
        "correctAnswer": 0,
        "explanation": "pom.xml chứa cấu hình nghiệp vụ của dự án và được commit lên Git chia sẻ cho cả team. settings.xml chứa thông tin nhạy cảm của cá nhân hoặc máy nội bộ (như tài khoản nexus, proxy công ty, master password) và KHÔNG ĐƯỢC commit lên Git.",
        "difficulty": "medium",
        "tags": ["SettingsXml", "PomXml", "MavenConfig"]
    },

    # --- ĐỀ 9D (L9_Q46 - L9_Q60): Git Workflows, Checkstyle & CI/CD Pipelines ---
    {
        "id": "L9_Q46",
        "lessonId": 9,
        "type": "single",
        "title": "So sánh giữa chiến lược 'Git Flow' và 'Trunk-Based Development' trong quản lý phiên bản mã nguồn:",
        "code": None,
        "options": [
            "Git Flow sử dụng nhiều nhánh dài hạn (develop, master, release, hotfix) với quy trình phát hành theo chu kỳ lớn; Trunk-Based Development khuyến khích các lập trình viên tích hợp thường xuyên trực tiếp vào một nhánh chính duy nhất (trunk/main) thông qua các nhánh tính năng rất ngắn ngày",
            "Git Flow không hỗ trợ merge code",
            "Trunk-Based Development bắt buộc chỉ có một người duy nhất được commit",
            "Git Flow chỉ dùng được cho dự án mã nguồn mở"
        ],
        "correctAnswer": 0,
        "explanation": "Git Flow là mô hình nhánh phức tạp với nhiều nhánh tồn tại lâu (develop, feature dài ngày), dễ dẫn tới 'Merge Hell' khi gộp nhánh. Trunk-Based Development là xu hướng hiện đại của DevOps/CI-CD: mọi người commit hàng ngày vào main/trunk, kết hợp Feature Toggles để ẩn tính năng chưa xong, giúp tích hợp liên tục thực sự.",
        "difficulty": "medium",
        "tags": ["GitFlow", "TrunkBasedDevelopment", "BranchingStrategies"]
    },
    {
        "id": "L9_Q47",
        "lessonId": 9,
        "type": "single",
        "title": "Sự khác biệt cốt lõi giữa lệnh 'git merge' và 'git rebase' khi tích hợp nhánh tính năng vào nhánh chính là gì?",
        "code": None,
        "options": [
            "'git merge' tạo ra một commit gộp mới (Merge Commit) và bảo toàn chính xác lịch sử phân nhánh theo thời gian; 'git rebase' viết lại lịch sử commit bằng cách đặt các commit của nhánh lên trên đỉnh của nhánh đích, tạo ra một lịch sử tuyến tính phẳng đẹp",
            "'git rebase' xóa bỏ toàn bộ mã nguồn của nhánh tính năng",
            "'git merge' chỉ chạy được khi không có xung đột (conflict)",
            "Hai lệnh hoàn toàn giống nhau 100%"
        ],
        "correctAnswer": 0,
        "explanation": "git merge giữ nguyên lịch sử rẽ nhánh thực tế (kèm merge commit). git rebase viết lại lịch sử (rewriting commit history) làm nhánh thẳng tắp. NGUYÊN TẮC VÀNG: Không bao giờ rebase trên các nhánh công khai/dùng chung (như main, develop) vì sẽ làm sai lệch lịch sử của các thành viên khác.",
        "difficulty": "medium",
        "tags": ["GitMerge", "GitRebase", "GitInternals"]
    },
    {
        "id": "L9_Q48",
        "lessonId": 9,
        "type": "single",
        "title": "Hiện tượng 'Fast-Forward Merge' trong Git xảy ra trong điều kiện nào?",
        "code": None,
        "options": [
            "Khi nhánh đích (target branch) chưa có bất kỳ commit mới nào kể từ thời điểm nhánh tính năng (feature branch) được tách ra; Git chỉ việc di chuyển con trỏ của nhánh đích trỏ thẳng tới commit cuối của nhánh tính năng mà không cần tạo commit gộp",
            "Khi mạng Internet có tốc độ cáp quang trên 1Gbps",
            "Khi có xung đột mã nguồn xảy ra",
            "Khi sử dụng lệnh git push --force"
        ],
        "correctAnswer": 0,
        "explanation": "Fast-forward merge xảy ra khi lịch sử của nhánh nguồn chứa toàn bộ lịch sử của nhánh đích mà nhánh đích không có commit nào mới xen giữa. Git chỉ đơn thuần dịch chuyển con trỏ HEAD của nhánh đích về phía trước.",
        "difficulty": "easy",
        "tags": ["FastForward", "GitMerge", "BranchPointer"]
    },
    {
        "id": "L9_Q49",
        "lessonId": 9,
        "type": "multiple",
        "title": "Công cụ phân tích mã tĩnh Checkstyle (như maven-checkstyle-plugin) trong các dự án Java thường kiểm tra và bắt lỗi những vi phạm nào?",
        "code": None,
        "options": [
            "Quy ước đặt tên (Naming Conventions: tên biến camelCase, tên class PascalCase, hằng số ALL_CAPS)",
            "Độ dài tối đa của phương thức (Method Length), số lượng tham số tối đa của hàm",
            "Định dạng mã nguồn: Thụt lề (Indentation), khoảng trắng, dấu ngoặc nhọn, vị trí import",
            "Hiệu năng chạy thực tế của thuật toán khi xử lý 1 triệu bản ghi"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Checkstyle là công cụ phân tích tĩnh (Static Analysis) kiểm tra cú pháp và phong cách viết mã (Code Style/Conventions) dựa trên file cấu hình XML (như Sun Checks hoặc Google Java Style). Nó không chạy mã nên không đo lường hiệu năng runtime.",
        "difficulty": "easy",
        "tags": ["Checkstyle", "StaticAnalysis", "CodingStandards"]
    },
    {
        "id": "L9_Q50",
        "lessonId": 9,
        "type": "single",
        "title": "Mục tiêu cốt lõi của Tích hợp liên tục (Continuous Integration - CI) là gì?",
        "code": None,
        "options": [
            "Tự động hóa quá trình biên dịch (build) và kiểm thử (test) mã nguồn ngay khi có thành viên đẩy commit mới hoặc tạo Pull Request, giúp phát hiện lỗi tích hợp càng sớm càng tốt",
            "Tự động gửi email đòi nợ khách hàng",
            "Tự động tạo ra các bài kiểm tra trắc nghiệm",
            "Loại bỏ hoàn toàn vai trò của lập trình viên"
        ],
        "correctAnswer": 0,
        "explanation": "CI (Continuous Integration) là thực hành văn hóa và kỹ thuật nơi các nhà phát triển gộp mã thường xuyên vào nhánh chính. Mỗi lần gộp được tự động kiểm chứng bằng build và automated test để phát hiện lỗi tích hợp ngay trong vòng vài phút.",
        "difficulty": "easy",
        "tags": ["ContinuousIntegration", "DevOps", "Automation"]
    },
    {
        "id": "L9_Q51",
        "lessonId": 9,
        "type": "single",
        "title": "Sự khác biệt căn bản giữa 'Continuous Delivery' và 'Continuous Deployment' là gì?",
        "code": None,
        "options": [
            "Continuous Delivery tự động hóa toàn bộ các bước cho đến khi bản dựng sẵn sàng triển khai, nhưng bước release lên Production cần sự phê duyệt thủ công của con người (Manual Approval); còn Continuous Deployment tự động triển khai thẳng lên Production mà không cần bất kỳ sự can thiệp thủ công nào",
            "Continuous Delivery chỉ dùng cho ứng dụng di động",
            "Continuous Deployment không cần chạy unit tests",
            "Cả hai khái niệm hoàn toàn đồng nghĩa 100%"
        ],
        "correctAnswer": 0,
        "explanation": "Sự khác biệt nằm ở bước cuối cùng lên Production: Trong Continuous Delivery, phần mềm luôn ở trạng thái sẵn sàng release, nhưng quyết định bấm nút deploy do con người/doanh nghiệp quyết định. Trong Continuous Deployment, nếu vượt qua mọi bài test tự động của pipeline, code sẽ tự động bay thẳng lên Production.",
        "difficulty": "medium",
        "tags": ["ContinuousDelivery", "ContinuousDeployment", "Comparison"]
    },
    {
        "id": "L9_Q52",
        "lessonId": 9,
        "type": "multiple",
        "title": "Cấu trúc một file kịch bản tự động hóa GitHub Actions (.github/workflows/*.yml) bao gồm những thành phần cơ bản nào?",
        "code": None,
        "options": [
            "Triggers (on: push, pull_request): Sự kiện kích hoạt quy trình tự động",
            "Jobs: Một hoặc nhiều nhóm tác vụ độc lập chạy trên máy ảo runner (ví dụ: runs-on: ubuntu-latest)",
            "Steps: Chuỗi các bước tuần tự bên trong một job (gồm action có sẵn qua uses: hoặc câu lệnh bash qua run:)",
            "Bắt buộc phải cài đặt máy chủ vật lý riêng tại nhà mới chạy được"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "GitHub Actions workflow định nghĩa bằng YAML gồm: Triggers (khi nào chạy), Jobs (chạy trên runner nào: ubuntu, windows, macos), và Steps (các bước chi tiết). GitHub cung cấp sẵn runner trên đám mây miễn phí.",
        "difficulty": "medium",
        "tags": ["GitHubActions", "WorkflowYAML", "DevOps"]
    },
    {
        "id": "L9_Q53",
        "lessonId": 9,
        "type": "single",
        "title": "Xem xét đoạn kịch bản GitHub Actions sau. Bước 'actions/setup-java@v4' có vai trò gì trong pipeline?",
        "code": "- name: Set up JDK 17\n  uses: actions/setup-java@v4\n  with:\n    java-version: '17'\n    distribution: 'temurin'\n    cache: maven",
        "options": [
            "Cài đặt môi trường máy ảo Java JDK 17 (bản phân phối Eclipse Temurin) lên máy ảo runner và kích hoạt cơ chế bộ nhớ đệm (cache) cho các thư viện Maven",
            "Biên dịch mã nguồn Java thành file .exe",
            "Tự động viết thêm các bài unit test còn thiếu",
            "Tải toàn bộ cơ sở dữ liệu MySQL lên đám mây"
        ],
        "correctAnswer": 0,
        "explanation": "'setup-java' là official action của GitHub giúp thiết lập nhanh môi trường JDK chỉ định trên runner và tích hợp sẵn tính năng cache các dependency Maven để tăng tốc độ cho các lần build tiếp theo.",
        "difficulty": "easy",
        "tags": ["SetupJava", "GitHubActions", "MavenCache"]
    },
    {
        "id": "L9_Q54",
        "lessonId": 9,
        "type": "single",
        "title": "Trong quy trình làm việc nhóm với Git, thao tác 'Pull Request' (PR) hoặc 'Merge Request' (MR) đóng vai trò chính là gì?",
        "code": None,
        "options": [
            "Là cơ chế để một lập trình viên yêu cầu sáp nhập nhánh tính năng của mình vào nhánh chính, tạo không gian để các thành viên khác xem xét mã nguồn (Code Review), chạy kiểm thử CI tự động trước khi phê duyệt",
            "Để xóa toàn bộ tài khoản Git của thành viên vi phạm",
            "Để sao chép toàn bộ dự án về máy tính cá nhân",
            "Chỉ dùng khi dự án bị lỗi hỏng máy chủ"
        ],
        "correctAnswer": 0,
        "explanation": "Pull Request là trụ cột của quy trình phát triển hiện đại: cho phép đồng nghiệp review code, thảo luận, phát hiện lỗi thiết kế và cho phép hệ thống CI tự động chạy kiểm thử trước khi code được phép hòa vào nhánh chính.",
        "difficulty": "easy",
        "tags": ["PullRequest", "CodeReview", "GitCollaboration"]
    },
    {
        "id": "L9_Q55",
        "lessonId": 9,
        "type": "multiple",
        "title": "Những lợi ích quan trọng nhất của việc duy trì một hệ thống CI/CD tự động trong dự án phần mềm là gì?",
        "code": None,
        "options": [
            "Giảm thiểu rủi ro khi phát hành sản phẩm nhờ việc kiểm thử liên tục mọi thay đổi nhỏ",
            "Rút ngắn thời gian đưa sản phẩm ra thị trường (Time-to-Market)",
            "Loại bỏ các thao tác đóng gói và triển khai thủ công dễ gây nhầm lẫn sai sót của con người",
            "Đảm bảo mã nguồn không bao giờ cần phải viết thêm tài liệu"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "CI/CD giúp phát hiện lỗi sớm (Fail Fast), tự động hóa quy trình deploy tẻ nhạt, giảm lỗi con người và tăng tốc độ release phần mềm. Nó không thể thay thế cho việc viết tài liệu kỹ thuật.",
        "difficulty": "easy",
        "tags": ["BenefitsOfCICD", "Automation", "SoftwareEngineering"]
    },
    {
        "id": "L9_Q56",
        "lessonId": 9,
        "type": "single",
        "title": "Trong file cấu hình '.gitignore' của dự án Java sử dụng Maven, những thư mục/tập tin nào sau đây BẮT BUỘC nên được thêm vào để tránh đẩy rác lên Git?",
        "code": None,
        "options": [
            "target/, *.class, .idea/, *.iml, .project, .settings/",
            "src/main/java/",
            "pom.xml",
            "README.md"
        ],
        "correctAnswer": 0,
        "explanation": "Thư mục target/ chứa các file biên dịch nhị phân .class, các file cấu hình IDE (.idea, .project) là các file sinh tự động theo môi trường cục bộ và tuyệt đối không bao giờ được commit lên Git. Các file mã nguồn src/ và pom.xml bắt buộc phải được theo dõi bởi Git.",
        "difficulty": "easy",
        "tags": ["GitIgnore", "TargetFolder", "CleanRepository"]
    },
    {
        "id": "L9_Q57",
        "lessonId": 9,
        "type": "single",
        "title": "Nguyên tắc 'Fail Fast' trong đường ống CI/CD (Pipeline) khuyến nghị điều gì?",
        "code": None,
        "options": [
            "Nên chạy các bước kiểm tra nhanh và rẻ nhất trước (như Checkstyle, Compile, Unit Test); nếu phát hiện lỗi thì dừng ngay pipeline và thông báo cho lập trình viên lập tức trước khi chạy các bước nặng nề tốn kém (như Integration Test, Security Scan, Deploy)",
            "Cố tình làm cho hệ thống bị sập càng nhanh càng tốt",
            "Bỏ qua tất cả các bài kiểm tra nếu có lỗi xảy ra",
            "Chỉ kiểm tra mã nguồn vào ban đêm"
        ],
        "correctAnswer": 0,
        "explanation": "Fail Fast tiết kiệm thời gian và tài nguyên máy tính: nếu mã nguồn sai convention hoặc fail 1 bài unit test nhỏ, pipeline dừng ngay trong 30 giây thay vì phải đợi 30 phút chạy hết integration test hay build docker image rồi mới báo lỗi.",
        "difficulty": "medium",
        "tags": ["FailFast", "PipelineOptimization", "DevOps"]
    },
    {
        "id": "L9_Q58",
        "lessonId": 9,
        "type": "single",
        "title": "Khi thực hiện lệnh 'git merge feature' và xuất hiện xung đột (Merge Conflict), lập trình viên cần làm gì để hoàn tất việc gộp nhánh?",
        "code": None,
        "options": [
            "Mở các file bị xung đột, chỉnh sửa bằng tay để thống nhất phần mã chính xác, xóa các ký tự đánh dấu (<<<<<<<, =======, >>>>>>>), sau đó dùng lệnh 'git add' và 'git commit' để hoàn tất",
            "Xóa toàn bộ thư mục .git và khởi tạo lại",
            "Tắt máy tính và tạo lại nhánh mới",
            "Chỉ cần gõ lệnh git push --force là xung đột tự động biến mất"
        ],
        "correctAnswer": 0,
        "explanation": "Quy trình giải quyết conflict chuẩn: Git chèn các conflict markers (<<<<<<< HEAD ... ======= ... >>>>>>>). Lập trình viên mở file, trao đổi với đồng nghiệp để quyết định giữ đoạn mã nào, lưu file, git add và commit merge commit.",
        "difficulty": "easy",
        "tags": ["MergeConflict", "GitResolution", "VersionControl"]
    },
    {
        "id": "L9_Q59",
        "lessonId": 9,
        "type": "multiple",
        "title": "Trong một kịch bản CI/CD, các bài kiểm thử kiểm thử hồi quy và tích hợp (Integration Tests) thường được phân tách với Unit Tests vì những lý do nào?",
        "code": None,
        "options": [
            "Unit Tests kiểm tra các hàm/lớp cô lập và chạy cực nhanh (mili-giây), cần chạy liên tục mỗi khi code thay đổi",
            "Integration Tests kiểm tra sự phối hợp giữa nhiều thành phần (kết nối DB thật, mạng, hệ thống file), chạy chậm hơn nhiều (vài phút đến hàng giờ)",
            "Tách riêng giúp lập trình viên nhận được phản hồi nhanh (Fast Feedback) từ Unit Tests trước khi chạy Integration Tests nặng",
            "Integration Tests chỉ có thể viết bằng ngôn ngữ Python chứ không thể viết bằng Java"
        ],
        "correctAnswer": [0, 1, 2],
        "explanation": "Mô hình Kim tự tháp kiểm thử (Test Pyramid) khuyến cáo: đáy kim tự tháp là nhiều Unit Tests chạy siêu nhanh; tầng giữa là Integration Tests chạy chậm hơn; tầng trên cùng là E2E Tests. Tách riêng giúp tối ưu hóa thời gian phản hồi của CI pipeline.",
        "difficulty": "medium",
        "tags": ["TestPyramid", "UnitVsIntegration", "PipelineDesign"]
    },
    {
        "id": "L9_Q60",
        "lessonId": 9,
        "type": "single",
        "title": "Lệnh Git nào sau đây cho phép hủy bỏ (undo) các thay đổi chưa được commit trong thư mục làm việc (Working Directory) để khôi phục lại trạng thái commit gần nhất?",
        "code": None,
        "options": [
            "git restore <file> (hoặc git checkout -- <file> trong phiên bản cũ)",
            "git push",
            "git commit --amend",
            "git remote -v"
        ],
        "correctAnswer": 0,
        "explanation": "Từ Git 2.23, lệnh 'git restore <file>' được giới thiệu để khôi phục nội dung file trong working directory về trạng thái của commit gần nhất (hoặc 'git restore --staged <file>' để bỏ stage). Lệnh cũ tương đương là 'git checkout -- <file>'.",
        "difficulty": "easy",
        "tags": ["GitRestore", "WorkingTree", "GitCommands"]
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
    update_file("lesson8.json", L8_NEW)
    update_file("lesson9.json", L9_NEW)
    print("All 60 questions for Lessons 8 and 9 generated and appended successfully.")
