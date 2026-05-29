from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SafeBrowsingResponse"]

class SafeBrowsingResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/SafeBrowsingResponse"
    __javaconstructor__ = [("()V", False)]
    backToSafety = JavaMethod("(Z)V")
    proceed = JavaMethod("(Z)V")
    showInterstitial = JavaMethod("(Z)V")