from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrapTogetherSpan"]

class WrapTogetherSpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/WrapTogetherSpan"