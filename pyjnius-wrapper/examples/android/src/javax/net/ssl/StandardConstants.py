from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardConstants"]

class StandardConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/StandardConstants"
    SNI_HOST_NAME = JavaStaticField("I")