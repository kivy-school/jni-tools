from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeView"]

class AttributeView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AttributeView"
    name = JavaMethod("()Ljava/lang/String;")