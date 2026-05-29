from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CommonDataSource"]

class CommonDataSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/CommonDataSource"
    getLogWriter = JavaMethod("()Ljava/io/PrintWriter;")
    setLogWriter = JavaMethod("(Ljava/io/PrintWriter;)V")
    setLoginTimeout = JavaMethod("(I)V")
    getLoginTimeout = JavaMethod("()I")
    getParentLogger = JavaMethod("()Ljava/util/logging/Logger;")
    createShardingKeyBuilder = JavaMethod("()Ljava/sql/ShardingKeyBuilder;")