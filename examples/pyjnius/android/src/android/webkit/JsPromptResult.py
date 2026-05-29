from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JsPromptResult"]

class JsPromptResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/JsPromptResult"
    confirm = JavaMethod("(Ljava/lang/String;)V")