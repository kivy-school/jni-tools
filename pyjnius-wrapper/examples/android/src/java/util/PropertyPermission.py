from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyPermission"]

class PropertyPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PropertyPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]