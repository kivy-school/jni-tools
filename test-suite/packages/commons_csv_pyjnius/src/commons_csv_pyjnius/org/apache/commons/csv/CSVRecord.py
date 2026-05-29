from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CSVRecord"]

class CSVRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/commons/csv/CSVRecord"
    size = JavaMethod("()I")
    get = JavaMultipleMethod([("(Ljava/lang/Enum;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaMethod("()[Ljava/lang/String;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    toList = JavaMethod("()Ljava/util/List;")
    stream = JavaMethod("()Ljava/util/stream/Stream;")
    toMap = JavaMethod("()Ljava/util/Map;")
    isSet = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(I)Z", False, False)])
    isMapped = JavaMethod("(Ljava/lang/String;)Z")
    putIn = JavaMethod("(Ljava/util/Map;)Ljava/util/Map;")
    getParser = JavaMethod("()Lorg/apache/commons/csv/CSVParser;")
    hasComment = JavaMethod("()Z")
    isConsistent = JavaMethod("()Z")
    getCharacterPosition = JavaMethod("()J")
    getRecordNumber = JavaMethod("()J")
    getComment = JavaMethod("()Ljava/lang/String;")