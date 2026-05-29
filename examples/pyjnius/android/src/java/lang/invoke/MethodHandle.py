from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MethodHandle"]

class MethodHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/MethodHandle"
    invoke = JavaMethod("([Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)
    invokeExact = JavaMethod("([Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)
    asFixedArity = JavaMethod("()Ljava/lang/invoke/MethodHandle;")
    type = JavaMethod("()Ljava/lang/invoke/MethodType;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeConstable = JavaMethod("()Ljava/util/Optional;")
    asType = JavaMethod("(Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/MethodHandle;")
    invokeWithArguments = JavaMultipleMethod([("(Ljava/util/List;)Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)Ljava/lang/Object;", False, True)])
    asSpreader = JavaMultipleMethod([("(Ljava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False), ("(ILjava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False)])
    isVarargsCollector = JavaMethod("()Z")
    asVarargsCollector = JavaMethod("(Ljava/lang/Class;)Ljava/lang/invoke/MethodHandle;")
    asCollector = JavaMultipleMethod([("(ILjava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False), ("(Ljava/lang/Class;I)Ljava/lang/invoke/MethodHandle;", False, False)])
    withVarargs = JavaMethod("(Z)Ljava/lang/invoke/MethodHandle;")
    bindTo = JavaMethod("(Ljava/lang/Object;)Ljava/lang/invoke/MethodHandle;")