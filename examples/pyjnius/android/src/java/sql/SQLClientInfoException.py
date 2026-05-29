from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLClientInfoException"]

class SQLClientInfoException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLClientInfoException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/util/Map;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/util/Map;Ljava/lang/Throwable;)V", False), ("()V", False), ("(Ljava/util/Map;)V", False), ("(Ljava/util/Map;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/util/Map;)V", False)]
    getFailedProperties = JavaMethod("()Ljava/util/Map;")