from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableCallSite"]

class MutableCallSite(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/MutableCallSite"
    __javaconstructor__ = [("(Ljava/lang/invoke/MethodType;)V", False), ("(Ljava/lang/invoke/MethodHandle;)V", False)]
    getTarget = JavaMethod("()Ljava/lang/invoke/MethodHandle;")
    dynamicInvoker = JavaMethod("()Ljava/lang/invoke/MethodHandle;")
    setTarget = JavaMethod("(Ljava/lang/invoke/MethodHandle;)V")
    syncAll = JavaStaticMethod("([Ljava/lang/invoke/MutableCallSite;)V")