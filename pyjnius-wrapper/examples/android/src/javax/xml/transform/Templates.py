from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Templates"]

class Templates(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Templates"
    newTransformer = JavaMethod("()Ljavax/xml/transform/Transformer;")
    getOutputProperties = JavaMethod("()Ljava/util/Properties;")