from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DriverPropertyInfo"]

class DriverPropertyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/DriverPropertyInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    name = JavaField("Ljava/lang/String;")
    description = JavaField("Ljava/lang/String;")
    required = JavaField("Z")
    value = JavaField("Ljava/lang/String;")
    choices = JavaField("[Ljava/lang/String;")