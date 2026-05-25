from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Driver"]

class Driver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Driver"
    connect = JavaMethod("(Ljava/lang/String;Ljava/util/Properties;)Ljava/sql/Connection;")
    acceptsURL = JavaMethod("(Ljava/lang/String;)Z")
    getPropertyInfo = JavaMethod("(Ljava/lang/String;Ljava/util/Properties;)[Ljava/sql/DriverPropertyInfo;")
    getMajorVersion = JavaMethod("()I")
    getMinorVersion = JavaMethod("()I")
    jdbcCompliant = JavaMethod("()Z")