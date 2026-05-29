from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpParams"]

class HttpParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/params/HttpParams"
    setLongParameter = JavaMethod("(Ljava/lang/String;J)Lorg/apache/http/params/HttpParams;")
    getIntParameter = JavaMethod("(Ljava/lang/String;I)I")
    getLongParameter = JavaMethod("(Ljava/lang/String;J)J")
    getDoubleParameter = JavaMethod("(Ljava/lang/String;D)D")
    getBooleanParameter = JavaMethod("(Ljava/lang/String;Z)Z")
    isParameterFalse = JavaMethod("(Ljava/lang/String;)Z")
    isParameterTrue = JavaMethod("(Ljava/lang/String;)Z")
    removeParameter = JavaMethod("(Ljava/lang/String;)Z")
    setBooleanParameter = JavaMethod("(Ljava/lang/String;Z)Lorg/apache/http/params/HttpParams;")
    setDoubleParameter = JavaMethod("(Ljava/lang/String;D)Lorg/apache/http/params/HttpParams;")
    setIntParameter = JavaMethod("(Ljava/lang/String;I)Lorg/apache/http/params/HttpParams;")
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Lorg/apache/http/params/HttpParams;")
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    copy = JavaMethod("()Lorg/apache/http/params/HttpParams;")