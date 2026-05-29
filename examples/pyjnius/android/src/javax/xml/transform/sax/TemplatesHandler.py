from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemplatesHandler"]

class TemplatesHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/TemplatesHandler"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getTemplates = JavaMethod("()Ljavax/xml/transform/Templates;")