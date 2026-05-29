from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SchemaFactoryLoader"]

class SchemaFactoryLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/SchemaFactoryLoader"
    newFactory = JavaMethod("(Ljava/lang/String;)Ljavax/xml/validation/SchemaFactory;")