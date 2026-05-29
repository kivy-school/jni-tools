from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrapTogetherSpan"]

class WrapTogetherSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/WrapTogetherSpan"