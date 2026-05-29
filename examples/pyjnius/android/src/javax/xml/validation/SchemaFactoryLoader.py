from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SchemaFactoryLoader"]

class SchemaFactoryLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/SchemaFactoryLoader"
    __javaconstructor__ = [("()V", False)]
    newFactory = JavaMethod("(Ljava/lang/String;)Ljavax/xml/validation/SchemaFactory;")