from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Result"]

class Result(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Result"
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")