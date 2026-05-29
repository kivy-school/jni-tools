from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JavascriptInterface"]

class JavascriptInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/JavascriptInterface"