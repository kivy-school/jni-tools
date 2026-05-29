from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ElementType"]

class ElementType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/ElementType"
    TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    FIELD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    METHOD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    CONSTRUCTOR = JavaStaticField("Ljava/lang/annotation/ElementType;")
    LOCAL_VARIABLE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    ANNOTATION_TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PACKAGE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_USE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    MODULE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    RECORD_COMPONENT = JavaStaticField("Ljava/lang/annotation/ElementType;")
    values = JavaStaticMethod("()[Ljava/lang/annotation/ElementType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/annotation/ElementType;")
    TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    FIELD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    METHOD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    CONSTRUCTOR = JavaStaticField("Ljava/lang/annotation/ElementType;")
    LOCAL_VARIABLE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    ANNOTATION_TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PACKAGE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_USE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    MODULE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    RECORD_COMPONENT = JavaStaticField("Ljava/lang/annotation/ElementType;")