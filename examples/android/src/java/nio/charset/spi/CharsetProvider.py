from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharsetProvider"]

class CharsetProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/spi/CharsetProvider"
    __javaconstructor__ = [("()V", False)]
    charsets = JavaMethod("()Ljava/util/Iterator;")
    charsetForName = JavaMethod("(Ljava/lang/String;)Ljava/nio/charset/Charset;")