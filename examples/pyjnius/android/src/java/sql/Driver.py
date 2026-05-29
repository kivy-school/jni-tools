from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Driver"]

class Driver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Driver"
    getMinorVersion = JavaMethod("()I")
    connect = JavaMethod("(Ljava/lang/String;Ljava/util/Properties;)Ljava/sql/Connection;")
    acceptsURL = JavaMethod("(Ljava/lang/String;)Z")
    getPropertyInfo = JavaMethod("(Ljava/lang/String;Ljava/util/Properties;)[Ljava/sql/DriverPropertyInfo;")
    jdbcCompliant = JavaMethod("()Z")
    getParentLogger = JavaMethod("()Ljava/util/logging/Logger;")
    getMajorVersion = JavaMethod("()I")