from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DriverManager"]

class DriverManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/DriverManager"
    getLogWriter = JavaStaticMethod("()Ljava/io/PrintWriter;")
    setLogWriter = JavaStaticMethod("(Ljava/io/PrintWriter;)V")
    getConnection = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/Properties;)Ljava/sql/Connection;", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/sql/Connection;", True, False), ("(Ljava/lang/String;)Ljava/sql/Connection;", True, False)])
    getDriver = JavaStaticMethod("(Ljava/lang/String;)Ljava/sql/Driver;")
    registerDriver = JavaStaticMethod("(Ljava/sql/Driver;)V")
    deregisterDriver = JavaStaticMethod("(Ljava/sql/Driver;)V")
    getDrivers = JavaStaticMethod("()Ljava/util/Enumeration;")
    setLoginTimeout = JavaStaticMethod("(I)V")
    getLoginTimeout = JavaStaticMethod("()I")
    setLogStream = JavaStaticMethod("(Ljava/io/PrintStream;)V")
    getLogStream = JavaStaticMethod("()Ljava/io/PrintStream;")
    println = JavaStaticMethod("(Ljava/lang/String;)V")