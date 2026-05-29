from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Array"]

class Array(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Array"
    getResultSet = JavaMultipleMethod([("(Ljava/util/Map;)Ljava/sql/ResultSet;", False, False), ("(JI)Ljava/sql/ResultSet;", False, False), ("(JILjava/util/Map;)Ljava/sql/ResultSet;", False, False), ("()Ljava/sql/ResultSet;", False, False)])
    getBaseTypeName = JavaMethod("()Ljava/lang/String;")
    getBaseType = JavaMethod("()I")
    close = JavaMethod("()V")
    getArray = JavaMultipleMethod([("(JILjava/util/Map;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False), ("(Ljava/util/Map;)Ljava/lang/Object;", False, False), ("(JI)Ljava/lang/Object;", False, False)])
    free = JavaMethod("()V")