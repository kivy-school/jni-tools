from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DriverManager"]

class DriverManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/DriverManager"
    getConnection = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/sql/Connection;", True, False), ("(Ljava/lang/String;Ljava/util/Properties;)Ljava/sql/Connection;", True, False), ("(Ljava/lang/String;)Ljava/sql/Connection;", True, False)])
    getLogWriter = JavaStaticMethod("()Ljava/io/PrintWriter;")
    registerDriver = JavaMultipleMethod([("(Ljava/sql/Driver;)V", True, False), ("(Ljava/sql/Driver;Ljava/sql/DriverAction;)V", True, False)])
    getDrivers = JavaStaticMethod("()Ljava/util/Enumeration;")
    setLogWriter = JavaStaticMethod("(Ljava/io/PrintWriter;)V")
    getDriver = JavaStaticMethod("(Ljava/lang/String;)Ljava/sql/Driver;")
    deregisterDriver = JavaStaticMethod("(Ljava/sql/Driver;)V")
    drivers = JavaStaticMethod("()Ljava/util/stream/Stream;")
    setLoginTimeout = JavaStaticMethod("(I)V")
    getLoginTimeout = JavaStaticMethod("()I")
    setLogStream = JavaStaticMethod("(Ljava/io/PrintStream;)V")
    getLogStream = JavaStaticMethod("()Ljava/io/PrintStream;")
    println = JavaStaticMethod("(Ljava/lang/String;)V")