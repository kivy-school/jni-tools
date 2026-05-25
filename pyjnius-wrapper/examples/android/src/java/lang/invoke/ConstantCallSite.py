from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConstantCallSite"]

class ConstantCallSite(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/ConstantCallSite"
    __javaconstructor__ = [("(Ljava/lang/invoke/MethodHandle;)V", False), ("(Ljava/lang/invoke/MethodType;Ljava/lang/invoke/MethodHandle;)V", False)]
    getTarget = JavaMethod("()Ljava/lang/invoke/MethodHandle;")
    setTarget = JavaMethod("(Ljava/lang/invoke/MethodHandle;)V")
    dynamicInvoker = JavaMethod("()Ljava/lang/invoke/MethodHandle;")