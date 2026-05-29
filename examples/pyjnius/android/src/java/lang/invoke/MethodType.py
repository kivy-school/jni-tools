from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MethodType"]

class MethodType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/MethodType"
    returnType = JavaMultipleMethod([("()Ljava/lang/Class;", False, False), ("()Ljava/lang/invoke/TypeDescriptor$OfField;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    wrap = JavaMethod("()Ljava/lang/invoke/MethodType;")
    describeConstable = JavaMethod("()Ljava/util/Optional;")
    descriptorString = JavaMethod("()Ljava/lang/String;")
    parameterType = JavaMultipleMethod([("(I)Ljava/lang/Class;", False, False), ("(I)Ljava/lang/invoke/TypeDescriptor$OfField;", False, False)])
    insertParameterTypes = JavaMultipleMethod([("(I[Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", False, True), ("(I[Ljava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;", False, False), ("(ILjava/util/List;)Ljava/lang/invoke/MethodType;", False, False)])
    changeReturnType = JavaMultipleMethod([("(Ljava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;", False, False), ("(Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", False, False)])
    methodType = JavaMultipleMethod([("(Ljava/lang/Class;Ljava/util/List;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;Ljava/lang/Class;[Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, True), ("(Ljava/lang/Class;[Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", True, False), ("(Ljava/lang/Class;Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/MethodType;", True, False)])
    dropParameterTypes = JavaMultipleMethod([("(II)Ljava/lang/invoke/TypeDescriptor$OfMethod;", False, False), ("(II)Ljava/lang/invoke/MethodType;", False, False)])
    appendParameterTypes = JavaMultipleMethod([("([Ljava/lang/Class;)Ljava/lang/invoke/MethodType;", False, True), ("(Ljava/util/List;)Ljava/lang/invoke/MethodType;", False, False)])
    parameterCount = JavaMethod("()I")
    genericMethodType = JavaMultipleMethod([("(IZ)Ljava/lang/invoke/MethodType;", True, False), ("(I)Ljava/lang/invoke/MethodType;", True, False)])
    lastParameterType = JavaMethod("()Ljava/lang/Class;")
    parameterList = JavaMethod("()Ljava/util/List;")
    erase = JavaMethod("()Ljava/lang/invoke/MethodType;")
    toMethodDescriptorString = JavaMethod("()Ljava/lang/String;")
    changeParameterType = JavaMultipleMethod([("(ILjava/lang/Class;)Ljava/lang/invoke/MethodType;", False, False), ("(ILjava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;", False, False)])
    hasPrimitives = JavaMethod("()Z")
    unwrap = JavaMethod("()Ljava/lang/invoke/MethodType;")
    parameterArray = JavaMultipleMethod([("()[Ljava/lang/invoke/TypeDescriptor$OfField;", False, False), ("()[Ljava/lang/Class;", False, False)])
    hasWrappers = JavaMethod("()Z")
    generic = JavaMethod("()Ljava/lang/invoke/MethodType;")
    fromMethodDescriptorString = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljava/lang/invoke/MethodType;")