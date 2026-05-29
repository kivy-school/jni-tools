from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CSVParser"]

class CSVParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/commons/csv/CSVParser"
    __javaconstructor__ = [("(Ljava/io/Reader;Lorg/apache/commons/csv/CSVFormat;JJ)V", False), ("(Ljava/io/Reader;Lorg/apache/commons/csv/CSVFormat;)V", False)]
    iterator = JavaMethod("()Ljava/util/Iterator;")
    stream = JavaMethod("()Ljava/util/stream/Stream;")
    close = JavaMethod("()V")
    parse = JavaMultipleMethod([("(Ljava/io/File;Ljava/nio/charset/Charset;Lorg/apache/commons/csv/CSVFormat;)Lorg/apache/commons/csv/CSVParser;", True, False), ("(Ljava/nio/file/Path;Ljava/nio/charset/Charset;Lorg/apache/commons/csv/CSVFormat;)Lorg/apache/commons/csv/CSVParser;", True, False), ("(Ljava/io/Reader;Lorg/apache/commons/csv/CSVFormat;)Lorg/apache/commons/csv/CSVParser;", True, False), ("(Ljava/io/InputStream;Ljava/nio/charset/Charset;Lorg/apache/commons/csv/CSVFormat;)Lorg/apache/commons/csv/CSVParser;", True, False), ("(Ljava/lang/String;Lorg/apache/commons/csv/CSVFormat;)Lorg/apache/commons/csv/CSVParser;", True, False), ("(Ljava/net/URL;Ljava/nio/charset/Charset;Lorg/apache/commons/csv/CSVFormat;)Lorg/apache/commons/csv/CSVParser;", True, False)])
    getCurrentLineNumber = JavaMethod("()J")
    isClosed = JavaMethod("()Z")
    getFirstEndOfLine = JavaMethod("()Ljava/lang/String;")
    getHeaderComment = JavaMethod("()Ljava/lang/String;")
    getHeaderMap = JavaMethod("()Ljava/util/Map;")
    getHeaderNames = JavaMethod("()Ljava/util/List;")
    getRecordNumber = JavaMethod("()J")
    getRecords = JavaMethod("()Ljava/util/List;")
    getTrailerComment = JavaMethod("()Ljava/lang/String;")
    hasHeaderComment = JavaMethod("()Z")
    hasTrailerComment = JavaMethod("()Z")