from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Templates"]

class Templates(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Templates"
    getOutputProperties = JavaMethod("()Ljava/util/Properties;")
    newTransformer = JavaMethod("()Ljavax/xml/transform/Transformer;")