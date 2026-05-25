from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpParams"]

class HttpParams(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/params/HttpParams"
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Lorg/apache/http/params/HttpParams;")
    copy = JavaMethod("()Lorg/apache/http/params/HttpParams;")
    removeParameter = JavaMethod("(Ljava/lang/String;)Z")
    getLongParameter = JavaMethod("(Ljava/lang/String;J)J")
    setLongParameter = JavaMethod("(Ljava/lang/String;J)Lorg/apache/http/params/HttpParams;")
    getIntParameter = JavaMethod("(Ljava/lang/String;I)I")
    setIntParameter = JavaMethod("(Ljava/lang/String;I)Lorg/apache/http/params/HttpParams;")
    getDoubleParameter = JavaMethod("(Ljava/lang/String;D)D")
    setDoubleParameter = JavaMethod("(Ljava/lang/String;D)Lorg/apache/http/params/HttpParams;")
    getBooleanParameter = JavaMethod("(Ljava/lang/String;Z)Z")
    setBooleanParameter = JavaMethod("(Ljava/lang/String;Z)Lorg/apache/http/params/HttpParams;")
    isParameterTrue = JavaMethod("(Ljava/lang/String;)Z")
    isParameterFalse = JavaMethod("(Ljava/lang/String;)Z")