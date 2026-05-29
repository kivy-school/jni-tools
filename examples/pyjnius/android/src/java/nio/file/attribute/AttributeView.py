from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeView"]

class AttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AttributeView"
    name = JavaMethod("()Ljava/lang/String;")