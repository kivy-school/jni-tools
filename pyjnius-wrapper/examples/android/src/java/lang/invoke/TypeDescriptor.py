from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeDescriptor"]

class TypeDescriptor(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/TypeDescriptor"
    descriptorString = JavaMethod("()Ljava/lang/String;")

    class OfField(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/invoke/TypeDescriptor/OfField"
        isArray = JavaMethod("()Z")
        isPrimitive = JavaMethod("()Z")
        componentType = JavaMethod("()Ljava/lang/invoke/TypeDescriptor$OfField;")
        arrayType = JavaMethod("()Ljava/lang/invoke/TypeDescriptor$OfField;")

    class OfMethod(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/invoke/TypeDescriptor/OfMethod"
        parameterCount = JavaMethod("()I")
        parameterType = JavaMethod("(I)Ljava/lang/invoke/TypeDescriptor$OfField;")
        returnType = JavaMethod("()Ljava/lang/invoke/TypeDescriptor$OfField;")
        parameterArray = JavaMethod("()[Ljava/lang/invoke/TypeDescriptor$OfField;")
        parameterList = JavaMethod("()Ljava/util/List;")
        changeReturnType = JavaMethod("(Ljava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;")
        changeParameterType = JavaMethod("(ILjava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;")
        dropParameterTypes = JavaMethod("(II)Ljava/lang/invoke/TypeDescriptor$OfMethod;")
        insertParameterTypes = JavaMethod("(I[Ljava/lang/invoke/TypeDescriptor$OfField;)Ljava/lang/invoke/TypeDescriptor$OfMethod;", varargs=True)