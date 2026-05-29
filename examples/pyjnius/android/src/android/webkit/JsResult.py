from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JsResult"]

class JsResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/JsResult"
    cancel = JavaMethod("()V")
    confirm = JavaMethod("()V")