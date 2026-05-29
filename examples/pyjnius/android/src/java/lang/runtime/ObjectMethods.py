from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectMethods"]

class ObjectMethods(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/runtime/ObjectMethods"
    bootstrap = JavaStaticMethod("(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/TypeDescriptor;Ljava/lang/Class;Ljava/lang/String;[Ljava/lang/invoke/MethodHandle;)Ljava/lang/Object;", varargs=True)