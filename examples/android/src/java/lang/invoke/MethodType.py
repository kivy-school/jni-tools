from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MethodType"]

class MethodType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/MethodType"
    methodType = JavaMultipleMethod([("(Ljava/lang/Class;[Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;Ljava/util/List;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;Ljava/lang/Class;[Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, True), ("(Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/MethodType;", True, False)])
    genericMethodType = JavaMultipleMethod([("(IZ)Ljava/lang/invoke/MethodType;", True, False), ("(I)Ljava/lang/invoke/MethodType;", True, False)])
    changeParameterType = JavaMethod("(ILjava/lang/Class;)Ljava/lang/invoke/MethodType;")
    insertParameterTypes = JavaMultipleMethod([("(I[Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", False, True), ("(ILjava/util/List;)Ljava/lang/invoke/MethodType;", False, False)])
    appendParameterTypes = JavaMultipleMethod([("([Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", False, True), ("(Ljava/util/List;)Ljava/lang/invoke/MethodType;", False, False)])
    dropParameterTypes = JavaMethod("(II)Ljava/lang/invoke/MethodType;")
    changeReturnType = JavaMethod("(Ljava/lang/Class;)Ljava/lang/invoke/MethodType;")
    hasPrimitives = JavaMethod("()Z")
    hasWrappers = JavaMethod("()Z")
    erase = JavaMethod("()Ljava/lang/invoke/MethodType;")
    generic = JavaMethod("()Ljava/lang/invoke/MethodType;")
    wrap = JavaMethod("()Ljava/lang/invoke/MethodType;")
    unwrap = JavaMethod("()Ljava/lang/invoke/MethodType;")
    parameterType = JavaMethod("(I)Ljava/lang/Class;")
    parameterCount = JavaMethod("()I")
    returnType = JavaMethod("()Ljava/lang/Class;")
    parameterList = JavaMethod("()Ljava/util/List;")
    lastParameterType = JavaMethod("()Ljava/lang/Class;")
    parameterArray = JavaMethod("()[Ljava/lang/Class;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    fromMethodDescriptorString = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljava/lang/invoke/MethodType;")
    toMethodDescriptorString = JavaMethod("()Ljava/lang/String;")
    descriptorString = JavaMethod("()Ljava/lang/String;")