from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallSite"]

class CallSite(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/CallSite"
    type = JavaMethod("()Ljava/lang/invoke/MethodType;")
    getTarget = JavaMethod("()Ljava/lang/invoke/MethodHandle;")
    dynamicInvoker = JavaMethod("()Ljava/lang/invoke/MethodHandle;")
    setTarget = JavaMethod("(Ljava/lang/invoke/MethodHandle;)V")