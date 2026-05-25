from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Array"]

class Array(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Array"
    getBaseTypeName = JavaMethod("()Ljava/lang/String;")
    getBaseType = JavaMethod("()I")
    getArray = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/util/Map;)Ljava/lang/Object;", False, False), ("(JI)Ljava/lang/Object;", False, False), ("(JILjava/util/Map;)Ljava/lang/Object;", False, False)])
    getResultSet = JavaMultipleMethod([("()Ljava/sql/ResultSet;", False, False), ("(Ljava/util/Map;)Ljava/sql/ResultSet;", False, False), ("(JI)Ljava/sql/ResultSet;", False, False), ("(JILjava/util/Map;)Ljava/sql/ResultSet;", False, False)])
    free = JavaMethod("()V")