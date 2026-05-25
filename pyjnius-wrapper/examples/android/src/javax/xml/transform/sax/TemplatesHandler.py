from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemplatesHandler"]

class TemplatesHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/TemplatesHandler"
    getTemplates = JavaMethod("()Ljavax/xml/transform/Templates;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")