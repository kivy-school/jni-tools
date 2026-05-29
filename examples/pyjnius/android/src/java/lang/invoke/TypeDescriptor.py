from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeDescriptor"]

class TypeDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/TypeDescriptor"
    descriptorString = JavaMethod("()Ljava/lang/String;")

    class OfMethod(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/invoke/TypeDescriptor$OfMethod"
        returnType = JavaMethod("()Ljava/lang/invoke/TypeDescriptor$OfField;")
        parameterType = JavaMethod("(I)Ljava/lang/invoke/TypeDescriptor$OfField;")
        insertParameterTypes = JavaMethod("(I[Ljava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;", varargs=True)
        changeReturnType = JavaMethod("(Ljava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;")
        dropParameterTypes = JavaMethod("(II)Ljava/lang/invoke/TypeDescriptor$OfMethod;")
        parameterCount = JavaMethod("()I")
        parameterList = JavaMethod("()Ljava/util/List;")
        changeParameterType = JavaMethod("(ILjava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;")
        parameterArray = JavaMethod("()[Ljava/lang/invoke/TypeDescriptor$OfField;")

    class OfField(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/invoke/TypeDescriptor$OfField"
        componentType = JavaMethod("()Ljava/lang/invoke/TypeDescriptor$OfField;")
        isPrimitive = JavaMethod("()Z")
        isArray = JavaMethod("()Z")
        arrayType = JavaMethod("()Ljava/lang/invoke/TypeDescriptor$OfField;")