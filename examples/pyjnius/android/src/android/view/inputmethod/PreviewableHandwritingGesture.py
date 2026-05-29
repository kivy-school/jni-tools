from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreviewableHandwritingGesture"]

class PreviewableHandwritingGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/PreviewableHandwritingGesture"
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")