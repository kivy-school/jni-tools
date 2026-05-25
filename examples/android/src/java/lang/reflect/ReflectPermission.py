from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReflectPermission"]

class ReflectPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/ReflectPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]