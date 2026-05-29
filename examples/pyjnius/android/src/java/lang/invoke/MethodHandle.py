from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MethodHandle"]

class MethodHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/MethodHandle"
    type = JavaMethod("()Ljava/lang/invoke/MethodType;")
    invokeExact = JavaMethod("([Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)
    invoke = JavaMethod("([Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)
    invokeWithArguments = JavaMultipleMethod([("([Ljava/lang/Object;)Ljava/lang/Object;", False, True), ("(Ljava/util/List;)Ljava/lang/Object;", False, False)])
    asType = JavaMethod("(Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/MethodHandle;")
    asSpreader = JavaMultipleMethod([("(Ljava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False), ("(ILjava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False)])
    withVarargs = JavaMethod("(Z)Ljava/lang/invoke/MethodHandle;")
    asCollector = JavaMultipleMethod([("(Ljava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False), ("(ILjava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False)])
    asVarargsCollector = JavaMethod("(Ljava/lang/Class;)Ljava/lang/invoke/MethodHandle;")
    isVarargsCollector = JavaMethod("()Z")
    asFixedArity = JavaMethod("()Ljava/lang/invoke/MethodHandle;")
    bindTo = JavaMethod("(Ljava/lang/Object;)Ljava/lang/invoke/MethodHandle;")
    toString = JavaMethod("()Ljava/lang/String;")