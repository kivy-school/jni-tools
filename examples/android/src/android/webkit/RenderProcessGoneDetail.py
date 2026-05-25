from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderProcessGoneDetail"]

class RenderProcessGoneDetail(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/RenderProcessGoneDetail"
    __javaconstructor__ = [("()V", False)]
    didCrash = JavaMethod("()Z")
    rendererPriorityAtExit = JavaMethod("()I")