from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLClientInfoException"]

class SQLClientInfoException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLClientInfoException"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Map;)V", False), ("(Ljava/util/Map;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/util/Map;)V", False), ("(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/util/Map;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/util/Map;Ljava/lang/Throwable;)V", False)]
    getFailedProperties = JavaMethod("()Ljava/util/Map;")