from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebViewMethodCalledOnWrongThreadViolation"]

class WebViewMethodCalledOnWrongThreadViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/WebViewMethodCalledOnWrongThreadViolation"