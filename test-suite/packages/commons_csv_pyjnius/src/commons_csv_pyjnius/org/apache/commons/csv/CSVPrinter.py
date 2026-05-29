from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CSVPrinter"]

class CSVPrinter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/commons/csv/CSVPrinter"
    __javaconstructor__ = [("(Ljava/lang/Appendable;Lorg/apache/commons/csv/CSVFormat;)V", False)]
    println = JavaMethod("()V")
    flush = JavaMethod("()V")
    print = JavaMethod("(Ljava/lang/Object;)V")
    close = JavaMultipleMethod([("(Z)V", False, False), ("()V", False, False)])
    printRecord = JavaMultipleMethod([("(Ljava/util/stream/Stream;)V", False, False), ("(Ljava/lang/Iterable;)V", False, False), ("([Ljava/lang/Object;)V", False, True)])
    printComment = JavaMethod("(Ljava/lang/String;)V")
    printRecords = JavaMultipleMethod([("(Ljava/util/stream/Stream;)V", False, False), ("([Ljava/lang/Object;)V", False, True), ("(Ljava/sql/ResultSet;)V", False, False), ("(Ljava/sql/ResultSet;Z)V", False, False), ("(Ljava/lang/Iterable;)V", False, False)])
    printHeaders = JavaMethod("(Ljava/sql/ResultSet;)V")
    getOut = JavaMethod("()Ljava/lang/Appendable;")